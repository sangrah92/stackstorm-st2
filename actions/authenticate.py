from core import azure_vm_deploy

__all__ = [
    'authenticate'
]
class authenticate(azure_vm_deploy.arm_template_provision):

    def run(self, client_id, serect, tanent_id, subscription_number, resource_group,region, template_file):
        print("==================================================================")
        print("Authenticating credentials ")
        return self.auth(client_id, serect, tanent_id, subscription_number, resource_group,region, template_file)