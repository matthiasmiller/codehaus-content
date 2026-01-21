9.4. Work Order Printout

  


Requirements

TODO_TR: spec out from copy that Jason sent [https://mail.google.com/mail/u/0/#inbox/FMfcgzGlkZBZMXwRXvHCDRfTFPMhKQrS?projector=1&messagePartId=0.1](https://mail.google.com/mail/u/0/#inbox/FMfcgzGlkZBZMXwRXvHCDRfTFPMhKQrS?projector=1&messagePartId=0.1)

  


DONE_CH: they currently have 2 separate printouts for WOs - one for the shop and one for the office. Right that we should combine these into one, and simply hide data for the shop one? See the office printout here:  [https://mail.google.com/mail/u/0/#search/label%3Ac.-design-phase-bald-eagle-barns+work+order/FMfcgzGkXdCSHdPxHvtnvRQSFmmChMXr?projector=1&messagePartId=0.1](https://mail.google.com/mail/u/0/#search/label%3Ac.-design-phase-bald-eagle-barns+work+order/FMfcgzGkXdCSHdPxHvtnvRQSFmmChMXr?projector=1&messagePartId=0.1)

DONE_JM: Can we use the same printout, but just hide some things for the shop?

TODO_TR: if separate, have a separate section of the proposal.

TODO_TR: It will be less expensive if we can have the exact same template. but just hide prices. If it varies too much between the two, we might as well have two separate templates.

TODO_TR / TODO_CH: Jason said they only need one - and the printout for the shop can serve the purpose. 

We do NOT need price info on this printout. 

  


  


Purpose: 

  


Printed From: 

  


File Format: PDF

  


Fields to be Filled: [ones marked with * are not for shop]

  * Work Order Date (
  * Delivery Date (
  * Work Order Type (
  * Building Category (pulled from ___



DONE_CH: would we need to have this on the WO record? 

TODO_TR: This can come from anywhere. The WO is tied to a building. Note that this is a spec for the PRINTOUT, not the record itself.

  * Customer (pulled from the Contact on the WO; displays first and last name, address, phone, email, fax; "Stock Order" for lot buildings)
  * Ship To (pulled from the Destination on the WO; displays address and/or coordinates, as applicable; blank for lot buildings)
  * Salesperson (name, FirstName LastName format; blank for lot buildings) 
  * Serial # (
  * Size (width X length) 
  * Style (style name) 
  * Siding Color 
  * Trim Color 
  * Roof Color 
  * Options (table of the following:) 
    * Item
    * Code
    * UOM 
    * Qty 
    * Unit Price 



  


  * Layout (image of building layout diagram; pulled from ___ DONE_CH: how would we do this, since it's linked to the Building record, not the WO record? TODO_TR: No problem, since the WO is tied to a building.
  * Notes (pulled from the Notes field on the WO) 
  * Delivery Notes (for Haul Requests, pulled from Delivery Notes field; blank for other WO Types) 



  


Template: 

  


Sample(s): 

  


Other Notes:

  


Development Specification

TODO_CCI: The top part/header probably would be very much like what we did for the ZTD Quote/Order and Packing List printouts. This would include the details for the WO, Salesperson, Customer, Ship To.
