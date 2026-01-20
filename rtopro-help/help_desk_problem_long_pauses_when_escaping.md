# http://www.rtopro.com/help/help_desk_problem_long_pauses_when_escaping.htm

# Problem: Long pauses when escaping from various screens when using RTO Pro over a network.

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Problem: Long pauses when escaping from various screens when using RTO Pro over a network.

|  [](help_desk_macro_can_not_be_found_or_is_disabled_message.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](date_warnings.md "Next Topic")  
---|---  
  
In RTO Pro this problem is usually seen in pauses when escaping from the inventory list screen or the customer list screen when using RTO Pro over a network using Windows NT,2000 or XP.

The changes listed below only need to be done on the server computer.

The keys described below are automatically changed by RTO Pro setup for installations after 10-20-02 to the following settings.

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters

Value Name: SharingViolationDelay

Data: 50

Value Name: SharingViolationRetries

Data: 1

The settings above have been tested on a Windows XP network and have been found to stop the delay.

Below is pasted from the article listed below from Microsoftâs website.

Q150384 : http://support.microsoft.com/support/kb/articles/Q150/3/84.asp

Shared File Access Is Delayed if the File Is Open on Another Computer

The information in this article applies to:

•Microsoft Windows NT Workstation versions 3.51, 4.0

•Microsoft Windows NT Server versions 3.51, 4.0

•Microsoft Windows 2000 Professional, versions SP1, SP2, SP3

IMPORTANT: This article contains information about modifying the registry. Before you modify the registry, make sure to back it up and make sure that you understand how to restore the registry if a problem occurs. For information about how to back up, restore, and edit the registry, click the following article number to view the article in the Microsoft Knowledge Base:

Q256986 Description of the Microsoft Windows Registry

SYMPTOMS

If you try to open a file on a computer that is running Windows NT over the network and the file is open on another client computer that has sharing restrictions, there is a delay of approximately one second before the sharing violation error message is returned. If the client application is accessing a number of files on the server, this delay may become significant. These symptoms can be easily seen with any multi-user, file-based application, such as the Jet database engine that has shared database files.

NOTE: This behavior is not observed when accessing files on LAN Manager or Windows for Workgroups shares.

CAUSE

This issues occurs because an optimization in the Windows NT Server service delays returning a status to the client while it tries to internally resolve the sharing violation.

RESOLUTION

To resolve this issue, it may be best to turn off this optimization. To do so, you must make the following two registry additions.

WARNING: If you use Registry Editor incorrectly, you may cause serious problems that may require you to reinstall your operating system. Microsoft cannot guarantee that you can solve problems that result from using Registry Editor incorrectly. Use Registry Editor at your own risk.

2.Start Registry Editor.

3.Locate the following registry key:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters

3.Add the following information:

Value Name: SharingViolationDelay

Data Type: REG_DWORD

Data: 0 (Default: 200)

Value Name: SharingViolationRetries

Data Type: REG_DWORD

Data: 0 (Default: 5)

4.Quit Registry Editor, and then restart the computer.

MORE INFORMATION

If the Server service receives a request for file that is already open, it receives a sharing violation from the local server. The service then waits for a short period before trying to access the file again. This process is repeated a number of times, internally to the server, to try to resolve the problem before returning to the client.

This feature is controlled by the following two registry values:

•SharingViolationDelay

Default 200 (msec)

This is the period of time that the server waits between retries. If it is set too low, the server receives multiple sharing violations. If it is set too high, the Server Message Block (SMB) response to the client might be delayed, thereby reducing performance.

•SharingViolationRetries

Default 5

This is the number of times that the server retries an SMB requested operation if it receives a sharing violation from the local server's file system. Operations that are affected by this include open, rename, and delete. This minimizes network traffic because if the server can resolve the sharing violation locally, the remote clientdoes not have to retry the operation.
