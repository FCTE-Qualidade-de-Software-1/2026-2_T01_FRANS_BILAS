---
icon: lucide/users
---

# Dados da Coleta: Capacidade de Interação (G1)

Esta página reúne os registros das sessões com usuários, de onde saem as métricas M1.1, M1.2, M1.3 e M1.5 definidas na [Fase 2](../../fases/2.md) e planejadas na [Fase 3](../../fases/3.md). A inspeção de acessibilidade (M1.4) não usa estas fichas.

**Situação em 17/11/2026**: nenhuma sessão registrada. As fichas desta pasta têm só o cabeçalho, e nenhum valor de TCR, TME, FET ou SUS pode ser calculado a partir delas. O julgamento do objetivo G1 fica para a Fase 4.

---

## 1. Execução

A Tabela 1 identifica a execução. Os campos em aberto são preenchidos na primeira sessão, como pede o passo 4 dos [Procedimentos de coleta](../../procedimentos/coleta.md).

**Tabela 1. Registro da execução das sessões.**

| Item | Valor |
| :--- | :--- |
| Repositório e commit | `decidim-govbr`, commit `176b04673d956af4b1ab645e922cedd796b6a22e` |
| Condução das sessões | Mateus Vinícius Vieira (issue #90) |
| Rotulagem por métrica | Miguel Arthur Oliveira de Lima (issue #72) |
| Datas das sessões, com fuso | A preencher |
| Máquina, sistema e navegador | A preencher |
| Processo participativo usado em T2 | A preencher |
| Proposta de teste usada em T4 | A preencher |
| URLs iniciais de T1 a T4 | A preencher |
| Sessões realizadas e sessões com gravação autorizada | A preencher |

Fonte: elaborado pela equipe.

Dois desvios do plano já estão registrados. A Fase 3 previa as sessões de 06/11 a 10/11, e até 17/11 não há registro de sessão realizada. A condução passou de João Victor da Silva Batista de Farias para Mateus Vinícius Vieira, a pedido de João. As novas datas entram na Tabela 1 e no cronograma da Fase 3.

---

## 2. Arquivos

A Tabela 2 liga cada arquivo à métrica que ele alimenta. Os nomes dos campos são os da Tabela 2 dos Procedimentos de coleta.

**Tabela 2. Arquivos das sessões e métricas correspondentes.**

| Arquivo | Conteúdo | Métrica |
| :--- | :--- | :---: |
| [`M1.1-M1.3-ficha.csv`](M1.1-M1.3-ficha.csv) | Uma linha por participante e tarefa: desfecho, ajuda, tempo e contagem de erros | M1.1, M1.2, M1.3 |
| [`M1.3-eventos.csv`](M1.3-eventos.csv) | Uma linha por erro observado: instante, ação do participante e resposta da plataforma | M1.3 |
| [`M1.5-sus.csv`](M1.5-sus.csv) | Uma linha por participante, com as respostas de 1 a 5 aos dez itens | M1.5 |

Fonte: elaborado pela equipe.

Valores aceitos na ficha:

- `participante`: código de `P01` a `P05`, que corresponde aos perfis P1 a P5 da Seção 2.1.1 da Fase 3.
- `tarefa`: `T1` a `T4`.
- `status`: `concluida`, `falhou`, `desistiu` ou `nao_iniciada`.
- `ajuda`, `tempo_valido`: `sim` ou `nao`.
- `fonte_tempo`: `video` ou `cronometro`.
- `duracao_s`: segundos, com uma casa decimal.
- `erros`: número inteiro, igual à quantidade de linhas do participante e da tarefa em `M1.3-eventos.csv`.

Uma resposta em branco no SUS fica em branco no arquivo. O questionário incompleto sai da média, e a quantidade excluída é informada junto com o resultado.

---

## 3. Roteiro do observador

O roteiro abaixo ordena o que os Procedimentos de coleta e o [TCLE](../../tcle.md) já definem. Ele não muda nenhuma regra de contagem.

**Antes de cada sessão**

1. Abra a cópia local no commit da Tabela 1 e confirme que as integrações com serviços reais estão desligadas.
2. Deixe a plataforma no estado inicial de T1: página inicial, sessão encerrada e conta de teste disponível.
3. Confira que o processo participativo está com propostas abertas e que a conta de teste ainda não apoiou a proposta de T4.
4. Separe o TCLE (duas vias impressas ou o formulário digital), o questionário SUS e as três fichas.

**Durante a sessão**

1. Entregue o TCLE e espere a assinatura e a escolha sobre a gravação. Sem o termo assinado, a sessão não acontece.
2. Diga ao participante que a avaliação é da plataforma, e não dele.
3. Inicie a gravação da tela, se autorizada. Sem autorização, use o cronômetro.
4. Leia a instrução de cada tarefa, uma por vez, sem indicar o caminho na interface.
5. Inicie o tempo quando o participante começar a ler a instrução. Pare na conclusão observável da tarefa ou na desistência.
6. Anote cada erro em `M1.3-eventos.csv` no momento em que acontece. Se você ajudar, marque `ajuda=sim` na ficha.
7. Prepare o estado inicial da tarefa seguinte fora da contagem de tempo.
8. Depois de T4, entregue o questionário SUS e não comente as respostas.

**Depois da sessão**

1. Preencha as quatro linhas do participante em `M1.1-M1.3-ficha.csv` e a linha dele em `M1.5-sus.csv`.
2. Guarde o termo assinado, a gravação e a planilha que liga nome e código na pasta restrita da equipe.
3. Devolva a plataforma ao estado inicial de T1 e confira de novo o estado inicial de T4 antes da próxima sessão.

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
