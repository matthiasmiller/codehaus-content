# http://www.rtopro.com/help/mapped_drives_and_windows_uac.htm

# Mapped Drives and Windows UAC

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Mapped Drives and Windows UAC

|  [](automatic_deposit_entry_in_end.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](xcharge_emv.md "Next Topic")  
---|---  
  
Mapped drives are not recommended to use with RTO Pro. There are issues using mapped drives on computers with UAC enabled.

Below is a topic from Microsoft Technet that explains the issue and a work around to fix the issue. If you must use mapped drives and you have UAC enabled this page may have a solution that will fix the issues you may run into, however use this at your own risk. We recommend using a UNC path instead of mapped drives for all network systems for RTO Pro. Contact support to setup your network for you that uses UNC paths instead of mapped drives.

<http://technet.microsoft.com/en-us/library/ee844140%28v=ws.10%29.aspx>

The PDF file below is from the page above 8/25/2014, in case the link above is ever not accessible.

<http://www.rtopro.com/MappedDrives.pdf>

This issue is commonly seen in the download update feature of RTO Pro from a workstation with UAC enabled that uses a mapped drive which will prevent the update program from running. There are probably other features in RTO Pro that will not work correctly with mapped drives that are not setup correctly also, but at the time of this writing it has not been thoroughly tested. After very limited testing it appears that because the update feature in RTO Pro downloads files from the internet it is being treated differently than the main RTO Pro program and this issue did not seem to cause any problems in other features of RTO Pro.

The best solution is to NOT used mapped drives for RTO Pro.

If not using a mapped drive is not an option for you and you cannot fix your network drive or apply a workaround you will have to install updates manually on affected workstations. To do this follow the steps below:

1\. Browse through your mapped drive to the "Update" subfolder.

2\. You should see a file there "update.exe", double click this file to start the install. Please note when you double click this file sometimes it takes a few minutes for the install to begin since the file is copied to the local computer first, then it is ran. If you do not see the file there download the update from your server computer and then the file will be present.
