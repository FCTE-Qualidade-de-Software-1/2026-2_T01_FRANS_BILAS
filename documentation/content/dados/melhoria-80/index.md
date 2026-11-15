---
icon: lucide/shield-check
---

# Melhoria 80: permissão nas ações de selos

Na coleta de [Segurança](../seguranca/index.md), 13 ações sensíveis ficaram sem verificação de permissão. Quatro estão no `ProposalBadgesController`, que o `decidim-govbr` criou para dar e tirar selos das propostas, como o "Mais Votada". Nenhuma das quatro conferia quem estava fazendo a requisição. A issue #80 corrige isso. Ela entra no objetivo G3, na questão Q3.3.

## O que mudou

O [patch](0001-melhoria-80-permissao-selos.patch) foi feito sobre o commit `176b04673d956af4b1ab645e922cedd796b6a22e`, o mesmo da coleta. Ele mexe em dois arquivos.

**Tabela 1. Arquivos alterados pelo patch.**

| Arquivo | Mudança |
| :--- | :--- |
| `app/controllers/decidim/admin/proposal_badges_controller.rb` | 16 linhas novas, nenhuma removida |
| `spec/controllers/decidim/admin/proposal_badges_controller_spec.rb` | Teste novo, com 8 exemplos |

Fonte: `git diff --stat` na cópia de trabalho. Os dois arquivos completos também estão em [`melhorias/80-permissao-selos`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_FRANS_BILAS/tree/main/melhorias/80-permissao-selos).

No controller entraram dois `before_action`, que rodam antes de qualquer ação. O primeiro carrega o componente e o usuário logado. O original já precisava disso: `update_proposal_badge` e `destroy_one_badge` usavam `@component` e `@user` sem nunca preenchê-los. O segundo chama `enforce_permission_to :update, :organization`, a mesma regra que o Decidim usa para editar os dados da organização. Na prática, só um administrador da organização passa. Se o componente for de outra organização, a resposta é `RecordNotFound`. O corpo das ações ficou igual.

## Teste

O teste rodou em 15/11/2026, no `docker-compose.yml` do próprio projeto: imagem `lappis/decidim-govbr:v1-release`, Ruby 3.0.4, Rails 6.1.7.2, Decidim 0.27.2 e PostgreSQL 13.2, com banco de teste local. A produção não foi acessada. O mesmo arquivo de teste rodou duas vezes, primeiro no controller original e depois no corrigido.

**Tabela 2. Resultado dos 8 exemplos no controller original e no corrigido.**

| Exemplo | Original | Corrigido |
| :--- | :---: | :---: |
| Sem login, `destroy_all_badges` | Falha | Passa |
| Sem login, `update` | Passa | Passa |
| Sem login, `destroy_one_badge` | Falha | Passa |
| Sem login, `update_proposal_badge` | Falha | Passa |
| Participante comum, `destroy_all_badges` | Falha | Passa |
| Participante comum, `update` | Passa | Passa |
| Administrador remove os selos do componente | Falha | Passa |
| Administrador com componente de outra organização | Falha | Passa |
| Total | 6 falhas em 8 | 0 falhas em 8 |

Fonte: [rspec-antes.txt](rspec-antes.txt) e [rspec-depois.txt](rspec-depois.txt).

Nos exemplos de acesso negado, o teste espera um redirecionamento com alerta e confere que o comando dos selos não foi chamado. No código original, sem login, `destroy_all_badges` chamou o comando com usuário `nil`, e `update_proposal_badge` só parou porque a proposta usada no teste não existia. Com o administrador logado, o comando também recebia `nil` no lugar do usuário. E o componente de outra organização foi aceito sem erro.

Os dois exemplos de `update` passaram nas duas versões, e por isso não contam como evidência. O componente criado no teste tem `most_voted_rule` igual a 0, e com esse valor a ação redireciona antes de chegar ao comando.

O script `scripts/m33_endpoints.py`, rodado na cópia corrigida, marcou as cinco ações do controller como protegidas pelo `before_action`. O total de ações protegidas passou de 136 para 141.

## O que ficou de fora

O teste revelou outro problema: `destroy_one_badge` chama `DestroyOneProposalBadge`, uma classe que não existe no commit, e quebra com `NameError`. Depois da correção, quem não tem permissão é barrado antes de chegar nessa linha, mas um administrador ainda recebe o erro. Consertar isso não faz parte da #80.

A regra escolhida também deixa de fora quem administra só um processo participativo. Antes, qualquer pessoa conseguia chamar essas ações. Agora, só o administrador da organização. Se o produto precisar liberar os administradores de espaço, a verificação tem que olhar o espaço do componente.

As rotas continuam no `config/routes.rb` principal. A página de Segurança sugeria levá-las para o escopo de administração, mas proteger o controller já cobre todas as rotas, então elas ficaram onde estavam.

O valor oficial de M3.3 continua 91,3%. A [Fase 3](../../fases/3.md) prevê uma coleta só, então não houve nova medição. Com o patch aplicado, as quatro ações de selos sairiam da lista das 13.

O patch não foi enviado ao repositório do `decidim-govbr` no GitLab.

## Como reproduzir

Precisa de uma cópia separada do `decidim-govbr` e de Docker com Compose v2.

```bash
git clone <decidim-govbr> decidim-govbr-melhoria-80
cd decidim-govbr-melhoria-80
git checkout 176b04673d956af4b1ab645e922cedd796b6a22e
git apply 0001-melhoria-80-permissao-selos.patch

docker compose up -d postgres redis-cache redis-queue
docker compose run --rm \
  -e RAILS_ENV=test \
  -e DATABASE_HOST=postgres \
  -e DATABASE_USERNAME=postgres \
  -e DATABASE_PASSWORD=postgres \
  decidim-service \
  bash -lc "bin/rails db:create db:schema:load && bundle exec rspec spec/controllers/decidim/admin/proposal_badges_controller_spec.rb"
```

Para ver o resultado do original, volte só o controller com `git checkout -- app/controllers/decidim/admin/proposal_badges_controller.rb` e rode o `rspec` de novo.

Issue #80, feita por José Vinícius Alvares Soares de Queiroz em 15/11/2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 15/11/2026 | Permissão nas ações de selos, com teste antes e depois | [José Vinícius Alvares Soares de Queiroz](https://github.com/JoseViniciusQueiroz) | A definir |
