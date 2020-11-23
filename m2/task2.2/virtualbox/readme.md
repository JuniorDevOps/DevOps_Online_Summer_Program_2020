# Working with Oracle __VirtualBox__

## __VirtualBox__ VM GUI

### [<u>Creating __VirtualBox__ VM</u>](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/gui-createvm.html "Official Docs")

![Screenshot](./img/vhd_screenshot.png)
![Screenshot](./img/vmcreation1.png)
![Screenshot](./img/vmcreation2.png)
![Screenshot](./img/vmcreation3.png)
![Screenshot](./img/vmcreation4.png)
![Screenshot](./img/vmcreation5.png)
![Screenshot](./img/creation6.png)


___

### [<u>Cloning __VirtualBox__ VM</u>](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/clone.html "Official Docs")


- **Clone Types** 
    - *Full Clone* (Copies all dependent disk images to the new VM folder. A full clone can operate fully without the source VM)
    - *Linked Clone* (Creates new differencing disk images based on the source VM disk images. If you select the current state of the source VM as the clone point, Oracle VM VirtualBox creates a new snapshot)

![Screenshot](./img/cloning.png)
![Screenshot](./img/clonesettings.png)

___

### [<u>Using VM **Groups**</u>](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/gui-vmgroups.html "Official Docs")

#### Using VirtualBox GUI:
![Screenshot](./img/groups.png)
![Screenshot](./img/groups1.png)

#### Using VBoxManage CLI:
```bash
VBoxManage modifyvm "Windows 10" --groups "/Windows VMs"

VBoxManage modifyvm "Ubuntu18.04" --groups "/Linux VMs"

VBoxManage modifyvm "SUSE 10.2" --groups "/Training VMs"

VBoxManage modifyvm "SUSE 10.2_copy" --groups "/Training VMs"

VBoxManage modifyvm "Ubuntu_Dubenchuk" --groups "/Training VMs"
```

___

### [<u>Working with **Snapshots**</u>](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/snapshots.html "Official Docs")

![Screenshot](./img/snapshot_creation.png)
![Screenshot](./img/snapshot_tree.png)
![Screenshot](./img/snapshot_restore.png)


___

### [<u>**Import / Export** VirtualBox VMs</u>](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/ovf.html "Official Docs")

![Screenshot](./img/import1.png)
![Screenshot](./img/import2.png)
![Screenshot](./img/import3.png)
![Screenshot](./img/import4.png)
![Screenshot](./img/import5.png)
![Screenshot](./img/import6.png)

___

### [<u>**Configuring** VMs</u>](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/BasicConcepts.html "Official Docs")


#### Main VirtualBox Settings:

- [General Settings](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/generalsettings.html "Official Docs")
- [System Settings](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/settings-system.html "Official Docs")
- [Display Settings](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/settings-display.html "Official Docs")
- [Storage Settings](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/settings-storage.html "Official Docs")
- [Audio Settings](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/settings-audio.html "Official Docs")
- [Network Settings](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/settings-network.html "Official Docs")
- [Serial Ports](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/serialports.html "Official Docs")
- [USB Support](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/usb-support.html "Official Docs")
- [Shared Folders](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/shared-folders.html# "Official Docs")
- [User Interface](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/user-interface.html "Official Docs")

#### To enable *Drag'n'Drop* functionality:
##### Go to: `Settings > General > Advanced`
![Screenshot](./img/dragndrop.png)
![Screenshot](./img/dragndrop2.png)


#### To enable *Screen Recording*:
##### Go to: `Settings > Display > Recording`
![Screenshot](./img/screenrecording.png)


#### Configuring *USB ports*:
##### Go to: `Settings > Ports > USB`
##### In case VM is running: `Devices > USB`
![Screenshot](./img/usbport1.png)
![Screenshot](./img/usb.png)



#### To configure *Shared Folder*:
##### Go to: `Settings > Shared Folders`
##### In case VM is running: `Devices > Shared Folders`
![Screenshot](./img/sharedfolder.png)
![Screenshot](./img/sharedfolder1.png)
![Screenshot](./img/sharedfolder2.png)


___

## [VirtualBox **Virtual Networking**](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/networkingdetails.html "Official Docs")

#### Main Networking Modes:
- NAT (Network Address Translation)
- NAT Network
- Bridged networking
- Internal networking
- Host-only networking

#### To configure *Networking Mode*:
##### Go to: `Settings > Network`
![Screenshot](./img/networkingmodes.png)

#### Overview of Networking Modes
![Screenshot](./img/table.png)

- #### NAT (Network Address Translation) mode
![Screenshot](./img/nat.png)
![Screenshot](./img/nat2.png)

#### Checking *`VM->Host`*
![Screenshot](./img/nat3.png)

#### Checking *`VM->Net/LAN`*
![Screenshot](./img/nat4.png)

#### Setting up **Port Forwarding**
##### Go to: `Settings > Network > Advanced > Port Forwarding`
![Screenshot](./img/pf.png)
##### Cheking SSH on guest:
![Screenshot](./img/pf2.png)
##### Checking *`VM<-Host`* using SSH:
![Screenshot](./img/pf3.png)

#### Using VBoxManage CLI
##### Create Port Forwarding rule:
```bash
VBoxManage modifyvm "Ubuntu18.04" --natpf1 "guestssh,tcp,,2281,,22"
```
##### Delete Port Forwarding rule:
```bash
VBoxManage modifyvm "Ubuntu18.04" --natpf1 delete "guestssh"
```



- #### NAT Network (NAT Service)
> The main difference from simple **NAT** is ability of VMs **in one NAT Network** to communicate betweeen each other.

![Screenshot](./img/natnetwork.png)
![Screenshot](./img/cp.png)
#### Creating **NAT Network**
##### Go to: `VirtualBox/File > Preferences > Network`
![Screenshot](./img/natnetwork2.png)
#### Using VBoxManage CLI
##### Creating NAT Network with DHCP server:
```bash
VBoxManage natnetwork add --netname "Network 1" --network "10.0.2.0/24" --enable --dhcp on
```
##### *Start* NAT Network Service:
```bash
VBoxManage natnetwork start --netname "Network 1"
```
##### *Stop* NAT Network Service:
```bash
VBoxManage natnetwork stop --netname "Network 1"
```
##### *Delete* NAT Network Service:
```bash
VBoxManage natnetwork remove --netname "Network 1"
```
#### Assigning NAT Network to VM
##### Go to: `Settings > Network`
![Screenshot](./img/natnetwork3.png)
#### Checking *`VM1<->VM2`*:
![Screenshot](./img/cp2.png)



- #### Bridged Adapter
![Screenshot](./img/br3.png)
![Screenshot](./img/br2.png)
#### Setting up **Bridged Adapter**
##### Go to: `Settings > Network`
![Screenshot](./img/br.png)
#### Checking *`VM->Host`* and `VM<-Host`:
![Screenshot](./img/br4.png)





- #### Internal Network
![Screenshot](./img/it.png)
#### Setting up **Internal Network**
##### Go to: `Settings > Network`
![Screenshot](./img/it2.png)


- #### Host-only Network
![Screenshot](./img/honly2.png)
#### Setting up **Host-only Adapter**
##### Go to: `Settings > Network`
![Screenshot](./img/honly.png)


___

## Main **VirtualBox** CLI commands


### <u>**CLI commands structure**</u>

```bash
VBoxManage [<general options>] <commands> [<option>]
```

#### Some of the `<general options>`:
 
```bash
[-v|--version]      Show VirtualBox version
```

#### Some of the `<commands>`:

- **[`list`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-list.html "Official Documentation")** 
    - `vms` [ `--long` ]
    - `runningvms`
    - `groups`
    - **[`...`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-list.html "Official Documentation")**

> The `list` command gives relevant information about your system and information about Oracle VM VirtualBox's current settings.

> Example: 

```bash
VBoxManage list vms
```
![Screenshot](./img/list_screenshot.png)

___

- **[`showvminfo`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-showvminfo.html "Official Documentation")** [ `--machinereadable` ]

> The `showvminfo` command shows information about a particular virtual machine. 

> Use the `--machinereadable` option to produce the same output, but in machine readable format with a `property=value` string on each line.

> Example: 

```bash
VBoxManage showvminfo Ubuntu18.04
```
![Screenshot](./img/showvminfo_screenshot.png)
___

- **[`createvm`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-createvm.html "Official Documentation")** 
    - `--name` [ *`name`* ]
    - `--basefolder` [ *`path`* ]
    - `--group` [ *`group-ID`* ]
    - `--ostype` [ *`ostype`* ]
    - `--uuid` [ *`uuid`* ]
    - `--register`
    - **[`...`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-createvm.html "Official Documentation")**

> The `VBoxManage createvm` command creates a new `XML` virtual machine definition file.

> Example: 
```bash
VBoxManage createvm --name "SUSE 10.2" --register
```
![Screenshot](./img/register_screenshot.png)

___

- **[`clonevm`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-clonevm.html "Official Documentation")**
    - `vmname` | `uuid`
    - `--basefolder` [ *`path`* ]
    - `--name` [ *`vmname`* ]
    - `--options` [ *`link`* ] [ *`keepallmacs`* ] [ *`keepdisknames`* ] [ *`keephwuuids`* ]
    - `--mode` [ *`machine`* ] [ *`machineandchildren`* ] [ *`all`* ]
    - **[`...`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-clonevm.html "Official Documentation")**


> The `VBoxManage clonevm` command clones an existing Oracle VM VirtualBox virtual machine.

> Example: 
```bash
VBoxManage clonevm 'SUSE 10.2' --name="SUSE 10.2_copy" --register --mode=all
```
![Screenshot](./img/clonevm_screenshot.png)

___

- **[`modifyvm`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-modifyvm.html "Official Documentation")**
    - `--name` [ *`vmname`* ]
    - `--memory` [ *`vm_ram_memory`* ]
    - `--ostype` [ *`osname`* ]
    - `--nic1` [ *`network_mode`* ]
    - **[`...`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-modifyvm.html "Official Documentation")**


> This command changes the properties of a registered virtual machine which is `not running`. 

> These commands require that the machine is `powered off`, neither running nor in a Saved state.

> Some machine settings can also be changed while a machine is running.

> Example: 
```bash
VBoxManage modifyvm Ubuntu_Dubenchuk --memory 1024 --nic1 nat
```
![Screenshot](./img/modifyvm_screenshot.png)

___


- **[`startvm`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-startvm.html "Official Documentation")**
    - `--type` [ *`gui`* ] [ *`headless`* ] [ *`separate`* ]
    - **[`...`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-startvm.html "Official Documentation")**

> This command starts a virtual machine that is currently in the `Powered Off` or `Saved` states. 

> Example: 
```bash
VBoxManage startvm Ubuntu_Dubenchuk
```
![Screenshot](./img/start_screenshot.png)


___


- **[`snapshot`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-snapshot.html "Official Documentation") [ `uuid|vmname` ]**
    - `take` [ `snapshot-name` ]
        - [ `--description` ] [ `description` ]
        - [ `--live` ]
        - [ `--uniquename` ] [ `Number` ] [ `Timestamp` ] [ `Space` ] [ `Force` ]
    - **[`...`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-snapshot.html "Official Documentation")**

___


- **[`controlvm`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-controlvm.html "Official Documentation")**  [ `vmname` ]
    - `pause`
    - `resume`
    - `reset`
    - `poweroff`
    - `savestate` 
    - **[`...`](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/vboxmanage-controlvm.html "Official Documentation")**




___

### <u>**Register VirtualBox VM**</u>

```bash
VBoxManage createvm --name "CHANGE_VM_NAME" --register
```
> Example: 
```bash
VBoxManage createvm --name "SUSE 10.2" --register
```

___

### <u>**Pause virtual machine**</u>

```bash
VBoxManage controlvm virtualMachineName pause
```
> Example: 
```bash
VBoxManage controlvm Ubuntu_Dubenchuk pause
```
___

### <u>**Resume the virtual machine**</u>

```bash
VBoxManage controlvm virtualMachineName resume
```
> Example: 
```bash
VBoxManage controlvm Ubuntu_Dubenchuk resume
```
___

### <u>**Save the virtual machine**</u>

```bash
VBoxManage controlvm virtualMachineName savestate
```
> Example: 
```bash
VBoxManage controlvm Ubuntu_Dubenchuk savestate
```
___



> This article is based on [Official Oracle VM VirtualBox Documentation](https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/user-preface.html  "Official Documentation")