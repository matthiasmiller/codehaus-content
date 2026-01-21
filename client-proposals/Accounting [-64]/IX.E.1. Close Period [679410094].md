9.5.1. Close Period

Overview:

[X] When an accounting cycle is completed an user can close the accounting period.

[X] This makes all the transactions on or prior to the date uneditable.

[X] This also updates the default start date and default end date on the report ask prompts.

[X] An user with "Close accounting periods" permission can see the link "Close Period".

[X] Running this import adds a row in the Accounting Closing Dates on the Accounting Periods record.

[X] "Transactions on or prior to the latest closing date cannot be modified." msg is displayed when user wants to edit any transaction.

[X] "You do not have permission to edit this record." msg is displayed if the user does not have permission "Reopen accounting periods" and wants to edit the closing date.

[X] If an user has "Reopen accounting periods", "Remove Last" button is displayed.

[X] "Remove Last" button removes the top row in the table. The rows are uneditable.

  


x30 Import:

[X] Level: Accounting Periods

[X] Simply adds a row in the "Accounting Closing Dates" table.

[X] Shows a success msg once the import is complete.

  


Menu link:

[X] Accounting | Accounting Tools | Accounting Periods | Close Period

  


Ask Prompt:

[X] As of Date

\- Required and by default it is today

  


[X] Label

\- * Transactions on or prior to the date specified cannot be created, modified, or deleted after closing the accounting period.

  


Title:

[X] Close Accounting Period

  


Success Message:

[X] Accounting period has been successfully closed through <mm/dd/yyyy>.

  


Validation Message:

[X] "You cannot enter a future closing date." when entered date is a future date.

[X] "You cannot enter a date prior to the latest closing date." when entered date is earlier than latest closing date.

  


Jobs:

[X] [[PC0094062]] - Move FinAcctClosingDates list to lookup record
