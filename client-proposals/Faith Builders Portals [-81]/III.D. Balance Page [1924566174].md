3.4. Balance Page

  


Requirements

Filters:

  * Date Range (two date fields, searches by Check Date for Distributions and Postmarked Date for Contributions)
  * Show Distributions (defaults to true)
  * Show Contributions (defaults to true)
  * Type (Droplist of Pre-K, K-12, OSTC, and Non-EITC; defaults to every type for which the school has distributions or contributions)



  


Buttons:

  * Download (downloads a csv file for the currently shown information)



  


Columns:

  * Check Date
  * Check Number
  * Business Name (visible when Show Contributions is checked)



(Repeating for each Type selected):

  * <Type> Amount
  * <Type> Balance


  * Full Balance (Summation of all balances for the school, regardless of Type filter settings. Visible if more than one Type is selected)



  


Notes:

  * Contributions through SPEs will have rows beneath them lacking a check date and number, showing the individual contributions.
  * If the table of data becomes too wide, it will side-scroll.



  


Development Specification

GET:

  * Create a report to get all types for the school. This will populate the Type filter. Wait to load the page until this report returns.
  * Create a report to get the data for the table.



  


POST:

  * Every time a filter field is changed, haze out the table and display a loading wheel until the data comes in.


