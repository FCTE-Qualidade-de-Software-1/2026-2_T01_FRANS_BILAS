---
icon: lucide/users
---

# Dados da Coleta: Capacidade de Interação (G1)

Esta página reúne os registros das sessões com usuários, de onde saem as métricas M1.1, M1.2, M1.3 e M1.5 definidas na [Fase 2](../../fases/2.md) e planejadas na [Fase 3](../../fases/3.md). A inspeção de acessibilidade (M1.4) não usa estas fichas.

**Situação em 22/11/2026**: três sessões realizadas e gravadas (P02, P03 e P04). As fichas usam as gravações das 20:31, 20:33 e 20:38, com tempo tirado do vídeo. Os participantes já tinham feito as tarefas em rodadas anteriores, o que favorece os resultados. As respostas do SUS estão em `M1.5-sus.csv`, com os três questionários completos. Os detalhes estão na Seção 8 do [roteiro](roteiro.md).

---

## 1. Execução

A Tabela 1 identifica a execução. Os campos em aberto são preenchidos na primeira sessão, como pede o passo 4 dos [Procedimentos de coleta](../../procedimentos/coleta.md).

**Tabela 1. Registro da execução das sessões.**

| Item | Valor |
| :--- | :--- |
| Repositório e commit | `decidim-govbr`, commit `176b04673d956af4b1ab645e922cedd796b6a22e` |
| Condução das sessões | Mateus Vinícius Vieira (issue #90) |
| Rotulagem por métrica | Miguel Arthur Oliveira de Lima (issue #72) |
| Datas das sessões, com fuso | 22/11/2026, UTC−3: P02 às 20:31:03, P03 às 20:33:32 e P04 às 20:38:48 (início das gravações). Rodadas anteriores com as mesmas contas entre 19:50 e 20:25 |
| Máquina, sistema e navegador | Notebook Lenovo, Ubuntu, Firefox (versões não registradas) |
| Processo participativo usado em T2 | Praças e Parques do Bairro (`pracas-e-parques-teste`), criado na cópia local e listado no menu principal |
| Proposta de teste usada em T4 | A proposta que o próprio participante publicou: proposta 10 (P02), 11 (P03) e 13 (P04, que publicou a 12 na T3 e criou a 13 durante a T4) |
| URLs iniciais de T1 a T4 | T1: `http://localhost:3000/?locale=pt-BR`; T2: página inicial com login; T3: `http://localhost:3000/processes/pracas-e-parques-teste/f/31`; T4: página da proposta publicada na T3 (`.../f/31/proposals/{id}`) |
| Sessões realizadas e sessões com gravação autorizada | 3 realizadas e 3 gravadas, com autorização. As gravações das rodadas anteriores travaram num quadro fixo |

Fonte: elaborado pela equipe.

Dois desvios do plano estão registrados. A Fase 3 previa as sessões de 06/11 a 10/11, e elas só aconteceram em 22/11, depois que a cópia local ficou pronta. A condução passou de João Victor da Silva Batista de Farias para Mateus Vinícius Vieira, a pedido de João. As datas executadas estão na Tabela 1 e no cronograma da Fase 3.

---

## 2. Arquivos

A Tabela 2 liga cada arquivo à métrica que ele alimenta. Os nomes dos campos são os da Tabela 2 dos Procedimentos de coleta.

**Tabela 2. Arquivos das sessões e métricas correspondentes.**

| Arquivo | Conteúdo | Métrica |
| :--- | :--- | :---: |
| [`M1.1-M1.3-ficha.csv`](M1.1-M1.3-ficha.csv) | Uma linha por participante e tarefa: desfecho, ajuda, tempo e contagem de erros | M1.1, M1.2, M1.3 |
| [`M1.3-eventos.csv`](M1.3-eventos.csv) | Uma linha por erro observado: instante, ação do participante e resposta da plataforma | M1.3 |
| [`M1.5-sus.csv`](M1.5-sus.csv) | Uma linha por participante, com as respostas de 1 a 5 aos dez itens | M1.5 |
| [`M1-resultados.csv`](M1-resultados.csv) | TCR, TME e FET por tarefa, ICA por página e SUS por participante, gerados pelo script [`scripts/calc_interacao.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_FRANS_BILAS/blob/main/scripts/calc_interacao.py) | M1.1 a M1.5 |

Fonte: elaborado pela equipe.

Valores aceitos na ficha:

- `participante`: código de `P01` a `P05`, que corresponde aos perfis P1 a P5 da Seção 2.1.1 da Fase 3.
- `tarefa`: `T1` a `T4`.
- `status`: `concluida`, `falhou`, `desistiu` ou `nao_iniciada`.
- `ajuda`, `tempo_valido`: `sim` ou `nao`.
- `fonte_tempo`: `video` ou `cronometro`.
- `duracao_s`: segundos, com uma casa decimal.
- `erros`: número inteiro, igual à quantidade de linhas do participante e da tarefa em `M1.3-eventos.csv`.

Para recalcular as cinco métricas e conferir as fichas, rode `python3 scripts/calc_interacao.py` na raiz do repositório. O script para com erro se o campo `erros` da ficha não bater com `M1.3-eventos.csv` ou se `M1.4-resultados.csv` não bater com os relatórios.

Uma resposta em branco no SUS fica em branco no arquivo. O questionário incompleto sai da média, e a quantidade excluída é informada junto com o resultado.

---

## 3. Roteiro do observador

O passo a passo das sessões, da cópia local ao preenchimento das fichas, está no [Roteiro das sessões com usuários](roteiro.md). Ele ordena o que os Procedimentos de coleta e o [TCLE](../../tcle.md) já definem e não muda nenhuma regra de contagem.

---

## 4. Questionário SUS

A Fase 2 define M1.5 pela escala de Brooke (1996), que está em inglês. Para a aplicação em português, a referência é a tradução e adaptação transcultural de Lourenço, Carmona e Lopes (2022). Os dez itens são copiados da versão em português publicada no artigo para o formulário, na mesma ordem e sem mudar a redação. Todos os participantes respondem à mesma versão.

O formulário usado, impresso ou digital, é anexado a esta pasta sem nenhuma resposta identificada.

---

## 5. O que fica fora do repositório

- Termos de consentimento assinados.
- Gravações de tela e de áudio.
- A planilha que relaciona o nome de cada participante ao código `P01` a `P05`.

Esses arquivos ficam na pasta restrita descrita na Seção 1 do TCLE, com o prazo de guarda definido lá.

---

## Referências

- BROOKE, J. SUS: A "Quick and Dirty" Usability Scale. In: JORDAN, P. W. et al. (ed.). *Usability Evaluation in Industry*. London: Taylor & Francis, 1996. p. 189-194.
- LOURENÇO, D. F.; CARMONA, E. V.; LOPES, M. H. B. M. Translation and Cross-Cultural Adaptation of the System Usability Scale to Brazilian Portuguese. *Aquichan*, v. 22, n. 2, e2228, 2022. DOI: [10.5294/aqui.2022.22.2.8](https://doi.org/10.5294/aqui.2022.22.2.8).

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `0.1` | 17/11/2026 | Fichas das sessões com usuários, roteiro do observador e referência do SUS em português, antes da coleta (issue #90) | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `0.2` | 22/11/2026 | Roteiro do observador movido para página própria (issue #90) | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `0.3` | 22/11/2026 | Fichas preenchidas com as sessões gravadas de P02, P03 e P04 (issue #90) | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `0.4` | 22/11/2026 | Resultados calculados por script a partir das fichas (#71) | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
