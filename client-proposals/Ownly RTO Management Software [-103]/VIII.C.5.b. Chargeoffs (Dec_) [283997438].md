8.3.4.2. Chargeoffs (Dec?)

Seth Miller 01/27/2026: TODO_SETH. Spec and delegate [[PC0189388]]

  


Contract:

  * Add "Chargeoff" to contract resolutions
  * Add "Chargeoff Date"



  


Contract Event Types

  * Rename "Contract - Transaction" to "Contract - Event" Seth Miller 01/27/2026: This is old. What should it be now?
  * Add a "Contract - Resolution"



  


Accounting Company

  * New fields
    * Early Payoff Revenue
    * Payout Revenue
    * Chargeoff Expense



  


Accounting Impact

  * Create a macro that generates just the contract-resolution part of the event
  * Handle chargeoffs



  


  


  


OLD NOTES

  


  


  * LONGER-TERM... Do you want to separate them out? See income accounts that we have:
    * Product Cash Sales
    * Early Payoff
    * Payout
    * Chargeoff - Matthias Miller 11/06/2025: This needs to be expensed out. The others would be revenue accounts



Matthias Miller 11/06/2025: yes, let's create configuration for these events.
