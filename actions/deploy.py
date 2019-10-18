from core import azure_vm_deploy
print("this is step 2-------------------->>")
class deploy_arm_template(azure_vm_deploy.arm_template_provision):
    print("this is step 1-------------------->>")
    def run(self, client_id,resource_group, subscription_number, tanent_id, serect, region, template_file):
        print("this is step 3-------------------->>")
        return self.deploy_vm(template_file)