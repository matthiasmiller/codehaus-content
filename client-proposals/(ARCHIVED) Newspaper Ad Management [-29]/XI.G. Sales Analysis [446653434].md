11.7. Sales Analysis

  


Requirements

There will be a menu option called "Sales Analysis", which is AppHosting's standard sales reporting, with the addition of a Publication column and a Publication filter for Full Admin Users. 

  


Clicking on the menu option will open a page that prompts for the following: 

  * Period (multiple options, including Year to date, Quarter to date, Last month, All history)
  * Show Sales by ... Then by (two lists of Month, Quarter, Product, Customer, State, Publication Date)
  * Report on (Revenue, Quantity)
  * Limit to Product(s) (multi-select list of codes for Sales Items that were set to show up in sales reporting)
  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Clicking Continue opens a report based off of the selected filters. These reports can be exported to Excel or PDF as desired.

  


This feature provides the main part of the reporting, including reporting on numbers of different Ad Sizes (by selecting Show Sales by Product, etc.). 

  


See [https://demo.apphosting.zone/Reports/Standard/Std_Sales_Report](https://demo.apphosting.zone/Reports/Standard/Std_Sales_Report) for examples of how this can work.

  


These reports would be customized to include a Publication column, visible only for Full Admin users.

  


Reporting is done on a per-Sales Item basis, so the numbers will show the base price for the ads, NOT the invoiced/discounted prices (discounts are separate Sales Items).

  


Development Specification

Tim Reitz 03/09/2021: Should we have another report that does include the final prices? Or do we have already that could do that? 

  


Standard report customizations: 

  * Use custom macros to control a customized column (heading, contents, visibility) and custom macro for report subset (custom ask prompt).
  * The "Publication Date" option in "Show Sales by" is a custom item in SalesReportGroups list.



  


Proposed changes to the standard Sales Analysis reporting: 

Add a new item to "Show Sales by" list: Customer

  * Add a secondary grouping option to the right of "Show Sales by", called "Then by", with the same list. This way we could show sales first by Customer, then by Product, etc. 
  * Move "Reporting" to below "Show Sales by" and change the name to "Report on" (to match the terminology of the other prompts)



Tim Reitz 02/26/2021: Talk to Ellis.

Tim Reitz 02/27/2021: Ellis likes this. We might charge John for this or at least split it with him.
