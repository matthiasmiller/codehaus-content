9.5.2. Lock Period

Overview:

[X] Sometimes it becomes necessary to make transactions uneditable for normal users. For this an admin user or an user with "Lock accounting periods" permission can lock transactions and make those uneditable.

[X] This is separate from "Close accounting periods" because when we close any period, the start date and end date in all our ask prompts are updated accordingly.

[X] Locking any period does not have any effect on ask prompt default dates.

[X] Running this import adds a row in the Transaction Locking Dates on the Accounting Periods record.

[X] "Transactions on or prior to the latest locking date cannot be modified." msg is displayed when user wants to edit any transaction.

[X] "You do not have permission to edit this record." msg is displayed if the user does not have permission "Reopen accounting periods" and wants to edit the closing date.

[X] If an user has "Reopen accounting periods", "Remove Last" button is displayed.

[X] "Remove Last" button removes the top row in the table. The rows are uneditable.

  


x30 Import:

[X] Level: Accounting Periods

[X] Simply adds a row in the "Transaction Locking Dates" table.

[X] Shows a success msg once the import is complete.

  


Menu link:

[X] Accounting | Accounting Tools | Accounting Periods | Lock Period

  


Ask Prompt:

[X] As of Date

\- Required and by default it is today

  


[X] Label

\- * Transactions on or prior to the date specified cannot be entered, modified, or deleted after locking accounting transactions.

  


Title:

[X] Lock Accounting Period

  


Success Message:

[X] Accounting transactions have been locked successfully through <mm/dd/yyyy>.

  


Validation Message:

[X] "You cannot enter a future locking date." when entered date is a future date.

[X] "You cannot enter a date prior to the latest locking date." when entered date is earlier than latest locking date.

  


Jobs:

[X] [[PC0095036]] - Separate field for locking transactions instead of closing period
