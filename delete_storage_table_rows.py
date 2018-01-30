from utils import authenticate,client_id, key, tenant_id,table_key,resource_group_name,vm_ss_name,table_name
from azure.storage.table import TableService,Entity

def delete_extra_ips_from_storage_table( storage_table_name ):
    credentials_dict = authenticate( client_id, key, tenant_id )
    table_service = TableService( account_name='progaccount', account_key=table_key )
    table_rows = get_all_rows( storage_table_name )
    print 'LIST of table rows:\n',table_rows
    print 'list of NIC rows:\n',get_all_ips(resource_group_name, vm_ss_name)
    for curr_storage_table_ip in table_rows['ip']:
        if curr_storage_table_ip not in get_new_ips( get_all_rows(table_name), get_all_ips(resource_group_name, vm_ss_name) ):
            print 'Deleting Entity:',table_rows['partition_key'][table_rows['ip'].index(curr_storage_table_ip)], ' Current storage table IP: ',curr_storage_table_ip
            table_service.delete_entity( storage_table_name, table_rows['partition_key'][table_rows['ip'].index(curr_storage_table_ip)], curr_storage_table_ip)
