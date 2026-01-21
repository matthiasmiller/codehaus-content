4\. RTO Calculator Report

  


Requirements

We need to lay the groundwork for RTO calculations.

  


  * RTOContractType (Investortools list)
    * Standard Contract
    * CRA Contract by Cash Received
    * CRA Contract by Monthly Payment



  


  * No-level macros for Josh
    * Display macros
      * RTOFinancingBase
      * RTOPaymentSubtotal
      * RTOPaymentTax
      * RTOPaymentDWF
      * RTOPaymentTotal
      * RTOSecurityDeposit
      * RTOCRAAmount
      * RTOCashDue
    * Editing macros
      * RTOContractError
        * If the contract template disallows large security deposits, show a message if it exceeds the default amount.
      * When someone makes edits, Josh can make the changes and refresh the macros.



  


  * Report with a lot of ask prompts to test these calculations.
    * Have a column for each factor
    * Could use a RepeatForList for each contract type.



  


Development Specification

Matthias Miller 06/23/2021: We need to lay the groundwork for RTO calculations.

  


Base it off the calculations in [https://docs.google.com/spreadsheets/d/1dRKwAs4XfPwF3ndcrWoZLQhPtI9QkplEvaY7qp06kxo/edit#gid=1484340395](https://docs.google.com/spreadsheets/d/1dRKwAs4XfPwF3ndcrWoZLQhPtI9QkplEvaY7qp06kxo/edit#gid=1484340395). The blue fields in the spreadsheet are the user-modifiable inputs (ask prompts in the target report).
