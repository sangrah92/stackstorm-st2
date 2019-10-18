from st2common.runners.base_action import Action

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import DeploymentMode

# from st2client.client import Client
# from st2client.models import KeyValuePair
import os,sys,json,random

class arm_template_provision(Action):
    
    
    def __init__(self, client_id,resource_group, subscription_number, tanent_id, serect, region):
        # super(arm_template_provision, self).__init__(client_id,resource_group, subscription_number, tanent_id, serect, region)
        _client_id = ""
        _vm_name = 'shield-x_POC_UM'+str(random.randint(1,1001))
        _client_secret = serect
        _tenant_id = tanent_id
        _subscription_id = subscription_number
        _resource_group = resource_group
        
        credentials = ServicePrincipalCredentials(
            client_id = _client_id,
            secret = _client_secret,
            tenant = _tenant_id
        )
        resource_group_params = {'location':region}
        
        resource_group_client = ResourceManagementClient(
            credentials,
            _subscription_id
        )
        
        resource_group_client.resource_groups.create_or_update(resource_group, resource_group_params)
        
    def get_template_path(self, existing_template_path):
        file_path = os.path.dirname(os.path.realpath(__file__ + "../templates/"))
        return file_path + existing_template_path
    
    def deploy_vm(self, existing_template_path):
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

            deployment_async_operation = self.resource_group_client.deployments.create_or_update(self._resource_group,self._vm_name,deployment_properties)
            result = deployment_async_operation.status()
            deployment_async_operation.wait()
            return(True,result)

        except Exception as e:
            return(False,str(e)) 