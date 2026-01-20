# http://www.rtopro.com/help/automate_webpay_payment_proces.htm

# Automate Webpay Payment Processing

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Automate Webpay Payment Processing

# 

|  [](automate_autopay.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](webpay_quickpay_link.md "Next Topic")  
---|---  
  
Scheduling Automatic Processing of Webpay Payments

You can also schedule the retrieval and processing of web payments, using the command line "ap_webpay" with the RTO Pro executable (RTO-win.exe"). When run RTO Pro with the command line "ap_webpay", for instance:

"c:\rtowin\rto-win.exe ap_webpay"

The following actions will take place. 

1\. The RTO Pro webpay server will be checked for new web payments. 

2\. Any un-processed web payments will be processed (payments entered into the system). 

3\. RTO Pro will be closed. 

4\. Any messages that would have displayed are logged to a log file stored on your server computer in "(Datapath)\Logs\AutomatedTaskLog.txt"

You can use Windows Task Scheduler to schedule this to happen automatically any time and as often as you wish. You should always check the webpay payment screen daily to check for any that may not have processed due to any number of possible reasons (agreement already closed, they paid more than the balance due etc.). Information about payments that could not be processed would be saved to the log file also.
