# http://www.rtopro.com/help/help_desk_server_not_found.htm

# Network Connection Troubleshooting / Not able to find Server computer on the network.

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Network Connection Troubleshooting / Not able to find Server computer on the network.

# 

|  [](rto_pro_information_registration.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_firewall_configuration.md "Next Topic")  
---|---  
  
![image52](image52.jpg)

![image56](image56.jpg)

Messages similar to the ones above can be caused by several different network problems or from the Firebird SQL Server Service being turned off. Below is a checklist of possible causes and solutions.

1\. Your computer is not connected to the network due to a cable being unplugged, a router being unplugged, etc.

2\. Your computer is not connected to the network due to a hardware failure such as a router, network card or network cable being bad.

3\. Your computer is not connecting to the server computer due to a firewall on the server computer or your computer blocking access to it. [See Firewall setup below.](help_desk_server_not_found.md#firewall) See [how to determine if port 3050 is blocked](help_desk_server_not_found.md#how_to_determine_if_port_3050_is_open)

4\. The Server Name is wrong. To correct this double click on "datapath=" at the bottom of the Main Menu and correct the Server name or click on the Search button then browse to your network computer and select the "path.dat" file in the data folder on the server computer.

5\. If you are on the server computer and you are getting this message the message from SQL engine will say "Unable to complete network request to host "localhost".". If this is the case the problem is in the firewall settings on this computer. See below for instructions on how to setup the Windows Firewall. If you have a different firewall see the instructions for that firewall to configure. Some firewalls such as Norton Security will start ignoring rules you setup and start blocking access to programs you have set to allow when the annual subscription to their service ends.

6\. The Firebird SQL Server Service has been shut down. This service has to be running, to check this [see the instructions at the bottom of this page or click here](help_desk_server_not_found.md#verifyfirebirdservice).

The first 2 possibilities can be eliminated by doing the following: Browse to Network Neighborhood > Entire Network and verify you can see and access the server computer from the computer you are getting this message, if you can then this would eliminate the problem possibility of the problem being caused by a cable being unplugged or network hardware failure. If you are prompted for a user name and password when you browse to the server computer through the Network then you will have to browse to the server computer manually through network neighborhood and enter the user name and password before using RTO Pro on the workstation or disable the password for the users account on the server so you will not have to enter a network password or map a network drive to the RTO Pro data folder on the server computer.

Note: By default RTO Pro uses the server's computer name for the "Server Name" setting as displayed below. This will work only when the clients (workstations) belong to the same Domain/Work group as the server computer. If they belong to different domains / work groups on your LAN you will have to get the IP address of your server computer and manually type the IP address where the "Server Name" is (this only applies to network versions of RTO Pro). To get IP address of your server computer click on Start then type cmd.exe in either the Vista search box or the XP run box, this will bring up a Command Window, type ipconfig and push enter, your IP address will display. It would be something like 192.168.1.100. You would then type that in the "Server Name" field on all of your workstations.

Note: If RTO Pro has been working on your system and then suddenly stops working and you are attempting to change the path and server settings STOP. Once the settings below are set and working they NEVER need to be changed unless you are changing your network configuration (changing computers etc.). If RTO Pro has been working with the settings you have and it suddenly stops the problem WILL NOT be the paths. Most of the time when workstation computers stop working it is due to network problems, router unplugged or needs to be reset, cable unplugged, hardware failure etc.

![image90](image90.jpg)

Firewall setup

If the problem is caused by a firewall below is how the firewall needs to be setup. These are screenshots from Windows Firewall in Vista, note other firewalls will be different and XP will look different. For instructions on how to configure [Mcafee Firewall click here.](help_desk_firewall_configuration.md#mcafee_firewall)

In Firewall Settings under the "Exceptions" tab make sure Firebird Server is present and add a Port and name it "Firebird Port".

![image53](image53.jpg)

Set port number to 3050 and Protocol to TCP.

![image54](image54.jpg)

Set scope to "My Network (subnet) only"

![image55](image55.jpg)

Below is what it looks like to add the Firebird Server to Windows Firewall.

![image57](image57.jpg)

How to verify the Firebird SQL Server Service is running

1\. Open Windows Control Panel (click Start > Control Panel)

2\. Switch to classic view if its not on classic view already (see top left of picture below)

3\. Double click on "Administrative Tools"

4\. Double click on "Services"

5\. Look for "Firebird Guardian" and "Firebird Super Server" in the list.

6\. Make sure status for both says "Started" and make sure Startup type for Firebird Guardian is "Automatic" and Firebird Super Server is "Manual" (like it shows in the picture below. To start a service if its stopped click the service and then click "Start the service", to change the startup type double click on the service and then select "Automatic" from the dropdown list for startup type.

In the services window below is how your system should be set for the Firebird Services.

![image66](image66.jpg)

How to determine if port TCP port 3050 is open or being blocked

TCP port 3050 is used by the Firebird SQL Server database that RTO Pro uses, to use RTO Pro on a network this port has to be open and not blocked by a firewall on the server computer. Below is how to check if the port is open.

1\. Open up a command window on the server computer (under programs<accessories>command prompt), then you can run the "netstat" command (just type netstat in the command window) and check to see if port 3050 is open. If it is open, you can test whether it accepts connections by telnet-ing to the port. Just type:

telnet [hostname|IPaddress] 3050

Example:

telnet localhost 3050

or if the name of your server computer is vista64 you could use

telnet vista64 3050

Try running telnet on the server and on the workstations to see if they can connect.

If netstat is not recognized as a valid command see the website here for instruction on installing the netstat utility: <http://www.wikihow.com/Telnet-in-Vista>

If telnet cannot connect you will get a message like below, if it is able to connect you will see an empty command window.

![image81](image81.jpg)

If all of this fails, perhaps you should check whether the remote server is reachable at all. You can use 'ping' command:

ping [hostname|IPaddress]

Example:

ping 192.168.0.22

To find out your servers IP address you can type "ipconfig" from the command prompt.

Please note that ping can still give you 'host unreachable' message even if host is up. This is because the firewall software can drop the ICMP (ping) packets (it's done to prevent some viruses from spreading, or network scans).
