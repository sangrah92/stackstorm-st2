from core import azure_vm_deploy

__all__ = [
    'create_resource_group'
]

class create_resource_group(azure_vm_deploy.arm_template_provision):
    
    def run(self,credentials):
        # subscription_id,region, resource_group
        print("==================================================================")
        print("Creating Resource Group")
        print(credentials)
        return(True,credentials)
        # resource_group_client = self.get_resource_group_client(credentials,subscription_id)
        # self.create_reource_group( resource_group_client, region, resource_group)
        # print("Resource group creation successful")
        # return resource_group_client