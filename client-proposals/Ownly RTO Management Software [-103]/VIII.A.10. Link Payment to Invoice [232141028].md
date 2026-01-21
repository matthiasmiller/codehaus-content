8.1.10. Link Payment to Invoice

Invoice Record

  * Payment embedded spreadsheet
    * Payment ID
    * Payment Amount (cannot be more than the total payment amount)
    * View Payment (link to the payment)
    * Payment Date (read-only and auto-calculated; from the payment record)
    * Payment Method (read-only and auto-calculated; from the payment record)
  * The amount due will calculate based on total - payments from the embedded spreadsheet.



  


  * On save, the Invoice's payment date will be automatically set to the latest date from the linked payments IF the invoice is fully paid.



  


Payment record

  * View Linked Invoices (visible if type is "Invoice")
  * View Linked Contract Payment Rows (visible if type is "Payment")


