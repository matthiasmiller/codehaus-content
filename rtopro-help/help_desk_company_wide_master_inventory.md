# http://www.rtopro.com/help/help_desk_company_wide_master_inventory.htm

# Company Wide Master Inventory and Remote Payment capability

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Company Wide Master Inventory and Remote Payment capability

|  [](category_markup_report_definit.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](epo-early-payoff-and-how-it-ch.md "Next Topic")  
---|---  
  
The company wide master inventory feature allows you to view all stock inventory in all stores from any store location. This is useful if you have multiple stores and transfer inventory from store to store. With this feature a store who has a customer who wants a particular item but doesn't have the item in stock can look through the other stores inventory and see if it is available from any of the other stores.

Remote payments is where any of your stores can take payments for other stores. For instance if you have a customer who has an account at your store #1 and they go into store #2 to pay a payment this functionality would allow them to do that. When a payment is taken at one store for another store the information is sent via the corporate office or our web servers to the store where the customers has the account. That store would be notified of the pending payment they need to process. When they process the payment a petty cash payout is created automatically to account for the money, the store that received the money will have a negative petty cash payout to account for the money they took in. This function uses the same connection as the master inventory so if you follow the directions below you can use either or both of these capabilities in RTO Pro. 

Requirements to enable remote payments or company wide inventory inquiry.

There are 2 options for using remote payments and companywide inventory inquiries in RTO Pro, requirements for each is below: 

Requirements if using RTO Pro web services to host data for remote payments and companywide inventory.

1\. Current RTO Pro support plan or lease plan... There are no additional fees or charges for this service.

2\. Internet access at stores.

If you plan on using RTO Pro web services you can skip the rest of this topic as it explains how to setup a WAN which is not needed for this feature if you use RTO Pro web services. Call 352-383-9375 to get a web services account.

* * *

Requirements if NOT using RTO Pro web services to host data for remote payments and companywide inventory.

1\. RTO Pro Corporate Edition / Home Office software.

2\. High speed Internet at stores and home office.

3\. Internet service at Home Office must have a static IP address (IP address that is always the same, check with your internet provider).

4\. Windows Server 2003 or 2008 in NOT required at your home office, Windows XP, Vista or Win 7 will work for your home office computer as well as the stores computers. Having Windows Server at your home office does have an advantage over other versions of Windows for this purpose as it has VPN features built into it.

Secure remote connections

Since the connection is made through the internet a secure connection needs to be setup between the stores computer and the home office computer. This can be done by setting up a VPN (Virtual Private Network) or using some generic tunneling software like SSH, SSL, Zebedee or K-Secure VPN. If you have Windows Server at your home office Windows Server has VPN capability built into it so no other VPN software would be required.

If you need further assistance setting up a secure connection between your stores and home office contact your internet service provider or a network specialist. Our support services do not include setting up your internet, routers, VPN or remote connections.

We recommend RTO Tech to anybody who needs help setting up a secure connection or VPN. See their website here http://www.rtotech.com They also offer remote network and hardware support and can lock down your system to prevent employees from accessing websites you do not authorize.

[If you already have a secure connection or tunnel from your store to home office see below for instructions.](help_desk_company_wide_master_inventory.md#securealready)

Setting up store to home office computer connection if you already have a secure tunnel or connection between store and home office

Setting up the server computer (computer running RTO Pro Home Office)

1\. Get the IP address of the server computer. Open a command prompt, to open a command prompt in Vista you can click on the Windows Start button and type "CMD" where it says "Start Search" and push enter. From the command prompt window type "IPCONFIG" and a window like below will be displayed. The IP address for the computer this was run on is 192.168.1.103.

![image35](image35.gif)

2\. Next your router has to be setup for port forwarding port 3050 to your home office server computer. Firebird SQL Server uses port 3050 and the IP address to forward to needs to be the servers computers (the one with the home office data file) IP address. See the image below. The 1st application listed is how it needs to be setup, the only thing that would need to be changed is put your servers IP in the IP address line and check the enable checkbox. Note all routers are different so see your router instructions on how to get to the setup for the router. For the test router we used to get to the setup mode you open internet explorer and type "http://192.168.1.1/" in the address line, then leave user name and password blank (only works if you have not setup password for the router). Note this example instructions are for a Linksys WRT54G router, other brands and even other models will be different.

![image67](image67.jpg)

3\. From your router setup find your routers IP address. You can also search online for "Whats my IP" to find your router IP. You will need this in the store setup below.

Setting up the remote (workstation) computers (computers running RTO Pro) if you already have a secure tunnel setup.

1\. In RTO Pro go into Setup > Store Setup and click on the Other tab. In the Master Inventory server name put the IP address of the router at your home office, make sure this is the ROUTER's IP not the server computers.

In the "Path to database file on home office server" put the following: c:\rtoho\

The path above is the default path, if your path is different put the correct path.

Below is a screenshot of where you put the settings in RTO Pro. It is in Store Setup under the "Other" tab.

![image37](image37.gif)
