from core import azure_vm_deploy

__all__ = [
    'destroy_resource_group'
]
class destroy_resource_group(azure_vm_deploy.arm_template_provision):

    def run(self, client_id,resource_group, subscription_number, tanent_id, serect, region):
        self.auth(client_id,resource_group, subscription_number, tanent_id, serect, region)
        return self.delete_resources()