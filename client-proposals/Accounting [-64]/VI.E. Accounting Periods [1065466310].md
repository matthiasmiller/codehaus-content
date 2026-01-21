6.5. Accounting Periods

Overview:

[X] It is a common practice in accounting to close accounting cycle. 

[X] When an accounting cycle is closed we do not allow any addition or modification on any transactions.

[X] If there is a need to modify any transaction, usually that is done by creating a new adjusting transaction in the new cycle.

[X] In our system when a closing date is entered, we do not allow any edit in any transaction prior to the date.

[X] Also the default start date and end date in all the accounting reports are updated.

  


[X] When users do not want any more modification on the transactions, they can add a transaction locking date. This makes the transactions uneditable.

[X] The purpose of transaction locking date is to freeze transactions i.e. do not allow any addition / deletion / modification on the transaction prior to the locking date.

[X] Only users with "Reopen accounting periods" permission can remove the locking date.

[X] The Accounting Closing Dates and Transaction Locking Dates are stored in "Accounting Periods" record.

  


Menu Link:

[X] Accounting | Accounting Tools | Accounting Periods | Show Accounting Periods

  


Fields:

[X] Accounting Period ID

\- This is a hidden field.

\- "Accounting Periods" is the default value.

  


[X] Accounting Closing Dates

\- Dated RG field.

\- Does not allow duplicate dates.

\- Editable if user has "Close accounting periods" permission

\- Column heading: "Closed as of".

  


[X] Accounting Periods Closing Row Modified

\- Hidden field to control editability of RG rows.

  


[X] Accounting Periods Locking Date

\- Dated RG field.

\- Does not allow duplicate dates.

\- Editable if user has "Lock accounting periods" permission

\- Column heading: "Locked through".

 

[X] Accounting Periods Locking Row Modified

\- Hidden field to control editability of RG rows.

  


Detail Screen Notes:

[X] Note: Only users with the necessary permissions are able to reopen closed accounting periods.

[X] Note: Only users with the necessary permissions are able to reopen locked accounting periods.

  


Buttons:

[X] "Remove Last"

\- Visible if user has "Reopen accounting periods" permission.

\- Removes the top row in the "Accounting Closing Dates" / "Transaction Locking Dates" RG.

  


Links:

[X] Modification History

  


Validations:

[X] "You do not have permission to edit this record." when user does not have "Reopen accounting periods" permission. However if the user has "Close accounting periods" or "Lock accounting periods" permission then user can add rows with the help of "Close Period" / "Lock Period" imports in the main menu.

  


[X] "You cannot enter a future closing date." when entered date is a future date.

[X] "You cannot enter a date prior to the latest closing date." when entered date is earlier than latest closing date.

  


[X] "You cannot enter a future locking date." when entered date is a future date.

[X] "You cannot enter a date prior to the latest locking date." when entered date is earlier than latest locking date.

[X] "You cannot enter a date prior to the latest closing date." when entered date is earlier than latest closing date.

  


Referenced:

[X] Accounting Transaction detail.

  


Validations on other records:

[X] In "Accounting Transaction" detail

[X] "Transactions on or prior to the latest locking date cannot be modified."

[X] "Transactions on or prior to the latest closing date cannot be modified."

  


Jobs:

[ ] [[PC0089540]] - Disable transaction modification after closing date

[ ] [[PC0094062]] - Move FinAcctClosingDates list to lookup record

[ ] [[PC0113652]] - Accounting: Review accounting periods

[ ] [[PC0095036]] - Separate field for locking transactions instead of closing period

  


Open Jobs:

[ ] [[PC0107232]] - Add support for period-closing transactions
