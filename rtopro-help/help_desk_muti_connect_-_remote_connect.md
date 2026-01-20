# http://www.rtopro.com/help/help_desk_muti_connect_-_remote_connect.htm

# Muti Connect - Remote Connect 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Muti Connect - Remote Connect 

|  [](remote_connections_into_rto_pr.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_purchase_order_inventory.md "Next Topic")  
---|---  
  
With the Multi connect - remote connect feature you can connect to several remote stores easily through an internet connection. A secure connection should be setup between your stores and the location you wish to remote in from. To use this feature you must have the Network version of RTO Pro in multiple locations.

To enable this feature you have to get a keycode from Tech Support, call 352-383-9375 for more info.

After you have enabled multi-connect and you have setup a secure connection between the remote location and the stores follow the directions below to setup each connection.

![image79](image79.jpg)

Select / Launch button: Click this button to launch the selected connection. You can also push ENTER or double click the connection with the mouse.

Add new Store / Connection button: Use this button to setup new connections. See details below about the data you fill in for each store / connection.

Remove Selected Connection button: Use this button to remove the selected connection.

Adding a new connection / store

Connection: This is a name you will enter and it is only for your reference, it can be anything you like to describe the store / connection. When you save the other settings below you will be prompted to enter the connection description.

Server Name: This is the computer name of your server computer or if connecting through the internet the IP address of the router at the store you are connecting to such as "76.26.111.11".

Location of Data File on Server: This is the folder the RTO Pro data file is located in on the server computer, it is not how the workstation computer finds the data file, it is how the server computer finds it, it is always a local path like "C:\RTOwin\" or "D:\rtowin\" it is NEVER a network path such as "\\\server\c\rtowin"it is also NEVER A MAPPED DRIVE or IP address.

Path for Shared files on Server (DataPath): This is the location of the shared folder for RTO Pro on the server, it should be a network path such as "\\\server\c\rtowin\" or include an IP address if connecting through the internet such as "\\\76.26.111.11\rtowin\".

There are many ways you can setup a secure connection between your multi connect computer and the stores computers. The topic in the link below is one example, except for the purposes of multi/ remote connect the Store computer is the SERVER and the Multi connect computer is the WORKSTATION.

[Click here for one example of how to setup a secure tunnel between 2 computers.](help_desk_company_wide_master_inventory.md#setting_up_secure_tunnel)
