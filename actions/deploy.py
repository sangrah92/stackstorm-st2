from core import azure_vm_deploy

class deploy_arm_template(arm_template_provision.arm_template_provision):
    def run(self, client_id,resource_group, subscription_number, tanent_id, serect, region, template_file):
        return self.deploy_vm(template_file)