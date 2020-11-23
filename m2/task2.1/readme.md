## Answers for task 2.1 of DevOps Online Training

### __What are the most popular hypervisors for infrastructure virtualization?__

 > Some of the most popular hypervisors are:
 - [_Red Hat Enterprise Virtualization Hypervisor (REVH)_](https://www.redhat.com/en/technologies/virtualization/enterprise-virtualization "Official website")
 - [_Citrix XenServer_](https://www.citrix.com/ru-ru/products/citrix-hypervisor/ "Official website")
 - [_Microsoft Hyper-V_](https://docs.microsoft.com/ru-ru/virtualization/hyper-v-on-windows/about/ "Official website")
 - [_Oracle VirtualBox_](https://www.virtualbox.org/ "Official website")
 - [_VMware vSphere Hypervisor_](https://www.vmware.com/ru/products/vsphere-hypervisor.html "Official website")

 ___

 ### __Briefly describe the main differences between the most popular hypervisors.__

All hypervisors come in several types. Hypervisors of _`type 1`_ run directly on the computer hardware, virtual machine operating systems run above the hypervisor. 

> _Because of great performance and some other factors, _`type 1`_ hypervisors are a primary choice for data centers._

Some examples of _`type 1`_ hypervisors are:

 - [_VMware ESX Server_](https://www.vmware.com/ru/products/esxi-and-esx.html "Official website")
 - [_Citrix XenServer_](https://www.citrix.com/ru-ru/products/citrix-hypervisor/ "Official website")
 - [_Microsoft Hyper-V_](https://docs.microsoft.com/ru-ru/virtualization/hyper-v-on-windows/about/ "Official website")


Hypervisors of _`type 2`_ run on the host operating system as any other software, guest operating systems run on one more layer higher, above the hypervisor. 

Some examples of _`type 2`_ hypervisors are:

 - [_Microsoft Virtual PC_](https://www.microsoft.com/ru-RU/download/details.aspx?id=3702 "Official website")
 - [_Oracle VM VirtualBox_](https://www.virtualbox.org/ "Official website")
 - [_Parallels Desktop_](https://www.parallels.com/ru/products/desktop/ "Official website")

> As it comes to hypervisors of _`type 3 and 4`_, the difference is in architecture itself. 

The **_Monolithic_** architecture of _`type 3`_ hypervisors includes all the hardware drivers, and when it comes to the architecture of _`type 4`_ hypervisors it is called **_Microkernel_**.

> In **_Microkernel_** architecture device drivers are located __inside__ the host operating system, and only the “parent” operating system has access to the hardware. 

A great example of the hypervisor with **_Microkernel_** architecture is [_Microsoft Hyper-V_](https://docs.microsoft.com/ru-ru/virtualization/hyper-v-on-windows/about/ "Official website"), [_VMware ESX Server_](https://www.vmware.com/ru/products/esxi-and-esx.html "Official website") on the other hand has **_Monolithic_** architecture.
 
