# Working with __Vagrant__

## Basic Usage

- ## Initialize **Vagrant** 
```bash
vagrant init [name [url]]
```
### Example:
```bash
vagrant init hashicorp/precise64
```
![Screenshot](./img/vag1.png)


- ## To **create / configure** guest machines according to **Vagrantfile** 
```bash
vagrant up [name|id]
```
### Example:
```bash
vagrant up 
```
![Screenshot](./img/vag2.png)


- ## Connect to **running machine** using **SSH**
```bash
vagrant ssh [name|id] [-- extra_ssh_args]
```
### Example:
```bash
vagrant ssh
```
![Screenshot](./img/vag3.png)
### Running `date` command on guest machine:
![Screenshot](./img/vag4.png)



- ## **Stopping** and **Deleting** machine
> Vagrant `suspend` effectively saves the exact point-in-time state of the machine, so that when you resume it later, it begins running immediately from that point, rather than doing a full boot.

```bash
vagrant suspend [name|id]
```
> Vagrant `halt` command will first attempt to gracefully shut down the machine by running the guest OS shutdown mechanism. If this fails, or if the --force flag is specified, Vagrant will effectively just shut off power to the machine.

```bash
vagrant halt [name|id]
```

> Vagrant `destroy` command stops the running machine Vagrant is managing and destroys all resources that were created during the machine creation process. After running this command, your computer should be left at a clean state, as if you never created the guest machine in the first place.

```bash
vagrant destroy [name|id]
```

### Example:
#### Shutting down machine
```bash
vagrant halt
```
#### Destroying machine
```bash
vagrant destroy
```
![Screenshot](./img/vag5.png)

## Creating **LAMP** Stack Dev Env on **Vagrant Box**

- ## Initialize **Vagrant**
```bash
mkdir vagrantdemo

cd vagrantdemo/

vagrant init ubuntu/trusty64
``` 
![Screenshot](./img/demo1.png)

- ## Initialize **Vagrant**
```bash
mkdir vagrantdemo

cd vagrantdemo/

vagrant init ubuntu/trusty64
``` 
![Screenshot](./img/demo1.png)
#### Initial Vagrant file:
![Screenshot](./img/demo2.png)



- ## Setting up **Vagrant** Box **Provider**
![Screenshot](./img/demo3.png)


- ## Creating **Vagrant Box**
![Screenshot](./img/demo4.png)

- ## **SSH** into **Vagrant Box**
![Screenshot](./img/demo5.png)


#### Updating packages:
```bash
sudo apt update
``` 
#### Cheking for Apache Server:
```bash
ls /var/www
```
![Screenshot](./img/demo6.png) 

#### Installing Apache Server:
```bash
sudo apt install apache2
```
#### Cheking for Apache Server again:
```bash
ls /var/www
```
![Screenshot](./img/demo7.png) 

- ## Setting up Vagrant Box **Port Forwarding**
![Screenshot](./img/demo8.png)

- ## Exit **SSH** session
![Screenshot](./img/demo9.png)

- ## Reload **Vagrant Box**
```bash
vagrant reload
```
- ## Checking **Port Forwarding** from **host** machine
![Screenshot](./img/demo10.png)
![Screenshot](./img/demo11.png)



- ## Setting up Vagrant Box **Private Network**
![Screenshot](./img/demo12.png)

- ## **Suspend** & **Reload** Vagrant Box
```bash
vagrant suspend

vagrant reload
```

- ## Checking Vagrant Box **Private Network**
![Screenshot](./img/demo13.png)
![Screenshot](./img/demo14.png)

- ## Adding **local** Domain Name on **host** machine
```bash
sudo nano /etc/hosts
```
![Screenshot](./img/demo15.png)

- ## Checking **local** Domain Name for **Apache Server**
![Screenshot](./img/demo16.png)
![Screenshot](./img/demo17.png)

- ## Setting up Vagrant Box **Synced Folders** for Apache Server
![Screenshot](./img/demo18.png)

- ## Reload **Vagrant Box**
```bash
vagrant reload
```

- ## Creating basic **index.html** file to serve
![Screenshot](./img/demo19.png)
![Screenshot](./img/demo20.png)


- ## Adding **Provision**
![Screenshot](./img/demo21.png)
![Screenshot](./img/demo22.png)

- ## Creating **Vagrant Box** with all the changes
```bash
vagrant halt

vagrant destroy

vagrant up
```
- ## Creating **MySQL** test table

![Screenshot](./img/demo23.png)

![Screenshot](./img/demo24.png)

![Screenshot](./img/demo25.png)


> This article is based on [Official Vagrant Documentation](https://www.vagrantup.com/docs/index "Official Documentation")














