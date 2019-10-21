from st2common.runners.base_action import Action

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import DeploymentMode

# from st2client.client import Client
# from st2client.models import KeyValuePair
import os,sys,json,random

class arm_template_provision(Action):
    
    
    def __init__(self,config):
        super(arm_template_provision, self).__init__(config)

    def auth(self,client_id,resource_group, subscription_number, tanent_id, serect, region):
        self.vm_name = 'shield-x_POC_UM'+str(random.randint(1,1001))
        self.resource_group = resource_group
        self.location = region
        credentials = ServicePrincipalCredentials(
            client_id = client_id,
            secret = serect,
            tenant = tanent_id
        )
        resource_group_params = {'location':region}
        
        self.resource_group_client = ResourceManagementClient(
            credentials,
            subscription_number
        )
        
        self.resource_group_client.resource_groups.create_or_update(resource_group, resource_group_params)
        
    def get_template_path(self, existing_template_path):
        file_path = os.path.dirname(os.path.realpath(__file__+"/../"))
        return file_path + "/templates/"+ existing_template_path
    
    def deploy_vm(self, existing_template_path):
        try:
            template_path = self.get_template_path(existing_template_path)

            with open(template_path) as f:
                template = json.load(f)

            parameters  = template['parameters']
            default_parameters = {k: v['defaultValue'] for k, v in parameters.items()}
            format_parameters = {k: {'value': v} for k, v in default_parameters.items()}    
            
            deployment_properties = {
                'mode': DeploymentMode.incremental,
                'template': template,
                'parameters': format_parameters
            }

            deployment_async_operation = self.resource_group_client.deployments.create_or_update(self.resource_group,self.vm_name,deployment_properties)
            deployment_async_operation.wait()
            deployment_async_operation.wait()
            result = deployment_async_operation.status()
            
            return(True,result)

        except Exception as e:
            return(False,str(e)) 