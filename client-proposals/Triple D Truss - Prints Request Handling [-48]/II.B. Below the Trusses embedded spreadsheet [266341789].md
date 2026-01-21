2.2. Below the Trusses embedded spreadsheet

  * Pending Truss Print Request: 
    * This would be an editable memo below the left side of the Trusses embedded spreadsheet. 
    * The default Pending Truss Print Request memo will be set up in AppHosting Settings 
    * It would include:
      * A table with the following:  
        * Facecut: 
        * Heel: 
        * Bearing: 
        * Wind Speed: 
        * Uplift: 
      * Drawings and Notes: (space for notes and attachments)
      * Note that since this is a memo, there would not be validation on these items. The user could essentially enter any text for them. On the request & preview, there should be space for at least 25 characters for the items from the table. 



  


  * View/Edit Sketch (link below the Pending Request memo) 
    * Clicking this link would open the Sketch in a new tab (see corresponding section of this proposal)



  


  * Truss Request Preview: This would be a read-only preview that shows all information that will be included in the request
    * Quote/Order #: (auto-fill lfrom order)
    * Salesperson: (auto-fill from order; FirstName LastName format)
    * Span: (auto-fill from order)
    * Pitch: (auto-fill from order; should have enough space for a long dual pitch)
    * Spacing: (auto-fill from order) 
    * Attic Loading: (auto-fill from order) 
    * Description: (formerly "Style" on the old sheet; auto-fill from the item Description field)
    * End Condition:
      * L OH: (auto-fill from item) 
      * R OH: (auto-fill from item) 
      * L Cant: (auto-fill from item) 
      * R Cant: (auto-fill from item) 
    * Facecut: (auto-fill from Pending Truss Print Request memo)
    * Heel: (auto-fill from Pending Truss Print Request memo)
    * Bearing: (auto-fill from Pending Truss Print Request memo)
    * Wind Speed: (auto-fill from Pending Truss Print Request memo)
    * Uplift: (auto-fill from Pending Truss Print Request memo) 
    * Loadings: 
      * "Ag" OR "Res/Com" (auto-fill from order)
      * GSL: (auto-fill from order)
      * TCLL: (auto-fill from order)
      * TCDL: (auto-fill from order)
      * BCDL: (auto-fill from order)
    * Drawings and Notes: (auto-fill from Pending Truss Print Request memo)
    * View/Edit Sketch (link; auto-fill from Pending Truss Print Request memo)
    * Completed (checkbox; for the designer's use) 



  


  * Generate Request (editable macro/checkbox below the View/Edit Sketch link and the Pending Request memo; default to cleared) 
    * Filling this checkbox would do the following: 
      * move any existing Truss Print for the selected row into History 
      * move any existing Print Request for the selected row into History 
      * clear the completed date on the request (if set from a previous print) 
      * set the Truss Print Request Date to Today
      * move the Request Preview into the Truss Request 
      * increment the Truss Print Pending Revision # to be used by the next upcoming request 
      * hide the Pending Truss Print for the current row
    * This checkbox would clear and disappear after it's been filled.


