10.1.4. Late Fees

An invoice that is not overdue will have a note such as, "The late fee is 1.5% after 30 days.", but will not automatically calculate or add the fee until the invoice is overdue. Once it is overdue, the fee will be applied automatically (but can be overridden).

  


The Invoice Detail will have a "Discounts & Fees" pop-out screen to view and edit Late Fee information. This would include the percentage (default to 1.5%), and an embedded spreadsheet of assessed fees. This spreadsheet would have the following columns: 

  * Date Assessed (auto-fill & read-only)
  * Days Overdue (auto-fill & read-only; "1-30", "31-60", etc.)
  * Amount (auto-filled; editable)



  


At 1 day overdue, it would enter a fee, then again at 31 days overdue, etc. This would be based on the invoice due date. There would be a nightly process that takes care of assessing these fees. 

  


The Late Fees would compound monthly with no proration. For example, an invoiced amount of $100.00 would become $101.50 after 30 days (100 * 1.015). It would then become $103.02 after 60 days (101.50 * 1.015), and $104.57 after 90 days (103.02 * 1.015).

  


The system would automatically charge the % on the 31st day, then again on the 61st day, then again on the 91st day. There would be a daily scheduled task to update overdue invoices with their late fees as needed. 

  


If an invoice has been partially paid before it becomes overdue, the late fee would only apply to the balance that is overdue. Therefore the customer can reduce the amount of the late fee by paying at least part of the invoice before the due date.

  


If partial payments are applied to an invoice after it is already overdue, subsequent late fees will only apply to the remaining balance when the invoice reaches the next overdue period.
