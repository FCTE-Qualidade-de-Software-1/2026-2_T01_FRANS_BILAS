---
icon: lucide/presentation
---

# Apresentação Final: Avaliação de Qualidade do Brasil Participativo

**Equipe Frans Bilas (Turma 02)**  
Disciplina: Qualidade de Software 1 (FGA0315, semestre 2026.2)  
Professora: Dra. Cristiane Soares Ramos  
Faculdade de Ciências e Tecnologias em Engenharia (FCTE, Campus UnB Gama)

Os slides no visual do Ponto de Controle 1 estão em [PDF](final/apresentacao-final.pdf), gerado a partir de [`final/apresentacao.html`](final/apresentacao.html). Esta página traz o mesmo roteiro, com quem apresenta cada slide e as notas de fala.

---

## 1. Produto e Propósito

<p class="apresentador">João Victor da Silva Batista de Farias</p>

<!--
NOTA PARA APRESENTAÇÃO (João):
- Brasil Participativo: plataforma do Governo Federal, fork do Decidim mantido pelo LAPPIS. Avaliamos o commit 176b046 do decidim-govbr.
- A avaliação apoia três decisões da Fase 1: D1 refatoração (LAPPIS), D2 autenticação e autorização (Dataprev e MGI), D3 fluxos cidadãos (Secretaria de Participação Digital).
- Todo o resto da apresentação volta a essas três decisões.
-->

- **D1, Refatoração**: priorizar as partes do código que mais pesam na manutenção. Quem decide: LAPPIS
- **D2, Autenticação e autorização**: revisar permissões e dependências vulneráveis. Quem decide: Dataprev e MGI
- **D3, Fluxos cidadãos**: redesenhar telas e formulários que causam desistência. Quem decide: Secretaria de Participação Digital

---

## 2. Modelo e GQM

<p class="apresentador">João Victor da Silva Batista de Farias</p>

<!--
NOTA PARA APRESENTAÇÃO (João):
- ISO/IEC 25010:2023, três características, um objetivo GQM para cada, três questões por objetivo, 12 métricas.
- Mostrar uma linha de cada objetivo com o nível aceitável, que é o limite da faixa Bom da Fase 2.
-->

| Objetivo | Questões e nível aceitável |
| :--- | :--- |
| G1, Capacidade de Interação | Q1.1 TCR ≥ 75% e TME ≤ 120 s; Q1.2 FET ≤ 1,0; Q1.3 ICA ≥ 85% e SUS ≥ 68 |
| G2, Manutenibilidade | Q2.1 TSN ≤ 25%; Q2.2 CCM ≤ 7 e DLC médio ≤ 100; Q2.3 ICT ≥ 70% |
| G3, Segurança | Q3.1 nenhum alerta alto e DVC ≤ 7; Q3.2 CDV ≤ 1; Q3.3 TPE ≥ 95% |

---

## 3. Como Coletamos

<p class="apresentador">Davi Mesquita Sousa</p>

<!--
NOTA PARA APRESENTAÇÃO (Davi):
- Nenhum teste contra a produção. Tudo no commit 176b046, com data, ferramenta e responsável registrados em cada página de dados.
- Análise estática (G2 e G3): RuboCop e coletor com Ripper, Brakeman 8.1.0, bundler-audit 0.9.3 e script próprio da M3.3.
- Sessões (G1): três participantes com TCLE, cópia local via docker compose, tela gravada no OBS sem áudio.
- Inspeção automática (M1.4): axe-core e Lighthouse nas quatro páginas, com a conta de teste logada.
- O login Gov.br não funciona fora da produção; as sessões usaram o login de estrangeiro.
-->

- **Análise estática**: G2 e G3, em 03/11 e 08/11
- **Sessões com usuários**: G1, em 22/11, com P02, P03 e P04 e TCLE assinado
- **Inspeção automática**: M1.4, em 22/11, com axe-core 4.14 e Lighthouse 13.6
- **Ambiente**: cópia local em modo de desenvolvimento, num notebook Lenovo com Ubuntu e Firefox

---

## 4. G1: As Sessões

<p class="apresentador">Miguel Arthur Oliveira de Lima</p>

<!--
NOTA PARA APRESENTAÇÃO (Miguel):
- O tempo vem da gravação: começa no quadro em que a tela da tarefa aparece, momento em que o observador dava o comando, e termina no estado final.
- T1: P03 e P02 clicaram em "Entrar com gov.br" e caíram no login simulado; P02 errou a senha.
- T2: foi a tarefa mais afetada pela build local. O botão "WAI WCAG" cobria o menu, e o banco só tinha o processo de teste, então a busca por "processo" não achou nada e o carrossel levava a processos inexistentes. Todos precisaram de ajuda.
- T3: P03 enviou descrição com 14 caracteres e a mensagem não disse o que corrigir.
- T4: P02 votou numa proposta alheia e recebeu erro 500 ao retirar votos.
- As contas p02 e p04 foram usadas trocadas; as fichas usam o código do perfil (P02, mais de 50 anos; P04, usuário do Gov.br).
-->

| Participante | T1 | T2 | T3 | T4 |
| :--- | :---: | :---: | :---: | :---: |
| P02 | 108,8 s, com ajuda, 2 erros | 73,8 s, com ajuda, 1 erro | 104,5 s | 107,1 s, com ajuda, 3 erros |
| P03 | 51,7 s, com ajuda, 1 erro | 83,0 s, com ajuda, 1 erro | 93,1 s, com ajuda, 1 erro | 38,1 s |
| P04 | 31,4 s | 19,7 s, com ajuda | 49,6 s | 5,2 s |

Fonte: [Dados de interação](../dados/interacao/index.md).

---

## 5. G1: Resultados

<p class="apresentador">Mateus Vinícius Vieira</p>

<!--
NOTA PARA APRESENTAÇÃO (Mateus):
- TCR abaixo de 75% nas quatro tarefas; é a regra da Fase 2 que indica barreira ao cidadão.
- Quem concluiu sozinho ficou dentro do tempo aceitável. FET no limite.
- Contraste: SUS de 80 mesmo com ajuda em várias tarefas. O SUS mede percepção.
-->

| Métrica | Resultado | Faixa |
| :--- | :--- | :--- |
| TCR | 33,3% · 0% · 66,7% · 66,7% | Insuficiente e Regular |
| TME | 31,4 s · indisponível · 77,1 s · 21,7 s | Excelente e Bom |
| FET | 1,00 · 0,67 · 0,33 · 1,00 | Bom e Excelente |
| ICA | 91,2% | Bom |
| SUS | 80,0 | Excelente |

---

## 6. G1: Acessibilidade

<p class="apresentador">Davi Mesquita Sousa</p>

<!--
NOTA PARA APRESENTAÇÃO (Davi):
- ICA de 91,2%: 196 de 215 verificações automáticas aprovadas; 48 itens sem decisão.
- As falhas se repetem nas quatro páginas: links feitos só de imagem, botões do cabeçalho com nome acessível diferente do texto, imagens sem texto alternativo e um título fora de ordem.
- O que a ferramenta não viu: a caixa de erro do formulário de proposta tem o aria-label "Data de início do afastamento inválida", copiado de outra tela.
-->

- **ICA**: 91,2% (axe 91,7%; Lighthouse 90,6%), faixa Bom
- **Falhas**: link sem nome acessível, nome diferente do texto visível, imagem sem texto alternativo e título fora de ordem
- **Fora do alcance da ferramenta**: `aria-label` errado na caixa de erro do formulário de proposta

Fonte: [Dados de acessibilidade](../dados/acessibilidade/index.md).

---

## 7. G2: Manutenibilidade

<p class="apresentador">Lucca Medeiros Silva</p>

<!--
NOTA PARA APRESENTAÇÃO (Lucca):
- TSN 60,14% e ICT 39,43%, ambos Insuficientes: dispara a regra da Fase 2 de risco de quebra ao atualizar o Decidim.
- Médias de complexidade e de tamanho no aceitável, com picos em permissions.rb (47) e form_builder.rb (595 linhas).
-->

| Métrica | Resultado | Faixa |
| :--- | :--- | :--- |
| TSN | 175 de 291 classes, 60,14% | Insuficiente |
| CCM | média 2,29; máximo 47 | Excelente pela média |
| DLC | média 67,03; máximo 595 | Insuficiente pelo máximo |
| ICT | 69 de 175 sobrescritas, 39,43% | Insuficiente |

---

## 8. G3: Segurança

<p class="apresentador">José Vinícius Alvares Soares de Queiroz</p>

<!--
NOTA PARA APRESENTAÇÃO (José):
- Dois alertas de confiança alta (Rails e Ruby sem suporte) classificam a segurança como Insuficiente e exigem chamado.
- Das 13 ações sem proteção, oito foram criadas pelo decidim-govbr.
-->

| Métrica | Resultado | Faixa |
| :--- | :--- | :--- |
| DVC | 22, com 2 alertas altos e 8 médios | Insuficiente |
| CDV | 156 pares (gem, CVE) em 51 gems | Insuficiente |
| TPE | 136 de 149 ações, 91,3% | Regular |

---

## 9. Respostas às Questões

<p class="apresentador">José Vinícius Alvares Soares de Queiroz</p>

<!--
NOTA PARA APRESENTAÇÃO (José):
- As hipóteses foram registradas na Fase 2, antes da coleta.
- Confirmadas: H2.1, H2.2, H2.3, H3.2. Em parte: H1.2, H1.3. Refutadas: H1.1, H3.1, H3.3.
- Destaque: na H1.1, a menor taxa foi achar o processo, e não enviar a proposta.
-->

| Situação | Hipóteses |
| :--- | :--- |
| Confirmada | H2.1, H2.2, H2.3, H3.2 |
| Confirmada em parte | H1.2, H1.3 |
| Refutada | H1.1, H3.1, H3.3 |

Fonte: [Fase 4](../fases/4.md), Tabela 2.

---

## 10. Relações entre as Características

<p class="apresentador">Mateus Vinícius Vieira</p>

<!--
NOTA PARA APRESENTAÇÃO (Mateus):
- O erro 500 da T4 vem do botão de voto sobrescrito, que chama um método existente só no ProposalsController.
- A mensagem vaga da T3 está fixa no controller sobrescrito; o aria-label errado está no formulário sobrescrito.
- As ações de selos sem permissão estavam num controller criado sem teste, corrigido na #80.
-->

- **Manutenibilidade → Interação**: botão de voto sobrescrito causa erro 500 na T4
- **Manutenibilidade → Interação**: mensagem fixa e `aria-label` errado no formulário sobrescrito
- **Manutenibilidade → Segurança**: ações de selos criadas sem verificação de permissão

---

## 11. Julgamento por Objetivo

<p class="apresentador">João Victor da Silva Batista de Farias</p>

<!--
NOTA PARA APRESENTAÇÃO (João):
- G1 atingido em parte; G2 e G3 não atingidos. As três regras de decisão da Fase 2 foram disparadas.
- D1 e D2 têm evidência suficiente para começar; D3 tem evidência em parte, pela amostra e pela repetição.
-->

| Objetivo | Julgamento | Regra disparada |
| :--- | :--- | :--- |
| G1 | Atingido em parte | Redesenho do formulário de propostas |
| G2 | Não atingido | Refatoração em *engines* isoladas |
| G3 | Não atingido | Chamado de segurança junto ao LAPPIS |

---

## 12. Recomendações e Melhorias

<p class="apresentador">João Victor da Silva Batista de Farias, Lucca Medeiros Silva e José Vinícius Alvares Soares de Queiroz</p>

<!--
NOTA PARA APRESENTAÇÃO:
- João: recomendações por decisão, com prioridade alta quando a regra exige ação.
- Lucca: melhoria #73, testes de regressão numa sobrescrita sem teste.
- José: melhoria #80, verificação de permissão nas ações de selos, modelo para as outras 12 ações.
-->

- **D1 (LAPPIS)**: testes de requisição nos fluxos de voto e proposta antes de refatorar; corrigir o erro 500
- **D2 (Dataprev e MGI)**: chamado de segurança; atualizar Ruby, Rails e gems; proteger as ações da M3.3
- **D3 (Secretaria)**: mínimo de caracteres e erro junto do campo; repetir a T2 com dados reais antes de mexer na navegação; nomes acessíveis
- **Executadas**: [melhoria #73](../dados/melhoria-73/index.md) e [melhoria #80](../dados/melhoria-80/index.md)

---

## 13. Gestão do Projeto

<p class="apresentador">Davi Mesquita Sousa e Miguel Arthur Oliveira de Lima</p>

<!--
NOTA PARA APRESENTAÇÃO (Davi e Miguel):
- Medição do Sprint 3 (04/11) e as decisões que ela gerou: critério de Pronto revisto, escopo replanejado, main exigindo PR.
- N3 a N5 ficaram sem cálculo porque horas e datas não estavam nas issues.
-->

| Indicador | Sprint 3 | Decisão |
| :--- | :--- | :--- |
| N1 | 1 de 17 itens no critério de Pronto | Critério de Pronto revisto |
| N2 | 20% concluído com 32% do prazo | Escopo replanejado |
| N3 a N5 | Não calculáveis | Horas e datas preenchidas ao fechar cada issue |
| N6 | 1 de 9 integrações revisada por outra dupla | A `main` passou a exigir PR |

Fonte: [Gestão](../gestao.md), Tabela 15.

---

## 14. Limites e Lições

<p class="apresentador">Mateus Vinícius Vieira</p>

<!--
NOTA PARA APRESENTAÇÃO (Mateus):
- Limites: 3 participantes, sessões repetidas, elementos do modo de desenvolvimento, ICA só automático, Gov.br não avaliado.
- Lições: testar a gravação antes, contas novas por sessão, script de cálculo publicado com os dados.
-->

- **Limites**: amostra de 3, sessões repetidas, build local (menu coberto e banco quase vazio na T2), ICA só automático e login Gov.br não avaliado
- **Lições**: testar a gravação antes da sessão, usar contas sem uso anterior, popular o banco da cópia local e publicar o script de cálculo com os dados

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 22/11/2026 | Apresentação final no visual do PC1, com PDF, roteiro e notas por apresentador (#84) | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `1.1` | 22/11/2026 | Códigos de P02 e P04 corrigidos e efeito da build local na T2 | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
