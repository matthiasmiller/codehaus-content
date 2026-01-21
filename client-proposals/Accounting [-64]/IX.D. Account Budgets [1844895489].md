9.4. Account Budgets

Overview:

In our system we can add budget amounts in "Account Budgets" report. With the saved amounts we do nothing further in general accounting system. But we have some reports in XLP system where we display if our income / expense is within the budget.

  


Entering Budget:

\- We can enter budget with the help of Account Budgets report.

\- Also budget can be entered from the Financial Account detail screen.

  


Report:

[X] Displays all financial accounts as per the chart of accounts hierarchy and their budget amounts.

[X] "Enter Budget" button opens an editable report where we can add the amounts.

[X] Amounts can be entered in the child accounts only, parent accounts are displayed in bold font for visual difference.

[X] If any amount is entered in the Budget column then that is distributed in all the month columns.

[X] Level: Financial Account

  


Menu link:

[X] Accounting | Accounting Tools | Account Budgets

  


Ask Prompt:

[X] Budget year

[X] Start month - Drop down of all months

[X] Number of months - Drop list of numbers from 1 to 12.

[X] Account Type - by default it is Expense

  


Title:

[X] Financial Account Budgets for <Account Type> 

  


Columns:

[X] Account

[X] Class - Visible if ConfigAcct_EnterBudgetsByClass is set.

[X] <N> Month Budget

\- The amount entered here is distributed in all the columns.

[X] <Month> <Year>

\- This column is repeated as per the "Number of months" ask prompt.

\- Amounts can be entered in these columns and the summation is updated in the "<N> Budget" column.

  


Sorting:

[X] As per Chart of Accounts.

  


Buttons:

[X] Enter Budget - Opens editable report.

\- On the editable report

[X] Save Changes - To save the report.

[X] Close - Closes the Budget Entry report and opens Budget report.

  


Preface: 

[X]  If ConfigAcct_EnterBudgetsByClass is set

\- "Budget that is not tied to any class."

\- "Budget for the class - <Class name>"

[X]  If ConfigAcct_EnterBudgetsByClass is false then there is no preface.

  


Alternate Background Color:

[X]  Gray

  


No Records Found Msg:

[X] "No budgets found."
