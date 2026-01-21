12.1. Payment Record

  


Requirements

The Customer Payment Records are used to track payments from and refunds back to customers.

  


  


DONE_CH: Tim Reitz 10/26/2021: It sounds like there are 2 payment record types in their current system: Payments (paid out to others) and Receipts (paid to them). We probably can sync data over from this and combine it into one??.

TODO_TR: I prefer their distinction, since it maps differently in QB.

  


This could track

  * Customer payments
  * Referrals payments
  * Payments between entities (Transit, Benchmark, BEB, RR)
  * Payments for completed tasks
  * Salesperson commission
  * Dealer commission
  * Driver %



  


TODO_TR / J: How/where are Payments created/initiated?

Tim Reitz 08/10/2021: from call with Jason today: When the customer is ready to buy, convert the quote to a Sales Order, then the deposit is due. We should be able to create the payment from the SO.

  


Report: Sales Orders without Payments

Weekly email notification

who should get it? (Sales Manager, Bookkeeper, __)

There are some customers who don't pay right away (schools, etc.). The user can weed those out visually.

  


  


This record would have the following sections, fields, and options:

  * Customer (auto-filled and read-only? 
  * Amount (required; number field to 2 decimal places)
  * Payment Date (required; defaults to "today")
  * Payment Type (required; drop list of the following:)
    * Check
    * Cash
    * Purchase Order
    * Credit Card
  * Check # (visible and required if Payment Type = Check)
  * Purchase Order # (visible and required if Payment Type = Purchase Order) 
  * Process Now (link; visible if Payment Type = Credit Card; opens a new tab to collect credit card information and process the charge)
  * Notes (plain text field; optional)
  * Sales Orders (RG)
    * Sales Order # (drop list of all SOs for the customer)



DONE_CH: would the salesperson be able to change the SO # from one to another here? (in the event that a customer would cancel a building and want to apply their payment to a different building) 

TODO_TR: Yes

  * Date (read-only; auto-filled from Date above)
  * Orig. Amt (read-only; auto-filled from SO)
  * Amt. Due (read-only; auto-filled from SO)
  * Payment (required; defaults to blank; editable; number field to 2 decimal places)


  * Invoice # (synced back from QB) 
  * QB Sync ID (hidden text field) 
  * Refunds (embedded spreadsheet: 
    * Sales Order # (list of SO's in the itemization RG)
    * Requested Date (required; default to "Today") 
    * Refund Amount (required; sum of refund amounts cannot excede the Payment amount)
    * Notes (memo OR text field to document the reason fro the refund) 
    * Completed Date (auto-fill and read-only) 
    * 


DONE_CH: Tim Reitz 10/08/2021: Most times they do a refund, it's processed as a discount because the customer hasn't paid in full yet. 

However, in the event that the customer has paid in full, they do a refund. It IS possible to have multiple separate refunds. 

So where does that leave us with RG vs. record for refunds? 

TODO_TR: We just leave it as is with an RG

  


DONE_CH: Restocking fees: If a customer cancels a whole building, there is a 5% restocking fee. BEB has already applied the 10% deposit to the General Building Income - Building Sales in QB. When the building is canceled, 5% of original building price is regategorized as General Building Income - Restocking Fee. The rest of the deposit goes back to the customer as an expense. BUT Jason needs to rethink

How should this be handled in AHZ? In the QB sync? 

TODO_TR: When you cancel, zero out the base building price and all the items, add a Restocking Fee option tied to a SKU and special QB expense account. For the QB sync, we'd simply need to make sure these ledger entries reflect the current SO.

  


See the Credit Card Payments Integration section of this proposal for more details about that feature.

  


The system will not support discounts on sales/payments. All discounts should be applied to the Sales Order prior to collecting payment. 

  


If a customer buys multiple buildings, they might pay with one check, but it will be marked as payment in full for all of the buildings.

  


  


Handling payments for sales made by independent dealers:

  * For cash, the dealer will turn it in.
  * If the customer pays with check, the dealer will send it in with the completed work order
  * If they pay with credit card, they currently call in and process it over the phone.



TODO_J: does this mean that dealers do or don't need to be able to create payments in the database? 

Tim Reitz 08/10/2021: Jason would like for the dealers to be able to create the payments. This would be handy with the card payment integration. 

  


TODO: Think about links on the menu, on the customer, on the order

  


TODO: Should there be a quick way to receive payment from a sales order?

  


TODO_J: It looks like we can accept payment for more than what is due. Do we need to continue to do this?

Tim Reitz 08/10/2021: Jason said that they actually can't do this. And he doesn't want to be able to do it. 

  


TODO_J: What amount do they collect on down payment?

Tim Reitz 08/10/2021: This is up to the Salesperson & customer. Policy is 10%. Doesn't need to be hardcoded.  

  


TODO_J: How do down payments work with dealer lots that need approval?

Tim Reitz 08/10/2021: same as above. 

  


TODO_J: Do customer payments get entered only in the database?

Tim Reitz 08/10/2021: Only entered in the database and then are synced to QB

  


Development Specification

Demo Walkthrough - 16:24
