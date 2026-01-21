10.1.1. Scheduled Process: "Send Reminder to Enter Proposal(s) into QuickBooks"

  * Name: "Send Reminder to Enter Proposal(s) into QuickBooks"
    * Description: Used to send the "Reminder to Enter Proposal(s) into QuickBooks" email.
    * Category: Email Notifications
    * Notes: Contains the contents of "Actions" point below 
    * Initiated: Weekly on Monday at 8:00am ET
    * Should Wait On: N/A
    * Commands: email "Standard/Std Email Reminder to Enter Proposals into QuickBooks.r20"
    * Prompts: 
      * TBD in coding
    * Action(s): 
      * Runs the email merge to send the "Reminder to Enter Proposal(s) into QuickBooks" email to to any users with the "Receives "Reminder to Enter Proposal(s) into QuickBooks" Email" checkbox checked on their Contact record, if there are any Proposals with "Proposal Status" = "Awarded" and the "Entered into QuickBooks" checkbox not checked.


