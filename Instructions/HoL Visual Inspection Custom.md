# Visual Inspections, Factory Floor.

This accelerator will help any person working in the factory floor set up their first automated visual inspection project.

Before you start this section, it is important you completed the steps on **Instructions/Before Hol Steps**

## Content:
- [Hardware Requirements](#hardware-requirements)
- [Exercise #1: Setting up your environment](#Exercise-1-Setting-up-your-environment)
- [Exercise #2: Developing Machine Learning Model in Custom Vision](#Exercise-2-Developing-Machine-Learning-Model-in-Custom-Vision)

- [Exercise #3: Deploying the machine learning model to the device](#Exercise-3-Deploying-the-machine-learning-model-to-the-device)

- [Exercise #4: Delete Resources](#Exercise-4-delete-resources)
- [Troubleshooting](#troubleshooting)

## Hardware requirements:
The following requirements will be for your Raspberry set up

- <a href="https://www.amazon.com/Raspberry-Pi-Computer-Suitable-Workstation/dp/B0899VXM8F/ref=sr_1_3?keywords=raspberry+pi+4+8gb&qid=1647631122&sprefix=raspbe%2Caps%2C299&sr=8-3">Raspberry Pi 4</a>


- <a href=">https://www.amazon.com/CanaKit-Raspberry-Power-Supply-USB-C/dp/B07TYQRXTK/ref=pd_day0fbt_img_1/130-9714781-1818961?pd_rd_w=Zws3A&pf_rd_p=bcb8482a-3db5-4b0b-9f15-b86e24acdb00&pf_rd_r=YBM58ZGJHTBQM0AM6SAZ&pd_rd_r=ca8f3c9c-a678-4ffa-a3d8-b32757872561&pd_rd_wg=CTO8L&pd_rd_i=B07TYQRXTK&psc=1">CanaKit 3.5A Raspberry Pi 4 Power Supply (USB-C)</a>


- <a href="https://www.amazon.com/SAMSUNG-Select-microSDXC-Adapter-MB-ME64HA/dp/B08879MG33/ref=sr_1_9?crid=R593LIS0AR5N&keywords=samsung+64+sd+card&qid=1647631833&s=electronics&sprefix=samsung+64+sd+card%2Celectronics%2C87&sr=1-9">SAMSUNG EVO Select 64GB microSDXC UHS-I U1 100MB/s Full HD & 4K UHD Memory Card with Adapter (MB-ME64HA)</a>


- <a href="https://www.amazon.com/UGREEN-Adapter-Ethernet-Compatible-Raspberry/dp/B06WWQ7KLV/ref=sr_1_3?keywords=micro+hdmi+to+hdmi&qid=1647632043&s=electronics&sprefix=micro+hdmi%2Celectronics%2C177&sr=1-3">Micro HDMI to HDMI Cable Adapter 4K 60Hz</a>

- Keyboard, any USB Keyboard for your raspberry pi setup
- Mouse, any USB Mouse for your raspberry pi setup
- Monitor, any Monitor with HDMI input for your - raspberry pi setup
- Ethernet Cable
- USB Camera

## Azure Services:
  - Azure IoT Central
  - Custom Vision
  - Azure Container Registry
  - Storage Account
  - Virtual Machine(Dev Environment)

## Other Tools:
  - VS Code. We will download it inside the Virtual Machine
  https://code.visualstudio.com/download
  - Docker Desktop personal. We will download it inside the Virtual Machine: https://www.docker.com/products/personal/


All the items above will be used during your raspberry pi set up. On addition to that list, you will need a laptop or computer with access to internet and **SD Adapter for MicroSD** to install the OS for your SSD  card which will be inserted in your raspberry pi, your laptop should have the following entrance as shown in the picture below:

![Laptop](./images/laptop-ssd-entry.png 'Laptop')

## Architecture Diagram

This workshop will follow the below architecture, in the course of a few sessions will be implementing a machine learning model developed during the training analyzing pictures in real time and pushing alerts to employees when the picture shows the anomalies the client defined as use case. Of course you can change from IoT Central to IoT Hub but those steps are not documented in this github. Power Apps, Power BI and SQL DBs will be optional that will provide an idea for future extensions.

![Architecture](./images/architecture.png 'Architecture')



## Exercise #1: Setting up your environment


Our first task will be setting up the OS in your SSD card so you Raspberry pi can operate properly.
For that you will insert the Samsung SSD card, 64gb into the SD Adapter inside your laptop to start the confirguration as shown below:

![Laptop](./images/ssd-card-inserted.png 'Laptop')

### **Task 1: Setting up your SSD Card**

1. Go to your browser, we will install Ubuntu on the SSD, click <a href="https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overviewSelect:%20Ubuntu%2020.4%20for%20arm64%20technologies.">here</a>

2. On the left side, click on **Prepare the SD Card**, then select **Raspberry pi imager for Windows**. This will trigger the download of the imager as show in the right top.

    ![Installing Ubuntu](./images/installing-ubuntu.png  'Installing Ubuntu')


3. Once the file is completed, go to the **Downloads Folder**, right click in the file and select "Run as Administrator". A new windows will open asking **Do you want to allow this app to make changes to your device?**, select **Yes**

4. Now you will have a new windows poping up, **Welcome to Raspberry Pi Imager Setup**, click **Install**. The installation only takes a few minutes, click **Finish**

5. A new window will open as shown below: 

    ![Imager](./images/Raspberry-Pi-Imager.png 'Imager')


6. Click on **Choose OS** Button and select **Other General Propose OS**, then select **Ubuntu** then **Ubuntu Server 20.04.4 LTS(RPI 3/4/400), 64-bit server OS with long term support for arm64 architecture**

    ![Imager](./images/ubuntu-selection.png 'Imager')

7. Next, click in **Storage** you will have one option available, select SDHCD Card, then back on the main screen, select **WRITE**. A new pop up window will indicate that all the information will be erased from the SSD asking if you would like to proceed, select **YES**


    ![Imager](./images/imager-write.png 'Imager')



8. The step above will take several minutes. When is done you will receive a sign saying **You can now remove the SD Card from the Reader**, click **Continue**. Remove the adapter from the laptop. Remove the SSD Card from the Adapter to inster it in the Raspberry Pi.


### **Task 2: Connecting your Raspberry PI.**

1. Once your SSD is ready you will need to insert it in the Raspberry PI for that is very important your Raspberry PI has all the equipment connected.

- Connect the Power Cord to your raspberry Pi
- Connect the Keyboard in one of the USB Ports
- Connect the mouse in one of the USB Ports
- Connect the monitor using one of the micro hdmi ports on the side of the raspberry pi and the other extreme to the monitor. 
- Connect a LAN cable to make sure you have internet connectivity quickly.

Make sure the raspberry pi is **OFF**. Once all your equipment is connected to the raspberry pi, you will insert the SSD card as shown below and then Turn **On** the power.


![Card Inserted](./images/card-inserted.png 'Card Inserted')

Now that all the equipment is connected and the rasbberry pi is OFF, should look exactly like the image below:

![RPI Connected](./images/raspberry-pi-connected.png 'RPI Connected')

2. Now you are ready to Turn on the switch in the power cord, once you do so, red lights will turn on and one green light will blink in your board.



![RPI On](./images/turnon.png 'RPI On')

 3. In the monitor connected to the Raspberry pi you will be prompt to Login:

    - Ubuntu Login: enter **ubuntu**
    - Paswword: enter **ubuntu** Next you will be ask to change your password, 
    - Current password: **ubuntu**
    - New Password: **Visual01!**
    - Retype password: **Visual01!**

    If there is no typos, you will see a message as below **Welcome to Ubuntu...** If there is a typo you will need to relogin and re start the password change steps again.

![RPI Login](./images/ubunut-login.png 'RPI Login')

4. Next we will install a lightweighted version of desktop in your raspberry pi to make things easier considering our end user, if you feel more comfortable using PuTTY you dont need the desktop.

    Type the following command

```linux
sudo apt update
```
   Press enter, this will quickly check packages to upgrade, then type the below command and press enter again.

```linux
sudo apt upgrade
```
You will be prompt to contynue type **Y**, this step will take some minutes.

5. After several minutes you will see in the screen the user again **ubuntu@ubuntu:~$** type the following command to install the desktop: 

```linux
sudo apt install xubuntu-desktop
```
Press enter, a lot of packages will appear unpacking then you will be ask if you want to continue type **Y**. Again this will take a few minutes and then you will see a purple screen asking you about the display, select with the arrown down **lightdm** and press enter.

![RPI Login](./images/select-version.png 'RPI Login')


6. Now you will restart the raspberry pi with the following command:
```linux
sudo reboot
```
Press enter, once the raspberry pi turn on again you will see the new dekstop interface.

![RPI Login](./images/desktop.png 'Dektop login')

Login with the credentials you set up before, in this lab we are using **Visual01!** as pasword.

Open a terminal in the raspberry pi, and run the following command, to see where the terminal is, see below the **step 9**

   ```linux
  sudo nano /boot/firmware/config.txt
   ```
  Identify these lines:
   
  #Config settings specific to arm64
  arm_64bit=1
  dtoverlay=dwc2

  **ADD THE BELOW LINE HERE**


 **dtoverlay=vc4-fkms-v3d.**

Crtl+X Save the changes when prompted 

At the end should look like this:

    #Config settings specific to arm64
    arm_64bit=1
    dtoverlay=dwc2 
    dtoverlay=vc4-fkms-v3d

  Now **Restart** your raspberry pi. The above step will allow you to use the display monitor without freezing.
  

7. Ideally your raspberry pi is connected to a LAN cable already and you have internet if so you can skip this step, otherwise set up the wifi user and password on the top right corner. click on networks, find yours and set up properly.

![wifi Login](./images/wifisetup.png 'Wifi login')


8. Open Firefox so now you can copy and paste the commands to install IoT Edge Runtinme from this github page.

![Firefox Access](./images/firefox-access.png 'Firefox Access')


9. Open a terminal to continue

  ![Firefox Access](./images/terminaaccess.png 'Firefox Access')




## Task 3: Setting up: IoT Edge Runtime

1. Run the following command in the terminal:

  ```bash
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb
 ```

2. Once those commands finished install Moby container engine

 ```bash
sudo apt-get update; \
  sudo apt-get install moby-engine
 ```
  When you are asked **Do you want to continue Y/N** press **Y** to continue

3. Next install edge runtime

 ```bash
sudo apt-get update; \
  sudo apt-get install aziot-edge 
 ```

  Once again you will be asked **Do you want to continue Y/N** press **Y** to continue

4. Next steps you will generate a template config.toml file to connect to IoT Central.

 ```bash
   sudo cp /etc/aziot/config.toml.edge.template /etc/aziot/config.toml
   ```


## Task #4 - Azure IoT Central


The following steps can be done in your regular laptop, don't need to do it in your raspberry pi.

1. Go to https://apps.azureiotcentral.com/

   ![Firefox Access](./images/iotcentral.png 'Firefox Access')

2. Click on **My apps** then **+ New Application**
3. In the next screen, select **Custom App**, then **Create App**

4. Now you will assign a name to your application, this name will be the URL for your app. 

   ![Firefox Access](./images/setting-up-central.png 'Firefox Access')

5. Pricing Standard 2 it is the most used, depends of your project you could apply Standard 1 also.

6. Scroll down to select you Subscription and the Region closer to your location. Then click **Create**.




7. Now that you have your new application up and running let's create a Device Template for your raspberry pi. On your left menu select **Device Templates** then **Create a devie template**


![Device Template](./images/create-device-template.png 'Device Template')


8. From the Templates Gallery select **Azure IoT Edge**, then **Next Customize**. 

![Device Template](./images/edge-template.png 'Device Template')


9. In this github you will find a folder named **Files**, click there and download locally the file **iotcentraltemplate.json**.


10. Go Back to IoT Central Application, assign a name to your template **Raspberrypi**. Then click on **Browse** to upload a deployment template, upload the file you just downloaded in the previous step.


![Device Template](./images/template-setup.png 'Device Template')


Your final screen should look like below **Validated**

![Device Template](./images/upload-template.png 'Device Template')

11. Click **Next: Review**, this will generate a simulated module SimulatedTemperatureSensor which we will use to check connectivity. Click **Create**. Finally click **Publish** on the top Menu.


12. Now we can create a Device, on your left menu, select **Devices** then click ** + New**

13. A new window will popup, assign a name to your device **RaspberrypiHoL** then select the template created in previous step, last click **Create**. Now your device will appear as **Registered** state

14. Click on the Device, then up top click on **Connect**. A new window will pop up with the information you need for the config.toml file in your raspberry pi.


![Device Template](./images/connect-device.png 'Device Template')

15. Go back to the raspberry pi, run the following command in the terminal

 ```bash
sudo nano /etc/aziot/config.toml
 ```

16. Use the arrow to go down to the section **[provisioning] source=dps**
Uncomment the lines, removing the **#** as shown below, 8 lines needs to be uncommented, also removed the comments after the **}** closing the symmetric key value if any. Your file should look like similar to my file below but with your new keys:


  ![Firefox Access](./images/config-toml.png 'Firefox Access')

Replace the Following values from IoT Central
  - Id_scope = Id Scope
  - Registration_Id = Device ID
  - Symmetric_key value = Primary Key

Once you are done, press Ctrl+X to close the file then **Y** to overwrite the file 


17. Then run the following command to apply and restart edge runtime:

 ```bash
 sudo iotedge config apply
 ```

18. You can run to see if the containers are deploying, first EdgeAgent should appear, then EdgeHub.

 ```bash
 sudo iotedge list
 ```
 


21. Wait a few minutes, go to your IoT Central App, click on the Device, **Raw Data** you should see the device connected sending simulated telemetry data.


  ![Config File.](./images/device-connected.png 'Config File')

## Exercise #2: Developing Machine Learning Model in Custom Vision

### **Task #1: Custom Vision Project**

**Pre Work, collect pictures of the business case previous to this session.**

1. To use the Custom Vision Service you will need to create Custom Vision Training and Prediction resources in Azure. To do so in the Azure portal, go to  Create Custom Vision page to create both a Training and Prediction resource. Select region and provide appropriate resource name and select Standard Tier for both training and predictions. Click Next.

 ![Custom Vision](./images/custom-vision-create.png 'Create')



2. Select all networks. This can be changed later once the resource is deployed. Click **Review+Create**


 ![Custom Vision](./images/cv-netowrks.png 'Create')


 3. Verify the final details and if it looks good click **Create**.

![Custom Vision](./images/create-cv.png 'Create')

These steps will deploy a Custom vision service. All the projects can use the same resource, or you can also deploy individual custom vision resource per each project.

4. After the deployment is successful  we need to make sure that all the people working on the project has correct access assigned to work with the resource. Go the custom vision resource page and select **Access control(IAM)**.

![Custom Vision](./images/cv-iam.png 'Create')

![Custom Vision](./images/cv-role-assignment.png 'Create')


![Custom Vision](./images/cv-contributor.png 'Create')

![Custom Vision](./images/select-members.png 'Create')

5. Search for user and select the email address. You can select more than one user if multiple people require access to the resource.

![Custom Vision](./images/cv-members.png 'Create')

![Custom Vision](./images/cv-users.png 'Create')

6. Next, we will follow the steps in the tutorial below, however select the following settings when you create the project in Custom vision portal as explained below.

7. When you **Create a new Project** in custom vision, 
- Project Type: **Object detection**
- Classification Types: **Multilabel (Multiple tags per image**
- Domains: **General Compact**

8. Now follow the tutorial to add pictures, tag them and train the model.
https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/getting-started-build-a-classifier

9. After the model is trained, go to **Performance** tab, select **Export** then click in **Docker File**, a new window will open, select **Linux** version, then download. This will generate a zip file in your Download folder.  We will use these files in the Virtual Machine configured in advance as development environment. 

**Note** If you don't see the **Export** option that means you select a different Domain than the General Compact defined above, you will need to re-do the project selecting the right domain.




## Exercise #3: Deploying the machine learning model to the device.

During this exercise, we will use the Virtual Machine we set up in Azure as development environment to put together the solution and push it to our edge device. 

1. Go to Azure Portal, search for the Virtual Machine you set up in the section **Before HoL Steps**. From the overview blade, click **START**, once the **Status: Running** you are ready to click **Connect** then click on **Bastion** enter the credentials you set up before.

2. From the custom vision portal you downloaded the machine learning model in a zip file for linux, you will extract those files and we will move only two files to the virtual machine: 
    - **Labels.txt**
    - **model.pb**

![Files](./images/custom-vision-files.png 'Files')

There are multiple ways to move the files, you can use OneDrive or an Storage Account or any storage sharing app if you can't login directly to Custom Vision and download directly from there inside the virtual machine.

3. Once you move the files, you will replace these files in the **detect** folder as shown below:

![Files](./images/replace-files.png 'Files')

4. Open Visual Studio Code, select the **Code** Folder to open.

5. Check that Docker Desktop is running, you should see your user at the top and the green bar on the bottom left indicates that is running.

![Docker login](./images/docker-login.png 'Docker login')


6. Login to your Container Registry using the Terminal, this step is explained above, follow the same steps and make sure you see **Login Succeeded**

7. In the **Explorer** panel on the left side, look for the file **DetectObj.py** in line #18, you will replace the connection string wiht yours. To get yours go to the storage account you created in Azure portal in the section **Before HoL steps**. Select **Access Keys** and copy the **Connection String** 


![SA](./images/sa-access.png 'SA')


8. In Visual Studio Code, go to the DetectObject.py and replace the connection string in line #18 inside the quotes ""

![replacing](./images/replace-line-18.png 'replacing')

**NOTE**: If you change the name of the container in the storage account from **test** to something else, you will need to go to line #135 and change the **container_name**

9. Click on the file **DetectObject.py** on the right side and press **Crtl+S** to make sure you are saving those changes.


10. Go to the top menu, select **Terminal** then **New Terminal** copy the below command and click enter. Don't forget the dot :)

```linux
docker  build -t rpi_mycontainer .
```

If you need to run this build many times, make sure you delete the image before the build with the below command: 

docker rmi rpi_mycontainer 


**NOTE** This Build will take around 3 hours, here we do a break and we will regroup the day after

**Day After**

11. Now that the solution is Built, we will tag it replacing in this command your container registry user, run it in the terminal also:


```linux
docker tag rpi_mycontainer YOUR-USER.azurecr.io/rpi_mycontainer:latest
```

In my example looks like the below:

```linux
docker tag rpi_mycontainer containervi.azurecr.io/rpi_mycontainer:latest
```
![Tag repo](./images/docker-tag.png 'Tag repo')


12. Now we are ready to push it to Azure Container Registry with the below command, once again, replace YOUR-USER with your actual user.

```linux
docker push YOUR-USER.azurecr.io/rpi_mycontainer:latest
```

In my example, looks like below: 

```linux
docker push containervi.azurecr.io/rpi_mycontainer:latest
```
![Tag repo](./images/push-container.png 'Tag repo')

The above command will take just a few minutes.

13. Once is completed go to Azure Portal, look for  your **Container registry**, click on repositories, now you should be able to see your repository published:

![repository](./images/acr-repository.png 'repository')


If you click in the repository you will see the version just created and the url to your repository:

![repository](./images/container-latest.png 'repository')


14. In Visual Studio Code click on the file **deployment.json** on the left panel, we will make some changes on the right side panel
Look fo the following lines: 
  - #13 **username**: YOUR-USER_HERE(this is the container registry user).

  - #14 **password**:YOUR-PASS-HERE(this is the container registry password)

  - #15 **address**:YOUR-LOGIN-SERVER(this is the container registry login server)

![Deployment](./images/deployment-change.png 'Deployment')


  - #45 **"image": "YOUR-USER-HERE.azurecr.io/rpi_mycontainer:latest",**

![Deployment](./images/deployment-45.png 'Deployment')




Now save the changes pressing **Ctrl+S**. Copy the content in this file, select all and copy.

15. Go to IoT central App, click on **Device Templates**, click on the template you have on the right. On the top click on **Version**, assign a name such as **Raspberrypi-v2**, then **Create**.

![New Template](./images/new-template.png 'New Template')


16. Click on **Edit Manifest**, remove the content and paste the content from Visual Studio Code from the file deployment.json. **Save**, close it with the **X** on the right corner.

17. Add capabilities, click **+ Add capability**:
  - Display Name: **data**
  - Name: **data**
  - Capability type: **Telemetry**
  - Semantic Type: **none**

**Save** the new capability, and then on the top Menu, select **Publish**

![Add Capability](./images/add-capability.png 'Add Capability')

15. Make sure your raspberry pi is connected to internet, the camera is also connected and infront of the items you use to train the Custom Vision Model, we are ready to test E2E your model here. Go to **Devices on the left** select your device on the right, click on **Manage Template**, then **Assign Template**, select the template you just created.

15. Restart the raspberry pi to trigger iotedge runtime to check the new deployment manifest. In the Modules tabs you can see the status of the modules during the deployment, will take a few minutes until they are all in **Running** mode. 

You can for the IoT Edge Runtime restart, by openning a terminal and running the following command:

 ```bash
 sudo iotedge config apply
 ```


You can also check inside the raspberry pi opening a terminal and running:
```bash
**watch sudo iotedge list**
```
16. At this point the camera should be connected through USB to the RPI should be infront of the object you took the pictures to train your model to start streaming telemetry data. Make sure your camera is ON. After a few minutes of the modules all running you should start checking your data.


![Modules](./images/iot-central-modules-running.png 'Modules')


17. Check telemetry, in IoT Central go to the tab **Raw Data** you should see the telemetry from your device coming through, in my case I trained with Batman, the character :) so I am successfully predicting Batman is infron of my camera with a confidence level of 94.29%. In your case you should see your item you use to train the model and a confidence level, this number will vary based on the # of pictures, lights, training and background. At this point you have a clear idea how solutions end to end works for Visual Inspections! 

![Modules](./images/telemetry.png 'Modules')

18. Check Storage account, in this storage account we are sending the latest picture taken from the camera is overwritting the picture every second, so if you change the elements infron of the camera you will see different pictures, however we are always replacing to avoid having 1000s of pictures very quickly.

19. Go To Azure, click on the Storage Account you created before, click in **Containers** on the left menu and select **test** container, there you should see the below file:

![Modules](./images/pics.png 'Modules')


20. Download the File to see what exactly the camera is seeing.

21. The camera is streaming inside the RPI, in the port 8000, however you don't have enough resources in the RPI to see a live streaming, remember is an small computer. So you can check the streaming but after a few second the RPI freeze and you need to restart.

22. To do that, in the RPI open a terminal and run the following command to 

```linux
sudo docker ps
```
23. Copy the ID of the module rpi_mycontainer

![Modules](./images/docker-ps.png 'Modules')

24. Run the following command using the ID you copy from your previous step.

```linux
sudo docker inspect YOU-ID-HERE
```

![Modules](./images/docker-inspect.png 'Modules')

25. Now, go down to the section **Networksettings**, then **Networks** then copy the **IPAddress** in my example is **172.18.0.3**, with that ip go to Firefox within the raspberry pi and go to **YOUR-IP:8000), now you should see the live streaming jsut for a few seconds/minutes. 

![Modules](./images/docker-ip.png 'Modules')

Before you go, please take 5min to send us your feedback: 

https://forms.office.com/r/swW9Y1a05G

## Exercise #4: Delete Resources

At this point you can delete all the resources, if you need to keep them running to continue training your peers or share the accelerator across you can keep the resources running, however we recomment to **STOP** the Virtual Machine to not incur in additional cost if you are not going to rebuild the solution. The steps to stop the VM are detailed in the section **Before HoL Steps**, Task 1, step **#9**

## Troubleshooting

1) "Low voltage detected", you need to change your power cord, not all the powerd cords works well in the Raspberry Pi 4.

2) If you need to set up the wifi through command line:
 Navigate to the **/etc/netplan** directory and locate the appropriate Netplan configuration files. The configuration file might have a name such as **01-network-manager-all.yaml** or **50-cloud-init.yaml**

    Type the following command:
      ```linux
      ls /etc/netplan/
      ```

    Then, edit the Netplan configuration file, type the command:
      ```linux
      sudoedit /etc/netplan/50-cloud-init.yaml
      ```

    Replace SSID-NAME-HERE and PASSWORD-HERE with your SSID network name and password. **Dhcp4:true** will enable static IP to your device.

    After the changes, run:

    ```bash
    sudo netplan apply
    ```


  3) If your raspberry freezes constantly run the following command: 
   ```linux
  sudo nano /boot/firmware/config.txt
   ```
   Identify these lines:
   
  #Config settings specific to arm64
  arm_64bit=1
  dtoverlay=dwc2
**ADD THIS LINE HERE: dtoverlay=vc4-fkms-v3d.**

Crtl+X Save the changes when prompted 

At the end should look like this:

    #Config settings specific to arm64
    arm_64bit=1
    dtoverlay=dwc2 
    dtoverlay=vc4-fkms-v3d


**Usefull commands:**
- **sudo poweroff**
- **sudo reboot**
- **ip r**: to get the raspberry IP in case you need to SSH your device.
- **ifconfig** to capture the docker ip, then go to the browser in your raspberry type that
ip:8000 and you should see the camera streaming. 
- **sudo iotedge system restart**
- **sudo iotedge check**
- **watch sudo iotedge list**




