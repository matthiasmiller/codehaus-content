30.12.1. (MM) Outbound ACH Payments - DOCUMENT

  


Requirements

  * TODO - ETA for InSight to start testing in Test Environment?
  * TODO_JN - Please involve Duane on this conversation on how this works - ie what triggers it, and how do we protect against wrong triggers, and/or two-person sign-off, and/or maximum transaction sizes, etc??
  * Matthias Miller 08/07/2023: TODO - Half done, should have version midweek
  * Matthias Miller 08/14/2023: Update - Josh is 3/4 of the way through it. Storing account numbers w/ permissioning. Currently work is tying it into Vendor Invoices.
  * Matthias Miller 08/21/2023: Done, waiting to test in Live.



  


Each bank account could be linked to an originating account through a third party.

  


Each contact could be linked to a routing and account number through a third party.

  


Each transaction could be paid via ACH if:

  * It still remains in Draft mode (not Posted or Voided)
  * It is linked to a single Contact configured to receive funds
  * It is linked to a single Bank account configured to send funds



  


Multiple attempts to pay the same transaction would ignored.

  


Matthias Miller 09/29/2023: This is Josh's court. I don't think it's going to get documented.

  


Development Specification

TODO_CCI - I'm thinking of driving this off Rubico, although if we run it concurrently, we could still push it through QB for the time being

  


Interesting options/sites:

  * [https://developer.bill.com/](https://developer.bill.com/)
  * [https://dwolla.com](https://dwolla.com)
  * [https://www.agilepayments.com/](https://www.agilepayments.com/)
  * [https://openach.com/](https://openach.com/) (under active development?)



  


They are using this for inbound ACH:

  * [https://ach.icheckgateway.com/](https://ach.icheckgateway.com/)


