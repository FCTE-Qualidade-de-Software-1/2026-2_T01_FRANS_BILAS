module Decidim
  module Admin
    class ProposalBadgesController < Decidim::Admin::ApplicationController
      helper_method :manifest, :current_participatory_space

      before_action :set_component_and_user
      before_action :enforce_badge_permission

      def index
        component_id = params[:id]
        @component = Decidim::Component.find(component_id)
        @user = current_user
      end

      def update
        component_id = params[:current_component]
        @component = Decidim::Component.find(component_id)

        if @component.settings.most_voted_rule.zero?
          flash[:alert] = "Não foi possível atualizar os rótulos. Insira quantas propostas você deseja que tenham o rótulo Mais Votada nas configurações do componente."
          redirect_to request.referer
        else
          UpdateBadgeProposals.call(@component, @user) do
            on(:ok) do
              flash[:notice] = "Atualização bem-sucedida!"
              redirect_to request.referer
            end

            on(:invalid) do
              flash[:alert] = "Ocorreu um erro ao atualizar os rótulos."
              redirect_to request.referer
            end
          end
        end
      end

      def update_proposal_badge
        proposal_id = params[:proposal_id]
        badge_name = params[:badge_id]

        UpdateOneProposalBadge.call(@component, proposal_id, badge_name, @user) do
          on(:ok) do
            flash[:notice] = "Atualização bem-sucedida!"
            redirect_to request.referer
          end

          on(:invalid) do
            flash.now[:alert] = "Ocorreu um erro ao atualizar o rótulo."
            redirect_to request.referer
          end
        end
      end

      def destroy_all_badges
        component_id = params[:component_id]
        @component = Decidim::Component.find(component_id)

        DestroyBadgeProposals.call(@component, @user) do
          on(:ok) do
            flash[:notice] = "Rótulo excluído com sucesso!"
            redirect_to request.referer
          end

          on(:invalid) do
            flash.now[:alert] = "Ocorreu um erro ao excluir o rótulo."
            redirect_to request.referer
          end
        end
      end

      def destroy_one_badge
        proposal_id = params[:proposal_id]
        badge_name = params[:badge_id]

        DestroyOneProposalBadge.call(@component, proposal_id, badge_name, @user) do
          on(:ok) do
            flash[:notice] = "Rótulo excluído com sucesso!"
            redirect_to request.referer
          end

          on(:invalid) do
            flash.now[:alert] = "Ocorreu um erro ao excluir o rótulo."
            redirect_to request.referer
          end
        end
      end

      private

      # As rotas usam :component_id; o formulário de update envia :current_component; o index usa :id.
      def set_component_and_user
        @user = current_user
        component_id = params[:component_id] || params[:current_component] || params[:id]
        @component = Decidim::Component.find(component_id) if component_id.present?
      end

      # Só administradores da organização atual alteram selos, e só de componentes dessa organização.
      def enforce_badge_permission
        enforce_permission_to :update, :organization, organization: current_organization
        raise ActiveRecord::RecordNotFound if @component && @component.organization != current_organization
      end

      def proposal_badge_params
        params.require(:proposal_badge).permit(:name, :description) # Ajuste conforme seus parâmetros
      end
    end
  end
end
