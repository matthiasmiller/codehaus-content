6.4.1. All Claims Report

  


Requirements

Overview: This is a report of Claim records, with various filters.

  


Accessed from: Admin | Admin Reports | All Claims (opens a prompt screen with the below filters, to search for a Claim in the Solution) 

  


Title:

  * On the filter screen when the report is opened: "Search Claims"



TODO_CCI: Tim Reitz 07/31/2025: What is the condition for displaying this title?

Sagar Sagar 12/11/2025: When the report is run from both Admin | Admin Reports | All Claims and Home | Claims | My Client Claims, it shows Search Claims prompts. So basically its the title of the ask prompts.

  * If "Client or Vehicle Owner Name" = blank: "All Claims"
  * If "Client or Vehicle Owner Name" is not blank: "Claims for <Client Name>"



  


Preface: N/A

  


Columns: 

  * Client
  * Originating Owner
  * ID (displays the "Claim ID"; link to open the Claim record)
  * Date of Accident
  * Current Agent for Client 
  * Current Agent for Orig. Owner 
  * Originating Agent
  * Driver
  * Other Party Insurance



  


Grouped by:

  * If "Group by Vehicle" filter checkbox is checked: Vehicle ID
  * Otherwise: N/A (no grouping)



  


Sorted by: Date of Accident + Claim ID

  


Filters: 

  * Client or Vehicle Owner Name (drop list of all Contacts and blank; defaults to blank = all)
  * Start Date (date; defaults to blank = all) 
  * End Date (date; blank = all; defaults to the current date) 
  * Current Agent (Blank = All) (visible for Admin users; drop list of active "In-State Agents"-type Contacts with a Fund; defaults to blank = all; looks at both "Current Agent for Client" and "Current Agent for Orig. Owner"; defaults to blank = all) 
  * Originating Agent (Blank = All) (visible for Admin users; drop list of active "In-State Agents"-type Contacts with a fund; defaults to blank = all;)
  * Group by Vehicle (checkbox; defaults to not checked)
  * Vehicle ID (hidden; plain text; when the All Claims report is opened from the "View / Create Claims" link on Vehicle record, this defaults to __)



TODO_CCI: Tim Reitz 07/31/2025: What does this one default to?

Sagar Sagar 12/11/2025: Nothing. We need to send value for this.

  * Claim Client (hidden; plain text; __; defaults to __)



TODO_CCI: Tim Reitz 07/31/2025: What does this one do?

Sagar Sagar 12/11/2025: Nothing. We need to send value for this.

  


Buttons: 

  * New Claim (opens a new Claim record, with the following fields defaulted: 
    * "Client": defaults to the Contact in the "Client or Vehicle Owner Name" prompt, if not blank, 
    * "Vehicle": defaults to the Vehicle specified by the hidden "Vehicle ID" filter, if not blank;
    * "Driver": defaults to the "Vehicle Primary Driver" for the Vehicle;
    * "Originating Agent": defaults to the current Agent for the "Client", if the "Client or Vehicle Owner Name" prompt is not blank;
    * "Originating Fund": defaults to the current Fund for the "Originating Agent", "Client or Vehicle Owner Name" prompt;
    * "Date of Accident": always defaults to the current date)



TODO_CCI: Tim Reitz 07/31/2025: Do the following default based on the ask prompt here, or OnChange when "Client" / "Vehicle" is set on the Claim record?

  * "Driver"
  * "Originating Agent"
  * "Originating Fund"



Also, does "Date of Accident" default OnInit, or based on a prompt/button?

Thanks!

Sagar Sagar 12/11/2025: Yes, they are based on the ask prompts. 

  


The Date of Accident is set Today on its OnInit, not from ask prompts.

  


Menu Visibility: Admin (by virtue of the menu option being on the Admin menu)

  


Other Notes:

  * N/A



  


Development Specification

Change Requests: 

  * Tim Reitz 09/30/2024: [[[IN10221](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10223&)]] - ZWA - Claims - Clarify Claim Client vs. Originating Owner & Corresponding Agents


