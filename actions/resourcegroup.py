from core import azure_vm_deploy

__all__ = [
    'create_resource_group'
]

class create_resource_group(azure_vm_deploy.arm_template_provision):
    
    def run(self,client_id, serect, tenant_id, subscription_number, resource_group, region, template_file):
        # athententicating credentials
        credentials = self.auth(client_id, serect, tenant_id, subscription_number, resource_group, region, template_file)
        print("==================================================================")
        print("Creating Resource Group")

        # creating resource crdentials
        resource_group_client = self.get_resource_group_client(credentials,subscription_number)
        
        # creating resource group
        self.create_reource_group( resource_group_client, region, resource_group)
        print("Resource group creation successful")
        return resource_group_client