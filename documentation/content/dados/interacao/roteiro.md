---
icon: lucide/clipboard-list
---

# Roteiro das Sessões com Usuários: Capacidade de Interação

Este roteiro conduz as três sessões do objetivo G1 com os perfis P02 (pessoa com mais de 50 anos), P03 (estudante de ciências humanas ou sociais) e P04 (usuário frequente do Gov.br). Cada sessão leva de 20 a 30 minutos e gera os dados de M1.1, M1.2, M1.3 e M1.5. As regras vêm dos [Procedimentos de coleta](../../procedimentos/coleta.md) e do [TCLE](../../tcle.md).

---

## 1. Antes de tudo: o ambiente local

As sessões só podem acontecer numa cópia local da plataforma. O TCLE assinado promete "ambiente de testes local" e "conta fictícia", e o plano proíbe testes na produção. Não use o site oficial do Brasil Participativo: as propostas seriam reais e ficariam públicas.

Até 17/11, a [Fase 3](../../fases/3.md) registra que a cópia local (issue #64) não tinha instância documentada. Confirme com quem cuida da #64 se ela está rodando antes de marcar as sessões.

Para subir a cópia:

1. Use o código no commit avaliado: [`decidim-govbr`, commit `176b046`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/tree/176b04673d956af4b1ab645e922cedd796b6a22e).
2. Siga a [wiki do projeto](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/wikis/home), nas páginas "Rodando o projeto via Docker" e "Configuração do ambiente".
3. Desligue as integrações que enviam dados para serviços reais e use apenas login local de teste, sem Gov.br.
4. Crie a massa de teste: uma conta de teste por participante, um processo participativo com propostas abertas e uma proposta que essas contas ainda não apoiaram.
5. Abra cada página da Tabela 2 no navegador e anote a URL. Elas mudam conforme a massa de dados.

Comandos (no Windows, pelo Git Bash), conforme a wiki "Rodando o projeto via Docker":

```bash
git clone -c core.autocrlf=false https://gitlab.com/lappis-unb/decidimbr/decidim-govbr.git
cd decidim-govbr
git checkout 176b04673d956af4b1ab645e922cedd796b6a22e
docker compose up
```

O `core.autocrlf=false` evita que o Windows troque as quebras de linha dos scripts, o que impediria o `start.sh` de rodar dentro do contêiner. Na primeira execução, o Docker baixa as imagens (a do LAPPIS tem cerca de 2 GB) e o `start.sh` cria e migra o banco.

**Tabela 1. Endereços da cópia local.**

| Endereço | Para quê |
| :--- | :--- |
| `http://localhost:3000/system` | Login do administrador do sistema, com `ADMIN_EMAIL` e `ADMIN_PASSWORD` do arquivo `.env.dev` |
| `http://localhost:3000` | Plataforma usada nas sessões |
| `http://127.0.0.1:1080` | Mailcatcher: recebe os e-mails de convite e de confirmação de conta |

Fonte: wiki do `decidim-govbr`, página "Rodando o projeto via Docker".

No primeiro login em `/system`, crie a organização com host `localhost`, português como idioma padrão e cadastro de participantes permitido. Aceite o convite do administrador pelo Mailcatcher. Em seguida, no painel de administração, crie o processo participativo com o componente de Propostas aberto para envio e apoio, uma proposta para a T4 e as três contas de teste.

**Tabela 2. Massa de dados a anotar antes da primeira sessão.**

| Item | Preencher |
| :--- | :--- |
| Página inicial (início da T1) | `http://localhost:3000/?locale=pt-BR`, sem ninguém logado |
| Contas de teste (e-mail de cada uma; a senha fica fora do repositório) | `p02@teste.local`, `p03@teste.local` e `p04@teste.local`. Na aplicação, P02 usou `p04@teste.local` e P04 usou `p02@teste.local` (ver Seção 8) |
| Processo participativo da T2 (nome e URL) | Praças e Parques do Bairro: `http://localhost:3000/processes/pracas-e-parques-teste` |
| Formulário de nova proposta da T3 | `http://localhost:3000/processes/pracas-e-parques-teste/f/31/proposals/new` |
| Proposta votada na T4 | A proposta que o próprio participante publicou na T3. A proposta 1, "Instalar bebedouros nas praças do bairro" (`http://localhost:3000/processes/pracas-e-parques-teste/f/31/proposals/1`), ficou na lista do processo |
| Texto de teste da proposta da T3 (título e descrição) | Título: "Colocar mais bancos e sombra no parque". Descrição: "O parque tem poucos bancos e quase nenhuma sombra. Proponho instalar bancos novos e plantar árvores perto da pista de caminhada." |
| Navegador e versão; sistema operacional | Firefox (versão não registrada); Ubuntu, num notebook Lenovo |

Fonte: massa de dados criada na cópia local em 22/11/2026. A proposta 1 é de autoria da conta `autor@teste.local` (Equipe de Teste), que não participa das sessões.

Se a cópia local não subir a tempo, as sessões não podem acontecer como o TCLE descreve. Nesse caso, as métricas M1.1 a M1.5 continuam como não calculáveis na [Fase 4](../../fases/4.md).

---

## 2. Materiais

**Tabela 3. Materiais de cada sessão.**

| Material | Onde está | Observação |
| :--- | :--- | :--- |
| TCLE | [Página do TCLE](../../tcle.md) | Já assinado pelos três. Confira a opção de gravação de tela marcada por cada um; o áudio fica desligado |
| Ficha das tarefas | [`M1.1-M1.3-ficha.csv`](M1.1-M1.3-ficha.csv) | Uma linha por participante e tarefa |
| Ficha de erros | [`M1.3-eventos.csv`](M1.3-eventos.csv) | Uma linha por erro |
| Respostas do SUS | [`M1.5-sus.csv`](M1.5-sus.csv) | Uma linha por participante |
| Questionário SUS | Lourenço, Carmona e Lopes (2022) | Copie os 10 itens em português do artigo, sem mudar a redação, para papel ou Google Forms |
| Cronômetro | Celular ou cronômetro online | Obrigatório quando não há gravação |
| Gravação de tela (opcional) | [OBS Studio](https://obsproject.com/) ou a gravação do Google Meet | Só para quem autorizou. Microfone desligado |
| Roteiro e protocolo | [Dados de interação](index.md) e [Procedimentos de coleta](../../procedimentos/coleta.md) | Fonte das regras deste roteiro |

Fonte: elaborado pela equipe.

A gravação de tela não é obrigatória. Sem gravação, o tempo vem do cronômetro (`fonte_tempo = cronometro`) e os erros são anotados na hora. Com gravação:

- **Presencial**: o participante usa o seu computador e o OBS grava a tela, com a captura de áudio desativada.
- **Remota**: o participante entra no Google Meet e compartilha a tela; você grava pelo Meet, se a conta permitir, ou pelo OBS. Para isso, a cópia local precisa estar acessível pela máquina dele, ou ele controla a sua tela pelo compartilhamento.

A gravação não vai para o GitHub. Ela fica na pasta restrita do Drive da equipe e é apagada no fim do semestre.

---

## 3. Agenda e preparação

Reserve 30 minutos por sessão e 10 minutos entre elas para devolver a plataforma ao estado inicial.

**Tabela 4. Agenda das sessões.**

| Código | Perfil | Data e hora | Modalidade | Gravação de tela autorizada? |
| :---: | :--- | :--- | :--- | :--- |
| P02 | Pessoa com mais de 50 anos | | | |
| P03 | Estudante de ciências humanas ou sociais | | | |
| P04 | Usuário frequente do Gov.br | | | |

Fonte: elaborado pela equipe.

Cada participante usa a própria conta de teste. Na T4 a conta vota na proposta que acabou de publicar na T3. Com três contas, uma para cada código, as propostas e os votos de um participante não aparecem como se fossem do outro.

Checklist antes de cada sessão:

- [ ] Cópia local rodando no commit `176b046`
- [ ] Navegador na página inicial, com a sessão encerrada (sem ninguém logado)
- [ ] Conta de teste do participante funcionando e sem uso anterior (nenhuma proposta nem voto)
- [ ] Processo participativo com propostas abertas
- [ ] Texto de teste da T3 impresso ou num papel para entregar
- [ ] TCLE assinado conferido, com a opção de gravação
- [ ] Cronômetro zerado e, se autorizado, OBS pronto com o microfone desligado
- [ ] Folha de anotação (Seção 5) e questionário SUS à mão

---

## 4. Roteiro de fala

**Abertura (fora do tempo)**

> "Obrigado por participar. Hoje vamos testar a plataforma Brasil Participativo numa cópia de teste, sem nenhum dado seu. Quem está sendo avaliada é a plataforma, não você: se algo for difícil, a culpa é do sistema. Vou ler quatro tarefas, uma por vez. Tente fazer sozinho, do jeito que faria em casa. Se quiser parar ou fazer uma pausa, é só avisar."

Se houver gravação autorizada, comece a gravar agora.

**As quatro tarefas.** Leia exatamente a instrução, sem mostrar onde clicar. O tempo começa quando o participante começa a ler e para na conclusão ou na desistência.

**Tabela 5. Instruções das tarefas.**

| Tarefa | O que você lê | Situação inicial | Termina quando |
| :---: | :--- | :--- | :--- |
| T1 | "Entre na plataforma com a conta de teste fornecida." (entregue e-mail e senha no papel) | Página inicial, ninguém logado | A tela mostra a conta logada |
| T2 | "Encontre o processo participativo [nome do processo]." | Página inicial, já logado | A página do processo está aberta |
| T3 | "Envie uma proposta nesse processo usando este texto." (entregue o texto de teste) | Página do processo, propostas abertas | A proposta foi publicada e aparece a confirmação |
| T4 | "Vote na proposta que você acabou de enviar." | Página da proposta publicada na T3 | O voto aparece registrado na tela |

Fonte: Tabela 1 dos [Procedimentos de coleta](../../procedimentos/coleta.md).

Entre uma tarefa e outra, pare o cronômetro e deixe a tela no ponto de partida da próxima. Não existe limite de tempo.

Se o participante pedir ajuda, responda primeiro: "Faça como acharia mais natural." Se ele continuar travado e você precisar orientar, ajude e marque `ajuda = sim` naquela tarefa.

**Encerramento**

> "Acabaram as tarefas. Agora são 10 frases sobre a sua experiência. Marque de 1, discordo fortemente, a 5, concordo fortemente. Não tem resposta certa."

Entregue o SUS e não comente as respostas. No fim: "Muito obrigado. Seus dados aparecem só como um código, nunca com o seu nome."

---

## 5. Como anotar

Use uma folha por participante, preenchida à mão durante a sessão.

**Folha de anotação.** Participante: ____ Data: ____ Fonte do tempo: vídeo / cronômetro

| Tarefa | Início | Fim | Duração (s) | Status | Ajuda | Nº de erros | Interrupção / observação |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T1 | | | | | | | |
| T2 | | | | | | | |
| T3 | | | | | | | |
| T4 | | | | | | | |

Status: `concluida`, `falhou`, `desistiu` ou `nao_iniciada`.

**Registro de erros.** Uma linha por erro, na hora em que acontece.

| Tarefa | Instante | O que o participante fez | O que a plataforma respondeu |
| :---: | :--- | :--- | :--- |
| | | | |
| | | | |
| | | | |

Regras de contagem:

1. Erro é um desvio sem querer: clicar no lugar errado achando que era o certo, ou enviar um formulário inválido. Explorar a tela por curiosidade não conta.
2. Um envio inválido conta um erro, mesmo com várias mensagens na tela. Uma nova tentativa inválida conta outro.
3. Tempo com uma casa decimal, em segundos, tirado do cronômetro ou do vídeo. Nunca estime de memória.
4. Se algo externo interromper (ligação, queda de internet), anote o motivo e marque o tempo como inválido.
5. Desistências e falhas ficam na amostra. Elas entram no cálculo da taxa de conclusão.

---

## 6. Questionário SUS

1. Use os 10 itens da versão em português de Lourenço, Carmona e Lopes (2022), na ordem do artigo e sem mudar a redação. Os três participantes respondem à mesma versão.
2. Cada item vai de 1 (discordo fortemente) a 5 (concordo fortemente).
3. Resposta em branco fica em branco. O questionário incompleto sai da média, e você informa quantos saíram.

Cálculo de cada participante:

- Itens ímpares (1, 3, 5, 7 e 9): resposta − 1.
- Itens pares (2, 4, 6, 8 e 10): 5 − resposta.
- Some as 10 parcelas e multiplique por 2,5. O resultado vai de 0 a 100.

Exemplo: se as parcelas somam 28, o SUS é 28 × 2,5 = 70 pontos. Pela [Fase 2](../../fases/2.md), de 68 a 79 pontos fica na faixa Bom.

---

## 7. Depois de cada sessão

1. Passe a folha para as fichas CSV, usando só o código do participante:
    - `M1.1-M1.3-ficha.csv`: 4 linhas (T1 a T4). O campo `erros` tem que bater com a quantidade de linhas daquela tarefa em `M1.3-eventos.csv`.
    - `M1.3-eventos.csv`: uma linha por erro anotado.
    - `M1.5-sus.csv`: uma linha com R1 a R10.
2. Guarde no Drive restrito da equipe, fora do GitHub: o TCLE assinado, a gravação (se houver) e a planilha que liga nome e código.
3. Volte a plataforma ao início da T1: deslogue e confira a conta do próximo participante.
4. Depois das três sessões, preencha a Tabela 1 da página [Dados de interação](index.md): datas com fuso, máquina, navegador, processo e proposta usados, URLs e quantas sessões tiveram gravação.

Exemplo de linha da ficha de tarefas:

```csv
participante,tarefa,data,commit,estado_inicial,status,ajuda,inicio,fim,duracao_s,tempo_valido,fonte_tempo,erros,interrupcao,observacao
P04,T1,2026-11-22,176b046,pagina inicial sem login,concluida,nao,,,48.3,sim,cronometro,1,,errou a senha uma vez
```

Com três participantes, a amostra fica menor que a meta de cinco do plano. Registre isso na Fase 4 junto com os resultados.

---

## 8. Registro da aplicação em 22/11/2026

- As sessões usadas nas fichas são as três gravadas em 22/11/2026 (UTC−3): P04 às 20:31:03, P03 às 20:33:32 e P02 às 20:38:48. Os arquivos ficam na pasta restrita como `p02.mp4`, `p03.mp4` e `p04.mp4`, nomeados pela conta usada.
- As contas foram usadas trocadas: P02 (mais de 50 anos) entrou com `p04@teste.local` e aparece em `p04.mp4`; P04 (usuário frequente do Gov.br) entrou com `p02@teste.local` e aparece em `p02.mp4`. O observador identificou a troca depois da coleta. As fichas e o SUS usam o código do perfil, como define a Fase 3, e o campo `observacao` da ficha registra a conta de cada linha.
- Antes dessas sessões, entre 19:50 e 20:25, as mesmas contas fizeram as tarefas em outras rodadas. As gravações dessas rodadas travaram num quadro fixo, e as rodadas das 19:50 e das 19:55 com a conta `p02` foram testes da equipe. Por isso, nas sessões gravadas, os participantes já conheciam o caminho, e o Firefox sugeria o e-mail e os títulos digitados antes. Isso favorece os tempos e precisa constar no julgamento.
- A T4 aplicada foi votar na proposta que o próprio participante publicou na T3, e não na proposta 1. A Tabela 5 já traz essa versão.
- O tempo vem das gravações. O início de cada tarefa é o primeiro quadro em que a tela inicial da tarefa aparece, porque o observador dava o comando nesse momento. A T1 começa no primeiro quadro da gravação, já na página inicial sem login. O fim é o primeiro quadro do estado final. Como o fim de uma tarefa é a tela inicial da seguinte, as tarefas ficam encadeadas. Quando a página carregava primeiro sem estilo, contou o primeiro quadro com a página já montada.
- Os erros vêm das gravações, conferidas com o log do servidor. As tentativas de abrir o menu coberto pelo botão "WAI WCAG" não ficam claras no vídeo e não entraram na contagem.
- O observador só orientou em quatro situações: depois de um envio inválido da proposta (pediu para ler o texto com atenção), quando o login dava erro (indicou o login de estrangeiro), quando um clique levava a uma URL quebrada e depois de cerca de dois erros ao tentar abrir o menu. Nessas tarefas, a ficha marca `ajuda = sim`. Na T4 de P02, o observador confirmou que orientou depois dos erros 500.
- Votos e visitas à proposta 1 feitos por iniciativa do participante não contam como erro (regra 1 da Seção 5).
- A plataforma respondeu com erro 500 quando P02 tentou retirar votos e com a página "Routing Error" quando P03 e P02 clicaram num destaque do carrossel. Os cliques contam como erro do participante. A resposta da plataforma fica registrada em `M1.3-eventos.csv`.
- A T2 foi a tarefa mais afetada pela build local. O botão "WAI WCAG" do modo de desenvolvimento cobria o menu, e o banco tinha só o processo de teste: a página inicial não listava processos, a busca por "processo" não retornou nada e os destaques do carrossel apontavam para processos que não existem na cópia local. Na produção, com o banco completo, esses obstáculos podem não aparecer.
- O botão "WAI WCAG", que cobria o menu, e a página "Routing Error" fazem parte do modo de desenvolvimento da cópia local. Eles não existem na produção, e isso precisa constar no julgamento da Fase 4.
- O questionário SUS foi respondido num formulário digital com os dez itens do artigo, mas com as pontas da escala escritas como "Discordo totalmente" e "Concordo totalmente". O artigo usa "fortemente". O formulário não registrou a data. As respostas foram transcritas das capturas de tela do formulário preenchido.

---

## Referências

- BROOKE, J. SUS: A "Quick and Dirty" Usability Scale. In: JORDAN, P. W. et al. (ed.). *Usability Evaluation in Industry*. London: Taylor & Francis, 1996. p. 189-194.
- LOURENÇO, D. F.; CARMONA, E. V.; LOPES, M. H. B. M. Translation and Cross-Cultural Adaptation of the System Usability Scale to Brazilian Portuguese. *Aquichan*, v. 22, n. 2, e2228, 2022. DOI: [10.5294/aqui.2022.22.2.8](https://doi.org/10.5294/aqui.2022.22.2.8).
- LAPPIS-UnB. *decidim-govbr*, commit `176b046`. Disponível em: <https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/tree/176b04673d956af4b1ab645e922cedd796b6a22e>.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `0.1` | 22/11/2026 | Roteiro das três sessões (P02, P03 e P04), com preparação da cópia local, fala, folha de anotação e cálculo do SUS (issue #90) | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `0.2` | 22/11/2026 | T4 ajustada para a versão aplicada (voto na própria proposta) e registro da aplicação (issue #90) | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `0.3` | 22/11/2026 | Registro refeito com as sessões gravadas das 20:31, 20:33 e 20:38 (issue #90) | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `0.4` | 22/11/2026 | Correção dos códigos de P02 e P04, que usaram as contas trocadas, e efeito da build local na T2 | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
