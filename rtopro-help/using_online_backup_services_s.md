# http://www.rtopro.com/help/using_online_backup_services_s.htm

# Using Online Backup Services such as Carbonite

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Using Online Backup Services such as Carbonite

# 

|  [](help_desk_rto_pro_backup.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](rto-pro-document-manager.md "Next Topic")  
---|---  
  
When using an online backup service such as Carbonite, Mozy etc. the recommended way to perform backups would be as described below.

1\. Create a backup folder on your hard drive, for example "c:\Backups".

2\. Have RTO Pro perform backups to this backup folder automatically, either through the End of Day program or by using Windows scheduler to schedule automatic backups using the RTO Pro backup program. See instructions under the [RTO Pro Backup help topic](help_desk_rto_pro_backup.md).

3\. Setup Carbonite, or whatever online backup service you use to backup the "backup" folder ("c:\Backups").

4\. If you use document imaging in RTO Pro, you should also have Carbonite backup the "C:\RTOwin\Images" folder. This is where scanned images are stored, they should be backed up directly by your online backup service. This is recommended since scanned images for a lot of customers can take up hundreds of megabytes or even gigabytes of hard drive space. These files are primarily static and are best backed up only as they change or new images are added.

The reason it is recommended to perform backups in this manner is because the RTO Pro backup program can perform "hot" backups, backups while the data file is open. Most online backup services will not backup a file while it is open, and the data file can be open all day or even days or weeks at a time. Because of this if you only have your backup service backup the live folder the data file could be days or weeks old if you ever need to restore it. Another reason is the backed up data file could be corrupted if it was backed up by an online service while it was open, unless the online backup service you use supports backing up Firebird Databases "hot". There are no online backup services that we are aware of that support "hot" backup of Firebird databases. Another reason not to use an automatic web backup service is it can cause issues with RTO Pro, for instance the software may create a file for a report or something similar, close the file, then reopen it, when the file is closed the backup service may try to back it up, then when RTO Pro tries to open it again it will not be able to because your backup service will have the file locked. You will usually get random file access errors if you have a backup service backup your data live.

Any backup service or system you implement should be tested after a backup is done to ensure the system is backing up what you think it is. It is always a good idea to perform a test backup and a test data restore with any backup system you choose to use, to verify it is working the way you think as well as to familiarize yourself with how it works. A backup system is useless if you cannot restore the data you need from it in case of an emergency. We have had numerous instances where users sign up with an online backup service and just assume it is backing up their data, only to find out when their computer crashes that they never set it up to backup anything.
