1\. ** PM PLAN **

Duane and Matthias Design

  


Seth Miller 12/16/2025: TODO_IDD: dropping this here. It was in the bills section and didn't fit in :)

Duane Burkholder 11/05/2025: TODO_MM: your question leads me to think you are referring to if someone has more than one contract and the refund from one would be moved to paying something in their other.

  


My first thought on this is that inside the software we need to process it out the refund as if we were sending the money back to the customer. If it is going to be brought back in on the management side again we may have some type of "paid type" denoting that and then you would process it in on their account with some note of that. Would it be nice to have some fancy linking to do that, maybe but I suspect this is a very significant outlier that we will wait for demand from clients for it.

  


  


Niccolas Miller 01/15/2026: TODO_NM: How do we get the financial account when paying a bill by check? In the parallel ZFP example, vendor invoices have a Payment Account field which is copied across to the check. However, an Ownly Bill can have multiple fin accts (one financial account per itemization line).

  


Matthias Miller 01/19/2026: 

  * Accounting Company
    * Accounts Payable account (I think this is already a standard field IIRC)
    * RG to Map from:
      * Asset Type -> Asset Financial Account (should be an asset type)
    * Product Premium - Expense account



  


  * Accounting Impact
    * Bill
      * Dr 
        * Product Expense - custom financial account field
        * Product Purchase - map from accounting company
        * Product Premium - see field
        * Other - custom financial account field
      * Cr Accounts Payable
    * Check
      * Dr Accounts Payable
      * Cr Primary Checking - OR - more likely, a bank account field that is only available when accounting is enabled, but defaults to the default bank account on the accounting company


