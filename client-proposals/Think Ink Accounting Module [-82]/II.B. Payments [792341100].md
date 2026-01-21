2.2. Payments

  


Requirements

The Solution will include a Payment Record which will include:

  


  * Payment Summary:
    * Customer Name
    * Payment Date (default to the current date)
    * Payment Method
    * Payment Total
  * Payment Details (embedded spreadsheet of):
    * ID (can be a Sales Order, Invoice, or approved RMA)
    * Credit Memo ID
    * Balance
    * Payment Amount
  * Other Items:
    * Description
    * Amount
  * Writeoffs:
    * Writeoff Date (default to Payment Date)
    * Writeoff Reason (list of Reasons)
    * Writeoff Amount
  * Notes (formatted text field)



  


Writeoff Reasons: The writeoff reason will be a separate record that has:

  * Name (required)
  * Active (checkbox; default to checked)
  * Type; required; choice of:
    * Decrease Customer Balance (default)
    * Increase Customer Balance



  


Other Notes:

  


  * The Payment Details should show all uninvoiced sales orders with a remaining balance, as well as all invoices with a remaining balance, and all credit memos with an unused balance.



  


  * If the payment is made prior to the invoice creation date, it should be associated with the Sales Order ID and should be considered a customer deposit, not a payment.



  


  * The Sales Order and Invoice should show a Payments Link that shows:
    * Payment Date
    * Sales Order ID
    * Invoice ID
    * Payment Method
    * Payment Amount



  


  * Add a link to Sales Orders, Invoices, and Credit Memos called "Create Payment" that creates a payment linked to the Customer and with a row added for the current Sales Order / Invoice / Credit Memo with the remaining balance amount. The link should be hidden if there's no balance.



  


  * The Payment may be negative in the case of refunds. In this case, simply notate any refund information in the notes.



  


  * Warn against overpayments.



  


Development Specification

Tim Reitz 02/13/2024: The HLD Requirements also included the following. I'm thinking it might be the same as the Payment Details RG mentioned there as well. 

It will have an embedded spreadsheet showing:

  * Sales Order ID or Invoice ID (drop list of all uninvoiced sales orders with a remaining balance, as well as all invoices with a remaining balance)
  * Balance (auto-calculated)
  * Payment Amount


