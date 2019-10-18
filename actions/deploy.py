from ./core import azure_vm_deploy

class deploy_arm_template(azure_vm_deploy.azure_vm_deploy):
    def run(self, client_id,resource_group, subscription_number, tanent_id, serect, region, template_file):
        return self.deploy_vm(template_file)