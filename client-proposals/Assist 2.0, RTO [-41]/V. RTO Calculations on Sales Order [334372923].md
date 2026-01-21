5\. RTO Calculations on Sales Order

  


Requirements

Add RTO Calculations to the sales order:

  


  * AppHosting.zone Settings
    * Damage Waiver Fee ($ w/ 2 decimals)



  


  * Sales Order Record
    * Add RTO checkbox to the sales order.
    * Show the RTO options if that's selected.



  


  * RTO Calculator section on Sales Order Record:
    * RTO Vendor (defaulted based on the dealer; find out from Josh where it's stored but probably Sales Order)
    * Contract Type
    * Contract Template (defaulted based on the state of the customer)
    * RTO Terms (use a helper list to only get the supported terms from the selected vendor)
    * Include Damage Waiver Fee (DWF) -- checkbox copies amount onto read-only field on the sales order record, or clears it out
    * [ ] Calculate RTO (checkbox with onchanges to freeze all inputs onto the record)
    * RTO Security Deposit (macro)
    * CRA Cash Received (macro)
    * CRA Monthly Payment (macro)
    * Fields:
      * All parameters needed for macros
    * Be sure to include all the Additional Macros Needed from the spreadsheet, since they will be referenced by the contracts.



  


Development Specification

See [https://docs.google.com/spreadsheets/d/1dRKwAs4XfPwF3ndcrWoZLQhPtI9QkplEvaY7qp06kxo/edit](https://docs.google.com/spreadsheets/d/1dRKwAs4XfPwF3ndcrWoZLQhPtI9QkplEvaY7qp06kxo/edit) for calculations
