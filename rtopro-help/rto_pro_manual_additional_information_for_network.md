# http://www.rtopro.com/help/rto_pro_manual_additional_information_for_network.htm

# Additional Information for Network Site License / Setting Up RTO Pro on a Network 

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** RTO Pro Manual >

# Additional Information for Network Site License / Setting Up RTO Pro on a Network 

# 

|  [](rto_pro_manual_store_setup_information.md "Previous Topic") [](welcome_welcome_1.md "Parent Chapter") [](rto_pro_manual_special_considerations_for_multiple_stores.md "Next Topic")  
---|---  
  
There are 2 configuration to use RTO Pro on a network with multiple computers, each is described below:

Peer to Peer Network (All computers have Windows XP or Vista)

When using RTO Pro on a network you need to have 1 computer that acts as a "Server". This will be the computer which stores the data files for all the other computers. This computer should be the fastest on the network and preferably should have some type of backup storage device like an external hard drive or USB drive for backup purposes..

This "Server" computer can also be used to take transactions (payments, loading contracts etc.), it does not need to be a dedicated server. The other computers on the network will be considered "Workstations".

When installing RTO Pro install on the "Server" computer first. When you are asked if you want to create databases on this computer, select yes. The "Workstation" computers do not need to have the databases on them. You will only have 1 set of databases, which will be used by all computers on the network. When installing RTO Pro on the "Workstation" computers when asked if you want to create databases on this computer, select no. On the "Workstation" computers you will need to enter or find the path to the directory on the "Server" computer, which has the databases installed into it. To select the path the network will have to be setup and functioning properly, consult your network administrator about setting up your network. The shared data folder (DataPath, default path "C:\RTOwin" on the server) has to be setup to be shared with read and write access on the server computer.

Server Network (At least 1 computer with Windows Server 2003 or 2008). This is the only method that will work if you need to have multiple simultaneous remote connections to the server or want to be able to access RTO Pro remotely with Remote Desktop and not interrupt the stores use of the computer you connect to.

When using RTO Pro with a Server Network the preferred method of installation is to have RTO Pro installed only on the Server 2003 computer and use Remote Desktop or Terminal Services to connect the workstations to the server. You can also use thin clients with a server computer instead of having complete computers at each workstation. A thin client (sometimes also called a lean or slim client) is a client computer (workstation) which depends primarily on the central server for processing activities, and mainly focuses on conveying input and output between the user and the remote server.

You can also have a Server 2003 network configured like a peer to peer network as described above.

RTO Pro Data Path Form

After installing Network version of RTO Pro the Data Path form will display, this form has 3 settings in it, each is described below:

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

The workstations should read:

Server Name: MYSERVER

Data on Server: C:\RTOWIN\

Localpath: C:\RTOWIN\

DataPath: \\\MYSERVER\rtowin\

Note: In order to use RTO Pro over a network you must purchase the Network Site License.
