6.3.1. Master Proposals Report

  


Requirements

Overview: This is a custom report of all Proposal records, with various filters. This is used as a "master report" to drive various Proposals-related reports.

  


Accessed from:

  * Main Menu | Proposals | Current Proposals (opens the report directly, bypassing the filter screen)
  * Various other menu options & links, which open varying versions of the master report (see corresponding specs) 



  


Title: Includes a main title, and may include conditionally-visible prefixes / suffixes:

  * Main title:
    * If "Report View" = "Current Leads": "Leads"
    * If "Report View" = "Proposals Needing Follow-Up": "Proposals Needing Follow-Up"
    * If "Report View" = "Proposals Needing Signatures": If "Report View" = "Proposals Needing Signatures"
    * If "Report View" = "Proposals Needing QuickBooks": "Proposals Needing to be Entered into QuickBooks"
    * Otherwise: "Proposals" 
  * Conditionally-visible prefix(es):
    * If "Proposal Type" filter = "Change Order": Includes the following prefix: "Change Order "
  * Conditionally-visible suffixes:
    * If "Customer" filter is not blank: Includes the following suffix: " for <Customer Name>"
    * If "Sales Rep" filter is not blank: Includes the following suffix (after the "Customer" suffix, if both apply): " (Sales Rep: <Sales Rep "Short Display Name">")"



  


Example titles:

  * "Leads (Sales Rep: James Smith)"
  * "Leads for Doe, John 123 Some St. (Sales Rep: James Smith)"
  * "Proposals (Sales Rep: James Smith)"
  * "Proposals for Doe, John 123 Some St. (Sales Rep: James Smith)"
  * "Change Order Proposals"
  * "Change Order Proposals for Doe, John 123 Some St. (Sales Rep: James Smith)"



  


Columns: 

  * Status
  * Proposal # (link to open the record; total row displays sum of the number of records) 
  * Customer 
  * Job Type
  * Sales Rep
  * Job Name
  * Job Contact
  * Job Address
  * Proposal Date (visible if "Report View" ≠ "Current Leads")
  * Initial Follow-Up Due Date (visible if "Report View" = "Proposals Needing Follow-Up")
  * Secondary Follow-Up Due Date (visible if "Report View" = "Proposals Needing Follow-Up")
  * Result/Awarded Date (visible if  "Report View" ≠ "Current Leads"; displays the "Proposal Result Date")
  * Total Proposal Price $ (visible if "Report View" ≠ "Current Leads"; total row displays sum)
  * Received Date (visible if "Report View" = "Current Leads")
  * Appointment Date & Time (visible if "Report View" = "Current Leads")
  * Print Lead Information Sheet (link; visible if "Report View" = "Current Leads")
  * Lead Source (visible if "Report View" = "Current Leads")
  * Referring Party (visible "Report View" = "Current Leads"; note that this and additional columns would also be visible for the "Gift Cards" report if/when that is added)
  * Paved Before (visible "Report View" = "Current Leads")
  * Decision Process (visible "Report View" = "Current Leads")
  * View Lead Information (ellipsis button; clicking this opens the "View Lead Information" child screen from the record, over top of the report)



  


Grouped by:

  * If "Report View" ≠ "Proposals Needing Follow-Up" (this is the standard / normal grouping):  
    * First: The selection in the "Group By (First)" filter:
      * if blank: no grouping;
      * if "Customer": grouped by Customer name (in alphabetical order);
      * if "Received Date Month": grouped by month + year, in the "MMMM YYYY" format (current month at the top);
      * if "Proposal Date Month": grouped by month + year, in the "MMMM YYYY" format (current month at the top);
      * if "Result Date Month": grouped by month + year, in the "MMMM YYYY" format (current month at the top);
      * if "Sales Rep": grouped by Sales Rep name (in alphabetical order);
      * if "Status": grouped by Status (in standard sequence);
      * if "Job Type": grouped by Job Type (in standard sequence) 
    * Second: The selection in the "Group By (Second)" filter: Follows the same logic as the "First" above.
  * If "Report View" = "Proposals Needing Follow-Up", this report includes special grouping instead of the standard grouping above:
    * "Needing Follow-Up": Proposals with "Status" = "Follow-Up Needed", in black font.
    * "Followed Up Today": Proposals with "Status" ≠ "Awarded" or "Lost" and either "Initial Follow-Up Complete" or "Secondary Follow-Up Complete" = the current date, in gray font.
    * "Awarded Today": Proposals with "Status" = "Awarded" and "Result Date" = current date, in green font.
    * "Lost Today": Proposals with "Status" = "Lost" and "Result Date" = current date, in black font.



  


Sorted by: The selection in the "Sort By" filter:

  * if "Received Date": oldest at the top;
  * if "Proposal Date": newest at the top;
  * if "Proposal #": reverse sorted by the full Proposal # (both numeric and suffixes), so that the latest is at the top



  


Filters: 

  * Report View (required; drop list of "Proposal Report Views" list items; defaults to "Standard"; the selection here determines the view for the report, including conditionally-visible filters, columns, groupings, and more, with the following details:
    * if set to "Standard":
      * the report subset includes all Proposal records;
      * this is the standard / default view for this report;
    * if set to "Current Leads":
      * the report subset includes only Proposal records with "Status" = "Lead Received", "Appointment Scheduled", and "Appointment Date Past";  
    * if set to "Proposals Needing Follow-Up":
      * the report subset includes only Proposal records that meet one or more of the following criteria:
        * "Status" = "Follow-Up Needed",
        * "Initial Follow-Up Complete" or "Secondary Follow-Up Complete" = the current date (regardless of "Status");
        * "Status" = "Awarded" and "Result Date" = current date;
        * "Status" = "Lost" and "Result Date" = current date;
    * if set to "Proposals Needing Signatures":
      * the report subset includes only items for which "Proposal Signed" is blank;
    * if set to "Proposals Needing QuickBooks":
      * the report subset includes only items for which "Proposal Status" = "Awarded" and "Entered into QuickBooks" is not checked)
  * Days Since Awarded Date (visible if "Report View" = "Proposals Needing Signatures"; number; 0 decimals; defaults to 7; this is the number of calendar days since the "Proposal Result Date", to only include Proposals that have gone that long as "Awarded" without a signature documented; note that if this default is changed, the "Proposals Needing Signatures Report Alert" report alert should also be changed to match - see corresponding spec) 
  * Status (visible if "Report View" ≠ "Current Leads" or "Proposals Needing Follow-Up" or "Proposals Needing QuickBooks"; optional; multi-select drop list of all "Proposal Statuses" list items; defaults to all selected)
  * Proposal Type (optional; drop list of Proposal Type list items; defaults to blank = all)
  * Proposal # (optional; plain text; defaults to blank = all; searches for all Proposal #s that include the entered value, i.e. if "15001" is entered, the report would display all versions of that number, such as "15001", "15001A", "15001B", etc.; if only "001" is entered, the report would display results such as "14001", "15001", "15001A", etc.)
  * Source Proposal # (plain text field; defaults to blank = all; if set to a valid Proposal #, the report displays only Proposals with "Source" = the entered Proposal, to display the Proposal "family")
  * Customer (optional; drop list of "Display Name" for all Customer-type Contacts; defaults to blank = all) 
  * Job Type (optional; multi-select drop list of Job Types list items; defaults to blank = all)
  * Sales Rep (optional; with the following details / behaviors:
    * drop list of "Short Display Name" for Contacts that meet the one or more of the following criteria:
      * all Employee-type Contacts with "Is Sales Rep" checkbox is checked; 
      * set as the "Sales Rep" on at least one Proposal record; 
    * defaults to blank = all)
  * Received Date Start (visible if "Report View" = "Current Leads"; optional; date; defaults to blank = all; looks at the "Received Date")
  * End (visible if "Report View" = "Current Leads"; optional; date; defaults to blank = all; looks at the "Received Date")
  * Appointment Date Start (visible if "Report View" = "Current Leads"; optional; date; defaults to blank = all; looks at the "Appointment Date")
  * End (visible if "Report View" = "Current Leads"; optional; date; defaults to blank = all; looks at the "Appointment Date")
  * Proposal Date Start (visible if "Report View" ≠ "Current Leads"; optional; date; defaults to blank = all; looks at the "Proposal Date") 
  * End (visible if "Report View" ≠ "Current Leads"; optional; date; defaults to blank = all; looks at the "Proposal Date") 
  * Job Scheduled Start Date Start (visible if "Report View" ≠ "Current Leads" or "Proposals Needing Follow-Up"; optional; date; defaults to blank = all; looks at the "Job Scheduled Start Date") 
  * End (visible if "Report View" ≠ "Current Leads" or "Proposals Needing Follow-Up"; optional; date; defaults to blank = all; looks at the "Job Scheduled Start Date") 
  * Result/Awarded Date Start (optional; date; defaults to blank = all; looks at the "Proposal Result Date") 
  * End (optional; date; defaults to blank = all; looks at the "Proposal Result Date") 
  * Group By (First) (visible if "Report View" ≠ "Proposals Needing Follow-Up"; optional; with the following details / behaviors: 
    * drop list of the following: 
      * blank; 
      * "Customer"; 
      * "Received Date Month" (visible only if "Report View" = "Current Leads"); 
      * "Proposal Date Month" (visible only if "Report View" ≠ "Current Leads"); 
      * "Result Date Month"; 
      * "Sales Rep"; 
      * "Status"; 
      * "Job Type"; 
    * defaults to "Status"; 
    * note that these are coded in the report, rather than being a separate list)
  * Group By (Second) (visible if "Report View" ≠ "Proposals Needing Follow-Up"; optional; drop list of the same options as "Group By (First)"); defaults to blank - see grouping spec) 
  * Sort By (visible if "Report View" ≠ "Proposals Needing Follow-Up"; optional; with the following details / behaviors: 
    * drop list of the following:
      * "Received Date" (visible only if "Report View" = "Current Leads"); 
      * "Proposal Date" (visible only if "Report View" ≠ "Current Leads"); 
      * "Proposal #"; 
    * defaults to: blank, but with the following special behaviors:
      * if "Report View" = "Current Leads": the report auto-sorts by "Received Date" (with this filter remaining blank); 
      * if "Report View" ≠ "Current Leads": the report auto-sorts by "Proposal Date" (with this filter remaining blank); 
    * note that these are coded in the report, rather than being a separate list)



  


Buttons: 

  * New Proposal (opens a blank new Proposal record, with "Customer" defaulted if "Customer" filter is set) 



  


Menu Visibility: All users

  


Other Notes:

  * This report (like all others) can be printed from the drop-down advanced menu in the top left-hand corner of the screen, by selecting "PDF" or "Excel".



  


Development Specification

Change Requests: 

  * Tim Reitz 11/17/2025: [[[IN12291](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12293&)]] - ZLP - Phase 1 - Improvements to Ask Prompts on Reports
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1649178932#gid=1649178932](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1649178932#gid=1649178932)

  


  


Ellis Miller 06/19/2025:

  


[ ] Title: 1 HOUR

[ ] Columns: 1 HOUR

[ ] Button opening child screen: 1 HOUR

[ ] Grouping 3 HOURS

[ ] Note that you will need GroupByExpr and GroupByLabel. Use local macros for each of the strings locCustomerStr, locReceivedDateMonthStr, etc.

[ ] Groupings are conditional.

[ ] Show first grouping if we have Group By 1 specified.

[ ] Show second grouping if we have Group By 2 specified.

[ ] You'll need logic to do eval a GroupingExpr and GroupingLabel, passing in the askGroupBy variable (1 or 2).

[ ] Sorting: 1 HOUR

  


Filters / Subsets: 8 HOURS

[ ] For most of these we don't use NdxFinds (just match on fields)

[ ] For Limit to Current Leads and Status, let's add a ProposalsByStatus.ndx (use BinString(StatusListNum, 4)).

  


[ ] For ProposalNumber searching, use ProposalNumberSubset Nic created

[ ] For SourceProposal searching, use the FromSourceProposalSubset subset Nic created.

  


TODO_EM: Tim Reitz 07/07/2025: Note / reminder about adding dev spec for the new search mode / report view drop list and those new views. 

  


  


  


_CCI: Tim Reitz 03/03/2025: Here is an example of the two Sort By options. The "Creation Date & Time" sequence used here is entirely hypothetical, simply showing how that sort order could differ from the other: 

Proposal #| Creation Date & Time  
---|---  
1500115000C15000B-215000B-115000B15000A-215000A-115000A1500014999A 14999| 15000C14999A 15000A-215000A-115000B-215000B-115000B15000A150011500014999  
  
  

