from core import azure_vm_deploy

__all__ = [
    'authenticate'
]
class authenticate(azure_vm_deploy.arm_template_provision):

    def run(self, client_id, serect, tenant_id, subscription_number, resource_group,region, template_file):
        print("==============================Authenticating credentials ====================================")
        # authenticating credentials
        credentials = self.auth(client_id, serect, tenant_id)
        return credentials