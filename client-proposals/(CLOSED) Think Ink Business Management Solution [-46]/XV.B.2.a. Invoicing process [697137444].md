15.2.2.1. Invoicing process

  


Requirements

TODO_NM: Tim Reitz 08/12/2022: We had 2 sections for Invoicing process. We need review and clean up.

  


  


#1:

Invoicing could be done in a few ways:

  * Batch invoicing all uninvoiced fees in the database (page counts, base charges) (via a "Create Invoices for Billing Period" menu option)
  * Batch invoicing all uninvoiced fees for a specific customer (via a "Create Invoice for Fees" button on the customer's Contact page)
  * Creating an individual blank invoice and manually setting the customer, line items, etc. (via a "New Invoice" menu option)



TODO_CH: good with this? would be similar to ZWA (manually-triggered batch + individual option) What do we need to spec out here? 

Matthias Miller 05/19/2022: Yes. Underling approach:

  * Have an x30 to create these, that prompts for customer (blank = all).
  * Note that Option 3 would not be tied out to a device, billing, etc -- correct?



  


The invoicing process is as follows:

TODO_TR

  


  


TODO_TR: handle Email and Print separately

TODO_JM: need more details here

  


DONE_JM: how should invoices be marked Paid?

\- Manual only? 

\- Automatic only? 

\- Automatic & manual? 

Tim Reitz 04/20/2022: Sending an email today. 

Tim Reitz 04/21/2022: TODO_TR: from the client: 

4\. How would you like to have the invoices be marked as Paid? We could do manual only, which would require each one to be done individually (either by opening each invoice or by having an editable report of all invoices that you could go through). We could also do it automatically if there's some criteria for triggering that. I think it should happen at the point a payment is processed. I am also wondering if we shouldn’t just stick to manual processing these payments from a saved card. We are going to need to check these auto calculated invoices to make sure everything is accurate first anyhow. If we could at that point process the payment that would make sense to me.

  


TODO_CH: Prorate for partial months/quarters (see notes about rounding down to the nearest 1/4 of a month.

  


  


\----------------

#2

Invoicing Process

  * Automatic page counts will be imported through the API or through a CSV import.
  * For manual page counts:
    * Generate an instruction sheet for each MPS+Billing Group that lists the devices and instructions.
    * Have responses sent to the ticketing system
    * Hand-enter these using the Page Count Entry view
    * Send reminders every X days, as configured
  * Once invoices are reviewed, they will be synced across to Classic Accounting.



  


TODO_JM: Pre-pay discount

  


Development Specification

Mockups: N/A (just add the menu options) 

DONE_AP: you can just make sure that the corresponding menu options. Thanks

  


  


Dev Specs for #2: 

HL Est: 40 Hours

  * X30 for automatic page counts: 8 Hours
  * Email Template to send instructions: 12 hours
  * Reminder (just scheduled task)
  * Review process (TODO_DD: What is this)
  * R20 Export to Classic Accounting: 8 hours


