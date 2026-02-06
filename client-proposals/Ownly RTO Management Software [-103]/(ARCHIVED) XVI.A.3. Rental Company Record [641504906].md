16.0.3. Rental Company Record

Seth Miller 08/01/2025: Rental companies are now a contact type. I moved the important details to the contact spec

  


______________________________________________________________________________

Overview: The Rental Company record is a simple custom record, and is used to track Rental Companies.

 

Accessed via: Settings | Configuration | Configure Rental Companies

  


Sections and Fields: 

  * Rental Company section:
    * Name (required; plain text; validate against duplicates)
    * Active (checkbox)
  * Credit Card Convenience Fees Matthias Miller 07/24/2025: DO NOT IMPLEMENT YET. Most likely this will be enabled via a system update AFTER Duane has received a signed contract from the customer that they assume liability for the feature.
    * Label: Some states limit fees to a specific percentage, a specific dollar amount, and/or actual merchant costs of process the transaction.
      * Matthias Miller 07/23/2025: TODO_DB - please come up with the scary legal verbiage
      * Matthias Miller 07/24/2025: TODO_DB - Please talk with LeAnn or legal counsel about the direction we want/need to take with this.



  


  * I accept the above terms and would like to enable credit card convenience fees. (checkbox)



  


  * Payment Method (could be shipped records that can be turned on via a system update)
    * Credit Card
    * Debit Card
    * Prepaid Card
    * Check
    * Cash
    * Other



  


  * States (embedded spreadsheet)
    * State (list of states)
    * Payment Method (list of Payment Method)
    * Fee Type (list of "Dollar Amount" or "Percentage")
    * Fee (editable macro for Fee $ when using Dollar Amount; otherwise, editable macro for Fee %; required)
    * Maximum (editable macro for Fee % when using Dollar Amount; otherwise, editable macro for Fee $)
    * Maximum Fee $ (hidden field; 2 decimals)
    * Maximum Fee % (hidden field; 2 decimals)



  


Sean Miller 07/24/2025: TODO_DB / TODO_MM: Convenience Fees: nail down ACH convenience fees

  


Sean Miller 07/24/2025: TODO_DB / TODO_MM: Handle NSFs

  


  


NOTE:

  * If a state limits the convenience fee by 1%, you cannot charge more than $10 for a $1000 payment. Thus, the total payment would be $1010.



  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

TODO_PERMISSIONS: Document based on Permission, rather than User Groups. 

  


Special Considerations: TODO_PERMISSIONS: 

  * Copy Record: __ (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: __ (think: allow deletion? under what circumstances?)
  * Merge Record: __ (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


MERCHANT FEE CAPS FOR CONVENIENCE FEES:

  * We could eventually consider getting more sophisticated when it comes to Stripe Payments but it's not necessary so we wont. We would add these fields.
    * Merchant Fee %
    * Merchant Transaction $
  * Note that when calculating the convenience fee of a transaction, you need to account for the convience fee of the overall transaction. For example, to calculate the total payment when using Stripe, you need to use this:
    * Charge Amount = (Target Amount + 0.30) / (1 - 0.029)
    * i.e. To net a $1000, you need a $29.59 convenience fee, charging a total of 1,029.59.



  


Matthias Miller 07/30/2025: TODO_PERMISSIONS:

  * Who can create/edit Rental Companies?
    * Administrator-level permission


