6\. Reminders

  


Requirements

Reminders are included in the "Reminders" proposal price.

  


The Reminders will appear as a system notification (red button on the left and on the menu). Clicking the notification will open a report showing:

  


This would generate a report of:

  * Due Date
  * Reminder Name
  * Record Name



  


The Record name will be a link to open the record and enter the required information to clear the reminder.

  


It will be sorted by Due Date.

  


This would support the following reminders:

  


  * Member Payment Due. This would show all members who have payments due. To clear the reminder, click the Record Name and enter the payment information. Alternatively, uncheck the "Accepted by SPE" checkbox.



  


  * May 15 State Filing. This would automatically disappear after May 15.
  * July 1 State Filing. This would automatically disappear after July 1.



  


  * Disbursement Due. This would be set for 60 days after the SPE application approval date (configurable in the system-wide configuration under # of Days Until Disbursement Due). To clear this reminder, click the Record Name and enter the disbursement information. This reminder will include instructions to send the request for proof to the Scholarship Organization. (This template is not automatically generated at this point because of its marginal use.) This should show up 14 days in advance.



  


  * SPE Application Receipt Due. This reminder date would be set based on the Receipt Submitted Due Date. To clear this reminder, click the Record Name and enter the Receipt Submitted Actual Date. The reminder should show up at least 7 days prior to the due date. 



  


  * Manually Entered Reminders. This would be used for things like checking with a member to see if a tax credit issue was resolved. Each reminder can be associated with a contact. To clear this reminder. click the Record Name to open the reminder details and click the Complete checkbox. (More details in the following section.)



  


  * New Online Submissions. This would show a report for any open online submissions. To clear this reminder, simply process the online submissions and close them out.



  


  * Schedule Checks for Deposit. This would show a reminder if there are any admitted applications that are currently held. It would run the Payments report to schedule them for a deposit.



  


  * Deposit Checks. This would show a reminder if there are any member applications that are Scheduled for Deposit on or before today's date. This would also run the Payments report to allow marking them as deposited.



  


The Reminders will be used to integrate into the Email Communications (see below). This will be configured through a single reminder that works for all email communications.

  


Development Specification

My proposal:

  


Create a Reminder base catalog with a System Reminder lookup record: Tim Reitz 01/19/2021: what is a lookup record?

Tim Reitz 01/19/2021: How should these look on the mockups? Like regular records, accessed from a "Config Reminders" or something like that?

Also the user reminders.

Matthias Miller 01/25/2021: I think this should be addressed now.

  * Name
  * # of Days Notice
  * Reminders Expression



Tim Reitz 01/19/2021: define how the reminder is cleared?

Matthias Miller 01/25/2021: The expression will need to handle how it is cleared.

  


Create a SystemReminderDef helper macro that would take the following parameters:

  * Record Link
  * Record Name
  * Due Date



It would generate an ini-style definition for the reminder.

  


The Reminders Expression would be an any-level expression that would do an Ndx/LookupConcat to generate the reminders.

  


We would create "Std Open Contact.r20" auto-push reports to use in the main Reminders report.

  


The report would be a Repeat for List on reminders. It would automatically exclude reminders that are more than "# of Days Notice" in the future.

  


  


Ellis Miller 02/09/2021:

  


TODO_CH: Rename these to "System Reminder" and "User Reminder".

  


[ ] SystemReminder detail screen with Expr Field Requirements (with config report):

Each SystemReminder will have an expression defined to create a set of reminders. These will look something like this:

  


RecordLink=fpspe.apphosting.zone/Reports/Standard/AutopushSomething?......

RecordName=Deposit Check from Good's

DueDate=1/1/2022

|RecordLink=fpspe.apphosting.zone/Reports/Standard/AutopushSomething?......

RecordName=Deposit Check from QuickMart

DueDate=8/1/2021

1 Day.

  


[ ] The Reminders report simply evaluates this expression for each SystemReminder and filters them based on whether the Due Date is within "# Days Notice". Use the IniGetKey to extract needed values. The action will be a URL:#IniGetKey(RepeatListITem, RecordLink)#

1 Day.

  


TODO_EM: CH will help do precise definitions after acceptance. We may need indices. Probably bid this at a ballpark of about 4 hrs per definition.

4 days.

  


[ ] We'll need to set up an SystemReminder for user reminders.

[ ] We'll probably need a DatabaseLevel import/export.

1 Day.
