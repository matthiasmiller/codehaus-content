# http://www.rtopro.com/help/help_desk_run_time_error_429_activex_component_can_t_create_object.htm

# Run-time error '429': ActiveX component can't create object

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Run-time error '429': ActiveX component can't create object

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
Below is directly from Microsoftâs web site with solutions to this problem. We include a file on our CDâs (VBRun60sp5.exe) that you can run that will reinstall the automation components in Windows. Call tech support to get more information. This topic refers to this error as when trying to use a contract, letter, etc. in Microsoft Word. This error can also be generated when a database is being created also, which can be caused by corrupt automation components in Windows also.

___________________________________________________________________________________________

This error occurs when the requested Automation object could not be created by COM, and is therefore unavailable to Visual Basic. The error is typically seen on certain computers but not others.

This article provides some troubleshooting tips to help you diagnose and resolve common problems that are known to cause this error.

MORE INFORMATION

Unlike some errors in Visual Basic, there is no one cause to an error 429. The problem happens because of an error in the application or system configuration, or a missing or damaged component. Finding the exact cause is a matter of eliminating possibilities. If you encounter this error on a client computer, there are a number of things you will need to check to isolate and resolve the error.

The items later give you some practical suggestions for troubleshooting this error when you work with Office Applications. Some of this information may also apply to non-Office COM servers as well, but this article assumes you are trying to automate Microsoft Office.

Checking the Automation Server

The most common reasons for an error with CreateObject or New are problems with the server application itself. Typically, these problems are with the configuration or setup of the application. Here are some items to check:

•Verify the Microsoft Office application you want to Automate is installed on the local computer, and make sure that you can start the application from the Start and then Run dialog box. If the program cannot be started manually, it will not work through automation.

•Re-register the application by typing the path to the server in the Start and then Run dialog box, and then append /RegServer to the end of the line. Press OK . This should silently run the application and re-register it as a COM server. If the problem is with a missing registry key, this will typically correct it.

•Check the LocalServer32 key under the CLSID for the application you want to Automate. Make sure it points to the correct location for the application, and make sure the path name is in a short path (DOS 8.3) format. While it is not a requirement that a server be registered using a short path name, long path names that include embedded spaces have been known to cause problems on some systems (see later).

To check the path key stored for the server, start the Windows Registry Editor by typing regedit in the Start and then Run dialog box. Navigate to the HKEY_CLASSES_ROOT\Clsid key. Under this key you will find the CLSIDs for the registered automation servers on the system. Using the values later, find the key that represents the Office application you want to Automate and check its LocalServer32 key for the path.

+========================+=========================================+ 

| Office Server | CLSID Key | 

+========================+=========================================+ 

| Access.Application | {73A4C9C1-D68D-11D0-98BF-00A0C90DC8D9} | 

+------------------------+-----------------------------------------+ 

| Excel.Application | {00024500-0000-0000-C000-000000000046} | 

+------------------------+-----------------------------------------+ 

| FrontPage.Application | {04DF1015-7007-11D1-83BC-006097ABE675} | 

+------------------------+-----------------------------------------+ 

| Outlook.Application | {0006F03A-0000-0000-C000-000000000046} | 

+------------------------+-----------------------------------------+ 

| PowerPoint.Application | {91493441-5A91-11CF-8700-00AA0060263B} | 

+------------------------+-----------------------------------------+ 

| Word.Application | {000209FF-0000-0000-C000-000000000046} | 

+------------------------+-----------------------------------------+ 

Does the path match the actual location of the file? Be aware that short path names can give you the impression that a path is correct when it may not be. For example, both Microsoft Office and Microsoft Internet Explorer (if installed in their default locations) will have a short path similar to "C:\PROGRA~1\MICROS~X\" where X is some number. It is not immediately obvious that you are looking at from a short path name.

You can test that the path is indeed correct by copying the value from the registry and pasting it into the Start and then Run dialog box (remove the /Automation switch before running the application). Does the application start when you select OK ? If yes, then the server is registered correctly. If not, you should replace the value of the LocalServer32 key with the correct path (use a short path name if possible).

•Problems have been known to occur when automating Word or Excel if either the Normal.dot template (Word) or the Excel.xlb resource file (Excel) has become corrupt. To test if a corruption has occurred, search the local hard drives to find all instances of Normal.dot or *.xlb. (Please note that if you are running Windows 2000, Windows NT, or Windows 95/98 with profiles enabled, you may find multiple copies of these files, one for each user profile on the system.) Temporarily rename the Normal.dot file(s) or the *.xlb file(s), and re-run your Automation test (Word and Excel will create these files if they cannot find them). Does the code now work? If yes, then the files you renamed should be deleted since they are corrupt. If not, you should rename them back to their original names so any custom settings saved in these files won't be lost.

•If you are on a Windows NT or Windows 2000 system, run the application under the Administrator account. Office servers require read/write access to the registry and disk drive, and may not properly load if your current security settings deny this privilege.

Checking the System

System configuration can also cause problems with the creation of out-of-process COM servers. The following are some things to check on systems where the error occurs:

•Does the problem happen with any out-of-process server? If you have an application that just uses a particular COM server (for example,, Word), you'll want to test a different out-of-process server to make sure the problem is not with COM layer itself. If no out-of-process COM server can be created on that system, then a reinstallation of the OLE system files (see below) or a reinstallation of the operating system will be required to resolve the issue.

Check the version numbers for the OLE system files that manage Automation. These files are typically installed as a set, and should match build numbers. An improperly configured setup utility can mistakenly install the files separately, causing them to become mismatched. To avoid problems with Automation, you should check the files to make sure the files match builds.

You will find the Automation files in the Windows\System or Winnt\System32 directory. The following is the list of files to check:

FileName | Version | Size  
---|---|---  
Asycfilt.dll | 2.40.4275.1 | 144 KB (147,728 bytes)  
Oleaut32.dll | 2.40.4275.1 | 584 KB (598,288 bytes)  
Olepro32.dll | 5.0.4275.1 | 160 KB (164,112 bytes)  
Stdole2.tlb | 2.40.4275.1 | 17.5 KB (17,920 bytes)  
  
Check the file version by right-clicking on the file in Explorer and selecting Properties from the popup menu. The values most important are the last four digits of the file version (the build number) and the date last modified. You want to make sure these values are the same for all the Automation files.

Please note that the version numbers and dates given above are for example purposes only. Your values may differ. The important thing is that these values match each other, rather than this table.

If the files don't match build numbers or modified dates, you can download a self-extracting utility that will update your Automation files.

For additional information, click the article number below to view the article in the Microsoft Knowledge Base:

Q235420 FILE: VBRun60sp5.exe Installs Visual Basic 6.0 SP5 Run-Time Files

•Windows NT 4.0 has a known problem with starting Automation servers that live in a folder that contains an embedded space in the name, and/or resembles another folder whose first 8 characters are identical. For example, a server living in C:\Program Files\SomeFolder may fail to start during a call to CreateObject if there is another folder on the system called C:\Program Stuff\SomeFolder. For more information on, see the following Knowledge Base article:

For additional information about this problem and steps to workaround it, click the article number below to view the article in the Microsoft Knowledge Base:

Q185126 BUG: COM/OLE Server Fails to Start on Windows NT 4.0

Reinstalling Microsoft Office

If none of the preceding steps helps to resolve the problem, consider uninstalling and reinstalling Microsoft Office. Microsoft recommends that you uninstall the existing version first, and then reinstall from the original installation disks.

For a complete list of the items to be removed, please see the following Knowledge Base articles:

Q219423 OFF2000: How to Completely Remove Microsoft Office 2000

Q158658 OFF97: How to Completely Remove Microsoft Office 97

REFERENCES

For additional information about troubleshooting the '429' error message, click the article number below to view the article in the Microsoft Knowledge Base:

Q240377 HOWTO: Insure Jet 3.5 Is Installed Correctly (Part I)

For the latest information and sample code regarding Microsoft Office Automation, please see the Microsoft Online support site at:

http://support.microsoft.com/support/officedev/

Published | Nov 1 1999 5:27AM | Issue Type | kbinfo  
---|---|---|---  
Last Modifed | May 14 2001 2:22PM | Additional Query Words |   
  
Keywords | kbAccess kbAutomation kbExcel kbFrontPage kbOutlook kbVBp500 kbVBp600 _IK11561 kbWord kbGrpDSO kbDSupport  
---|---
