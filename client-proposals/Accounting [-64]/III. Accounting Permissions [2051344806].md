3\. Accounting Permissions

This is the current permissions with their hierarchy as of date.

  


View accounting data

        Edit accounting data

                Post transactions

                        Edit posted transactions

                Lock accounting periods

                        Close accounting periods

                                Reopen accounting periods

                Edit budget

        View diagnostic accounting data

  


  


View accounting data

[X] Coded in [[PC0088156]].

[X] In 2D menu, the "Accounting" tab is visible if the permission is true.

[X] If record is opened from Advanced | General | Lists, it displays list name but does not show any record name.

[X] Open reports / exports from file browser.

[X] If a financial report is opened, it displays no record found msg.

[X] If Account records or Transaction records are exported, the excel does not show any data rows.

[X] If activity history of records are opened, it displays no record found msg.

[X] Used in the following systems

AppHosting Accounting --> Allow Admin

AppHosting - Management [AHZ] --> Deny All

  


Edit accounting data

[X] Coded in [[PC0088156]].

[X] Displays msg "You do not have permission to edit this record." while trying to edit any account or transaction record.

[X] Used in the following systems

AppHosting Accounting --> Allow Admin

AppHosting - Management [AHZ] --> Deny All

  


Post transactions

[X] Coded in [[PC0090095]].

[X] An user can change the transaction status to "Posted" if this permission is set.

[X] An user cannot edit any posted transaction if "Edit posted transactions" is not set.

[X] Used in the following systems

AppHosting Accounting --> Allow Admin

AppHosting - Management [AHZ] --> Deny All

  


Edit posted transactions

[X] Coded in [[PC0090095]].

[X] An user can edit posted transactions if "Edit posted transactions" is set.

[X] Used in the following systems

AppHosting Accounting --> Allow Admin

AppHosting - Management [AHZ] --> Deny All

  


Lock accounting periods

[X] Coded in [[PC0095036]]

[X] No transaction can be added before the latest locking date.

[X] Used in the following systems

AppHosting Accounting --> Allow Admin

AppHosting - Management [AHZ] --> Deny All

  


Close accounting periods

[X] Coded in [[PC0094062]]

[X] The user with this permission can add an accounting closing date.

[X] Used in the following systems

AppHosting Accounting --> Allow Admin

AppHosting - Management [AHZ] --> Deny All

  


Reopen accounting periods

[X] Coded in [[PC0113652]]

[X] Only user with this permission can open a closed or locked accounting period.

[X] Used in the following systems

AppHosting Accounting --> Allow Admin

AppHosting - Management [AHZ] --> Deny All

  


Edit budget

[X] Coded in [[PC0116391]]

[X] If user has this permission,

[X] "Enter Budget" report button in "Account Budgets" report should be visible.

[X] "Enter Budget" button in the financial account detail screen should be visible.

[X] If "Std Financial Account Budgets - Entry" report is opened from file browser, 

[X] All the columns would be editable and budget amount can be entered.

[X] If user does not have this permission and "Std Financial Account Budgets - Entry" report is opened from file browser, all the columns would be uneditable and budget amount cannot be entered.

[X] Used in the following systems

AppHosting Accounting --> Allow Admin

AppHosting - Management [AHZ] --> Deny All

  


View diagnostic accounting data

[X] Coded in [[PC0110011]]

[X] If this is set, Match Key appears in the Transaction report and its ask prompt.

[X] In transaction detail "Imported Line" child detail is visible for imported records.
