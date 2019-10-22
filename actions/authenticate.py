from core import azure_vm_deploy

__all__ = [
    'authenticate'
]
class authenticate(azure_vm_deploy.arm_template_provision):

    def run(self, client_id,resource_group, subscription_number, tanent_id, serect, region, template_file):
        return self.auth(client_id,resource_group, subscription_number, tanent_id, serect, region)