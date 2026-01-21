3.1. 3rd Party Integration for Plain Transaction Imports

  


Requirements

Plaid Transactions will be imported into the Solution via a tool such as BankToSheets ([https://banktosheets.com/](https://banktosheets.com/)). These will then be used to reconcile transactions with bank statements.

  


Development Specification

NOTE: BankToSheets can have customized columns, if you dig into the documentation. I think we'd have a Google Script that would pull it, and do a webservices call to an x30.
