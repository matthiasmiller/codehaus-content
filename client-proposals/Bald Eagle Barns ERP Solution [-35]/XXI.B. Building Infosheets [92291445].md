21.2. Building Infosheets

  


Requirements

When a building is completed, BEB prints out an Infosheet (currently generated off of the Work Order) for that building and physically posts in the building. This is normally printed by the roofer or the shop manager when the final inspection is done. 

  


Purpose: When a building in on the lot, the customers can go from building to building and see the building details on the Infosheets. The salesman can also reference it in the sales process. This can also be helpful for documenting finished goods inventory. 

  


These Infosheets tend to be pulled out of the buildings pretty often, so there should be a way to reprint these 

  


Printed from: 

  * Building Record 
  * New Building Work Order? 
  * Finished Goods Inventory Report



  


File Format: PDF 

  


Fields to be Filled:

  * Building Image (
  * Style - need to note there accordingly; see files from Jason) 
  * Building Size (
  * Building Color (
  * Trim Color ( 
  * Roof Color (
  * S/N (
  * Base Price (
  * Added Options (from ___; allow for up to __ rows of options without adding another page) 
    * TODO_JM
  * 36 Month RTO 
    * Monthly Payment (
    * Security Deposit (
    * Sub Total Initial Payment (
  * 48 Month RTO 
    * Monthly Payment (
    * Security Deposit (
    * Sub Total Initial Payment (
  * Copyright year (filled from the Year of the building's Serial Number)



  


  


Template: [[File:Info Sheet Template (filled items highlighted).pdf]] 

  


Sample(s): See Dev Specs

  


  


Tim Reitz 10/06/2021: Note that Jason said that "Infosheets" (one word) is fine, but that he doesn't have a preference between "Info Sheets" and "Infosheets". We should settle on one.

  


Development Specification

TODO_CCI: What's the best way to handle the building image?

  * We could put the entire image into a memo, if we get good enough quality.
  * We could use file attachments, then use ArchivedDocumentImage. Not sure how that helps quality.
  * We could have a series of templates, then use something like InsertRTF
  * We could put all the images into the template, and use an IncludeIf for each one.



  


  


Link to Drive folder with the separate templates: TODO_TR 

  


  


Tim Reitz 10/01/2021: Samples: 

  * Barn Cabin [[File:BC (Barn Cabin) Info Sheet.pdf]] 
  * High Barn [[File:HB (High Barn) Info Sheet.pdf]] 
  * Workshop [[File:Workshop Info Sheet.pdf]]


