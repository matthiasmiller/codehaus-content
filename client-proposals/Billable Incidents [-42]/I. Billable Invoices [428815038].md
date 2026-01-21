1\. Billable Invoices

On the billing child screen:

  


  * Add a "Time & Materials" section label above the Employee's RG
  * Add a "Material" RG in that section that has:
    * Quantity
    * Sales Item Code
    * Description
    * Unit Price
    * Price
    * Migrate the Credit/Discount items into this RG.
  * To the right of it, show:
    * Total Time
    * Total Materials
    * Total Cost



  


  * Add a "Payments" section that has the payment information.
    * Rename "Date" to "Invoice Date"
    * Keep the Amount column
    * Add a "Paid" checkbox (editable expression). If checked, it will update the "Payment Date" to today's date. If unchecked, it will clear it
    * Add a "Payment Date".
    * Use a name change to populate payment date if the status was "Paid".
  * To the right of it, show:
    * Billing Type:
      * Time and Materials
      * Fixed Cost
    * "Budget" or "Price" (based on Billing Type)
    * Estimated Completed % (editable but auto calculated; updates cost)
    * Estimated Total Cost (stored; defaults to budget or price)
    * Projected Profit $ (auto-calculated)
    * Projected Profit %   (auto-calculated)
  * Cash Flow
    * Total Earned (auto-calculated)
    * Total Invoiced (auto-calculated)
    * Total Uninvoiced (auto-calculated)
    * Total Paid (auto-calculated)
    * Total Unpaid (auto-calculated)



  


NOTE: Completed % must be filled in for Fixed Cost jobs for Total Earned. Otherwise, it will remain as 0/NA.
