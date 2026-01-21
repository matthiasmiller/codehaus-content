2\. Configuration & Settings

  


Requirements

System switches:

[X] ConfigAcct_UseAccountNumber

[X] We use account number with account label if this is true, otherwise we consider the name as string.

[X] Label: Use alphanumeric account number

[X] Added in [[PC0078489]]

[X] Used in the following systems

External\AppHosting Accounting --> No

External\AppHosting - Management [AHZ] --> Yes

External\AppHosting Provident Fund BD --> Yes

External\CodeCrafters - CodeCrafters Admin [XCC] --> Yes

External\LAMB Project [XLP] --> Yes

  


[X] ConfigAcct_ManualOrderChartOfAccts

[X] When this is true we can change the order of accounts, otherwise accounts are sorted alphabetically.

[X] Label: Allow manual ordering in chart of accounts

[X] Organize button is visible in Chart of Accounts report if this is true.

[X] Added in [[PC0077836]]

[X] Used in the following systems

AppHosting Accounting --> Yes

LAMB Project [XLP] --> No

  


[X] ConfigAcct_NumberOfAccountLevels 

[X] Determines the allowed level of hierarchy in Chart of Accounts.

[X] Label: Number of account levels.

[X] Hidden, User Changeable system switch. Added in [[PC0089251]]

[X] This configures the maximum levels of sub-accounts for any financial account. 

[X] Default value is "5". Default value was changed from 3 to 5 in [[PC0086237]].

[X] In XLP system this is set to "4". Coded in [[PC0089377]].

[X] Used in the following systems

AppHosting Accounting --> 5

LAMB Project [XLP] --> 4

  


[X] ConfigAcct_AllowDraftTransactions

[X] In Transaction status field we can see "Draft" option.

[X] If this is false, "Posted" becomes the default status of transaction records.

[X] Label: Allow draft transactions

[X] Used in the following systems

AppHosting Accounting --> "Yes"

  


[X] ConfigAcct_DefaultTransactionStatus

[X] Determines the default status of any transaction with the options "Draft | Posted".

[X] Label: Default transaction status

[X] Used in the following systems

AppHosting Accounting --> "Draft"

  


[X] Config_FiscalYearStartMonth

[X] Displays a list of all the months. Determines the start month of fiscal year.

[X] This is used in the report ask prompts to determine the start date of accounting reports.

[X] Label: Fiscal year starts in.

[X] Used in the following systems

AppHosting Accounting --> "January"

CodeCrafters - CodeCrafters Admin [XCC] --> "July"

CodeCrafters - Provident Fund [XPF] --> "July"

LAMB Project [XLP] --> "July"

  


[X] ConfigInvoice_LinkAccounting

[X] Specifies whether invoices are linked to the accounting system. (See Module: Accounts Receivable)

[X] Label: Link invoice to accounting

[X] Used in the following systems

AppHosting Accounting --> No

AppHosting Invoicing Accounting Link --> Yes

  


[X] ConfigAcct_TransExportMatchKeyPrefix

[X] Specifies a prefix to add to match key for accounting transaction export. (See Transaction Export)

[X] Label: Transaction export match key prefix

[X] Used in the following systems

AppHosting Accounting --> "SourceSystemID"

  


[X] ConfigAcct_TransactionHasLinkedRecs

[X] Returns yes if accounting transaction has linked records.

[X] Label: Accounting transaction has linked records

[X] Used in the following systems

AppHosting Accounting --> No

AppHosting Invoicing Accounting Link --> Yes

  


  


[X] ConfigAccounting_HasJobsModule

[X] Specified whether jobs module is included. It displays Incident IDs in the transaction detail if set to Yes.

[X] Label: Has job module

[X] Coded in [[PC0112451]]

[X] Used in the following systems

AppHosting Accounting --> No

CodeCrafters - Sample System [E00] --> Yes

  


[X] ConfigAccounting_JobsUseHelperList

[X] Specified whether jobs module use helper list of ids

[X] Label: Jobs use helper list

[X] Coded in [[PC0112451]]

[X] Used in the following systems

AppHosting Accounting --> No

CodeCrafters - Sample System [E00] --> Yes

  


[X] ConfigAccounting_JobsUseChoiceRpt

[X] Label: Jobs use choice report

[X] Coded in [[PC0112451]]

  


[X] ConfigAcct_EnableAccountLinking

[X] Enables linking financial accounts with other records (e.g., Contacts)

[X] Label: Enable linking financial accounts with other records

[X] Coded in [[PC0113951]]

[X] Used in the following systems

AppHosting Accounting --> No

  


[X] ConfigAcct_PayablesNumDaysDue

[X] Label: Payables due in day(s)

[X] Used in Std Accounts Payable.r20 report

  


[X] ConfigAcct_DupPriorLineClass

[X] Duplicates class field from the prior transaction row

[X] Label: Duplicate prior line class

[X] Coded in [[PC0115069]]

[ ] Used in the following systems

AppHosting Accounting --> No

LAMB Project [XLP] --> Yes

  


[X] ConfigAcct_DupPriorLineNotes

[X] Duplicates notes field from the prior transaction row

[X] Label: Duplicate prior line notes

[X] Coded in [[PC0115069]]

[X] Note: we have similar switches in XLP, ConfigAcct_DupPriorLineJournalRef.

[X] Used in the following systems

AppHosting Accounting --> No

LAMB Project [XLP] --> Yes

  


[X] ConfigAcct_EnterBudgetsByClass

[X] Allows budget entering by classes.

[X] Label: Enter budgets by class

[X] Coded in [[PC0147399]]

[X] Used in the following systems.

AppHosting Accounting --> Std Financial Account Budgets.r20.

  


[X] ConfigAcct_UseMultipleCompanies

[X] We support accounting for multiple companies if this is "Yes".

[X] Label: Use multiple companies.

[X] Coded in [[PC0147104]].

[X] Used in the following systems.

AppHosting Accounting --> No

CodeCrafters - Sample System [E00] --> Yes

Joel Iwashige [XJI] --> Yes

  


Development Specification

TODO: Document all config_ and Custom_ options. 

  


Note anything else that stands out that may not be obvious to a user looking at the detail screen (conditionally visible settings, configuration of Type fields, etc).
