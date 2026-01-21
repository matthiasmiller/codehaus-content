8.1.3. Order Cancelations and Changes

Matthias Miller 12/08/2021:

  


  * The more he thinks about it, he wonders if it would be better not to
    * They are currently using General Journal entries, and they've had some success with taht, but he's been something wrong, and it'll work in the short term, but at the end fo the year, looking at the A/R, there's still money that's attached to the customer's name
    * Customer Credit shows as a credit to that customer --



  


  


OLD ----- Cash Sale Cancellation, We could do:

  * Line Item 1 = Building Total
  * Line Item 2 = -Building Total
  * Line Item 3 = Restocking Fee
  * Create Refund for Balance



  


  


Matthias Miller 12/08/2021:

Cash Sale Cancellation, We could:

  * Cancel original invoice, which would unapply the payments
  * Create a new invoice for the restocking fee, and out of the credit, pay that
  * Issue a refund for overpayment



From a syncing standpoint, it creates an audit trail, and it's less likely for something to go wrong from a technical standpoint than the other approach.

  


RTO Sale that is cancelled would work the same way

  * The money should be taken out of the right category



  


We could use a General Journal from Cash/RTO switches.

  


Cash & Canceled

RTO & Canceled

RTO -> Cash

Cash -> RTO

Cash -> Turned into larger building with a restocking fee

  


  


It's often enough that you need procedures, but not so often that it sticks. It's not a deal, as long as the system can automatically generate a report of what was done.

  * If there could be an audit trail of what happened to that invoice.



Would prefer automatic on cancellations as well, but if it becomes a drawn-out process,

  


Prefer automatic if possible, just because it's always up-to-date

  


  


When you sell a building in a cash sale, it goes into "General Income: Building Sales"

When you sell a building in an RTO, collect the intial payment, it goes into a passthrough account, and if they cancel the rent-to-own sale, and switch it to a cash, then have to pull that money out from that account and put it into the "general income: building sales"

  


Invoice for full amount, and appleis the partial payment to the invoice, and once that partial payment is applied, QB shows it as undeposited funds, and they you can manually make the deposit record.

  * It just puts it into Undeposited Funds when you receive a payment
  * The deposit has a debit from Undeposited Funds and a credit to the income account
  * SO WHAT NEEDS to happen, is the income account needs to shift on this deposit.



  


RTO -> The money needs to be taken out of the passthrough account, and apply the restocking fee category, refund the customer portion back to the customer. It all needs to come through the passthrough account, which needs to go back to 0.

  


RTO -> Cash -- There's no restocking fee on that, but the money needs to be debited from the initial payments account and credited to the Building Sales account, or write a check to BEB, and deposit it as a new sale.

  


Cash -> RTO -- It needs to be taken from buildding sales into the passthrough account.

  


  


  


We would also need to handle amending of invoices

  


  


They do have a 60-day cutoff for the sync, so that it's not through thousands of invoices.

  


  


  


\-----

  


Matthias Miller 12/08/2021: they're still having to put the building back in inventory, and it's like an SRB, but it's a trade-in for a buy-back building. This was just an ability to issue a credit if a customer is buying another one to the new sales invoice. They would just buy it back from them, and then pay for it on the new invoice itself.

  


  


\----

  


  


There are various changes that can happen to sales orders: 

  


  


TODO_CH: Tim Reitz 12/02/2021: I think it might be good for Matthias to get on a call with the Jason and Jason's dad to talk through the QB details for this. And it might be good to consult a QB expert to make sure things are

Tim Reitz 12/02/2021: Jason is planning to work on the instructions a bit and send over an update.

TODO_CH: After further discussion, Jason is thinking that it might be better to have the database generate a notification for the admin and a detailed report/printout of what happened with each building, and then someone would make the changes in QB manually. He's concerned about creating a massive mess with the system doing some things and a person doing some things. But he still feels that it would be ideal for it to all happen automatically if that's possible.

Also note that currently the RTO sales numbers are not being handled in the sync (they have to enter them manually), but the Cash sales are synced automatically. This probably is the reason things are so complicated within QB when doing cancelations or making changes to sales.

TODO_TR: This piece can go into a QB section, I think.

  


TODO_TR:

Cancelations: (up to when a building is delivered)

Process:

  * If a lot building:
    * Cancel the Sales Order
    * Put the building back into inventory
  * If a custom building:
    * Cancel the Sales Order



DONE_JM: who can cancel orders?

TODO_TR: Admin, member sp, non-member sp can (use a permission??)

\- If a non-member SP cancels an order, it should require approval by an admin or member SP

  * If the building has not been started, then automatically cancel the Work Order



TODO_TR: the shop foreman should be notified

  * If the building has been started (if a Task has been completed), require a choice of whether to cancel the WO or not.


  * Refund:
    * Generate a canceled SO printout for the customer showing the refund and restocking fee
    * A check is sent to the customer later OR have a command to generate the check right away



  


  


  


Handling cancelations in QB: 

\- when a payment has been applied to an invoice, be able to refund as needed and change the income to the right category

  


TODO: We need a good efficient way to cancel and put it back into stock, then handle the money that's already been paid:

  * portion as a restocking fee that's kept
  * refunding another amount



[ ] If you cancel a sales order, you need to cancel the work order(s) associated with it.

DONE_CH: What would it look like to do this automatically vs. prompt to do it manually? 

TODO_TR: You would need to have an X30 button to cancel a sales order. It would need to exit edit mode to happen

[ ] When it comes to the financial part, you also need to handle it that way as well.

[ ]  Portion as a restocking fee that's kept

[ ]  Refunding another amount

[ ] You need to undo everything in QB.

  * Probably want to push something back into QB



[ ] Think through partial and full credit card refunds

[ ] Same process for cash and RTO cancelations? 

  


TODO_TR:

RTO to Cash: (up to the point it's delivered, it can be changed (after the building has been marked as delivered, the details are between the customer and the RTO company).

  


Sometimes someone starts out on an RTO basis, then they change it to a cash sale. 

Process:

  * Change the Sales Order from RTO Sale to Cash Sale 



DONE_JM: who can make this change? 

Tim Reitz 12/02/2021: admins and member SP (unless the process ends up being very clean and straighforward

  * The RTO section of the Sales Order can be hidden (the RTO Contract can disappear as well)
  * There should be a note in the Building History (or Notes) that the building was changed from RTO to Cash
  * The RTO Down Payment should be changed to a Cash Sale Deposit (this involves QB)
  * 


  


  * RTO Company doesn't buy until it's delivered.



  


TODO_TR:

Cash to RTO: (up to the point it's delivered)

Process:

  * Change the Sales Order from Cash Sale to RTO Sale



DONE_JM: who can make this change? 

Tim Reitz 12/02/2021: admins and member SP (unless the process ends up being very clean and straighforward

  * RTO section would appear and be required
  * There should be a note in the Building History (or Notes) that the building was changed from Cash to RTO
  * 


  


  


Trade-Ins: TODO_TR / TODO_CH: see the "Trade-ins" section of the proposal 

  


  


Change Orders: 

DONE_JM: who can make this change? 

Tim Reitz 12/02/2021: admins and member SP (unless the process ends up being very clean and straighforward

TODO_CH: we would need to think through how to handle situations where a change order reduces the price of the building. 

One question would be whether change orders before delivery are done as line items on the original QB invoice or a separate invoices. 

TODO_TR: I think from AppHosting side, we should allow negative change orders. Then, we just need to figure out how this should work with QB.

  


Note: For Change Order that reduce the price, allow for the Sales Orders of the "Change Order" type to be of a negative amount.  

  


  


See instructions on this doc (but they're not quite right): [https://docs.google.com/document/d/1vyxlpn9tJsg1LlD1CZZsFpP-04auMaSu/edit](https://docs.google.com/document/d/1vyxlpn9tJsg1LlD1CZZsFpP-04auMaSu/edit)
