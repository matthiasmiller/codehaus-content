10.7.0.1. Promised Payments

TODO_SETH - Can you review this design and give feedback?

  * Promised Payments support
    * Note record
      * Type - Promised Payment
      * Promised Amount - $ (2 dec; required)
      * requires followup date
  * Payment
    * Open Promised Payments
      * [ ] to complete
      * Created On
      * Promised Amount
      * Followup Date
    * On save, trigger an x30 to complete the checked promised payments
    * Warn on save if the there are open (Current / Past Due) promised payments but none have been checked off
  * Promised Payments report (editable report)
    * report of all open promised payment notes
    * filter
      * RTO company
      * status (open/complete)
    * columns
      * customer
      * created date
      * promised amount
      * followup date
      * last payment date
      * last payment amount
      * row color
        * if followup date is today or yesterday, and no payment since creation, mark it red
        * if payment after creation, mark it green
      * checkbox to complete the note
    * group by past due vs upcoming (??)


