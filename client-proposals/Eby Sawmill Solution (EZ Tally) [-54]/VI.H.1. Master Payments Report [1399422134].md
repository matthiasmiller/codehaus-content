6.8.1. Master Payments Report

  


Requirements

This is an editable 3-pane report of Payments and related records: 

  * Left pane: Payment records
  * Top right pane: Related Yard Tally records and Tract records 
  * Bottom right pane: Related Pulpwood Load records 



  


Note that this is one base report that is run in multiple different versions and is used for Payments Due reports and the Payments Summary reports, with various columns and filters that are conditional on the selected Payment Type and Payment Status filters.

  


If at some point in the future customizations are desired for either the Payments Due Reports or the Payments Summary Reports, the Master Payments Report might be split into two separate master reports (one for Payments Due and one for Payments Summaries) instead of one. 

  


New payment itemization items (Yard Tallies, Pulpwood Loads, etc.) will be linked automatically to Payment records, and the report will be updated automatically with new and updated Payments (though the user will need to refresh the open report screen to see the changes). 

  


The title of the report will vary based on which version of the report is being displayed (see the corresponding sections of the proposal).

  


Menu Visibility: Users with the View and Edit Financials permission (by virtue of it being on the Financial Menu)

  


Save Type: Instant Save

  


Development Specification

Change Requests: 

  * 


  


Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=223505632](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=223505632)

  


  


  


Ellis Miller 12/22/2022:

[ ] Ask Prompts and subset

[ ] TractsByPurchaseTypeAndOwnerAndTract.ndx -- repeating ndx for PurchaseTypeID + OwnerID + ListNum(TractName) . For filtered list of Landowner contacts, use something like:

SortPipeList(TractsByPurchaseTypeAndOwnerAndTractNdxConcat(<PurchaseTypeID> \+ "...", ListString( Contacts, BinStringToNum( Mid( NdxKey, 4, 4)))

[ ] For filtered list of Tract Names s, it's almost the same except we extract the Tract Name List num from the key.

[ ] Title is vAskPaymentType + " " \+ if Status = "All Paid", "Payment Summary", "Payments Due")

BID: 4 HOURS for this

  


BID: 4 HOURS EXTRA MARGIN
