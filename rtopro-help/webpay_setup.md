# http://www.rtopro.com/help/webpay_setup.htm

# WebPay Setup

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# WebPay Setup

# 

|  [](customer_import_fields.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](webpay-flowchart.md "Next Topic")  
---|---  
  
[To see more information on the RTO Pro WebPay service, click here to see our website.](http://rtopro.com/webpay.html)

When you are ready to set up your computer for WebPay, you will first need to know your FTP user name and password. If you don't know it, contact tech support at 352-383-9375.

Go to the Other tab in your Store Information Setup (from the Setup Menu). Enter your FTP user name and password on lines 34 and 35. (Unless you are using multiple payment portals for one company, see note below).

Next you need to manage your settings on lines 44-50, such as in the example below.

If you run an End of Day Report daily, do not check the box on line 50. If you don't use the End of Day Report, you will need to check this box and set up a task in your Windows Task Scheduler to sync with the WebPay server daily. Use the program/script "c:\rtowin\income.exe" and add the argument "-webpay".

Starting with RTO Pro version 5.8.697, you can automate the retrieval and processing of RTO Pro webpay payments. When you run RTO Pro with the command line "ap_webpay", for instance "c:\rtowin\rto-win.exe ap_webpay", the following actions will take place. 

1\. The RTO Pro webpay server will be checked for new payments. 

2\. Any new and un-processed payments will be processed (payments entered into the system). 

3\. RTO Pro will be closed. No receipts will print, receipts will be emailed if your system is set up to email receipts to customers.

You can use Windows Task Scheduler to schedule this to happen automatically any time and as often as you wish.

![WebPay settings](hmfile_hash_cef51521.png)

Now that you're set up, sync with the server by running an End of Day Report or using your scheduler. At this point, you may call tech support at 352-383-9375 (M-F 9am-6pm EST) to make your payment portal go live, or wait until the next day (after midnight) and it will be ready for you.

Note: Some companies on Central Server who own multiple Rent To Own businesses may choose to have separate payment portals (WebPay sites) for each store. In this instance, your varying FTP user names and passwords will need to be entered on lines 51 and 52 in the contracts tab for each company.

Next see the topic [Processing Web Payments](processing_web_payments.md) for more info about how to process payments customers pay online through webpay.
