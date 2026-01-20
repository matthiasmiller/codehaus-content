# http://www.rtopro.com/help/scheduling_autodialeracm_to_ru.htm

# Scheduling Autodialer(ACM) to run automatically

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Scheduling Autodialer(ACM) to run automatically

# 

|  [](credit_card_partial_approvals.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_contract_info_page.md "Next Topic")  
---|---  
  
On the setup page of the Automated Collection Module(ACM) you can setup a task for the ACM to run automatically. When the ACM is started from a scheduled task the following steps are taken.

1\. Any existing call list is deleted.

2\. A new call list is created using the "default.acm" saved layout or the passed saved layout file, so make sure you save a layout on the report screen before scheduling a task for the ACM to run automatically.

3\. Calls will be started for the newly created list, all saved options will be enforced such as earliest and latest calls allowed.

4\. For cloud service redials will be done for no answers and busy according to the last saved settings on the dial page.

To add a task for the ACM to run automatically just click the "Add Task" button. It will create a task to run Monday - Saturday at the time it is when the button is clicked, you can edit the time or scheduled days by clicking the "Properties" button.

Below is a screen show of a scheduled task in the ACM, it will display the last run time, the next scheduled run time, the status and the run schedule.

To delete the task just click the "Delete" button.

![ACM task schedule](hmfile_hash_91d733e5.png)

To run the ACM using a different layout you can click the "Properties" button shown above and add the name of the layout after "-auto" like the highlighted section below, which would run the saved layout named "monday".

You can also create tasks manually in Windows Task Scheduler if you wish to run the ACM different days / times with different saved layouts.

![clip0022](clip0022.png)

* * *

Notes for Central Server Companies:

The command line must contain more information for central server companies (companies that run multiple stores / companies from one instance of RTO Pro). Below are examples

The line below would be for Central Server store 3 , this command would run the "default.acm" saved layout.

"c:\rtowin\Automated Collections Module.exe" ~3-auto

The line below would be for Central Server store 1, this command would run the "test layout.acm" saved layout.

"c:\rtowin\Automated Collections Module.exe" ~1-auto test layout

Please note for central server companies the ACM will use the settings in the ACM setup to determine if all companies will be included in the list that is created when it is automated.

* * *

Below for central server stores that are REMOTE from each other (add a "~" after the store number) Remote means for companies that run multiple remote locations (stores) from a central server

The line below would be for Central Server remote store 3, this command would run the "default.acm" saved layout.

"c:\rtowin\Automated Collections Module.exe" ~3~-auto

The line below would be for Central Server remote store 1, this command would run the "test layout.acm" saved layout.

"c:\rtowin\Automated Collections Module.exe" ~1~-auto test layout

* * *

Please Note: When a scheduled task is created the task will run as scheduled until the task is deleted, if you forget you scheduled the task it will continue to run regardless, even if you replace the computer but keep using it for other purposes, the scheduled task will continue to run. Also scheduled tasks are computer specific, you should only create a scheduled task on one computer, otherwise you could have the same customers being called multiple times daily from different computers. Use this at your own risk, you are solely responsible for all charges for the calls or text messages created by the tasks as well as any legal liability for placing the calls or sending the text messages.
