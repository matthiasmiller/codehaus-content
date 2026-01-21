6\. Workflow: Invoicing

  


Requirements

Once the entire order has been packaged, it will show up in a Ready to Invoice report. The left side will show a list of all the customers with orders that are complete and ready to be invoiced. When you select a customer, you will see a list of the orders on the right.

  


This view will have a button called "Create Invoices" that will create invoices for all customers displayed there.

  


Each order will be assigned to a separate invoice. We will have an option to print statements. The statement will be a PDF with all unpaid invoices, along with a cover sheet of the unpaid invoices, their remaining balances, and the total balance.

  


Development Specification

Future Upsell -- Could do a voice message to people for people with landlines...but this might not be a big deal, either.

  


Matthias Miller 06/10/2019: 

  * CCI - 3 days
    * Display Multi-Pane Report
    * r20 to feed x30
    * x30 itself
    * Adding Order # to Invoice RG



  


Ellis Miller 06/10/2019: What if a customer has one complete and one incomplete order? Do we want to wait to invoice until all orders are complete? Two examples:

  * Customer brings two deer on the same day. We definitely want to invoice them together if they are ready 2 hours apart.
  * Customer brings in one deer on Monday and another on Thursday. On Friday when first deer is ready, should we go ahead and invoice that one separately?



Perhaps we need columns for # Orders Ready and # Orders Processing.

  


How do we populate the Invoices from the Orders? Do we copy all line items across? Do we tie it out to specific orders in any way? Do orders become readonly once packaged or once invoiced?

Matthias Miller 06/10/2019: Copy across, then make the order read-only. You have to cancel the invoice if you need to adjust the order for any reason.

  


I think we store the Order # on the invoice -- this is easier than storing the Invoice # on the Order. I think we can have an Order # field in the RG.

Matthias Miller 06/10/2019: Sounds right.
