3.1. Sales Item

  


Requirements

Overview: This replicates the sales items in QuickBooks.

  


Accessed via: 

  * N/A



  


Sections and Fields: 

  * ID (text)
  * Parent ID (text)
  * Name (text)
  * Active (checkbox)



  


Data Access: 

  * Import Only



  


Other Notes:

  


Development Specification

See [https://developer.intuit.com/app/developer/qbdesktop/docs/api-reference/qbdesktop/itemquery](https://developer.intuit.com/app/developer/qbdesktop/docs/api-reference/qbdesktop/itemquery)

  


Per conversation with the client, Description is not required.

TODO_MM: Tim Reitz 04/28/2022: I think we should double-check. There are some of the items that seem pretty unclear with just the Name (see [https://docs.google.com/spreadsheets/d/12olKDUC8e6AkeGGBN_27R5p3X0z6DvKX/edit#gid=741872649](https://docs.google.com/spreadsheets/d/12olKDUC8e6AkeGGBN_27R5p3X0z6DvKX/edit#gid=741872649)).

Tim Reitz 05/04/2022: Update: It does seem like we should sync the Description (see [https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-5226&State=ISwSvCyE0ts&](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-5226&State=ISwSvCyE0ts&))
