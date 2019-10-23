from core import azure_vm_deploy

__all__ = [
    'authenticate'
]
class authenticate(azure_vm_deploy.arm_template_provision):

    def run(self, azure_client_id, azure_client_secret, azure_tenant_id, azure_subscription_id, resource_group,region, template_file):
        print("==============================Authenticating credentials ====================================")
        # authenticating credentials
        credentials = self.auth(azure_client_id, azure_client_secret, azure_tenant_id)
        return credentials