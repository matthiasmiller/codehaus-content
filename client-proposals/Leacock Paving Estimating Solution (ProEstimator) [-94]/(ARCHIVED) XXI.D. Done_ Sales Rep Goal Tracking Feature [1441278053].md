21.4. Done: Sales Rep Goal Tracking Feature

  


Requirements

_VA: Tim Reitz 07/03/2025: Client would like to do this.

Tim Reitz 07/07/2025: archive once the maintenance pricing is done. 

  


The following feature could be added to facilitate tracking of annual/weekly sales goals for the Sales Reps. 

  


[ ] Estimated Cost:

  * [X] Upfront: $1,000-2,000
  * [ ] Annual maintenance: $150-200 (10-15% of the upfront cost)



  


Initial Spec: 

  


[X] Part 1: Changes to the Contact Record: Add the following:

  * Employee Details Section: 
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
        * Entire embedded spreadsheet is editable only for users that match one or both of the following:
          * users with the "Create/Edit Other User Profiles" Permission";
          * the user linked to the Contact record.)



  


  * View Sales Goal Tracker (visible if "Is Sales Rep" checkbox is checked or if any rows exist on the "Sales Rep Goals" embedded spreadsheet; link; opens the "Sales Goal Tracker" report, filtered to the corresponding Sales Rep) 



  


Goal Tracker RG editability: 

_VA Ellis Miller 07/02/2025: Who can edit?

_EM / _VA: Tim Reitz 07/02/2025: Is the above spec good, or should this be based on Permissions?

EM: Could be permissions to manage other users.

TR: Yeah, that had crossed my mind.

For a Sales Rep to edit his own, should we link the User Profile to the Contact record and base it on that?

  


Contact Record Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1529895558#gid=1529895558](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1529895558#gid=1529895558)

  


  


[X] Part 2: New "Sales Goal Tracker" Report: Add the following report: 

Overview: This is a custom totals-only report of goals and actual achievements by Sales Rep for a single selected year, showing results for one or all Sales Reps (based on the filter selections), with one row for each Sales Rep.

  


Note that this is very similar to the main Sales Report, but is being kept separate for now for complexity reasons. The two could be combined if deemed reasonably simple. 

  


Note that this report contains data from multiple record types:

  * Contact records (information from the Sales Rep's Goals embedded spreadsheet)
  * Proposal records (general Proposal information and information from the Groups embedded spreadsheet)
    * This report includes Proposals that meet the same criteria as the main Sales Report (see corresponding spec)



  


Accessed from:

  * Main Menu | Sales | Sales Goal Tracker (opens the report directly, bypassing the filter screen)
  * "View Sales Goal Tracker" link on the Contact record  



  


Title: Includes a main title, and may include conditionally-visible suffixes:

  * Main title: "Sales Goal Tracker for <Year>"
  * Conditionally-visible suffix(es):
    * Sales Rep suffix options (after the "Year" suffix):  
      * If "Sales Rep" filter is not blank: Includes the following suffix: " (<Sales Rep "Short Display Name">")"; 
      * If "Sales Rep" filter is blank: Includes the following suffix "(All Sales Reps)"  



  


Example titles:

  * "Sales Goal Tracker for 2025 (All Sales Reps)" 
  * "Sales Goal Tracker for 2023 (Smith, James)"
  * "Sales Goal Tracker for 2024 (All Sales Reps)"



  


Preface: N/A

  


Columns:

  * Sales Rep (displays the "Short Display Name)
  * # Leads Received (displays the number of Proposals for which "Sales Rep" = the Sales Rep for the row and "Received Date" is within the selected "Year"; total row shows sum; note that this is the total number of leads assigned to the Sales Rep in the time period, and does not necessarily correspond to "Actual: # Proposals Sent" and/or "Actual: # Proposals Awarded")
  * Goal: # Proposals Sent (displays the corresponding value from the selected "Year" row of the "Sales Rep Goals" embedded spreadsheet on the Sales Rep's Contact record; total row shows sum) 
  * Actual: # Proposals Sent (displays the number of Proposals for which "Sales Rep" = the Sales Rep for the row and "Proposal Date" is within the selected "Year"; total row shows sum)
  * Actual: # Proposals Awarded (with the following details: 
    * displays the number of Proposals for which "Sales Rep" = the Sales Rep for the row and "Proposal Result" = "Awarded" and "Result Date" is within the selected "Year"; 
    * total row shows sum;
    * note that a Proposal with "Proposal Date" in one year and "Result Date" in the following year do not appear together in the same year's reporting, so early in a year there might be more "Awarded" than "Sent" on this report)
  * Goal: # Proposals Sent/Week (with the following details: 
    * displays the corresponding value from the selected "Year" row of the "Sales Rep Goals" embedded spreadsheet on the Sales Rep's Contact record; 
    * total row shows average)
  * Actual: # Proposals Sent/Week (with the following details: 
    * displays the average number of Proposals per week for the Sales Rep for the selected "Year"; 
    * based on the following formula: "<"Actual: # Proposals Sent" for the report row> / <current fractional week # - see details below>, with the result rounded to the nearest whole number; 
    * total row shows average; 
    * weeks are counted as fractional weeks since January 1 of the selected "Year"; i.e. January 1 through the first Saturday of the year counts as the first week, then weeks start on Sunday from there on out; also, each day counts as a fraction of the week since January 1, to ease large jumps in percentages at the turn of each week; 
    * column heading includes the following tooltip, visible when the user hovers their cursor over the heading: "<#> weeks since Jan 1", with "#" displaying the fractional number of weeks for the current day, rounded to 2 decimal places, based on the following formula: "<day # for the current date> / 7"; i.e. "0.14" on January 1, or "4.12" on January 29, or "51.43" on December 26)
  * Goal: Awarded % (displays the corresponding value from the selected "Year" of the "Sales Rep Goals" embedded spreadsheet on the Sales Rep's Contact record; total row shows average, rounded to 1 decimal place) 
  * Actual: Awarded % (with the following details: 
    * displays the percentage of Awarded Proposals for the Sales Rep for the row within the selected "Year", rounded to 1 decimal place; 
    * based on  the following formula: "<"Actual: # Proposals Awarded"> / <"Actual: # Proposals Sent"> * 100", i.e. "71 / 150 * 100" = 47.33, rounded to 47.3; 
    * total row shows average of the rounded values, also rounded to 1 decimal place) 
  * Goal: Total $ (displays the corresponding value from the selected "Year" on the "Sales Rep Goals" embedded spreadsheet on the Sales Rep's Contact record; total row shows sum) 
  * Actual: Total $ (with the following details: 
    * displays the sum of "Group Printout Price $" for all Groups that meet the following criteria: 
      * "Sales Rep" for the Proposal = the Sales Rep for the row and
      * "Group Awarded Date" is within the selected "Year"; 
    * total row shows sum) 



  


Grouped by: N/A (no grouping) 

  


Sorted by: Sales Rep (alphabetically)

  


Filters: 

  * Sales Rep (with the following details: 
    * optional; 
    * drop list of "Short Display Name" for all Employee-type Contacts that meet at least one of the following criteria: 
      * "Is Sales Rep" is checked or 
      * "Sales Rep Goals" embedded spreadsheet contains at least one row; 
    * defaults to blank = all) 
  * Year (with the following details:
    * required; 
    * single-select drop list of all years for which at least one Proposal contains one of the following dates within that year (this is to give a full selection of all years that could yield results on this report): 
      * "Proposal Date" or 
      * "Proposal Result Date" (for "Awarded" Proposals) or 
      * "Group Awarded Date"; 
    * latest Year at the top; 
    * defaults to the current year) 



  


Buttons: 

  * N/A



  


Menu Visibility: All users 

  


Other Notes:

  * For situations where there is one or more "Revised" Proposals within a "Proposal family", the same logic applies to this report as to the main Sales Report (only displaying 1 Proposal per family per year, and only displaying a max of 2 - the Original and 1 "Revised" Proposal - if the "family" spans multiple years). See the corresponding logic with the Sales Report spec.



  


Sales Goal Tracker Report Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1156575686#gid=1156575686](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1156575686#gid=1156575686)

  


Development Specification

Sales Goal Tracker Report Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1156575686#gid=1156575686](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1156575686#gid=1156575686)

  


Contact Record Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1529895558#gid=1529895558](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1529895558#gid=1529895558)

  


  


_EM: Tim Reitz 06/05/2025: Thoughts on merging this into the main Sales Report? Maybe with an ask prompt: 

  * Report Type (required; drop list of "Main Sales Report" / "Sales Goal Tracker"; defaults to __) 
  * then the goal tracker details (columns, title stuff, etc.) would be conditionally visible 
  * "Date Type" probably would probably have its displayed list option limited to only "Year-to-Date" if "Sales Goal Tracker" (like we're limiting "Group By" / "Sort By" on the master proposals report) 



TODO_PRICING Ellis Miller 06/02/2025: Let's leave it separate. Will review in pricing.

  


Tim Reitz 06/26/2025: Per conversation with the client today, this is an important feature for the software. He would like a price on it.

  


\--------------

  


Tim Reitz 07/03/2025: Client said on call today that he wants to do this one.
