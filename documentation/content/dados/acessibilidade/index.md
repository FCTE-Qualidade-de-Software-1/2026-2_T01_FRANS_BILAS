---
icon: lucide/accessibility
---

# Dados da Coleta: Acessibilidade (M1.4)

Esta página reúne a inspeção automática de acessibilidade das quatro páginas do fluxo de participação, de onde sai a métrica M1.4 (ICA) definida na [Fase 2](../../fases/2.md). O procedimento seguido é o da seção M1.4 dos [Procedimentos de coleta](../../procedimentos/coleta.md). O julgamento do objetivo G1 está na [Fase 4](../../fases/4.md).

---

## 1. Execução

**Tabela 1. Registro da execução.**

| Item | Valor |
| :--- | :--- |
| Data | 22/11/2026, das 21:53 às 21:55 (UTC−3) |
| Repositório e commit | `decidim-govbr`, commit `176b04673d956af4b1ab645e922cedd796b6a22e`, na cópia local em modo de desenvolvimento |
| Ferramentas | `@axe-core/cli` 4.14.0 com `axe-core` 4.14.1; Lighthouse 13.6.0; Node 22.23.3; Chrome for Testing 158.0.8127.36 com o ChromeDriver da mesma versão |
| Janela | axe: Chrome sem interface, 1366 × 568. Lighthouse: emulação móvel padrão, 412 × 823 |
| Autenticação | Perfil de navegador exclusivo, logado com a conta `autor@teste.local` pelo login de estrangeiro. Cookies não essenciais recusados no perfil |
| Responsável | Mateus Vinícius Vieira |

Fonte: elaborado pela equipe.

Os comandos são os da seção M1.4 dos Procedimentos de coleta, com dois parâmetros a mais no axe: `--chromedriver-path` e `--chrome-path`, que apontam para o Chrome for Testing e o ChromeDriver, e `--load-delay 3000`, que espera a página terminar de carregar. Antes, uma tentativa com o Chromium do snap travou o Lighthouse e foi descartada sem gerar relatório válido. As versões instaladas ficam em [`ferramentas/package-lock.json`](ferramentas/package-lock.json); para repetir, use `npm ci` nessa pasta.

**Tabela 2. Páginas inspecionadas.**

| Código | Página | URL |
| :--- | :--- | :--- |
| `1-inicio` | Página inicial | `http://localhost:3000/?locale=pt-BR` |
| `2-processos` | Lista de processos | `http://localhost:3000/processes` |
| `3-formulario` | Formulário de proposta | `http://localhost:3000/processes/pracas-e-parques-teste/f/31/proposals/new` |
| `4-proposta` | Visualização de proposta | `http://localhost:3000/processes/pracas-e-parques-teste/f/31/proposals/1` |

Fonte: elaborado pela equipe.

Nas oito execuções, o `url` do axe e o `finalDisplayedUrl` do Lighthouse são iguais à URL planejada. Nenhuma página redirecionou para o login, e o formulário de proposta só abre com a conta autenticada.

---

## 2. Arquivos

| Arquivo | Conteúdo |
| :--- | :--- |
| [`relatorios/`](relatorios/1-inicio-axe.json) | Os oito relatórios em JSON, um por ferramenta e página. Dos relatórios do Lighthouse foi removida só a captura de tela da página inteira (`fullPageScreenshot`) |
| [`M1.4-resultados.csv`](M1.4-resultados.csv) | Verificações aprovadas, reprovadas e sem decisão, por ferramenta e página |
| [`M1.4-falhas.csv`](M1.4-falhas.csv) | Cada falha com página, ferramenta, regra, impacto (no axe) e seletor |
| [`ferramentas/`](ferramentas/package.json) | `package.json` e `package-lock.json` das ferramentas |

Fonte: elaborado pela equipe.

Os relatórios citam apenas a conta fictícia "Equipe de Teste". Não há e-mail, token nem dado pessoal.

---

## 3. Resultados

No axe, cada ID distinto de `passes` conta como aprovado e cada ID de `violations` como reprovado. Os IDs de `incomplete` ficam sem decisão, e os de `inapplicable` ficam de fora. No Lighthouse, contam só as auditorias binárias da categoria de acessibilidade, com nota 0 ou 1. As auditorias manuais, informativas e não aplicáveis ficam de fora.

**Tabela 3. Verificações por ferramenta e página.**

| Página | axe: aprovadas | axe: reprovadas | axe: sem decisão | Lighthouse: aprovadas | Lighthouse: reprovadas | Lighthouse: manuais |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Página inicial | 24 | 3 | 2 | 23 | 3 | 10 |
| Lista de processos | 25 | 2 | 2 | 23 | 3 | 10 |
| Formulário de proposta | 26 | 2 | 2 | 26 | 2 | 10 |
| Visualização de proposta | 25 | 2 | 2 | 24 | 2 | 10 |
| **Total** | **100** | **9** | **8** | **96** | **10** | **40** |

Fonte: [`M1.4-resultados.csv`](M1.4-resultados.csv).

$$
ICA = 100 \times \frac{100 + 96}{(100 + 9) + (96 + 10)} = 100 \times \frac{196}{215} = 91{,}2\%
$$

Separadas, as ferramentas dão 91,7% (axe, 100 de 109) e 90,6% (Lighthouse, 96 de 106). Pela Fase 2, um ICA de 91,2% fica na faixa **Bom** (de 85% a menos de 95%).

Ficaram sem decisão 48 itens: no axe, `color-contrast` e `aria-prohibited-attr` em cada página; no Lighthouse, 10 auditorias manuais por página. Eles pedem revisão manual e não entram no índice.

---

## 4. Falhas encontradas

As quatro regras reprovadas aparecem nas duas ferramentas, exceto `heading-order`, que só o Lighthouse aponta.

**Tabela 4. Regras reprovadas.**

| Regra | Páginas | Onde |
| :--- | :--- | :--- |
| `link-name` (link sem nome acessível) | As quatro | Links feitos só de imagem: logo do rodapé, logos de Dataprev, UnB e gov.br, selo Creative Commons. Na página inicial, também os três destaques do carrossel e os logos da seção de parceiros. Na lista de processos, o cartão do processo. Na proposta, os quatro botões de compartilhar (Facebook, X, LinkedIn e WhatsApp) |
| `label-content-name-mismatch` (nome acessível diferente do texto visível) | As quatro | Botão de idioma ("PT-BR") e botão da conta no cabeçalho |
| `image-alt` (imagem sem texto alternativo) | Página inicial | As três imagens dos cartões de novidades |
| `heading-order` (níveis de título fora de ordem) | Lista de processos | Título `h3` do cabeçalho da lista |

Fonte: [`M1.4-falhas.csv`](M1.4-falhas.csv).

Todas as falhas estão em componentes da plataforma: cabeçalho, rodapé, carrossel, cartões e botões de compartilhar. Nenhuma vem do botão "WAI WCAG" nem de outra parte do modo de desenvolvimento. O atributo `data-accessibility-violation`, que aparece em alguns seletores, é a marcação que essa ferramenta de desenvolvimento coloca nos elementos. Ele não muda o resultado.

O formulário de proposta, onde os participantes erraram na T3, passou nas regras de rótulos de campo (`label`) nas duas ferramentas. O problema observado nas sessões é de mensagem de validação, que as ferramentas automáticas não avaliam.

---

## 5. Limites

- O índice só descreve verificações automáticas. Elas cobrem parte dos critérios WCAG, e a conformidade com WCAG 2.1 AA ou eMAG depende das 48 verificações sem decisão e de revisão manual.
- Há regras sobrepostas entre axe e Lighthouse. Uma mesma falha, como `link-name`, conta uma vez em cada ferramenta.
- A cópia local roda em modo de desenvolvimento, com conteúdo de demonstração na página inicial e um processo criado para os testes. As páginas da produção podem ter outros elementos.
- O Lighthouse usou a emulação móvel padrão, e o axe usou a janela de computador. A coleta não repetiu cada ferramenta nos dois tamanhos.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 22/11/2026 | Inspeção automática das quatro páginas com axe-core e Lighthouse e cálculo do ICA (M1.4) | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
