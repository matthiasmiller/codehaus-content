# http://www.rtopro.com/help/automate_ach_send.htm

# Automate ACH Send

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Automate ACH Send

# 

|  [](ach_-_setting_up_and_using_in_.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_autopay_autocharge_.md "Next Topic")  
---|---  
  
When ACH is used as a payment form the ACH transaction is saved in the ACH table, but you will not be paid for it until it is sent to your ACH provider. 

By default when you run the end of day process any unsent ACH transactions are sent automatically. You can also send them manually at anytime from the Autopay screen. After the transactions are sent it then takes 4 to 7 days before you find out if the transaction cleared or was returned. 

Note that you can turn off the End of Day automatic sending of ACH transactions in store setup. You can also password protect sending of ACH transactions in Security, this will prevent them from being sent automatically through the end of day also.

You can automated the process to send ACH transactions to the ACH system by sending the command line "ach_send" to the End of Day executable (income.exe). So to have ACH transactions sent you could launch for instance "c:\rtowin\income.exe ach_send". 

This can be scheduled through Windows Task Scheduler. Below is a screen shot of the Action setup in Windows Task Scheduler, it shows the command line to the income.exe program and the command line argument that needs to be sent. Note this example assumes you have RTO Pro installed in the default c:\rtowin folder, if you have RTO Pro installed in a different folder you would use that path instead.

Note for Central Server companies running the ACH sync by command line will send ACH transactions for ALL companies.

![clip0021](clip0021.png)
