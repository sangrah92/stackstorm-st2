from st2common.runners.base_action import Action

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import DeploymentMode

import os,sys,json,random

class arm_template_provision(Action):
    
    def __init__(self,config):
        super(arm_template_provision, self).__init__(config)

    def auth(self,client_id, serect, tanent_id, subscription_number, resource_group,region, template_file):
        credentials = ServicePrincipalCredentials(
            client_id = client_id,
            secret = serect,
            tenant = tanent_id,
        )
        data = dict()
        data['credentials'] = credentials
        data['resource_group'] = resource_group 
        data['subscription_id'] = subscription_number 
        data['location'] = region 
        data['template_file'] = template_file 
        return(True,data) 
        
    def get_resource_group_client(self,credentials,subscription_id):
        resource_group_client = ResourceManagementClient(
            credentials,
            subscription_id
        )
        return resource_group_client
    
    def create_reource_group(self, resource_group_client, region, resource_group):
        response = resource_group_client.resource_groups.create_or_update(resource_group, {'location':region})
        return(True,response)
        
    def get_template_path(self, existing_template_path):
        file_path = os.path.dirname(os.path.realpath(__file__+"/../"))
        return file_path + "/templates/"+ existing_template_path
    
    def deploy_vm(self, existing_template_path, resource_group_client, resource_group):
        try:
            vm_name = "shield_x_POC_UM_{}".format(random.randint(1,1001))
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

            deployment_async_operation = resource_group_client.deployments.create_or_update(resource_group,vm_name,deployment_properties)
            deployment_async_operation.wait()
            result = deployment_async_operation.status()
            return(True,result)

        except Exception as e:
            return(False,str(e)) 
    
    
    def delete_resources(self, resource_group_client, resource_group):
        try:
            response = resource_group_client.resource_groups.delete(resource_group)
        except Exception as e:
            return (False,str(e))
        else:
            return(True,str(response) + "Success, Resource group along with VM is deleted")