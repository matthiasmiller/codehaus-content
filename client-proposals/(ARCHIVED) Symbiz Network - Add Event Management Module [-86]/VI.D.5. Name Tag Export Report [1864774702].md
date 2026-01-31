6.4.5. Name Tag Export Report

  


Requirements

*Documented 

  


Add the following new report: 

  


This is a report of all Main Registrants and Guests for one selected Event (looking at the Event Registration records with Registration Status = Attending or Tentative). This report is used to generate an Excel file, which in turn can be used to print name tags for all registrants.

  


This is accessed from:

  *  Admin | Event Management | Generate Name Tag Export (opens the filter screen to prompt for an Event) 



  


Title: "Name Tag Export for <Event Name> (<Event Type>)"

  


Columns (one row for each Registrant and one row for each Guest): 

  * First Name (either Registrant or Guest) 
  * Last Name (either Registrant or Guest) 
  * Organization (either Registrant or Guest)  
  * City, State (comma separated; either Registrant or Guest)
  * Guest of (for Registrant rows: blank; for Guest rows: displays a "Guest of" prefix, followed by the Registrant's name, in the following format: "Guest of <FirstName LastName>")
  * Industries (for Registrant rows: comma-separated list of all Industries that are selected on the Registrant's Contact record in the sequence in which they are listed there, with text wrapping; for Guest rows: blank) 
  * Registration Status (for visual / informational purposes; to be manually excluded from the name tags after exporting the Excel file)



  


Grouped by: 

  * First by: Industry (alphabetically by the first-listed industry)
  * Second by: Registrant type (Main Registrants at the top, then Guests) 



  


Sorted by: Last Name (alphabetically) 

  


Filters: 

  * Event (required; drop list of all Event IDs, with the latest "Event Date" at the top; filters down as you type; defaults to blank) 
  * Include Tentative Registrations (checkbox; defaults to checked; if not checked, the report displays only Registrations with Status = Attending) 



  


Buttons: 

  * N/A



  


Menu Visibility: Regional Reps & Super Admins (by virtue of the visibility settings for the admin menu)

  


Other Notes:

  * To generate an Excel file from this report, the user can click on the drop-down Advanced menu in the top right-hand corner of the report (the round down arrow button), and select "Excel", then download and save the file.



  


Development Specification

Mockup: N/A 

TODO_CCI: Tim Reitz 06/03/2024: Please send us screenshots of the report once you have it coded so we can review it prior to testing. Thanks!
