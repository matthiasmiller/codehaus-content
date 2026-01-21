5.2.2. Contact - Employee Details Section

  


Requirements

The Contact record also includes the following custom section and fields: 

  


  * Employee Details section (visible if "Contact Type" includes "Employee"): 
    * Is Sales Rep (checkbox; editable for users with the "Edit User Groups and Profiles" Permission; if checked, the Contact appears on Sales Rep lists & options throughout the Solution) 



  


  * Sales Rep Goals (embedded spreadsheet; visible if "Is Sales Rep" checkbox is checked or if any rows exist on this embedded spreadsheet (to continue to display the information if the checkbox is unchecked); includes the following:
    * Columns: 
      * Year (required; numeric year; with the following additional details / behaviors: 
        * when a row is added, defaults to the year after the latest existing year on the table, or to the current year if no other rows exist;
        * validate against duplicate Years - error on Save: "Duplicate years for goals are not allowed.")
      * # Proposals/Year (required; number; 0 decimals; this is the Sales Rep's annual goal for created/sent Proposals, to be counted based on the "Proposal Date")
      * # Proposals/Week (read-only macro; number; 0 decimals; with the following additional details / behaviors: 
        * displays the value of "<"# Proposals/Year" for the row> / 52", rounded up to a whole number; 
        * this is the calculated weekly goal for created/sent Proposals, to be counted based on the "Proposal Date") 
      * Awarded % (required; number; 0 decimals; this is the Sales Rep's annual goal for percentage of Proposals awarded, to be counted based on the "Proposal Result Date") 
      * Total $ (required; number; 2 decimals; wide enough for 11 digits before the decimal point; this is the Sales Rep's annual goal for awarded Proposal $)
    * Automatically sorted by: Year (current/latest at the top)
    * Buttons to add/remove rows: "✚" / "🞭"
      * Clicking "✚" adds a new row to the top of the embedded spreadsheet (since new rows are always for a later year).
    * Shows 6 rows without scrolling
    * Other Notes: 
      * This entire embedded spreadsheet is editable only for users that match one or both of the following:
        * users with the "Edit User Groups and Profiles" Permission";
        * the user linked to the Contact record via the "User ID" field) 
  * View Sales Goal Tracker (visible if "Is Sales Rep" checkbox is checked or if any rows exist on the "Sales Rep Goals" embedded spreadsheet; link; opens the "Sales Goal Tracker" report, filtered to the corresponding Sales Rep) 



  


  * Receives "Reminder to Enter Proposal(s) into QuickBooks" Email (checkbox; editable for users with the "Edit User Groups and Profiles" Permission; users for whom this checkbox is checked on their linked Contact record receive the mentioned email notification (see corresponding spec))
  * Receives "Jobs Awaiting Scheduling" Email (checkbox; visible to and editable by users with the "Create/Edit Other User Profiles" Permission; determines whether the Contact receives the notification)



  


Development Specification

Change Requests:

  * Tim Reitz 11/25/2025: [[[IN11677](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11679&)]] - ZLP - Job Scheduled Tracking



  


  


  


Ellis Miller 06/10/2025: 

[ ] New section and field

[ ] New Sales Rep RG

6 hours

  


_EM: Tim Reitz 07/07/2025: Note about adding dev spec for the following as needed: 

Sales Rep Goals RG

View Sales Goal Tracker link

Receives "Reminder to Enter Proposal(s) into QuickBooks" Email checkbox
