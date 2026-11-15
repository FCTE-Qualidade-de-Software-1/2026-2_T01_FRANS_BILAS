# Permissão nas ações de selos

Implementação da issue #80, ligada à Segurança (G3/Q3.3/M3.3). Este diretório guarda o controller corrigido e o teste. O patch aplicável ao produto, as duas saídas do RSpec e a análise estão em [dados da melhoria](../../documentation/content/dados/melhoria-80/index.md).

Os arquivos vão para o `decidim-govbr`, commit `176b04673d956af4b1ab645e922cedd796b6a22e`:

- `proposal_badges_controller.rb` em `app/controllers/decidim/admin/`
- `proposal_badges_controller_spec.rb` em `spec/controllers/decidim/admin/`

Use o patch para não errar os caminhos. O teste rodou no `docker-compose.yml` do próprio projeto: 6 falhas em 8 exemplos no controller original e nenhuma falha no corrigido. A suíte completa da aplicação não foi executada, e a amostra da coleta G3 continua sem alteração.
