from utils import storage_account_name,table_key,client_id,key,tenant_id

def get_all_rows( storage_table_name ):
    credentials_dict = authenticate( client_id, key, tenant_id )
    rows_in_table = {'partition_key': [],'ip':[]}
    credentials_dict = authenticate( client_id, key, tenant_id )
    table_service = TableService( account_name=storage_account_name, account_key=table_key )
    tasks = table_service.query_entities( storage_table_name, filter= '' )
    for task in tasks:
        rows_in_table['partition_key'].append( str( task.PartitionKey ) )
        rows_in_table['ip'].append( str( task.RowKey ) )
    return rows_in_table
