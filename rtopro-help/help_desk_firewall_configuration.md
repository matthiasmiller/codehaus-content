# http://www.rtopro.com/help/help_desk_firewall_configuration.htm

# Firewall configuration 

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Firewall configuration 

# 

|  [](help_desk_server_not_found.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_permissions_-_file_and_folder.md "Next Topic")  
---|---  
  
Below are some examples of configuring firewalls. This only needs to be done if you are getting a error message such as "Unable to locate server".

[For McAfee Firewall setup click here.](help_desk_firewall_configuration.md#mcafee_firewall)

Windows Firewall

In Firewall Settings under the "Exceptions" tab make sure Firebird Server is present and if you are on a network system make sure "Firebird Port" is present also.

![image53](image53.jpg)

Below is what the properties of Firebird Server should look like.

![image57](image57.jpg)

On 64 bit Windows fbserver.exe is in the "Program Files (x86)\Firebird\Firebired_2_1\bin\" folder

![clip0003](clip0003.png)

If you are on a network system (multiple computers using RTO Pro) and Firebird Port is not in the exceptions list click on the "Add port" button. Set port number to 3050 and Protocol to TCP.

![image54](image54.jpg)

Set scope to "My Network (subnet) only"

![image55](image55.jpg)

McAfee Firewall setup

After installing RTO Pro you should see a message similar to the image below. Make sure you choose "Allow access". See below for how to verify Mcafee firewall is setup correctly.

![mcafee1](mcafee1.jpg)

To verify Mcafee is setup correctly follow the steps below.

Double click on the Mcafee icon by the clock, then click on Internet & Network like it shows below, then click configure. (see below this image for more instructions)

![mcafee2](mcafee2.jpg)

Click on the Advanced button in the Firewall section. Then click Program permissions on the left of the screen. Find Firebird SQL Server in the list and make sure it is set to Full Access as it shows below.

![mcafee3](mcafee3.jpg)
