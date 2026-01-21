11.1. "Recently Changed Church Affiliations" Report Alert

_GZ: Tim Reitz 09/10/2025: Do you want this alert to appear right away, or have a weekly alert / email that includes all recent ones (to reduce noise)?

TODO_VA: Tim Reitz 10/09/2025: Per Glen today, weekly is fine. If there are none, skip the email. 

TODO_VA: Tim Reitz 10/09/2025: Change this to an email instead of an in-app alert. 

  


Overview/Purpose: This is a custom report alert notification that notifies certain users when the "Church Affiliation" or "Other Church Affiliation" is changed on a Contact record. 

  


Details: 

  * Title (can include an expression): "<#> Recently Changed Church Affiliation(s)"
  * Displays within 20 minutes of: __ 



TODO_VA: weekly, per note above 

TODO_VA: Tim Reitz 09/10/2025: Specifically, when "Church Affiliation" or "Other Church Affiliation" is changed from a non-blank value. 

  * Action: Opens the "Recently Changed Church Affiliations" report (see corresponding spec)
  * User(s) to notify:
    * Any "Account Resellers" for accounts under which the Contact is an "Account Manager" or "Driver".
    * The Primary Group Admin for any Account Groups under which the Contact is an "Account Manager" or "Driver".
  * Dismiss type: choose one of the following: 
    * Auto-dismiss when all items are resolved
    * Auto-dismiss when the report is opened 
    * Manually dismiss via button on report 



TODO_GZ: Tim Reitz 09/10/2025: How would you like the alert to dismiss? What is considered resolution here?

TODO_VA: If dismissing before items are resolved, specify what should cause this alert to reappear (most likely it should be based on modified fields in Activity History).

  


Other Notes: N/A
