1.5. Settlement Record (mid jan?)

Seth Miller 01/08/2026: TODO_IDD: design please.

  


Matthias Miller 10/24/2025: TODO_SETH - Is there a world in which a settlement record is a special kind of deposit?

  


Matthias Miller 12/16/2025: Proposal:

  * Proposal: Pull in Clearant settlement information into special Clearant records, THEN decide where things go from there.
  * 


  


  * Merchant Processing (CC + ACH) - TODO_JB
    * List
      * Merchant Processor
        * Xplor Pay
        * iCheckGateway
        * Also needs to be stored on the payment record



  


  * Clearent / xplor-pay
  * Problems with Assist
    * We need to store user-identifiable payment methods (tokenized)
      * On the customer, RG of:
        * Desc (i.e. "VISA x1234 exp 12/45")
        * Merchant Processor
        * Hidden Token
        * Primary checkbox (sorts to the top, only 1 allowed)
        * Fielded expiration date (?)
        * Method - CC/ACH (if needed)
    * Declines w/ no clear message
      * was it a credit card issue?
      * what type of issue? bad CVV? bad address? NSF?
      * was it a Silverloom issue?
      * How will we handle fallbacks if we fail to import / record a payment
        * ideas - could first past x30 contents to an s3 sweep bucket so we save results
        * \-- have a process to import + archive items from the s3 bucket
        * daily / hourly sync
    * Need to be able to refund from the software
  * Settlement record
    * RTO Company
    * Settlement Date
    * need linking for
      * transaction
      * fee
    * need a way to model refunds in settlements
    * can be polled nightly
  * First Iteration
    * Full Refund on Single Payment
      * Refund Type on Payment Rows
      * Refund Transaction ID on Payment Record (?)



  


  


  


DONE_IDD

Jonathan Bergen 08/26/2025: Should we store the processing fee on the payment record? This would only be applicable to ACH and CC payments. We'll come back to this after 

We need a record transaction ID: ie. StripeTransactionID.

  


Matthias Miller 12/16/2025: TODO_JB: This depends how they think about it

  


  


Matthias Miller 10/24/2025: TODO: This (deposits) could be used for settlements/payouts from merchant processors. The main thing we need is to have a Fee column (depending how XplorPay does fees) so that we can account for credit card fees withheld from deposit.
