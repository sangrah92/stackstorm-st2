from core import azure_vm_deploy

__all__ = [
    'destroy_resource_group'
]
class destroy_resource_group(azure_vm_deploy.arm_template_provision):

    def run(self, azure_client_id,resource_group, azure_subscription_id, tanent_id, azure_client_secret, region):
        self.auth(azure_client_id,resource_group, azure_subscription_id, tanent_id, azure_client_secret, region)
        return self.delete_resources()