6.3.3. Sales Report

  


Requirements

Overview: This is a custom multi-pane report of sales by Sales Rep, based on Proposal records, with various filters. 

  


This report includes Proposals that meet the following criteria (others are not relevant to sales reporting):

  * "Proposal Type" = one of the following:
    * "Original" or
    * "Revised"
  * and "Proposal Status" ≠ "Archived" or "Canceled";
  * and at least one of the following dates is within the date range or year(s) selected in the filters:
    * "Received Date" or 
    * "Proposal Date" or 
    * awarded date ("Proposal Result Date" for "Awarded" Proposals)



  


Note that sales reporting is done with some specific details in mind: 

  * Leacock Paving has been looking at sales reporting by job start year/date rather than proposal awarded year/date. Since the ProEstimator Solution does not include project tracking in Phase 1, this Sales Report runs based on the awarded date ("Proposal Result Date"). In the future (i.e. Phase 2), once Job Tracking is included in the Solution, this reporting might be changed to run based on the actual job date, but details remain to be determined.
  * This main Sales Report shows data on a per-Proposal basis rather than on a per-Group basis, to report on total Proposals that have been sent and awarded/lost. Therefore, it does not include dollar amounts or any Group-specific information.
  * This main Sales Report does not include the Sales Rep Goal Tracking features, which are handled with a separate report to reduce complexity. If it is deemed reasonably simple to merge the two, that could happen in Phase 1 or at some point in the future.



  


Additional important notes about sales reporting:

  * The maximum number of Proposals in a Proposal family that can be included on sales reporting is 2 (and this can only happen if the family spans 2 or more years) -- the Original (Sent and Lost) and the Awarded revision (Sent and Awarded).
    *  If the Proposal family only spans one year, the maximum number of Proposals in the family that can be included on sales reporting is only 1 -- either the Original (if no Proposal is the family is marked as Awarded, or if it itself is marked as Awarded) or the "Awarded" revision -- and it is counted as both Sent and Awarded.
    * In a Proposal family, only count 1 as "Sent" per year.
  * When a revision is sent, it does not count as a Sent Proposal on the sales reporting until it is Awarded, at which point it is counted as both "Sent" and "Awarded".
    * Note that a Proposal that is counted as "Sent" in one year technically can be counted as "Awarded" in a later year, meaning that "Sent" and "Awarded" for the same Proposal do not have to be in the same year. 
  * When a revision is marked as "Awarded", the "Original" Proposal from a previous year is marked as "Lost" and any other revisions in the Proposal family are marked as "Archived".
  * All of this is handled by the "Set Proposal Results for Other Proposals in Family" automatic process (see corresponding spec) and the logic in the report.
  * Examples: 
    * 1. If both the Original and the revision were made in 2023, and the revision is the one that is awarded:
      * The Original shows up on the 2023 sales report as the only "Sent" proposal for the family until the revision is marked as "Awarded", at which point the revision shows up as both "Sent" and "Awarded", and the Original does not show up at all.
        * Note that in this case, the revision shows up as "Awarded" in the year in which is was marked as Awarded, which could be 2024 or 2025, etc.
    * 2. If both the Original and the revision were made in 2023, and the Original is the one that is awarded:
      * The Original shows up on the 2023 sales report as "Sent" and "Awarded", and the revision does not show up at all.
    * 3. If the Original was in 2023, and a revision was made in 2024, and the revision is the one that is awarded:
      * The Original shows up on the 2023 sales report as only "Sent" until the revision is marked as "Awarded", at which point the Original is marked as "Lost" for 2023.
      * The 2024 revision does not count as "Sent" (does not show up on sales reporting at all) unless it is marked as Awarded, at which point it shows up in the sales report as both "Sent" and "Awarded" (it shows up as "Awarded" in the year in which is was marked as Awarded, which could be 2024 or 2025, etc.).
    * 4. If the Original was in 2023, a revision was made in 2024 but not awarded, and another revision was made and awarded in 2025, and the revision is the one that is awarded:
      * The Original shows up on the 2023 sales report as only "Sent" until the revision is marked as "Awarded", at which point the Original is marked as "Lost" for 2023.
      * The 2024 revision never shows up on sales reporting.
      * The 2025 revision is counted as both "Sent" and "Awarded" on the 2025 sales report.



  


Accessed from:

  * Main Menu | Sales | Sales Report (opens the report directly, bypassing the filter screen)



  


Title: 

  * If "Date Type" = "Date Range" and both dates are blank: "Sales for All Time" 
  * If "Date Type" = "Date Range" and only "Start Date" is blank: "Sales until <End Date>" 
  * If "Date Type" = "Date Range" and "Start Date" is not blank: "Sales from <Start Date> to <End Date>" (if "End Date" is blank, uses current date) 
  * If "Date Type" = "Years": "Sales for <Year(s)>" (e.g. "Sales for 2025, 2024, and 2023") 
  * If "Date Type" = "Current Year-to-Date": "Sales for <current year> Year-to-Date" 
  * If "Date Type" = "Year Comparison": "Sales Comparison for <Year 1> and <Year 2>" 



  


Left pane: This is a totals-only report of Proposal records, showing sales by Sales Rep, for one or all Sales Reps in the selected timeframe(s) (based on the filter selections), with one row for each Sales Rep + Job Type combination:

  


Preface: "Reporting based on Proposal Date for "Sent" Proposals and Proposal Result Date for "Awarded" Proposals."

  


Columns: 

  * Sales Rep + Job Type (displays the "Job Type"; note that the column heading references "Sales Rep" because the "Sales Rep" grouping label appears to be in the same column)
  * <Comparison Year 1> # Leads Received (with the following details:
    * displays the number of Proposals for the "Sales Rep" \+ "Job Type" combination with "Received Date" within the selected filter date range;
    * total row at the top displays sum;
    * note that this is the total number of leads in the time period, and does not necessarily correspond to # Proposals Sent and/or # Proposals Awarded;
    * "<Comparison Year 1>" portion of the heading label is conditionally visible - only visible if the "Date Type" filter = "Year Comparison")
  * <Comparison Year 2> # Leads Received (visible if "Date Type" = "Year Comparison"; displays the the value for the "Comparison Year 2" filter selection, based on the same logic as the corresponding main/"Comparison Year 1" column)
  * <Comparison Year 1> # Proposals Sent (with the following details: 
    * displays the number of Proposals for the "Sales Rep" \+ "Job Type" combination with "Proposal Date" within the selected filter date range; 
    * total row at the top displays sum;
    * "<Comparison Year 1>" portion of the heading label is conditionally visible - only visible if the "Date Type" filter = "Year Comparison")
  * <Comparison Year 2> # Proposals Sent (visible if "Date Type" = "Year Comparison"; displays the the value for the "Comparison Year 2" filter selection, based on the same logic as the corresponding main/"Comparison Year 1" column)
  * <Comparison Year 1> # Proposals Awarded (with the following details: 
    * displays the number of Proposals for the "Sales Rep" \+ "Job Type" combination with "Proposal Result" = "Awarded" and with "Proposal Result Date" within the selected filter date range; 
    * total row at the top displays sum; 
    * note that if one or more additional Groups on a Proposal are marked as "Awarded" at a later date, those will not appear on this report; 
    * note that a Proposal with "Proposal Date" in one year and "Result Date" in the following year do not appear together in the same year's reporting, so early in a year there might be more "Awarded" than "Sent" on this report;
    * "<Comparison Year 1>" portion of the heading label is conditionally visible - only visible if the "Date Type" filter = "Year Comparison") 
  * <Comparison Year 2> # Proposals Awarded (visible if "Date Type" = "Year Comparison"; displays the the value for the "Comparison Year 2" filter selection, based on the same logic as the corresponding main/"Comparison Year 1" column)
  * <Comparison Year 1> Awarded % (with the following details:
    * displays the awarded percentage for values for the row, rounded to 1 decimal place, using the following formula: "<# Proposals Awarded> / <# Proposals Sent> * 100", i.e. "71 / 150 * 100" = 47.33, rounded to 47.3;
    * total row at the top displays average of the rounded values, also rounded to 1 decimal place;
    * "<Comparison Year 1>" portion of the heading label is conditionally visible - only visible if the "Date Type" filter = "Year Comparison") 
  * <Comparison Year 2> Awarded % (visible if "Date Type" = "Year Comparison"; displays the the value for the "Comparison Year 2" filter selection, based on the same logic as the corresponding main/"Comparison Year 1" column)



  


Grouped by: 

  * First by: Sales Rep (alphabetically; displays the "Short Display Name) 
  * Second by: Job Type (alphabetically) 



  


Sorted by: N/A

  


Filters (all are directly applied to the left pane, then secondarily to the right pane): 

  * Sales Rep (optional; with the following details / behaviors: 
    * drop list of "Short Display Name" for Contacts that meet the one or more of the following criteria:
      * all Employee-type Contacts with "Is Sales Rep" checkbox is checked;
      * set as the "Sales Rep" on at least one Proposal record; 
    * defaults to blank = all)
  * Job Type (optional; multi-select drop list of Job Types list items; defaults to all selected)
  * Date Type (required; drop list of "Date Range" / "Years" / "Current Year-to-Date" / "Year Comparison"; defaults to "Date Range"; with the following details:
    * if "Date Range" is selected: the Start and End Date filters are made visible, and the report includes results for the selected dates;
    * if "Years" is selected: the "Years" multi-select drop list is made visible, and the report includes results for all selected years, combined into the same columns/rows;
    * if "Current Year-to-Date" is selected: the report displays results for the current year, from January 1 through the current date;
    * if "Year Comparison" is selected: "Comparison Year" filters are made visible, and the report includes additional columns for comparisons; if one of the selected Comparison Years is the current year, the report displays year-to-date comparisons)
  * Start Date (visible if "Date Type" = "Date Range"; optional; date; blank = all; defaults to January 1 of the current calendar year; looks at the dates specified in the column specs) 
  * End Date (visible if "Date Type" = "Date Range"; optional; date; defaults to blank = all; looks at the dates specified in the column specs) 
  * Year (visible and required if "Date Type" = "Years"; with the following details:
    * multi-select drop list of calendar years, starting with the year of the earliest Proposal Date on any Proposal in the Solution through the current year; 
    * latest Year at the top; 
    * defaults to only the current year selected; 
    * can be used to report on totals from one or multiple years) 
  * Comparison Year 1 (visible and required if "Date Range" = "Year Comparison"; with the following details:
    * drop list of calendar years, starting with the year of the earliest Proposal Date on any Proposal in the Solution through the current year;
    * latest Year at the top; 
    * defaults to the current year) 
  * Comparison Year 2 (visible and required if "Date Range" = "Year Comparison"; with the following details:
    * drop list of calendar years, starting with the year of the earliest Proposal Date on any Proposal in the Solution through the current year;
    * latest Year at the top; 
    * defaults to the year before the current year)



  


  


Right pane: This is the "Master Proposals Report", filtered based on the selected filters for the left pane of this Sales Report (all other filters for this pane, such as Group By and Sort By, are set to the defaults for the "Master Proposals Report").

  


Buttons: 

  * N/A



  


Menu Visibility: All users

  


Other Notes:

  * N/A



  


Development Specification

Change Requests: 

  * Tim Reitz 11/17/2025: [[[IN12291](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12293&)]] - ZLP - Phase 1 - Improvements to Ask Prompts on Reports
  * Tim Reitz 11/25/2025: [[[IN12315](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12317&)]] - ZLP - Phase 1 - Misc. Changes Job #1
  * 


  


Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=504348521#gid=504348521](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=504348521#gid=504348521)

  


Ellis Miller 06/19/2025: 

  


CODING BY NIC WORKING WITH ELLIS

[ ] Need to work through implementation details when coding

[ ] NOTE (from above): if one of the selected Comparison Years is the current year, the report displays year-to-date comparisons

[ ] for the right pane: We can run it as an Identify sub-pane which will ensure correct records are included.

  


From Tim: Note that the feature for Sales Rep goal tracking was added in the IDD (fields on the Contact record and columns on this report). 

BID 3 DAYS
