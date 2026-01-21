5.3. System Switches

  


Requirements

The following System Switch(es) should be set as following (listed in alphabetical order):

  


  


  * Label: "From" email address for notifications" 
    * Code: EmailNotificationsSendingAddress
    * Field Type: Plain text 
    * Description: Specifies the 'From' email address to be used whenever the application sends notification emails.
    * Value / set to: [notifications@symbiz.org](mailto:notifications@symbiz.org) 
    * Other Notes: 
      * Editable



  


  * Allow duplicate organization names (excluding IDs)
    * Code: "ConfigContacts_AllowDupOrgNames"
    * Description: For systems including contact ID in name, allows organization names to match other contacts.
    * Value / set to: "No"



  


  * Allow multiple organizations
    * Code: "Config_AllowMultipleOrganizations"
    * Description: 
    * Value / set to: "Yes"



  


  * Allow user password reset 
    * Code: "AllowUserPasswordReset"
    * Description: 
    * Value / set to: "Yes"



  


  * Contact allow duplicate organization names 
    * Code: "ConfigContacts_AllowDupOrgNames"
    * Description: 
    * Value / set to: "No" 



  


  * Enter edit mode on detail screens 
    * Code: "AutoEnterEditMode"
    * Description: 
    * Value / set to: Yes (checked)
    * Note: This applies to the live and "deploy" versions of the Solution, not the test system. 



  


  * Include contact ID in name
    * Code: "ConfigContacts_IncludeIDInName" 
    * Description: 
    * Value / set to: "Yes"
    * Note: After this has been set, run the "Apply Changes" button on AppHosting Settings.



  


  * Show Country 
    * Code: "ConfigContacts_ShowCountry"
    * Description: 
    * Value / set to: "Yes"



  


  * Show attachment on email reminders 
    * Code: "ConfigEmailReminders_ShowAttachment" 
    * Description: This enables attachments on email reminders
    * Value / set to: Yes (checkbox checked)



  


Development Specification

Change Requests: 

  * [[[IN9534](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9536&)]] - ZSB - Open All Records Out of Edit Mode
  * Tim Reitz 04/10/2024: [[[IN9074](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9076&)]] - ZSB - Contact Types - Handle Organizations more cleanly
  * Tim Reitz 04/16/2024: [[[IN8957](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8959&)]] - ZSB - Add Email Reminders Module (prev. Internally created email reminders) 
  * 


  


  


BID: 1 HOUR

  


Tim Reitz 07/14/2023: To allow user password reset, we will need to make sure that the SMTP setting are set (see [[[W0202](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-203&)]] - Using Username / Password for AppHosting Login ).
