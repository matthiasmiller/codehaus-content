19.3. Minimize Data Entry Errors

Matthias Miller 07/26/2023: The current verification process eliminates the need for this.

  


A delivered PO creates a SKU lot.

  


From the SKU Lot, automatically create a

  * Credit to Accounts Payable
  * Debit to Raw Materials



  


  


TODO_HLD

[ ] From the Vendor Invoice, have a "Create Bill"

[ ] On payment

  


  


SKU has a GL account

Vendor Invoice can override the default

TODO - negotiate it w/ them

  


>>>>>>>>>>>>

  


  


  


[ ] Inventory Adjustments 

  


  


  * Bills -- alrweady works as expected
  * Vendor Invoices
  * Sales Orders



  


  


  


TODO_HLD - minimize data entry errors

  


For data entry purposes, InSight is wanting a way to ensure that transactions are entered from the correct account.

  


For example, payroll will be paid out of a "Finished Goods - Production Labor" asset account, NOT from a "Cost of Goods - Production Labor" expense account.

  


Two approaches:

  * On a per-contact basis, add a list of expected accounts. For example, for an employee, specify the "Finished Goods - Production Labor" account, the "Accounts Payable" account, as well as the "Primary Checking" account. This would simply warn when entering a transaction that is not in the list. We could also warn if the contact does not have any expected accounts.



  


  * On a per-account basis, add a list of contra accounts (or whatever the proper term is). For example, indicate that the "Finished Goods - Production Labor" account correlates to the "Accounts Payable" account. We would verify that the sum of all "Finished Goods - Production Labor" entries on the transaction (subsetted by class) are offset by the sum of all "Accounts Payable" entries for the same class.



  


  


Expense Invoice

  * Has a dropdown to pay out of:
    * Petty Cash
    * Checking
    * any of those types of assets



  


  * The Vendor Invoice knows what it should happen when it's paid



  


  * Each line item on the vendor invoice gets it own line item



  


To the extent of:

  * Vendor will always Credit the asset
  *  



  


Utilites

  * If it's autopay



  


  


POs can come in at various parts of the process.

  


  * Payroll Liability
    * Then when it gets paid, because a Labor Asset



  


  * Payroll - Biweekly



  


  * When you calculate payroll
    * It hit FGI Production Labor inventory
    * It hit Payroll Liability
  * When you pay it
    * It hits Payroll Liability
    * It hits Checking Asset



  


  


Number of transactions:

  * EBMS -- full automation -- is 1.5 person full-time
  * If every transaction would be manual -- then checking the work and fixing the mistakes -- More than double



  


  


For every invoice / sales items -- enters a GL entry
