5.4.1. Tally Info Section

  


Requirements

Tally Info section:

  * Status (auto-set and read-only; Open, Confirmed, Closed; see explanation in Other Notes below)
  * Yard Tally ID (auto-numbered and sequential, starting at 400001; read-only; unique identifier) 
  * Source (required; drop list of Vendor, Tract; editable if Status = Open)
  * Tract (visible and required if Source = Tract; list of Tract records with Status of Harvest Started; editable if Yard Tally Status = Open; cleared on Save if Source is changed to Vendor) 
  * Landowner(s) (visible if Source = Tract; auto-filled and read-only based on selected Tract; comma-separated list; cleared on Save if Source is changed to Vendor)
  * Logger (visible and required if Source = Tract; drop list of Logger Contacts from the selected Tract; if there is only one Logger, default to that; editable if Status = Open; cleared immediately if Tract is changed; cleared on Save if Source is changed to Vendor)
  * Vendor (visible and required if Source = Vendor; drop list of active Vendor Contacts; editable if Status = Open; cleared on Save if Source is changed to Tract) 
  * Eby Freight (visible and required if Source = Vendor; drop list of Yes, No; default to blank; editable if Status = Open; cleared on Save if Source is changed to Tract) 
  * Load Comments (multi-line plain text; for leaving general notes about the load/tally)



  


Other Notes: 

  * Yard Tally Status:
    * "Open": if the Confirmed checkbox is not filled
    * "Confirmed": if the Confirmed checkbox is filled
    * "Closed": based on Source and other criteria:
      * Source = Vendor: "Closed" if Confirmed and marked Paid to the Vendor
      * Source = %-based Tract: "Closed" if Confirmed and marked Paid to the Logger and to the Landowner
      * Source = Flat payment Tract: "Closed" if Confirmed and marked Paid to the Logger



  


Development Specification

Ellis Miller 01/03/2023: 

[ ] Talk to me about how to start a high number for the tally ID's.

  


[ ] Add basic screen

[ ] Landowners is just a concatRG macro

[ ] Status macro

BID: 2 HOUR
