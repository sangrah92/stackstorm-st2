from core import azure_vm_deploy

__all__ = [
    'template_deploy'
]

class template_deploy(azure_vm_deploy.arm_template_provision):
    
    def run(self,existing_template_path, resource_group_client, resource_group):
        print("==================================================================")
        print("Deploying VM")
        self.deploy_vm(existing_template_path, resource_group_client, resource_group)