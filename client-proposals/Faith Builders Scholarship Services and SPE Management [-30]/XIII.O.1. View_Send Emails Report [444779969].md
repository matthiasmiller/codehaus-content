13.15.1. View/Send Emails Report

  


Requirements

Overview: This is a two-pane report of Email records, with various filtering options and buttons.

  


Accessed from:

  * Faith Builders Scholarship Services | Communications | View/Send FBSS Emails (see corresponding section of the living spec) 
  * Faith Builders SPE | Communications | View/Send SPE Emails (see corresponding section of the living spec) 



  


Title: View/Send Emails

  


Left Pane:

Columns:

  * Date
  * From
  * Recipients
  * Subject (link to open the record)
  * # Attachments



  


Grouped by: 

  * "Draft - Needs Review" (if both the "Ready to Send" and "Sent" checkboxes are not checked) 
  * "Draft - Ready to Send" (if the "Ready to Send" checkbox is checked and the "Sent" checkbox is not checked) 
  * "Sent" (if the "Sent" checkbox is checked)



  


Sorted by: Date (most recent first) + Email ID 

  


Right Pane: Displays the Email Body for the selected row in the left pane.

  


Filters:

  * From FB Department (drop-list of all FB Departments; blank = all)
  * Template (blank = all) (multi-select drop-list of templates; blank = all)
  * Contact (blank = all) (drop-list of contacts)
  * Contact Group (blank = all) (drop-list of contact groups)
  * Member Application (blank = all) (drop-list of member applications)
  * SPE Approval (blank = all) (drop-list of contacts)



  


Buttons:

  * Delete Selected (to delete selected drafts, either "Draft - Needs Review" or "Draft - Ready to Send")
  * Send Selected Drafts (to send selected "Draft - Ready to Send" items; any "Draft - Needs Review" items that are selected simply are skipped) 



  


Menu Visibility: All users

  


Other Notes:

  * If the email has CC or BCC, the Recipients column is formatted as follows:



To: (list of contacts)

CC: (list of contacts)

BCC: (list of contacts)

  * Otherwise, it shows a list of 'To' names and email addresses.
  * If one or more emails with the "Ready to Send" checkbox not checked are selected when the "Send Selected Drafts" button is clicked, the import gives an error.



  


Development Specification

Change Requests: 

  * Austin Priest 07/04/2023: [[[IN8307](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8309&)]] - XFB - Std Email.r20: Add 'Send Selected Drafts' Button
  * 


  


  


  


[ ] Create a "Std Emails.r20" in the "AppHosting Emails" folder.

  


[ ] Create a Emails_CustomReportSubset macro that is true in the "AppHosting Emails" catalog. Override it with the above ask prompts for the client catalog. It should filter the custom fields.

  


[ ] The Delete Drafts is simply a Delete Selected Records

  


[ ] The Send All Drafts is a "modify on export" that sends all emails (no preview) and updates the Sent checkbox (and also updates the date/time)
