5.3.2.1. Copy Action Details

  


Requirements

Detailed information on the copy action for fields / embedded spreadsheets that are affected when a copy action button is clicked (note that items that remain unchanged are not listed here, and items that are not always changed are marked with "N/A" here for times that they remain unchanged): 

  


  
Field| When "Revised Proposal" Button is Clicked| When "Change Order" Button is Clicked| When "Duplicate Proposal" Button is Clicked  
---|---|---|---  
Copy Type Section: |   
|   
|   
  
"Is Revised"| Set to checked| Uncheck| Uncheck  
"Is Change Order"| N/A| Set to checked| N/A  
"Is Duplicate"| Uncheck| Uncheck| Set to checked  
  
|   
|   
|   
  
Customer & Job Info Section:|   
|   
|   
  
"Customer"| N/A| N/A| Clear  
"Job Name"| N/A| N/A| Clear  
"Job Contact"| N/A| N/A| Clear  
"Stored Job Contact ID"| N/A| N/A| Clear  
"Customer is Job Contact"| N/A| N/A| Uncheck  
"Stored New Job Contact Name"| N/A| N/A| Clear  
"Stored Job Contact Phone"| N/A| N/A| Clear  
"Stored Job Contact Email"| N/A| N/A| Clear  
"Stored New Job Contact Phone"| N/A| N/A| Clear  
"Stored New Job Contact Email"| N/A| N/A| Clear  
"Use Customer Address for Job"| N/A| N/A| Uncheck  
"Job Address"| N/A| N/A| Clear  
"Address Line 2"| N/A| N/A| Clear  
"City"| N/A| N/A| Clear  
"State"| N/A| N/A| Clear  
"Zip"| N/A| N/A| Clear  
  
|   
|   
|   
  
Lead Information Section:|   
|   
|   
  
"Lead Source"| N/A| Clear| Clear  
"Referring Party"| N/A| Clear| Clear  
"Lead Source Note"| N/A| Clear| Clear  
"Paved Before"| N/A| Uncheck| Uncheck  
"Pavement Age"| N/A| Clear| Clear  
"Pavement Condition"| N/A| Clear| Clear  
"Stone Base Good"| N/A| Uncheck| Uncheck  
"Have Drawings"| N/A| Uncheck| Uncheck  
"Grading Required"| N/A| Uncheck| Uncheck  
"Ideal Project Timeframe"| N/A| Clear| Clear  
"Decision Process"| N/A| Clear| Clear  
"Decision Process Note"| N/A| Clear| Clear  
"Additional Lead Notes"| N/A| Clear| Clear  
"Lead Information Required"| N/A| Uncheck| Uncheck  
"Received Date"| Clear| Clear| Set to the current date  
"Received By"| Clear| Clear| Set to the current user's Contact record  
"Appointment Date"| Clear| Clear| Clear  
"Appointment Time"| Clear| Clear| Clear  
  
|   
|   
|   
  
Documentation Section:|   
|   
|   
  
"Proposal Attachments" embedded spreadsheet| N/A| Delete all rows| N/A  
  
|   
|   
|   
  
Proposal Itemization Section:|   
|   
|   
  
"Groups" embedded spreadsheet| N/A| Delete all rows| N/A  
"All Items for Proposal" embedded spreadsheet| • If the row has a "Sales Item Code" and "Overridden" is not checked: The row is copied and the following fields are auto-updated to match the current values on the linked Sales Item record ("SI") or Automated Proposal Group record ("APG"): • Sales Item Code ("SI")• Item Description ("SI")• Item Qty (with the following conditions:

  * if "Group Type" = "Automated" and "Automatically Added" is checked for the row: "APG"; 
  * otherwise: is copied from Source Proposal)

• UOM ("SI")• Unit Cost $ ("SI")• Markup % ("SI")• Unit Price $ ("SI")• If a row has a "Sales Item Code" and "Overridden" is checked: The row is copied over directly and no fields are auto-updated, since they are no longer being drawn from another record. • If a row does not have a "Sales Item Code": The row is copied over directly, since nothing is coming from another record (note that this also means that any Items that were manually added to the Proposal are not auto-removed). | Delete all rows| Same as spec for "Revised Proposal" button.  
  
|   
|   
|   
  
Proposal Details Section:|   
|   
|   
  
"Proposal #"| Clear (auto-set on the first Save)| Clear (auto-set on the first Save)| Clear (auto-set on the first Save)  
"Stored Proposal Oil Index"| • If "Override Oil Index" is not checked: Cleared• Otherwise: N/A| Clear| N/A  
"Override Oil Index"| N/A| Uncheck| N/A  
"Deposit Required"| N/A| Uncheck| N/A  
"Deposit Amount $"| N/A| Clear| N/A  
"Include Unit Price Details"| N/A| Uncheck| N/A  
"Unit Price Details"| N/A| Clear| N/A  
"Proposal Notes"| N/A| Clear| N/A  
  
|   
|   
|   
  
Proposal Finalization Section:|   
|   
|   
  
"Ready to Send to Customer"| Uncheck| Uncheck| Uncheck  
  
|   
|   
|   
  
Printing / Emailing Section:|   
|   
|   
  
"Print / Email Proposal"| Uncheck| Uncheck| Uncheck  
  
|   
|   
|   
  
Customer Acceptance Section:|   
|   
|   
  
"Proposal Date"| Clear| Clear| Clear  
"Proposal Valid Through"| Clear| Clear| Clear  
"Sent to Customer"| Clear| Uncheck| Uncheck  
"Initial Follow-Up Due"| Clear| Clear| Clear  
"Initial Follow-Up Complete"| Clear| Uncheck| Uncheck  
"Secondary Follow-Up Due"| Clear| Clear| Clear  
"Secondary Follow-Up Complete"| Clear| Uncheck| Uncheck  
"Proposal Result"| Clear| Clear| Clear  
"Proposal Result Date"| Clear| Clear| Clear  
"Job Target Start Comments"| Clear| Clear| Clear  
  
|   
|   
|   
  
Job Scheduling Section:|   
|   
|   
  
"Job Scheduled"| Uncheck| Uncheck| Uncheck  
"Job Scheduled Start Date"| Clear| Clear| Clear  
  
  


  


Development Specification

Change Requests: 

  * Tim Reitz 11/25/2025: [[[IN12308](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12310&)]] - ZLP - Phase 1 - Proposal Record - Copy Proposal Issues
  * 


  


  


\--------------

  


_EM: Tim Reitz 06/24/2025: Do you want all of these in a single table, or should we split it out into separate tables by section? (pretty easy to copy & paste out to create new tables, then delete the big one)

_VA Ellis Miller 06/25/2025:No preference. Whatever is easiest.

TODO_: Tim Reitz 06/25/2025: It was fastest for now to do it all as one table, but it could be nice to eventually split them into separate tables (maybe do this once the crunch is done for getting the proposal ready).
