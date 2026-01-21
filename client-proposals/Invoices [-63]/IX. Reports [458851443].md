9\. Reports

Sagar Sagar 12/20/2022: The visible reports from menu items are

[ ] Estimates

[ ] the columns are

[ ] Estimate Number

[ ] Estimate Date

[ ] Total Amount

[ ] Contact

[ ] Organization

[ ] Location - City, State, Country format

[ ] the report is reversely sorted by Estimate Date and Estimate Number

  


[ ] the prompts are

[ ] Estimate #

[ ] Contact - list of contacts

[ ] Organization - list of organizations

[ ] City

[ ] State - list of states

[ ] Zip

[ ] Estimate date range (from and through)

[ ] Sales Items - multi-selection list of sales items

[ ] the only report button is New Estimate

  


Sagar Sagar 02/02/2023: This report has been added in [[PC0111842]] - Support Estimates in our Invoicing module

  


[ ] Invoices

[ ] left pane

[ ] only column is Views

[ ] rows are

[ ] Open Invoices

[ ] Closed Invoices

[ ] All Invoices

[ ] Recent Invoices

Sagar Sagar 02/02/2023: Recent Invoices view has been added in [[PC0108165]] - Accounts Receivable: Invoice cockpit- add recent invoices view

  


[ ] right pane

[ ] the columns are

[ ] Invoice Number

[ ] Invoice Date

[ ] Total Amount

[ ] Contact

[ ] Organization

[ ] Location - City, State, Country format

[ ] Payment Date

[ ] Status

[ ] Agent - only visible in ZWA system

[ ] the pane is grouped by 

[ ] if first three rows are selected in left pane then Status

[ ] if Recent Invoices is selected in left pane then based on invoice date, Days, Today, Yesterday, Last Week, Two Weeks Ago, Three Weeks Ago, Last Month, Older, Future

Sagar Sagar 01/11/2023: Previously this was based on activity date. Now its based on sales form date. This has been coded in [[PC0126082]] - Grouping Label in recent invoices view seems incorrect

[ ] the pane is reversely sorted by Invoice Date and Invoice Number

Sagar Sagar 01/08/2023: The sorting was coded in [[PC0078283]] - E00 - Invoices should be sorted in reverse date order

[ ] the report buttons are

[ ] Search - to search in the invoices

[ ] New Invoice

[ ] the has footnote - 

  


[ ] the prompts are visible if you click on the Search button

[ ] Invoice #

[ ] Contact - list of contacts

[ ] Organization - list of organizations

[ ] City

[ ] State - list of states

[ ] Zip

[ ] Invoice date range (from and through)

[ ] Status - multi-selection list of status list

[ ] Sales Item(s) - multi-selection list of sales items

[ ] Show recent invoices only (modified in last 60 days) - checkbox

Sagar Sagar 01/05/2023: Searching feature in the report has been added in [[PC0076188]] - E00 - Search Invoices

  


Sagar Sagar 01/05/2023: Invoices report has been added in[[PC0072187]] - E00 - Generic Invoicing Module

  


[ ] Sales Analysis

[ ] the columns are

[ ] Configurable

[ ] if "Show Sales by" prompt selected as Month, then Month

[ ] if "Show Sales by" prompt selected as Quarter, then Quarter

[ ] if "Show Sales by" prompt selected as Product, then Product

[ ] if "Show Sales by" prompt selected as State, then State

[ ] if "Show Sales by" prompt selected as Customer, then Customer

[ ] Configurable

[ ] if "Period" prompt selected as Month to date, then MTD <ThisYear>

[ ] if "Period" prompt selected as Quarter to date, then QTD <ThisYear>

[ ] if "Period" prompt selected as Year to date, then YTD <ThisYear>

[ ] if "Period" prompt selected as Annual, then <ThisYear>

[ ] if "Period" prompt selected as Last month, then <LastMonth ThisYear>

[ ] if "Period" prompt selected as Last quarter, then <QNumber ThisYear>

[ ] if "Period" prompt selected as All History, then Sales

[ ] More Configurable columns with previous years

[ ] if "Also show prior years" checkbox prompt is checked

  


[ ] the report is a totals only report

[ ] the report is grouped by configured by "Period" ask prompt

[ ] the report is sorted by Invoice Number

[ ] the ask prompts are

[ ] Period - list of periods

[ ] Month to date

[ ] Quarter to date

[ ] Year to date

[ ] Annual

[ ] Last month

[ ] Last quarter

[ ] All History

[ ] Also show prior years - checkbox to show prior years columns

[ ] Show Sales by - list of groupings

[ ] Month

[ ] Quarter

[ ] Product

[ ] State

[ ] Customer

[ ] Reporting - list of reporting type

[ ] Revenue

[ ] Quantity

[ ] Limit to Product(s) - multi-selection list of sales items

  


[ ] the rows of the first column and column totals of the report are all links and you can dig in more to see the details of the invoices

[ ] the detailed report has columns of

[ ] Invoice Date

[ ] Invoice Number

[ ] Description

[ ] Quantity

[ ] Price

[ ] the report is reversely sorted by invoice date and invoice number

  


Sagar Sagar 01/08/2023: The identity report has been added in [[PC0086045]] - Sales Report: Enable identify

  


[ ] Active Product / Sales Items

[ ] the columns are

[ ] Code

[ ] Description

[ ] Category

[ ] Taxable?

Sagar Sagar 01/08/2023: This column was added in [[PC0078443]] - E00 - Invoices: Add "Taxable?" to Sales Items and Invoices

[ ] Unit Price

[ ] Active

[ ] the report is grouped by first of all active / inactive status and then by category, pushing uncategorized ones at the last

[ ] the report is sorted by Code

[ ] the ask prompts are

[ ] Code

[ ] Category - list of categories

[ ] Description

[ ] Active items only - checkbox

[ ] you can see the prompts by clicking on report title or Search button

[ ] the report buttons are

[ ] Search - opens the ask prompts to filter down with the searched terms

[ ] New Item - creates a new record

  


Sagar Sagar 01/05/2023: The Sales Items report was added in [[PC0076133]] - E00 - Invoicing: Add Product/Sales Item Table

 

[ ] Royalty Categories

[ ] the columns are

[ ] Name

[ ] SBI Percent

[ ] JN Percent

[ ] AHZ Percent

[ ] Provider Percent

[ ] the report is sorted by royalty category name

[ ] the report has only one button - New Royalty Category, to create a new record

  


Sagar Sagar 01/23/2023: The report has been added in [[PC0144196]] - AHZ - Respect Royalty Categories for calculations

  


Sagar Sagar 01/26/2023: If accounting module is included then there will be a new report called Aging Invoice.

[ ] Aging Invoices

[ ] the columns are

[ ] Invoice Number

[ ] Invoice Date

[ ] Invoice Status

[ ] Invoice Due Date

[ ] if there is no invoice due date, shows a red asterisk (*)

[ ] if the invoice due date is before today, shows the due date in red font, otherwise in normal font

[ ] Days Overdue

[ ] Contact

[ ] Organization

[ ] Due Amount

[ ] Current

[ ] 1-30 Days

[ ] 31-60 Days

[ ] 61-90 Days

[ ] 90+ Days

[ ] the report is grouped by the ask prompt Group By

[ ] the report is sorted by due date and overdue days

[ ] the ask prompts are

[ ] Group By - list of Days overdue, Contact and Organization

[ ] Invoice date range (from and through date)

[ ] Contact(s) - multi-selection list of contacts

[ ] Organization(s) - multi-selection list of organizations

[ ] Include draft invoices - checkbox

[ ] the report has a footnote - "* Invoices without specified due dates are due since invoice date." visible if there are due dates

  


Sagar Sagar 01/26/2023: The report has been added in [[PC0109472]] - Accounts Receivable: Invoices aging report
