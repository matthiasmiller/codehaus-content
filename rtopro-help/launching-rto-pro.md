# http://www.rtopro.com/help/launching-rto-pro.htm

# Launching RTO Pro

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Launching RTO Pro

# 

|  [](epo-early-payoff-and-how-it-ch.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](remote_connections_into_rto_pr.md "Next Topic")  
---|---  
  
You can launch RTO Pro so that it opens to a customers payment screen. You can pass a phone number, account number or contract number for the customer you want to open. This feature will allow you to use your phone system or other software to launch RTO Pro from to pull up a customer automatically.

To use the feature the exe file you launch is called "Launcher.exe", it can be found in your RTO Pro install folder, default folder is C:\RTOwin

You will start Launcher.exe with a passed command line, like below

C:\rtowin\Launcher.exe -start,p,352-383-9375

This would start RTO Pro and search for a customer with 352-383-9375 as a phone number. 

If a matching record is found you will see a popup like this one at the bottom right side of your screen, you click the link to launch the customer.

![clip0084](clip0084.png)

If RTO Pro is not running an instance of RTO Pro would be started, if you are already running RTO Pro it will prompt you in the instance you are running.

Below are some other examples of command line you can use.

To pass an account number, for instance 1001

C:\rtowin\Launcher.exe -start,a,1001

To pass a contract number, for instance C100

C:\rtowin\Launcher.exe -start,c,C100

To pass a phone number, note the phone number has to be formatted like: 352-383-9375

C:\rtowin\Launcher.exe -start,p,352-383-9375 

Adding -noprompt switch to the end will make RTO Pro open the passed customer without the user being prompted if they want to open the customer and having to click the pop up message. So if you are in middle of doing something and this command is launched you could possibly lose your progress on whatever you are doing when this command is launched.

To pass an account number, for instance 1001, with -noprompt switch

C:\rtowin\Launcher.exe -start,a,1001,-noprompt

To pass a contract number, for instance C100, with -noprompt switch

C:\rtowin\Launcher.exe -start,c,C100,-noprompt

To pass a phone number, , with -noprompt switch. Note the phone number has to be formatted like: 352-383-9375

C:\rtowin\Launcher.exe -start,p,352-383-9375,-noprompt
