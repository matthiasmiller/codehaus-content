8.3. Packing List Printout

  


Requirements

TODO_AP: Ben Reitz 11/14/2025: Standardize the entire printout spec as needed.

  


Purpose/Overview: This is a PDF printout that contains all of the Packing List information from the corresponding Quote or Order record.

  


Printed From: 

  * "Print Standard Packing List" buttons on the Quote or Order record
  * "Print Yard Packing List" buttons on the Quote or Order record



  


File Format/Name:

  * If the record is a Quote record and the PDF is generated from a "Print Standard Packing List" button: "Packing List_Quote <Quote Number> (exported on <Current Date>).pdf"
  * If the record is a Order record and the PDF is generated from a "Print Standard Packing List" button: "Packing List_Order <Order Number> (exported on <Current Date>).pdf"
  * If the record is a Quote record and the PDF is generated from a "Print Yard Packing List" button: "Yard Packing List_Quote <Quote Number> (exported on <Current Date>).pdf"
  * If the record is a Order record and the PDF is generated from a "Print Yard Packing List" button: "Yard Packing List_Order <Order Number> (exported on <Current Date>).pdf"



  


Fields to be Filled: 

  * Truss Packing List Page (visible if the "Truss Order" checkbox is checked on the corresponding record): see corresponding section of this proposal
  * Lumber Packing List Page (visible if the "Lumber Order" checkbox is checked on the corresponding record): see corresponding section of this proposal
  * Metal Packing List Page (visible if the "Metal Order" checkbox is checked on the corresponding record): see corresponding section of this proposal



  


Handling Page Breaks: 

  * Each of the above pages (Truss, Lumber, and Metal) will begin on a new page.
  * Begin breaking a page after 20 rows.



  


Other Notes:

  * Note that the letterhead is displayed at the top of every page of this printout, unless the page is the result of the second bullet point regarding page breaks above.
  * Delivery / Pickup Information (displays the contents of the "Delivery / Pickup Notes" memo on the Order record; displayed just above the "Packaged by: ___" field; only displayed on the last page of each order type)
  * "Packaged By: ______________________________" (always displayed at the bottom of every page)
  * Note that the Yard Packing List always includes the Standard Packing List.



  


Development Specification

Change Requests:

  * Ben Reitz 05/08/2025: [[[IN10787](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10789&)]] - ZTD - Add Yard Packing List Printout (prev. Changes to Lumber Order RG)
  * Ben Reitz 05/08/2025: [[[IN10784](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10786&)]] - ZTD - Printouts - Auto-populate Metal Ft
  * Ben Reitz 09/17/2025: [[[IN11483](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11485&)]] - ZTD - Packing List printouts - Add "Delivery / Pickup Notes" to printout


