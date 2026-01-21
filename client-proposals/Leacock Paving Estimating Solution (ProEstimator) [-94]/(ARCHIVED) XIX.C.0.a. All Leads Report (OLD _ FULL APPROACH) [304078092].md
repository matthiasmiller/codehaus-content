19.3.0.1. All Leads Report (OLD / FULL APPROACH)

_EM: Tim Reitz 04/22/2025: There are some things that would be good to have on a Leads report, but not really needed on a Proposals report. Do you like putting it all onto a "master" report like we've been doing for some of the more recent projects? Or better to split them apart?

Tim Reitz 04/28/2025: I've copied in the main spec from the All Proposals Report. Struck through the items from there that don't apply to Leads, and added Lead-specific things in purple.

The most complicated things feel like:

  * Title: conditionally saying "Leads" vs. "Proposals" (presumably based on the selected Status(es))
  * "Group By" and "Sort By" ask prompts: each would have items included/excluded
  * Columns: it might be a lot of conditionally visible columns (haven't heard from the client how many they want)



Ellis Miller 05/06/2025: _VA: "Limit to Leads" (filtering down ask lists with this checkbox is fine, conditional columns is fine).

_VA: Tim Reitz 05/13/2025: I've merged the "Leads Report" spec into the "All Proposals Report" spec. Archive this soon, unless we end up changing course on the combined master report. 

  


Overview: This is a custom report of leads (Proposal records with "Status" = __), with various filters.

DO_: Tim Reitz 04/28/2025: Fill this in once we have the Statuses list finalized. Would be the ones prior to "Estimating in Progress".

  


Accessed from:

  * Main Menu | Proposals | All Proposals (opens the report directly, bypassing the filter screen)
  * Other menu options & links, with varying filter settings - see corresponding specs.
  * Main Menu | Leads | All Leads (opens the report directly, bypassing the filter screen)



  


Title: "Leads" "Proposals", with various conditionally-visible prefix(es) and/or suffix(es):

  * If "Proposal Type" filter = "Change Order": Includes the following prefix: "Change Order "
  * If "Customer" filter is not blank: Includes the following suffix: " for <Customer Name>"
  * If "Sales Rep" filter is not blank: Includes the following suffix (after the "Customer" suffix, if both apply): " (Sales Rep: <Sales Rep>")"
  * If "Customer" filter is not blank: Includes the following suffix: " for <Customer Name>"
  * If "Sales Rep" filter is not blank: Includes the following suffix (after the "Customer" suffix, if both apply): " (Sales Rep: <Sales Rep>")"



  


Example titles:

  * "Leads (Sales Rep: Smith, James)"
  * "Leads for Doe, John 123 Some St. (Sales Rep: Smith, James)"



  


Columns: 

  * Status
  * Proposal # (link to open the record) 
  * Customer 
  * Job Type
  * Sales Rep
  * Job Name
  * Job Contact
  * Job Address
  * Received Date
  * Appointment Date & Time (__)
  * Print Lead Information Sheet (link; __)
  * Lead Source
  * Referring Party
  * Paved Before
  * Decision Process
  * View Lead Information (ellipsis button; clicking this opens the "View Lead Information" child screen over the report)



_EM: Tim Reitz 04/28/2025: Fine to do this?

  * Proposal Date
  * Proposal Result Date
  * Total Proposal Price $



  


Grouped by: The selection in the "Group By" filter:

  * if blank: no grouping;
  * if "Customer": grouped by Customer name (in alphabetical order);
  * if "Proposal Date Month": grouped by month + year, in the "MMMM YYYY" format (current month at the top);
  * if "Result Date Month": grouped by month + year, in the "MMMM YYYY" format (current month at the top);
  * if "Sales Rep": grouped by Sales Rep name (in alphabetical order);
  * if "Status": grouped by Status (in standard sequence);
  * if "Job Type": grouped by Job Type (in standard sequence)



  


Sorted by: The selection in the "Sort By" filter:

  * if "Proposal Date": most recent at the top;
  * if "Proposal #": reverse sorted by the full Proposal # (both numeric and suffixes)
  * if "Received Date": oldest at the top



  


Filters: 

  * Status (optional; multi-select drop list of all Proposal Statuses list items; defaults to __)



: Tim Reitz 04/28/2025: Follow up here once we have the Proposal Statuses list finalized. I'm thinking right now that we'll include only "Estimating in Progress" through "Awarded", and users can add in the others if desired.

  * Proposal # (optional; plain text; defaults to blank = all; searches for all Proposal #s that include the entered value, i.e. if "15001" is entered, the report would display all versions of that number, such as "15001", "15001A", "15001B", etc.; if only "001" is entered, the report would display results such as "14001", "15001", "15001A", etc.)
  * Customer (optional; drop list of "Display Name for all active Contacts; defaults to blank = all)
  * Source Proposal # (plain text field; defaults to blank = all; if set to a valid Proposal #, the report displays only Proposals with "Source" = the entered Proposal)
  * Proposal Type (optional; drop list of Proposal Type list items; defaults to blank = all)
  * Received Date Start (optional; date; defaults to blank = all; looks at the "Received Date")
  * End (optional; date; defaults to blank = all; looks at the "Received Date")
  * Appointment Date Start (__)



  


  * End (__)



  


  * Proposal Date Start (optional; date; defaults to blank = all; looks at the "Proposal Date") 
  * End (optional; date; defaults to blank = all; looks at the "Proposal Date") 
  * Result/Awarded Date Start (optional; date; defaults to blank = all; looks at the "Proposal Result Date") 
  * End (optional; date; defaults to blank = all; looks at the "Proposal Result Date") 
  * Sales Rep (optional; drop list of "Display Name for all Employee-type Contacts with "Is Sales Rep" checked; defaults to blank = all)
  * Job Type (optional; multi-select drop list of Job Types list items; defaults to blank = all)
  * Status (optional; multi-select drop list of Proposal Status list items; defaults to none selected = all)
  * Group By (optional; drop list of blank / "Customer" / "Proposal Date Month" / "Result Date Month" / "Sales Rep" / "Status" / "Job Type"; defaults to "Status")



_EM: Tim Reitz 04/03/2025: Does this need to be a list in the system? Or just coded on the report?

Ellis Miller 05/06/2025: _VA: IN REPORT IF one report

  * Sort By (required; drop list of blank / "Proposal Date" / "Proposal #" / "Received Date"; defaults to "Proposal Date")



_EM: Tim Reitz 04/03/2025: Does this need to be a list in the system? Or just coded on the report?

Ellis Miller 05/06/2025: _VA: IN REPORT IF one report

Buttons: 

  * New Proposal (opens a blank new Proposal record, with "Customer" defaulted if "Customer" filter is set) 



  


Menu Visibility: All users

  


Other Notes:

  * This report (like all others) can be printed from the drop-down advanced menu in the top left-hand corner of the screen, by selecting "PDF" or "Excel".



  


: Tim Reitz 03/03/2025: Follow up here once the main report spec is done (considering grouping, etc.).
