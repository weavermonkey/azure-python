from utils import client_id, key,tenant_id
from authenticate import authenticate

def get_all_ips( resource_group_name,vm_ss_name ):
    ips_list = []
    credentials_dict = authenticate( client_id, key, tenant_id )
    network_client = NetworkManagementClient( credentials_dict['credentials'], credentials_dict['subscription_id'] )
    vm_nic_configs =  network_client.network_interfaces.list_virtual_machine_scale_set_network_interfaces( resource_group_name,vm_ss_name )
    for paged_nic_config in vm_nic_configs:
        for curr_private_ip in  paged_nic_config.ip_configurations:
            ips_list.append( str( curr_private_ip.private_ip_address ) )
    return ips_list
