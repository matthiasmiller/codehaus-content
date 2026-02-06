2\. Incoming Orders

  


Requirements

Orders vs Invoices

We want to number deer separately, but be able to bill them all at once. For this reason, we are tracking orders separately from the invoice. The order is created and processed, then one or more orders are added to an invoice to be billed to the customer.

  


New Customers

New customers will check in at the front counter. We will have at least two laptops to place orders.

  


The employee will type in the customer's name. If the customer doesn't exist, they will create a new customer with a blank order.

  


Otherwise, they will be able to pull up the prior year's orders to see what they got. They do not need to be able to duplicate prior orders. They can just refer to it for reference.

  


Orders and invoices will share product codes for easy entry. These product codes can be easily updated at any time.

  


The order will specify:

  * Order Number (automatic)
  * Order Date (default to today)
  * Customer
  * Workflow (automatically calculated)
  * Received As
    * Bone-in
    * Deboned
  * Items (items with a specified weight will automatically sort to the top)
    * Item (same as invoice sales items)
    * Description (same as invoice sales items)
    * Specified Weight (becomes read-only with calculated weight after deboned weight is entered)
    * Specified %
    * Final Weight
    * Amount
    * Total
    * Package Date
  * Notify Customer Via ("Text Message" or "Phone Call")
    * It will default to blank. It should NOT auto-fill based on prior orders. By asking the customer each time, it allows them to override any prior "stop" via text message.
    * If "Text Message", it will show the cell phone number from the contact, allowing the user to confirm the number with the customer. (If this needs to be changed, you can easily open the contact in another tab, change the phone number, save, then return to the pending order.)
  * Deboned Weight (in pounds) - immediately required for deboned orders
    * Date Weighed (set automatically when weight is filled in)
  * Processed Date
  * Invoice - link to the invoice



  


When the order type is deboned, the workflow will automatically be set to "Processing" and the weight will be required.

  


When the weight is specified, the Items by Percentage will automatically calculate their weight. This is based on the processed weight minus the total "Items by Pound". These weights will be manually adjustable.

  


When the order is saved, it will be printed to a thermal paper on plastic. Two identical copies will be printed: one for the customer and one for LCM. This will include the customer name, order date, order number, and all of the line items. It will NOT include any pricing information, since that can only be determined after it's processed. The tag color will be different based on the Order Type (bone-in vs. deboned).

  


Workflow

The orders will have an automatic workflow and will go through the following process:

  * Deboning - Default status. Requires customer, items, and notification.
  * Processing - Workflow for deboned orders or if a deboned weight is specified.
  * Packaging - Workflow if any items have not been packaged
  * Invoicing - Workflow if the order has not been invoiced
  * Pickup - Workflow if the order has been invoiced but not paid
  * Complete



  


Invoices

The invoice will have a "Scheduled Pickup Date", which will be described later. It will also track contact attempts and followup.

  


Development Specification

Ellis Miller 06/10/2019: I'm proposing we start from the Contact Report and on the Contact record we have a split detail report grouped by "Orders (1 open, 2 closed)". Show "Create Order" link close to the top. The Order report will have a "Create Order". Use a [SaveRecord].

OrdersByContactAndStatus.ndx

  


Should we add a # Orders column in the Contacts report? We could maybe color-code it (blue if open, gray or black if closed). Let's have them drill into the Contacts record to see the orders. If we can avoid cloning the report, charge 1/2 day. If they need actions another 1/2 day. If we clone the report -- it's $500 extra.

Matthias Miller 06/10/2019: I don't think this is necessary

  


  


Ellis Miller 06/10/2019: We still probably want OnCopy expressions that blank out the appropriate fields on an order (e.g. date, status). 1 hour.

  


Matthias Miller 06/10/2019: I will want an RG Row ID -- either autonumber or random ID

  


The record should be read-only if there's an invoice for it. Perhaps create an index for such.

  


  


Matthias Miller 06/12/2019: When modifying weights before packaging, we do not have to worry about the totals adding up or about adjusting any other totals.

  


  


Matthias Miller 06/10/2019: Notes:

  * Contact detail -- 1/2 day
  * Order detail -- 3 days (must be custom DB level)
  * Order workflow macros -- 1 day
  * Order PDF export - 1 day



  


  


  


  


  


Thermal printer -- 

[ ] We need to find a Thermal Printer that works and ties in

[ ] Buy the Kiosk and ship it to them

[ ] We need to link invoices and sales orders

  


Random Notes:

* They don't currently give them customer copies, but that would be really nice. Specced out above.

  


Ellis Miller 06/10/2019: The two RG's are separate. The by Pound specifies items such as steaks and other special cuts. Once these are processed, everything else gets tossed into ground meat or chunks. These can have different flavorings. The customer will specify how to divide this meat by percent (e.g. 50% normal, 25% flavored sausage, 25% extra spicy sausage)
