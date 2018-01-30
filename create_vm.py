from utils import client_id,key,tenant_id
from azure.mgmt.compute import ComputeMangementClient
from utils import create_nic

def create_vm( computer_name ):
    credentials_dict = authenticate( client_id, key, tenant_id )
    compute_client = ComputeManagementClient( credentials_dict['credentials'], credentials_dict['subscription_id'] )
    nic_id = create_nic( computer_name )
    param_dict = {
        'network_profile':
        {
            'virtualNetworkName':'testRunbookSSVnet',
            'subnetName':'default',
            'network_interfaces': 
            [
                {
                    'id': nic_id
                }
            ]
        },
        'location' : 'centralindia',
        'os_profile':
        {
            'computer_name': computer_name,
            'admin_username': 'prog_user',
            'admin_password': 'progressive@123'
        },
        'hardware_profile': 
        {
            'vm_size': 'Standard_A0'
        },
        'storage_profile': 
        {
            'image_reference': 
            { 
                'publisher': 'Canonical', 
                'offer': 'UbuntuServer', 
                'sku': '17.10', 
                'version': 'latest' 
            }
        }
    }
    compute_client.virtual_machines.create_or_update( 'DEV-Central', computer_name, param_dict )
