3.1. Silverloom Settings

  


Requirements

TODO_AP: Ben Reitz 11/14/2025: Compare this spec with the test system and standardize as needed.

  


The Silverloom Settings page, accessed from Advanced | Admin | Silverloom Settings, includes the following custom sections and fields for various configuration settings. It also may include standard sections & fields. 

  


  * Delivery Holidays custom section: 
    * Unlabeled embedded spreadsheet with the following:
      * Columns: 
        * Holiday (date; defaults to the current date)
      * Automatically sorted by: Holiday (most recent at the top)
      * Buttons to add/remove rows:
        * "✚" / "🞭"
      * Shows 10 rows without scrolling
      * Other Notes: 
        * N/A)



  


  * Pricing custom section (located underneath the "Delivery Holidays" section):
    * Setting Fee (number field allowing 2 decimals; used to set the "Setting Fee $" field on the "Order" and "Clipboard Sheet" printouts)
    * Truss Spacers $/pc (number field allowing 2 decimals; used to set the "Truss Spacers" field on the "Clipboard Sheet" printout)



  


Development Specification

Change Requests:

  * Ben Reitz 09/17/2025: [[[IN11586](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11588&)]] - ZTD - Logo / Branding changes
  * Ben Reitz 11/26/2025: [[[IN11979](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11981&)]] - ZTD - Add new "Clipboard Sheet" printout


