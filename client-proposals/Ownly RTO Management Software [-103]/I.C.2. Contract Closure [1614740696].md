1.3.2. Contract Closure

  * Can close contracts w/ a balance
  * Can pay on closed contracts



  


  


  


  


  


  * NOTE: We you do an EPO, we want to create a note with the EPO breakdown.~



  


  * Need to handle EPO for partial / lesser amounts (balance gets written off as bad debt)
    * Add an "Discounted EPO" adjustment type
    * Add settings to the accounting company
      * Proposing an RG of:
        * Adjustment Type (just these two)
          * Discounted EPO
          * Forgiveness
        * Ledger Account
          * Revenue or Expense account
      * Also:
        * EPO Revenue (revenue account)



  


  * Contract
    * Needs a way to end the rental
      * (i.e. you might have an unpaid balance you're trying to collect, but you're trying to collect)
      * (i.e. you might have retrieved the building, but you're trying to collect)
    * And needs a way to close out / write off the contract



  


  * NOTE: If the unpaid rent is too high for the discount you want to give, the user can just move the due date forward and move more things into EPO



  


NOTE:

  


  


  


[ ] Should we have a contract resolution date?

Early Payoff - autocalc to date of payoff

Payout - autocalc to date of payout

Return

Retrieval

  


  


  * Configurable date range between contract close and possible reinstatement
    * i.e. hold 90-day period of past due rent, holding as AR, and expense it as bad debt
    * Ask Accountants how to handle outstanding balances after end of contract



  


  


  


  


TODO_IDD: Building & Contract Closure

  * damage waiver fee writeoff
    * in theory these should be held as a liability (???) account until they are used OR written off... (posted as revenue at closure?)
  * chargeoff (closing out building as lost --
    * i.e. moved the building don't know where it is, can't collect because customer has disappeared
    * i.e. hostile customer prevents repo
  * early payoff
  * payout (end of life contract, paying last payment)
  * skip (building disappeared)
  * reposession (?)
  * return (?)



  


  


Scenario

  * God Gets Building -- Building Disappears/Destroyed (theft, hurricane, act of God  etc)
  * Customer Gets Building
  * RTO Company Gets Building



  


  


  


  


  * DWF Writeoff
  * Other Writeoff (other reason)



  


Q1 - What happened to the building

  * Add notice-- to forgive any past due rents or fees, 



  


  * It's Gone
    * Theft (contract balance + all fees remains)
    * DWF (past due rents/fees persist)
  * Customer Gets It (results in $0 balance on contract)
    * Early Payoff
    * Payout
  * RTO Company Gets It (past due rents/fees persist)
    * Retrieval
    * Return (fees can be forgiven as part of this process)



  


  


NOTE: Payment screen shows all active contracts and all contracts with an open balance

  * The only time you take a payment on a contract close event is for an EPO.



  


  


  


  
| Customer Charged?| Building "Exists"?  
---|---|---  
DWF Writeoff| [ ] | [ ]  
Other Writeoff| [ ]| [ ]  
Early Payoff| [X]| [X]  
Payout| [X]| [X]  
Retrieval| [ ]| [X]  
Return| [ ]| [X]  
  
  


  


  


  


add a field change expression that:

  * when the balance is zero:
    * automatically resolve as a epo if there is an epo on the account
    * automatically resolve as a payoff if not



  


create a scheduled task for:

  


  * Prompt for:
    * Payoff Template
    * EPO Template
    * Assignee
  * for any closed contract that does not have any tasks with the respective template, create one and assign it to the assignee
    * NOTE - if one of these tasks were completed BEFORE the contract close date, create a Contract note with a "Payoff Template sent before contract closure" or something like that'



  


[ ] What happens with the sale of a building to a non-building owner? We need sales tax.
