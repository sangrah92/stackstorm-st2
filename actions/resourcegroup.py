from core import azure_vm_deploy

__all__ = [
    'create_resource_group'
]

class create_resource_group(azure_vm_deploy.arm_template_provision):
    
    def run(self,resource_group_client, region, resource_group):
        
        print("==================================================================")
        print("Creating Resource Group")
        # creating resource group
        response = self.create_reource_group( resource_group_client, region, resource_group)
        print("Resource group creation successful")
        return(True,response)