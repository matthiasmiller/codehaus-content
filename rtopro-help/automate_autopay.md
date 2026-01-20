# http://www.rtopro.com/help/automate_autopay.htm

# Automate AutoPay

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Automate AutoPay

# 

|  [](syncing_to_webpay_server.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](automate_webpay_payment_proces.md "Next Topic")  
---|---  
  
It is possible to run autopay as a scheduled task using Windows Task Scheduler.

You can also schedule AutoPay using the command line "-autopay" with the RTO Pro executable (RTO-win.exe"). When run RTO Pro with the command line "-autopay", for instance "c:\rtowin\rto-win.exe -autopay", the following actions will take place. 

1\. RTO Pro will be started. 

2\. Autopay process will be ran. 

3\. RTO Pro will be closed. 

Any messages that would have displayed are logged to a log file stored on your server computer in "(Datapath)\Logs\AutomatedTaskLog.txt". 

The autopay reports will be created same as usual and can be viewed from the Print Utility (F5 from the main menu). When running as a task the autopay failures will be appended to the end of the normal autopay report.

You can use Windows Task Scheduler to schedule this to happen automatically any time and as often as you wish.

Options for Central Server companies

-autopay | run autopay for stores selected by default in the form (stores selected the last time autopay was ran)  
---|---  
-autopay all | run autopay for ALL stores   
-autopay 1,2,4,10 | run autopay for passed stores, this would run autopay for store 1, 2, 4, and 10  
  
Please note when you automate Autopay you should still check autopay reports or run autopay manually often also, to catch declines etc., so you can contact customers who need to provide new credit card numbers etc. Just because you automate the autopay process doesn't mean you can just set it and forget it.
