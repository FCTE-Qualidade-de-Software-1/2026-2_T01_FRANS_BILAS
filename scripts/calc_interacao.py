#!/usr/bin/env python3
"""
calc_interacao.py - Cálculo das métricas de Capacidade de Interação (G1).

Lê os dados brutos publicados em documentation/content/dados/ e calcula:
- M1.1 TCR: conclusões sem ajuda / tentativas iniciadas, por tarefa.
- M1.2 TME: média das durações com status=concluida, ajuda=nao e tempo_valido=sim.
- M1.3 FET: erros / participantes, por tarefa; confere o campo `erros` da ficha
  com as linhas de M1.3-eventos.csv.
- M1.4 ICA: 100 x aprovadas / (aprovadas + reprovadas), somando axe-core e
  Lighthouse nas quatro páginas, a partir dos relatórios JSON.
- M1.5 SUS: 2,5 x (soma de Rk-1 nos itens ímpares + 5-Rk nos pares), por participante.

As regras são as dos Procedimentos de coleta (Fase 3). O script grava
M1-resultados.csv na pasta de interação e os gráficos Mermaid usados na Fase 4
em documentation/snippets/avaliacao/, incluindo um gráfico de TSN, ICT e TPE lido
dos dados de Manutenibilidade e Segurança. Sai com erro se encontrar divergência.

Uso:
    python3 scripts/calc_interacao.py
"""
import csv
import json
import sys
from collections import Counter
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "documentation" / "content" / "dados"
INTERACAO = DADOS / "interacao"
ACESSIBILIDADE = DADOS / "acessibilidade"
GRAFICOS = RAIZ / "documentation" / "snippets" / "avaliacao"

TAREFAS = ["T1", "T2", "T3", "T4"]
PAGINAS = ["1-inicio", "2-processos", "3-formulario", "4-proposta"]
CORES = '%%{init: {"themeVariables": {"xyChart": {"plotColorPalette": "#2563eb, #dc2626"}}}}%%'


def ler_csv(caminho):
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def fmt(valor, casas=1):
    """Arredonda meio para cima, como nas tabelas da Fase 4 (77,05 vira 77,1)."""
    passo = Decimal(1).scaleb(-casas)
    return str(Decimal(repr(valor)).quantize(passo, rounding=ROUND_HALF_UP))


def calcular_tarefas(ficha, eventos):
    erros_eventos = Counter((e["participante"], e["tarefa"]) for e in eventos)
    divergencias = [
        (l["participante"], l["tarefa"])
        for l in ficha
        if int(l["erros"]) != erros_eventos[(l["participante"], l["tarefa"])]
    ]
    if divergencias:
        sys.exit(f"Campo erros diverge de M1.3-eventos.csv em: {divergencias}")

    resultado = {}
    for tarefa in TAREFAS:
        linhas = [l for l in ficha if l["tarefa"] == tarefa]
        iniciadas = [l for l in linhas if l["status"] != "nao_iniciada"]
        autonomas = [l for l in iniciadas if l["status"] == "concluida" and l["ajuda"] == "nao"]
        validas = [l for l in autonomas if l["tempo_valido"] == "sim"]
        tcr = 100 * len(autonomas) / len(iniciadas) if iniciadas else None
        tme = sum(float(l["duracao_s"]) for l in validas) / len(validas) if validas else None
        erros = sum(int(l["erros"]) for l in iniciadas)
        fet = erros / len(iniciadas) if iniciadas else None
        resultado[tarefa] = {
            "iniciadas": len(iniciadas),
            "sem_ajuda": len(autonomas),
            "tcr": tcr,
            "tme": tme,
            "n_tme": len(validas),
            "erros": erros,
            "fet": fet,
        }
    return resultado


def calcular_sus(respostas):
    escores = {}
    for linha in respostas:
        valores = [linha[f"R{k}"] for k in range(1, 11)]
        if any(v == "" for v in valores):
            continue
        r = [int(v) for v in valores]
        soma = sum(r[i] - 1 if i % 2 == 0 else 5 - r[i] for i in range(10))
        escores[linha["participante"]] = 2.5 * soma
    excluidos = len(respostas) - len(escores)
    media = sum(escores.values()) / len(escores) if escores else None
    return escores, media, excluidos


def calcular_ica():
    linhas = []
    for pagina in PAGINAS:
        axe = json.loads((ACESSIBILIDADE / "relatorios" / f"M1.4-{pagina}-axe.json").read_text())
        axe = axe[0] if isinstance(axe, list) else axe
        aprovadas = {r["id"] for r in axe["passes"]}
        reprovadas = {r["id"] for r in axe["violations"]}
        linhas.append((pagina, "axe-core", len(aprovadas - reprovadas), len(reprovadas)))

        lh = json.loads((ACESSIBILIDADE / "relatorios" / f"M1.4-{pagina}-lighthouse.json").read_text())
        a = r = 0
        for ref in lh["categories"]["accessibility"]["auditRefs"]:
            auditoria = lh["audits"][ref["id"]]
            if auditoria["scoreDisplayMode"] == "binary" and auditoria["score"] in (0, 1):
                if auditoria["score"] == 1:
                    a += 1
                else:
                    r += 1
        linhas.append((pagina, "lighthouse", a, r))

    publicado = {(l["pagina"], l["ferramenta"]): (int(l["aprovadas"]), int(l["reprovadas"]))
                 for l in ler_csv(ACESSIBILIDADE / "M1.4-resultados.csv")}
    for pagina, ferramenta, a, r in linhas:
        if publicado.get((pagina, ferramenta)) != (a, r):
            sys.exit(f"M1.4-resultados.csv diverge dos relatórios em {pagina}/{ferramenta}")
    total_a = sum(l[2] for l in linhas)
    total_r = sum(l[3] for l in linhas)
    return linhas, 100 * total_a / (total_a + total_r), total_a, total_r


def grafico_barras(titulo, eixo_x, eixo_y, maximo, barras, linha=None):
    texto = [CORES, "xychart-beta", f'    title "{titulo}"',
             "    x-axis [" + ", ".join(f'"{x}"' for x in eixo_x) + "]",
             f'    y-axis "{eixo_y}" 0 --> {maximo}',
             "    bar [" + ", ".join(fmt(v) for v in barras) + "]"]
    if linha is not None:
        texto.append("    line [" + ", ".join(fmt(linha) for _ in eixo_x) + "]")
    return "\n".join(texto) + "\n"


def main():
    ficha = ler_csv(INTERACAO / "M1.1-M1.3-ficha.csv")
    eventos = ler_csv(INTERACAO / "M1.3-eventos.csv")
    tarefas = calcular_tarefas(ficha, eventos)
    escores, media_sus, excluidos = calcular_sus(ler_csv(INTERACAO / "M1.5-sus.csv"))
    paginas, ica, total_a, total_r = calcular_ica()

    saida = [("metrica", "recorte", "valor", "n", "detalhe")]
    for tarefa, r in tarefas.items():
        saida.append(("M1.1 TCR (%)", tarefa, fmt(r["tcr"]), r["iniciadas"], f"{r['sem_ajuda']} sem ajuda"))
        saida.append(("M1.2 TME (s)", tarefa, fmt(r["tme"]) if r["tme"] is not None else "indisponivel",
                      r["n_tme"], "conclusoes sem ajuda e com tempo valido"))
        saida.append(("M1.3 FET (erros por participante)", tarefa, fmt(r["fet"], 2), r["iniciadas"], f"{r['erros']} erros"))
    for pagina, ferramenta, a, r in paginas:
        saida.append(("M1.4 verificacoes", f"{pagina} {ferramenta}", f"{a}/{a + r}", a + r, "aprovadas/decididas"))
    saida.append(("M1.4 ICA (%)", "total", fmt(ica), total_a + total_r, f"{total_a} aprovadas"))
    for participante, escore in escores.items():
        saida.append(("M1.5 SUS (pontos)", participante, fmt(escore), 10, "itens"))
    saida.append(("M1.5 SUS (pontos)", "media", fmt(media_sus), len(escores), f"{excluidos} questionarios excluidos"))

    with open(INTERACAO / "M1-resultados.csv", "w", newline="", encoding="utf-8") as arquivo:
        csv.writer(arquivo, lineterminator="\n").writerows(saida)

    GRAFICOS.mkdir(parents=True, exist_ok=True)
    (GRAFICOS / "m11-tcr.mmd").write_text(grafico_barras(
        "M1.1 TCR por tarefa (linha: nível aceitável de 75%)", TAREFAS, "TCR (%)", 100,
        [tarefas[t]["tcr"] for t in TAREFAS], 75))
    com_tempo = [t for t in TAREFAS if tarefas[t]["tme"] is not None]
    (GRAFICOS / "m12-tme.mmd").write_text(grafico_barras(
        "M1.2 TME por tarefa com tempo válido (linha: 120 s)", com_tempo, "TME (s)", 180,
        [tarefas[t]["tme"] for t in com_tempo], 120))
    (GRAFICOS / "m13-fet.mmd").write_text(grafico_barras(
        "M1.3 FET por tarefa (linha: nível aceitável de 1,0)", TAREFAS, "Erros por participante", 2,
        [tarefas[t]["fet"] for t in TAREFAS], 1.0))
    (GRAFICOS / "m14-ica.mmd").write_text(grafico_barras(
        "M1.4 aprovação por página e ferramenta (linha: 85%)",
        [f"{p.split('-', 1)[1]} {f.split('-')[0]}" for p, f, _, _ in paginas], "Aprovadas (%)", 100,
        [100 * a / (a + r) for _, _, a, r in paginas], 85))
    (GRAFICOS / "m15-sus.mmd").write_text(grafico_barras(
        "M1.5 SUS por participante (linha: nível aceitável de 68)", list(escores), "SUS (pontos)", 100,
        list(escores.values()), 68))

    # Gráfico de apoio às questões Q2.1, Q2.3 e Q3.3, com os dados já publicados de G2 e G3.
    resumo = json.loads((DADOS / "manutenibilidade" / "summary.json").read_text())
    endpoints = ler_csv(DADOS / "seguranca" / "M3.3-endpoints.csv")
    protegidas = sum(1 for e in endpoints if e["conferencia_manual"].startswith("protegida"))
    sem = sum(1 for e in endpoints if e["conferencia_manual"].startswith("sem"))
    medidos = [resumo["M2.1"]["percent"], resumo["M2.4"]["percent"], 100 * protegidas / (protegidas + sem)]
    (GRAFICOS / "g2-g3-percentuais.mmd").write_text("\n".join([
        CORES, "xychart-beta",
        '    title "TSN, ICT e TPE medidos (barras) e nível aceitável (linha)"',
        '    x-axis ["TSN (aceitável até 25)", "ICT (aceitável a partir de 70)", "TPE (aceitável a partir de 95)"]',
        '    y-axis "%" 0 --> 100',
        "    bar [" + ", ".join(fmt(v) for v in medidos) + "]",
        "    line [25.0, 70.0, 95.0]",
    ]) + "\n")

    for linha in saida[1:]:
        print(" | ".join(str(c) for c in linha))


if __name__ == "__main__":
    main()
