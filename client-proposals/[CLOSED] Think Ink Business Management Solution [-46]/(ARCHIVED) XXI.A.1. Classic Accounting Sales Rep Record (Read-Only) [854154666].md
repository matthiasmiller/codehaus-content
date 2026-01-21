21.1.1. Classic Accounting Sales Rep Record (Read-Only)

  


Requirements

Matthias Miller 08/26/2022: We don't need this anymore.

  


Overview: This is a hidden record type that mirrors the contacts in Classic Accounting and is used for syncing between the two programs.

  


Accessed via: The Classic Accounting Sales Reps report (see corresponding section of this proposal)

  


Fields:

  * AppHosting ID
  * Classic Accounting ID
  * Rep Name



  


Development Specification

TODO_CCI - Price This

  


DB Level:

[ ] Acct_Sales_Rep

  


CA_Org Fields:

[ ] Acct_Sales_Rep__AHZID

[ ] Acct_Sales_Rep__ID (string; 36 characters)

[ ] Acct_Sales_Rep__Name (string)
