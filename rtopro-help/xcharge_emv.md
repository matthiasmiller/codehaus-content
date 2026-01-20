# http://www.rtopro.com/help/xcharge_emv.htm

# Xcharge EMV support

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Xcharge EMV support

|  [](mapped_drives_and_windows_uac.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_how_to_move_due_dates.md "Next Topic")  
---|---  
  
Starting in RTO Pro version 5.8.602 Xcharge EMV support was added. EMV is a global standard for cards equipped with computer chips and the technology used to authenticate chip-card transactions.

To contact Xcharge support their phone number is 800-338-6614.

To find out more about EMV see this site: [www.openedgepay.com/emv](http://www.openedgepay.com/emv)

If you are currently using Xcharge to process credit cards and upgrade to this version of RTO Pro or later please follow the steps below to setup your Xcharge account in RTO Pro. 

1\. On your computers that have the Xcharge client and or Xcharge server installed already make sure you have the latest version of Xcharge installed. Ver 8.0 release 4 or newer. You can download it here: <http://www.rtopro.com/XC8.0.4.4_OI.exe> Note this file and maybe newer ones are also available directly from Xcharge at [www.x-charge.com](http://www.x-charge.com). Please note you may need to contact Xcharge support to complete the installation of this file, their number: 800-338-6614.

2\. On your computers without the Xcharge client installed install the XCclient.dll file with the setup file here: <http://www.rtopro.com/XCClient8.0.4.4.exe> Note this file and maybe newer ones are also available directly from Xcharge at [www.x-charge.com](http://www.x-charge.com).

3\. Go into RTO Pro > Setup Menu(option 5) > Store Information Setup(Option 1), click on the credit card tab. You will see line 2 and 3 have changed, you will need to enter your "Processing Account Name" from Xcharge in these boxes(if you only have one merchant account only line 2 is required). See the next step for instructions to find your Processing Account Name in Xcharge. Please note the other credit card options have not changed but you should verify you have your Xcharge user name and password entered in lines 4 and 5. This step only needs to be done on ONE computer per company/store.

![Xcharge Setup EMV](hmfile_hash_a1b62a47.png)

4\. To retrieve your Processing Account Name go into the Xcharge client, click the "Transaction" menu item, then hover over Processing Account, you will see the name in the menu that opens, like it shows below ("Live" in this case).

![Xcharge Client PAN](hmfile_hash_e74fecd6.png)

You will be ready to process credit cards after this is completed. Contact Xcharge if you wish to purchase EMV compatible credit card swipers / pin pads.

To contact Xcharge support their phone number is 800-338-6614.

* * *

Additional notes that may be helpful:

Processing Account Names cannot contain spaces, some versions of Xcharge will allow you to enter them with spaces, if your PAN has spaces in it you must edit the PAN and remove the spaces.

You can edit the processing account name from the Xcharge Server Setup screen. You can start the Xcharge server by clicking on the Xcharge icon in the task tray(beside the clock on the task bar).

If Xcharge server was installed as a service on your computer, follow the steps below to bring up the Xcharge Server Setup screen.

1\. End the xchrgsrv.exe and xcservice.exe (not xcsecurityservice.exe) processes in the task manager.

2\. Open XCharge from the desktop icon. That should put the server in the system tray and allow to open the server to make the changes.

Once you are in Setup for the Xcharge Server, click on Credit Cards, then click the connections tab, as shown below. From there you can see or edit your processing account name.

![clip0018](clip0018.png)

To contact Xcharge support their phone number is 800-338-6614.
