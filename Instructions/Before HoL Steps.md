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
- Region: East US or the closest to your location.
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
  - Docker Desktop personal download: https://www.docker.com/products/personal/
