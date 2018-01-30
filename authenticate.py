from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient

#create service principal using https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?toc=%2Fazure%2Fazure-resource-manager%2Ftoc.json&view=azure-cli-latest
tenant_id = ''
client_id = ''
key = ''

def authenticate( client_id, secret, tenant ):
    authentication_dict = {}
    credentials = ServicePrincipalCredentials( client_id=client_id, secret = secret, tenant=tenant )
    subscription_client = SubscriptionClient( credentials )
    subscription = next( subscription_client.subscriptions.list() )
    authentication_dict['credentials'] = credentials
    authentication_dict['subscription_id'] = str( subscription.subscription_id )
    return authentication_dict
