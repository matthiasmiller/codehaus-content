13.6. Reporting for Handwritten SO ID

TODO_MM

  * Add field
  * No search for now
  * Add Mark's notes here



  


AR Process: Add Field for Handwritten Sales Order Number

  


One thing that I failed to mention on the AR process is that we want to build so you can add a secondary Sales Order Number.

  


  * The use case for this is when you have a customer write out a check, referencing the manually created Sales Order number. When applying this payment you will need the ability to search by the secondary Sales Order number.
  * For example:
    * John Doe walks into ST and buys 5 pcs. OSB.
    * ST creates a handwritten SO with a number of 5214.
    * John Doe writes out a check and references 5214.
    * BurMan recreates this Sales Order in ASSIST with an auto generated SO number of 23092496. At the same time BurMan also enters the secondary invoice number of 5214, for future reference.
    * The check is entered on a Received Payment form and sent to BurMan to be entered as Undeposited Funds. When applying this payment BurMan can now search by either 23092496 or 5214.


