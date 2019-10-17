from st2common.runners.base_action import Action

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import DeploymentMode

from st2client.client import Client
from st2client.models import KeyValuePair
import os,sys,json

class arm_template_provision(Action):

    def __init__(self,config):
        super().__init__(config)

    def get_template_path(self, existing_template_path):
        file_path = os.path.dirname(os.path.realpath(__file__ + "/../"))
        return file_path + existing_template_path
    
    def deploy_vm(self, existing_template_path):
        try:
            template_path = self.get_template_path(existing_template_path)
            client_id = ""
            client_secret = ""
            tenant_id = ""
            subscription_id = ""
            resource_group= ""
            vm_name = ""
            credentials = ServicePrincipalCredentials(
                client_id = client_id,
                secret = client_secret,
                tenant = tenant_id
            )
            resource_group_client = ResourceManagementClient(
                credentials,
                subscription_id
            )

            with open(template_path) as f:
                template = json.load(f)

            parameters  = template['parameters']
            format_parameters = {k: {'value': v} for k, v in parameters.items()}    
            
            deployment_properties = {
                'mode': DeploymentMode.incremental,
                'template': template,
                'parameters': format_parameters
            }

            deployment_async_operation = resource_group_client.deployments.create_or_update(resource_group,vm_name,deployment_properties)
            result = deployment_async_operation.status()
            return(True,result)

        except Exception as e:
            return(False,str(e)) 