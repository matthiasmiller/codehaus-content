9.1.1. CRA Termination

TODO_SETH

  


In some cases, the CRA must be terminated and must be converted to a security deposit. In almost cases, this is because the customer has defaulted, and we need to convert it to a security deposit and apply that to payments. (NOTE: The CRA is set aside for an EPO.)

  


Add a button to the contract called "Terminate CRA". It should show the following message:

  


IRREVERSIBLE ACTION – PROCEED WITH EXTREME CAUTION

  


You are about to terminate this Cost Reduction Account and convert it into a Security Deposit on this Rent-to-Own contract.

  


  * This will permanently terminate the Cost Reduction Account.
  * The CRA balance of $123.56 will be moved into the Security Deposit.
  * The contract will permanently convert from the reduced monthly payment of $123.45/mo to $234.56/mo.



  


THIS CHANGE CANNOT BE UNDONE.

  


Are you sure you want to continue?

  


NOTE: You can show this in a memo on the detail screen if you want. You can add a "Type CONFIRM to continue"  (ask prompt or x30; x30 or detail button; really don't care)

  


When this gets clicked:

  * Clears the CRA amount for the contract calculation, forcing the contract value and monthly payment to revert to the original contact value and monthly payment. NOTE: The historical or fully-paid invoices all remain unchanged. Update any future unpaid/partially paid periods to the new payment amount.
  * Adds a row to decrease the CRA by the CRA amount
  * Adds a row to increase the security deposit that amount


