# frozen_string_literal: true

require "rails_helper"

module Decidim
  module Admin
    describe ProposalBadgesController, type: :controller do
      include Devise::Test::ControllerHelpers

      let(:organization) { create(:organization) }
      let(:component) { create(:proposal_component, organization: organization) }
      let(:admin) { create(:user, :admin, :confirmed, organization: organization) }
      let(:participant) { create(:user, :confirmed, organization: organization) }

      before do
        request.env["decidim.current_organization"] = organization
        request.env["HTTP_REFERER"] = "http://#{organization.host}/admin"
      end

      shared_examples "acesso negado" do
        it "redireciona com alerta e não altera selos" do
          expect(DestroyBadgeProposals).not_to receive(:call)
          expect(UpdateBadgeProposals).not_to receive(:call)

          perform

          expect(response).to have_http_status(:redirect)
          expect(flash[:alert]).to be_present
        end
      end

      describe "sem login" do
        context "DELETE destroy_all_badges" do
          let(:perform) { delete :destroy_all_badges, params: { component_id: component.id } }

          it_behaves_like "acesso negado"
        end

        context "PATCH update" do
          let(:perform) { patch :update, params: { component_id: component.id, current_component: component.id } }

          it_behaves_like "acesso negado"
        end

        context "DELETE destroy_one_badge" do
          let(:perform) do
            delete :destroy_one_badge, params: { component_id: component.id, proposal_id: 1, badge_id: "mais-votada" }
          end

          it_behaves_like "acesso negado"
        end

        context "PATCH update_proposal_badge" do
          let(:perform) do
            patch :update_proposal_badge, params: { component_id: component.id, proposal_id: 1, badge_id: "mais-votada" }
          end

          it_behaves_like "acesso negado"
        end
      end

      describe "participante sem papel de administrador" do
        before { sign_in participant, scope: :user }

        context "DELETE destroy_all_badges" do
          let(:perform) { delete :destroy_all_badges, params: { component_id: component.id } }

          it_behaves_like "acesso negado"
        end

        context "PATCH update" do
          let(:perform) { patch :update, params: { component_id: component.id, current_component: component.id } }

          it_behaves_like "acesso negado"
        end
      end

      describe "administrador da organização" do
        before { sign_in admin, scope: :user }

        it "executa a remoção dos selos do componente" do
          expect(DestroyBadgeProposals).to receive(:call).with(component, admin)

          delete :destroy_all_badges, params: { component_id: component.id }
        end

        it "não acessa componente de outra organização" do
          other_component = create(:proposal_component)

          expect(DestroyBadgeProposals).not_to receive(:call)
          expect do
            delete :destroy_all_badges, params: { component_id: other_component.id }
          end.to raise_error(ActiveRecord::RecordNotFound)
        end
      end
    end
  end
end
