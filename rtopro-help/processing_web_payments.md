# http://www.rtopro.com/help/processing_web_payments.htm

# Processing Web Payments

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Processing Web Payments

# 

|  [](webpay_quickpay_link.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](excluding_customers_from_webpay.md "Next Topic")  
---|---  
  
To view and process your web payments, go to Point of Sale, then Process Web Payments (Alt+P) up at the top of the screen in the toolbar. You can also find this button when you hit F2 to go to Payments. See screen shot below of the image of this page.

When your computer checks the WebPay server for payments any online payments made since the last sync will be made available in RTO Pro for processing. Online payments will not show up on the customers records until until you process them. 

The computer you have designated to sync with the RTOwebpay server for payments will check hourly for any new payments(note RTO Pro would have to be running on that computer for it to check for payments). You will also be sent an email for every payment paid online, after you receive the email you can go to the process web payments screen and click the "Start Webpay Sync" button to download the webpay payments, you can then click the "Process Now" button to enter those payments in RTO Pro.

View your payments, if any, and verify that they are correct before processing. You may also choose to display web payments from customers with a specific customer rating in the drop down box on the right. Sync with the server at any time to check for payments with the button in the top left.

Scheduling Automatic Processing of Webpay Payments

You can also schedule the retrieval and processing of web payments, using the command line "ap_webpay" with the RTO Pro executable (RTO-win.exe"). When run RTO Pro with the command line "ap_webpay", for instance:

"c:\rtowin\rto-win.exe ap_webpay" [Click here for more info about scheduling Automatic Webpay Processing of Payments](automate_webpay_payment_proces.md)

![Process WebPay](hmfile_hash_8547819f.png)
