from core import azure_vm_deploy

__all__ = [
    'create_resource_group'
]

class create_resource_group(azure_vm_deploy.arm_template_provision):
    
    def run(self,credentials, azure_subscription_id, region, resource_group):
        print("=============================Creating Resource Group=====================================")
        # creating resource group
        resource_group_client = self.get_resource_group_client(credentials,azure_subscription_id)
        resource_group_params = { 'location': region } 
        response = resource_group_client.resource_groups.create_or_update(resource_group, resource_group_params)
        # self.create_reource_group( resource_group_client, region, resource_group)
        print("Resource group creation successful")
        return(True,response)