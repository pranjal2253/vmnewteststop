from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
# from azure.mgmt.network import NetworkManagementClient
# from azure.mgmt.compute.models import DiskCreateOption
from flask import Flask

SUBSCRIPTION_ID = 'c2a4acfe-bc6d-4a33-ac04-46fa9d475860'
GROUP_NAME = 'PranjalVM'
LOCATION = 'westus'
VM_NAME = 'myVM'


def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id = 'ec539ba3-6787-4760-b63d-b37067b67a28',
        secret = '98q3FlN].R/W6VjGKR=sG*+yLJXtXwR?',
        tenant = 'e525031f-bb1f-4659-aa0e-c0f3fbfa832f'
    )

    return credentials

app = Flask(__name__)

@app.route('/')
def Vm_check():
  return 'VM is getting checked' 

@app.route('/stopvm')
def VM():
  stop_vm(compute_client)
  return 'VM is stopped' 
 

# def status(compute):
#   vm = compute.virtual_machines.get(GROUP_NAME, VM_NAME, expand='instanceView')
#   status_vm = vm.instance_view.status_vm
#   return status_vm[1].display_status
  

def stop_vm(compute_client):
  compute_client.virtual_machines.power_off(GROUP_NAME, VM_NAME)
  
  
if __name__ == '__main__':
  credentials = get_credentials()
  compute_client = ComputeManagementClient(
    credentials,
    SUBSCRIPTION_ID
    )

  VM()
  app.debug = True
  app.run()
