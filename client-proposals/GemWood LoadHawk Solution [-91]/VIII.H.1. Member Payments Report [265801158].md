8.8.1. Member Payments Report

  


Requirements

Overview: This is a custom report of Member Payments (Payment records with "Payment Category" = "Member"), with various filters. 

  


Accessed from: Main Menu | Payments | Member Payments (opens the filter screen)

  


Title: Member Payments

  


Preface (conditionally visible): 

  * "Payments made today:" (visible if "Payment Date Start" and "End" filters both are set to the current date) 



  


Columns: 

  * Member 
  * Payment ID (displays the Member Payment ID, as a link to the record)
  * Ticket Date
  * Payment Type
  * Due Date
  * Payment Amount $ (total row shows sum)
  * Payment Date
  * Confirmation #
  * Notes
  * Member Total $ (total row displays sum)
  * Sent to Member (displays the date and time)



  


Grouped by: Status (standard sequence)

  


Sorted by:

  * First by: Member Payment ID (alphabetically) 



  


Filters: 

  * Member (drop list of Member-type Contacts and blank; defaults to blank = all)
  * Payment ID (optional; drop list of all Member Payment IDs for the selected Member (or blank = all if "Member" is blank); filters down as you type; defaults to blank = all)
  * Payment Status (drop list of "Draft / Complete / Canceled" list options and blank; defaults to blank = all) 
  * Payment Date Start (date; looks at the Payment Date; defaults to blank = all)
  * End (date; looks at the Payment Date; defaults to blank = all)



  


Buttons: 

  * N/A



  


Menu Visibility: All users

  


Other Notes:

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1176989114#gid=1176989114](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1176989114#gid=1176989114)

Tim Reitz 02/21/2025: Updated.

  


Change Requests:

  * Ben Reitz 10/08/2025: [[[IN11556](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11558&)]] - ZGW - Member Payment record - Add "Sent" confirmation field


