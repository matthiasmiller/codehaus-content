11.3. Aging Bills

See "Module: Accounts Payable" on the left pane for more details of the feature.

  


Overview:

  * While creating any bill record we can add a due date. This report displays the due bills and due date in separate columns for a better understanding. If there is a bill due for a 61 days or more then that is displayed in Overdue column. If there is no due date specified, then we consider transaction date or transaction date + "ConfigAcct_PayablesNumDaysDue" system switch value.



  


Jobs:

  * [[PC0114923]] - Accounts Payable: Aging Report
  * [[PC0115761]] - Accounts Payable: Changes to Aging Bills report



  


Report:

[X] This report always runs in context of Today.

[X] Only bills that have due amount are displayed here.

[X] The due amount as per date ranges are displayed in separate columns.

[X] If no due date is specified then considers transaction date as the due date or transaction date + "ConfigAcct_PayablesNumDaysDue" system switch value.

[X] Overdue items are displayed in Overdue column.

[X] Level: Accounting Transaction

  


Menu link:

[X] Accounting | Accounts Payable | Aging Bills

  


Ask Prompt:

[X] Bill due date [date]

[X] Through [date]

  


Title:

[X] Bills Aging as of <Today>. This report always runs in context of today.

[X] Dates are in the format <mmmm dd, yyyy>.

  


Columns:

[X] Transaction ID

\- Links to Transaction detail screen

[X] Bill Date

\- Accounting transaction date.

[X] Contact

\- Contact linked in the transaction detail

[X] Bill Due Date

\- Accounting transaction due date for bill payment.

\- Displayed in red font if the due date is less than today.

[X] Last Paid On

\- Displays the last payment date of this bill.

[X] Days Overdue

\- Number of days passed after the due date.

[X] Balance

\- Total due amount minus the paid amount.

[X] Blank column

\- This is there to separate the remaining columns.

[X] Due in < 7 Days

\- As the name suggests, due date is within today and 6 days from today.

[X] Due in 7-14 Days

\- Due date is in between 7 to 14 day.

[X] Due in 15-30 Days

\- Due date is in between 15 to 30 day.

[X] Due in 31-60 Days

\- Due date is in between 31 to 60 day.

[X] Due in 61+ Days

\- Due date is after 60days.

[X] Overdue

\- Due date is less than today/.

  


Sorting:

[X] By Bill due date, oldest date on top.

  


Grouping:

[X] Totals and subtotals only: No

[X] Report is grouped by Due Bills and Paid Bills

  


Buttons:

[X] New Bill

\- Opens Std Autopush New Bill.r20 autopush report.

  


Footnotes:

[X] "* Payables without specified due date are assumed to be due from transaction date." when the ConfigAcct_PayablesNumDaysDue switch value is blank.

[X] "* Payables without specified due date are assumed to be due in <N> days from transaction date." when the ConfigAcct_PayablesNumDaysDue switch value is not blank.

  


No Records Found Msg: 

[X] No bills found.
