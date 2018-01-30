from utils import tenant_id,client_id,key, resource_group_name,storage_account_name,table_key as storage_account_key
from utils import location_name,file_uri
def run_script_inside_vm(vm_name, ip_to_write):
    credentials_dict = authenticate( client_id, key, tenant_id )
    compute_client = ComputeManagementClient( credentials_dict['credentials'], credentials_dict['subscription_id'] )
    GROUP_NAME = resource_group_name
    ext_type_name = 'CustomScriptForLinux'
    ext_name = 'script-extension-test'
    params_create = {
        'location':location_name,
        'publisher': 'Microsoft.OSTCExtensions',
        'virtual_machine_extension_type': ext_type_name,
        'type_handler_version': '1.5',
        'auto_upgrade_minor_version': True,
        'settings':
        {
            'fileUris': [file_uri],
            'commandToExecute': 'sh test_shell_script.sh ' + ip_to_write
        },
        'protectedSettings':{
            'storageAccountName':storage_account_name,
            'storageAccountKey': storage_account_key
        }
    }
    ext_poller = compute_client.virtual_machine_extensions.create_or_update( GROUP_NAME, vm_name, ext_name, params_create )
