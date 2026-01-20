# http://www.rtopro.com/help/syncing_to_webpay_server.htm

# Syncing TO Webpay Server

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Syncing TO Webpay Server

# 

|  [](webpay-flowchart.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](automate_autopay.md "Next Topic")  
---|---  
  
Note if you get a message that you have not synced to the webpay server in several days you should contact support to verify your sync process is set up correctly.

Syncing to the webpay server is the process that sends your customer records to the webpay server, so current info can be displayed to customers such as due date, amount due etc. This should be done daily, this is not the same as the process that checks for incoming webpay payments paid online, that process is done multiple times daily to check for new payments coming in.

Note you can also start a webpay sync from the reminder on the main menu, right click on the sync to webpay reminder and choose "Sync TO Webpay now".

There are 2 options to automatically sync to the webpay server. In Store Setup you choose the option you want to use.

1\. Sync to the server when you run the End of Day process. This is the easiest and most common, but if you do not run the end of day process or run it multiple times a day you should use option 2 below instead.

2\. Automate the sync to the webpay server using Windows Task Scheduler. Instruction to set this up are below.

•The Webpay sync to server process has been improved to help prevent missing payment history records on the webpay side. Your computer will now poll the webpay server for the biggest history record present for your store and the records after that record will be sent. Previously the biggest record sent was stored locally, so if a file did not send completely due to an internet issue and it couldn't be processed it could cause missing history. Ver 5.9.425 7/18/2024

Setting up Windows Task Scheduler

![clip0009](clip0009.png)

![clip0010](clip0010.png)

![clip0011](clip0011.png)
