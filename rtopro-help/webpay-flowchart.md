# http://www.rtopro.com/help/webpay-flowchart.htm

# Webpay Flowchart

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Webpay Flowchart

# 

|  [](webpay_setup.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](syncing_to_webpay_server.md "Next Topic")  
---|---  
  
Below is a simplified Flowchart to demonstrate how the webpay system works. 

Your system needs to [send data TO the server ONCE DAILY](syncing_to_webpay_server.md), so it has accurate info for due dates, how much is due etc.

You [retrieve webpay payments](processing_web_payments.md) to process anytime you want, as many times a day as you like.

![webpay flowchart](hmfile_hash_a80a87b9.png)[](processing_web_payments.md)[](syncing_to_webpay_server.md) | ![webpay flowchart 2](hmfile_hash_088b3785.png)  
---|---  
  
When you run the end of day process, or whenever you have your system set to sync TO webpay is when new info is sent from your system to the webpay server, this should be once daily, usually after your business day is over. The webpay server starts processing these sync files just after midnight, so if you load a new customer today, then at the end of the day sync TO webpay, the next day that customer would be able to pay online.

•The Webpay sync to server process has been improved to help prevent missing payment history records on the webpay side. Your computer will now poll the webpay server for the biggest history record present for your store and the records after that record will be sent. Previously the biggest record sent was stored locally, so if a file did not send completely due to an internet issue and it couldn't be processed it could cause missing history. Ver 5.9.425 7/18/2024
