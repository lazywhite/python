
# -*- coding: utf-8 -*-
from novaclient.client import Client
from os_config import *
from keystoneauth1 import loading, session



loader = loading.get_plugin_loader("password")
#auth = loader.load_from_options(auth_url=OS_AUTH_URL, username=OS_USERNAME, password=OS_PASSWORD, project_id=OS_PROJECT_ID, project_domain_name = OS_PROJECT_NAME, user_domain_name=OS_USER_DOMAIN_NAME)
#auth = loader.load_from_options(auth_url=OS_AUTH_URL, username=OS_USERNAME, password=OS_PASSWORD, project_domain_name = OS_PROJECT_NAME, user_domain_name=OS_USER_DOMAIN_NAME)
auth = loader.load_from_options(auth_url=OS_AUTH_URL, username=OS_USERNAME, password=OS_PASSWORD, project_id = OS_PROJECT_ID)


session = session.Session(auth=auth)
nova = Client("2", session=session)


print nova.flavors.list()
print nova.hypervisors.findall()


hypervisor_all = nova.hypervisor_stats.statistics()

hypervisor_all.memory_mb

hypervisor_all.memory_mb_used

hypervisor_all.disk_available_least  # 磁盘总量
hypervisor_all.free_disk_gb ## 可用磁盘


hypervisor_all.vcpus
hypervisor_all.vcpus_used

hypervisor_all.running_vms

hypervisor_all.count #物理机总量

