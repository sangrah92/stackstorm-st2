# from core import azure_vm_deploy
from st2common.runners.base_action import Action

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import DeploymentMode

# from st2client.client import Client
# from st2client.models import KeyValuePair
import os,sys,json,random
class deploy_arm_template(Action):

    def run(self, client_id,resource_group, subscription_number, tanent_id, serect, region, template_file):
        try:
            vm_name = 'shield-x_POC_UM'+str(random.randint(1,1001))
            client_secret = serect
            subscription_id = subscription_number
            resource_group = resource_group
            
            credentials = ServicePrincipalCredentials(
                client_id = client_id,
                secret = client_secret,
                tenant = tanent_id
            )
            resource_group_params = {'location':region}
            
            resource_group_client = ResourceManagementClient(
                credentials,
                subscription_id
            )
            
            resource_group_client.resource_groups.create_or_update(resource_group, resource_group_params)
            response = self.deploy_vm(template_file,resource_group,vm_name)
            return (True,response)
        except Exception as e:
            return(False,str(e))

    def get_template_path(self, existing_template_path):
        file_path = os.path.dirname(os.path.realpath(__file__ ))
        return file_path+ "/templates/"+ existing_template_path
    
    def deploy_vm(self, existing_template_path,resource_group,vm_name):
        try:
            template_path = self.get_template_path(existing_template_path)

            with open(template_path) as f:
                template = json.load(f)

            parameters  = template['parameters']
            format_parameters = {k: {'value': v} for k, v in parameters.items()}    
            
            deployment_properties = {
                'mode': DeploymentMode.incremental,
                'template': template,
                'parameters': format_parameters
            }

            deployment_async_operation = self.resource_group_client.deployments.create_or_update(resource_group,vm_name,deployment_properties)
            result = deployment_async_operation.status()
            deployment_async_operation.wait()
            return result
        except Exception as e:
            return(e)