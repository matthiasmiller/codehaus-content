11.2. All Bills

See "Module: Accounts Payable" on the left pane for more details of the feature.

  


Overview:

  * The report displays all the bills recorded in the system.



  


Jobs:

  * [[PC0115455]] - Accounts Payable: Bills Report



  


Report:

[X] This displays all Bills type of transactions. We consider a transaction as Bill if there is any liability type and payable subtype account with credit amount in transaction lines.

[X] We can filter the report to display due bills only.

[X] Level: Accounting Transaction

  


Menu link:

[X] Accounting | Accounts Payable | All Bills

  


Ask Prompt:

[X] Bill date from [Date]

[X] Through [Date]

[X] Show due bills only [Checkbox]

\- Default is unchecked.

  


Title:

[X] Bills <Start Date> through <End Date>. [See more on "Report Title" on the left pane.]

[X] Dates are in the format <mmmm dd, yyyy>.

  


Columns:

[X] Transaction ID

\- Links to Transaction detail screen

[X] Bill Date

\- Accounting transaction date

[X] Bill Due Date

\- Accounting transaction due date for bill payment

\- Displayed in red font if the due date is less than today.

[X] Last Paid On

\- Returns the date when there was the last payment made.

[X] Total Amount

\- Displays the total amount from the bill transaction detail screen.

Murshid Rahman 01/19/2023: I think this is showing all the credit which is not looking correct to me. Need more research on this.

[X] Paid Amount

\- Displays the Paid amount from the bill transaction detail screen.

[X] Balance

-Displays the balance amount from the bill transaction detail screen.

  


Sorting:

[X] Transaction Date and Transaction ID.

  


Grouping:

[X] Totals and subtotals only: No

[X] Report is grouped by Due Bills and Paid Bills

  


Buttons:

[X] New Bill

\- Opens Std Autopush New Bill.r20 autopush report.

  


No Records Found Msg:

[X] No bills found.
