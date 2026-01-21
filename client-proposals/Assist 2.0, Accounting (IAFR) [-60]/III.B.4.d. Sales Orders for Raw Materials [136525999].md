3.2.4.4. Sales Orders for Raw Materials

  


Requirements

The builders regularly create sales orders that impact raw material cost.

  


  * Add a custom field to sales orders for "Raw Materials Cost"
  * Update the Sales Order Accounting Impact report to:
    * Credit the Raw Material FGI Source Account for sold sales orders
    * Debit the Raw Material FGI COGS Expense Account for sold sales orders
  * Confirm that when accounting calculates the total raw material cost for buildings for a period, these are not included in that total.



  


Development Specification

Niccolas Miller 04/25/2023: [[PC0153587]] - ZFP - FGI: Sales Orders: Sales Orders for Raw Materials (T&M)
