26.3. Accounts Payable Scratchpad

  * Move GL Override from the VI to the SKU



  


  


  * Create an invoice -- with a status of "WAITING ON GL ACCOUNT" \-- and it doesn't hit accoutning until it's assigned to it, then at that point, 



  


  


  


Once 

  


Current:

  * Kanban Card
  * Negotiated
  * Prenegotiated
  * 


  


  


TODO_HLD - consider moving SKUs to a SKU Linking

  


  


  


Marketing bill gets split between 2-3 GL accounts:

\- This is done at the PO level

\- Three PO's tied to the same GL account

- 

  


  


Receipt

When you receive item, it increases your inventory

And even if you haven't paid for it, it hits your A/P until you pay for it -- as soon as you as you receive it, it turns into an outstanding invoice

  


No redefining of it until they're liable for it as an asset

  * Need to report on the District Manager



  


  


  * SKU needs to define:
    * Balance Sheet Account
    * Income Statement Account
  * VI needs to define
    * Override for Class
    * Override for Balance Sheet Account
    * Override for Income Statement Account



  


When a PO has a "COMPLETE" status (can be manual or by a shop sending back in the PO Confirmation) -- at that point, we would drop it into the Default GL accounts for the SKU items in the purchase order. That lives there, until Vendor Invoice is assigned, ends up in the verification report, and it g

  


District - determined by Bill To

  


We need to make the PAID process for Vendor Invoice that's a bit more strict, to make sure that this is a little ore "defined" process. Currently it's just a drop list STATUS of PAID, which is too easy to change. We need a verified process for paid vendor invoice.

  


Classes

  * 


  


\--

  


  * PO - Hits Balance Sheet When It's Received
    * Other than prepaid items, the only ones to hit the balance sheet would be a subcategory of Raw Materials or Production Overhead or Production Labor
  * PO - Prepayment - (see Vendor Invoice)



  


  


  


  * Credit



  


  * Split 2 gallons of paint w/ separate categories into separate POs's



  


  * Default GL account assigned at the SKU level, which is carried over ito the VI record, where that can be overridden
  * Josh is coming up with a way to automatically create backorders.



  


  


TODO:

  * What should happen with current GL accounts? Do they get tied out to Accounting Accounts?
    * Matthias Miller 11/07/2022: When they started looking at it, they said they need a structured list of GL accounts, and -- the source of truth or the list of accounts, should all be stored in the GL, and if thye want to add a new account, then it needs to be added to the accounting system, and IMS follows suit.
    * TODO - we need to map these over to Chart of Accounts
  * TODO - will need class assignments
  * Prepayments Tied to PO
  * TODO - Can auto-populate the pre-set to what the vendor is...
    * Remove SKU reqiurement for the PO
    * Move GL acount from VI to the PO
    * in the short-term, create a SKU for every Class+GL account combination.
    * 


  


  * Purchase Order Entered
    * Nothing happened to the financials
    * Put in ETA / cost etc
  * Vendor Invoice Received



  


  


Current Process:

  * Shop sees they've entered reorder level
  * Shop scans kanban card, and goes into assist
  * Assist creates purchase order and sends to vendor
  * Vendor looks at it, responds to it with an ETA
  * This sends an order confirmation to the shop
  * The vendor delivers it
  * The shop marks it as recevied as ordered
  * Assist creates a SKU Lot w/ order adjustment



  


A/P side

  * Knows that PO has been received, and gets the invoice from vendor -- and if it matches the purchase order, then she marks invoice as "confirmed receipt + price"
  * Gets sent to distract manager once a week as a double-check, then marks which invoices he wants to pay
  * This gets updated in Assist, and sees the invoices that have been approved and pays them



  


Everything based on invoice:

  * Any payment before delivery goes to prepayment
  * Delivery adjusts raw materials
  * Payment after delivery gets moved into 



  


  


>>>>>>>>>>

  * May be prepaid in part
  * May be postpaid entirely



  


  


Three accounts at play:

  * Prepayments
  * Raw Materials
  * Checking (or could be paid out of other asset accounts)



Sometimes paid with multiple payments

  


  


<<<<<<<<<<<<<<<<<<<<<

  


  * On a vendor invoice, you can create any number of transactions for prepayments. (Technical details -- need to indentify as prepayments, but...so far so good.)
    * 


  


  * When inventory is received:
    * Creates adjustments for inventory
    * This when it gets tied out to A/P
    * This creates a bill, but we need a way to prevent bills from being paid



  


JUST FIX IT queue ->>> How do we update accounting?

>>> Basically just reverse the prior adjustment, make edits, then reprocess it to reapply the changes

  


  * If the invoice amount is too high/low, it's a "



  


  * Create a Bill when it is completed
    * Automatically created and linked back to Vendor Invoices



  


Option to view open purchase orders

  


  


Matthias Miller 12/05/2022: 

  * Review Vendor Invoice (coming to the builder?)
    * If paid by the accountant:


