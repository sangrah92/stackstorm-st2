from core import azure_vm_deploy

__all__ = [
    'template_deploy'
]

class template_deploy(azure_vm_deploy.arm_template_provision):
    
    def run(self,credentials, azure_subscription_id, existing_template_path, resource_group):
        print("==================================================================")
        print("Deploying VM")
        resource_group_client = self.get_resource_group_client(credentials,azure_subscription_id)

        self.deploy_vm(existing_template_path, resource_group_client, resource_group)