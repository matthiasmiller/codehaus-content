5.6. User Alert Record

*Done. 

  


Overview: This is a standard Silverloom feature included in this Solution. It can be used by Admins to send messages to all users via "in-app" notifications alerts.

  


Accessed via:

  * View User Alerts Report (see corresponding spec) 
  * Admin | User Alerts | New User Alert (opens a blank new User Alert record)



  


Sections and Fields: 

  * Title (plain text; required; validates against duplicates - error message on the field and on Save: "A UserAlert name cannot be empty.")
  * Message (plain text)
  * Sent (read-only; displays date + time + user)



  


Data Access: Admin

  


Other Notes:

  * When the record is saved for the first time, the Alert is "sent", and will soon display as a System Notification for all users. See the "User Alerts Notification" spec for more details.


