# Visual Inspections, Factory Floor.

This guide will help any person working in the factory floor set up their first automated visual inspection project. The steps below should be done before attending the workshop to make sure you have the right priviledges in Azure for your solution

## Content:
- [Hardware Requirements](#hardware-requirements)
- [Exercise #1: Setting up your environment]

## **Task 1:  Virtual Machine**
This virtual machine will be our development environment for the solution. 
1. Go to Azure https://ms.portal.azure.com/
2. Click on **+ Create Resource**, look for **Virtual Machine**, usually the first item in the list and click **Create**
3. A new window will appear with multiple tabs to fill the information for that Virtual Machine:
**Basics Tab:**
- Subscription: Select the subscription you are using for this workshop
- Resource Group: Select the resource group you are using for this workshop
- Vistual Machine name: **devenv**
- Region: **East US** or the closest to your location.
- Avaialbility Options: **No infrastructure required**
- Security Type: **Standard**
- Image: **Windows 10 Pro, version 21H2 - Gen 2** if you don't see it in the list just click in **See all images**
- Username: **devenvisinsp**
- Password: **Visualinsp01!**
- Public inbound ports: **None**
- Licensing: Check, **I confirm I have an eligible windows 10 license with multi-tenant hosting**

The image below will provide additional guidance:

![Create VM](./images/create-vm.png 'Create VM')

If you don't find the right size for the virtual machine, click on **See all sizes** in the **Size** Section, a new window will open, search for **d16** and select the appropiated as shown below. The cost of the VM considered the whole month, however we will use it just for a few hours and then we will deallocated, so will be significantly lower.

![Find the right sizing](./images/vm-size.png 'Find the right sizing VM')

**Management Tab**:

In the monitoring section, **Disable** Boot diagnostics.

4. Click, **Review + Create** at the bottom of the page, once the validation is complete, click on **Create**.

The create will take approximetly 5 minutes. 

## **Task 2: Set up Virtual Machine**

1. Once the resource is available, you will see a button **Go To Resource**, click on it, a new window will appear, check the **Status** should be **Running** then click **Connect**, select **Bastion**, a new window will open,

If you see the warning message below, you can continue with the steps as long as the VM is running.

![VM](./images/vm-connect.png 'VM')

Once you click Bastion, you will need to follow the steps for complete the configuration, step 1 might be already set up. In **Step 2** click on **Create Subnet**

![Bastion](./images/bastion-step2.png 'Bastion Step 2')

After step 2 is completed, you will see **Step 3** click on **Create Azure Bastion using Defaults**

![Bastion](./images/bastion-step3.png 'Bastion Step 3')

After a few minutes you will be able to enter your credentials, the same credentials used when you created the VM, then click **Connect**

![Bastion](./images/bastion-connect.png 'Bastion Connect')

2. A new tab will open asking you to **Accept** Microsoft Privacy settings. Now you are inside the Virtual Machine.

3. Open Microsoft Edge, select **Start without your data**, then **Continue withut data**, **Confirm and start browsing**. and go to this github repo.

4. Now you will download the following Dev tools we will use to build the solution:

    - VS Code. 
  https://code.visualstudio.com/download
  Select **User Installer** **64 bit** for Windows. The download will start, once is completed, check your **Downloads** folder in the VM,right click in the installation file and **Run as Administrator**. Follow the instructions by default.
    
    - Docker Desktop personal download: https://www.docker.com/products/personal/
    Scroll to the bottom of the page, select **Docker Desktop** under **Features**, then click on **windows

    ![Docker](./images/docker-windows.png 'Docker')

    The download will start, once is completed, check your **Downloads** folder in the VM,right click in the installation file and **Run as Administrator**. After the installation you will ask to restart the virtual machine. After restart you will be ask to **Accept the terms** for Docker. You might have a warning sign to dowloand **WSL2 Linux Kernel update packages for x64 machines**, follow the link, download the package and install it.

    Open Docker Dekstop, click on **Sign in**, if you have a docker account, just login, otherwise create a new one, select **Personal** and click on **Free**.
  Open Powersheel "Run as Administrator" and run the following commands, you might need to restart in between:

    ```linux
    Enable-WindowsOptionalFeature -Online -FeatureName $("Microsoft-Hyper-V", "Containers") -All
    ```
    ```linux
    Enable-WindowsOptionalFeature -Online -FeatureName $("VirtualMachinePlatform", "Microsoft-Windows-Subsystem-Linux")
    ```

    
Open with notepad settings.json located in C:\\User\AppData\Roaming\Docker

Make sure the below settings looks like below or change them false to true to look like that:
 **"wslEngineEnabled": true**
 "**"useWindowsContainers": true**

 At this point you should be able to login and see the Docker Dekstop Started succesfully. 


 5. In this github, go to the main folder, click on **Code** and then **Download ZIP**.

![Github](./images/github-download.png 'Github')

6. Go to Downloads Folder, unzip it **Extract All**. 


## **Task 3: Azure Services**

1. Go back to Azure Portal https://ms.portal.azure.com/

2. Click on **"+ Create Resource"**, search for **Container Registry**, then click **Create**.

- Subscription: Select the subscription you have assigned for this workshop.
- Resource Group:The resource group you selected for this workshop
- Name: **visinsp**+companyname.
- SKU: Standard

![ACR](./images/container-registry.png 'ACR')

Then **Review + Create** once the validation is completed click on **Create**.

3. **Go To resource** once the creation is completed. On the left menu click on **Access Keys**, toggle to enable **Admin User**
In a notepad copy the following values:
  - Login server
  - Username
  - pasword

  ![ACR](./images/repo-info.png 'ACR')

```linux
docker login -u visinsp -p =o7ag0JfN+IZRinblhXko=PVHKZlo=fK visinsp.azurecr.io
```

4. Test that you can connect to the Container REgistry using the credentials above, copy this command and replace the values for yours 

```linux
docker login -u YOUR-USER -p YOUR-PASSWORD YOUR-USER.azurecr.io
```

In my example the final command will look like the below:

```linux
docker login -u visinsp -p =o7ag0JfN+IZRinblhXko=PVHKZlo=fK visinsp.azurecr.io
```

5. Open Visual Studio Code, you will be prompted to **Open a Folder**, select from Downloads, the extracted github material and select the **Code** Folder.

6. Go to Terminal on the top menu, and click **New Terminal**

  ![Terminal](./images/terminal.png 'Terminal')

7. At the bottom paste the command to login, then press Enter.

 ![ACR Login.](./images/acr-login.png 'ACR Login')


8. You should receive a message saying **Login Succeeded**

 ![ACR Login.](./images/login-succeded.png 'ACR Login')


9. Go to Azure Portal, look for the Virtual Machine, click on it, the overview blade will open, select **Stop**

 ![Stop VM](./images/stop-vm.png 'Stop VM')

 10. Now you are all set to continue to the next section **HoL Visual Inspection Custom**






 







