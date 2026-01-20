# http://www.rtopro.com/help/help_desk_networksetup.htm

# Network Setup

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Network Setup

# 

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
After installing Network version of RTO Pro the Data Path form will display (image is below), this form has 4 settings on it, each is described below:

![Capture7](capture7.png)

Server Name: This is the computer name of your server computer. (This should be the same for all computers on the network)

Location of Data File on Server: This is the folder the RTO Pro data file is located in on the server computer, it is not how the workstation computer finds the data file, it is how the server computer finds it, it is always a local path like "C:\RTOwin\" or "D:\rtowin\" it is never a network path such as "\\\server\rtowin"it is also NEVER A MAPPED DRIVE. (This should be the same for all computers on the network)

Path for Shared files on Server (DataPath): This is the location of the shared folder for RTO Pro on the server, it should be a network path such as "\\\server\rtowin\", except on the server computer it will be a local path such as "C:\rtowin\". (This must point to the same folder on the server for all computers and this folder must also have the RTO Pro data file in it.)

(Optional) Enter a title: Anything you enter here will be displayed in red on the status bar (lower right of the screen) and in the taskbar. This is to help locations that run several different companies from one computer see which company they are currently working with.

An example of the info a SERVER computer should have is below:

Server Name: MYSERVER

Location of Data File on Server: C:\RTOWIN\

Path for Shared files on Server (DataPath): C:\RTOWIN\

An example of the info a WORKSTATION computer should have is below:

Server Name: MYSERVER

Location of Data File on Server: C:\RTOWIN\

Path for Shared files on Server (DataPath): \\\MYSERVER\RTOWIN\

Note: After setting the network system check on the bottom of the Main Menuâs in RTO Pro.

The server should read:

Server Name: MYSERVER

Data on Server: C:\RTOWIN\

Localpath: C:\RTOWIN\

DataPath: C:\RTOWIN\

Note: The server computer must be setup so the datapath folder is shared with read and write access for all users who will be using RTO Pro on your network.

The workstations should read:

Server Name: MYSERVER

Data on Server: C:\RTOWIN\

Localpath: C:\RTOWIN\

DataPath: \\\MYSERVER\rtowin\

To setup the path to the server the easiest way is to click the "Search" button and browse to the server and select the "path.dat" file that will be on the server. Below are instructions on how to use the Search button to browse to setup a workstation as well as how to use it to setup the server computer. Note the server computer has to be setup first before you can setup any of the workstations.

Using the Search button to setup a workstation

On the workstation when the datapath form is displayed click on the "Search" button. A file open dialog box will be displayed, the file that needs to be found is "path.dat" that is in the data folder on your server computer. Most versions of Windows the browse screen looks different but below is a screen shot of what it looks like in Windows 7. You will browse to Network > your server computer > RTOwin and then click the "path.dat" file and click open on the lower right (or double click on the file "path.dat" when it is displayed in the file list). Note "RTOwin" is the default folder your folder may be different on your server if you did not use the default installation folder or named the folder something different when you setup the sharing.

![Capture8](capture8.png)

Using the Search button to setup a server computer

On the server computer when the datapath form is displayed click on the "Search" button. A file open dialog box will be displayed, the file that needs to be found is "rtoprodata.fdb" that is in the data folder on your server computer. You will browse to Computer > C > RTOwin and then click the "rtoprodata.fdb" file and click open on the lower right (or double click on the file "rtoprodata.fdb" when it is displayed in the file list). Note "RTOwin" is the default folder your folder may be different if you did not use the default installation folder.

Note: You must purchase the network license to use RTO Pro in a networked / shared environment.

After setting up the path to the server if you get a message "Unable to connect to server computer" or something similar when you run RTO Pro you need to configure your firewall on the server computer. [See the topic here for instructions on how to configure a firewall.](help_desk_firewall_configuration.md)
