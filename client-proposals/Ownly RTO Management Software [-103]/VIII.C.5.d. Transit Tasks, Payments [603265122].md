8.3.4.4. Transit Tasks, Payments

TODO_HLD - Add a way to look for completed retrieval tasks that require to close contracts

  


TODO_SETH: We can look at ZFP's transit tasks for inspiration

Seth Miller 01/27/2026: TODO_SETH. Spec and delegate [[PC0189389]]

  


Transit Roles list:

  * Escort
  * Assistant
  * do not allow adding items 



  


TransitTags list; user-editable but ships with:

  * HOLD
  * ASAP
  * DELAY



  


TransitStatuses; investortools-owned

  * Unscheduled
  * Scheduled
  * Complete



  


Contact:

  * Disallow multiple address of the same type
  * If there's a transit task attached, make sure there is EITHER 1 row in the address RG or a Physical address



  


RTO Company

  * Minimum Payment % to Stop Retrieval (number; 2 decimals)
  * RG of Haulers (list of active hauler type contacts)



  


Contact Type:

  * Hauler
  * Does NOT map to RTO Company



  


Transit Task

  * RTO Company
  * Asset (via drop list like elsewhere)
  * Request Date (macro for creation date)
  * Canceled (checkbox)
  * Status; use logic in the following order
    * Completed (if any of the rows are complete)
    * Scheduled (requires schedule date, assignee, and confirmation but NOT attempted/complete)
    * Unscheduled (no incomplete schedule date)
  * Tags (multi-select list with underlying RG of TransitTags)



  


  * Type
    * Building Move
    * Delivery
    * Lot Haul
    * Retrieval
    * Day Off
    * Maintenance
    * Repair
    * Site Check
    * NOTE: We are going to need a way to track which ones move the building (i.e. the top 4). Up to you how you model it.
  * Minimum Payment to Stop Retrieval (number; 2 decimals; visible for retrievals; calculated based on RTO Company settings)
  * Override checkbox (makes the above editable, presumably with a stored underlying field)



  


  * Start Location
    * Contact (list that includes Rental Company, Manufacturer, Primary & Secondary Customer for all contracts linked to the contract, Salesperson)
    * Show All (Detail Variable checkbox; expands the Contact list to everyone linked to the RTO Company)
    * Address (lookup Physical address if specified; first row if there's only 1)
    * Phone Numbers (show all phone numbers & types; click to call)
    * Primary Email (click to email)
  * End Location
    * Same as start location



  


  * Google Maps URL
    * Use EncodeURL to embed {Origin} & {destination} address [https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode=driving&](https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode=driving&)



  


  * Attachments (S3 RG)



  


  * Scheduling
    * RG of:
      * Scheduled Date
      * Confirmed checkbox
      * Outcome
        * Attempted
        * Completed
      * Actual Date
      * Actual Time
      * Hauler
      * Hauler Notes (multi-line plain text as MRG field)
      * (Only allow 1 Completed outcome)



  


  * Primary Assignee (contact; list of active haulers)
  * Additional Assignees; RG of:
    * Contact (list of active haulers)
    * Role (list of Transit Roles)



  


  * Scheduling Notes (memo)



  


  * Status
    * Completion Date (read-only based on the RG)



  


Asset:

  * Have a way to calculate the current location of a building
    * Have an index
      * Subset
        * Only for Transit Types that do a building move
        * Have a completed outcome/date
      * Key
        * RTO Company
        * Asset ID
        * Completed Date
        * Completed Time
        * Transit Task ID
    * Use a LastNdxField on Company + Asset ID + ... and get the end location
  * View Transit Tasks link (use Transit Task Search report for Company + Asset ID)
  * New Transit Task link



  


Reports:

  * Transit task search by:
    * RTO Company
    * Asset (blank = all)
    * Status (blank = all)
    * Assignee (list of active haulers)
    * Location (list of contacts)
    * Type (list of transit types)
  * Columns:
    * Transit Task ID
    * Asset Primary ID
    * Scheduled Date
    * Completion Date
    * Assignees
    * Status
    * Start Location (Name + Address, wordwrap)
    * End Location (same as Start)
    * View Map (link to Google)
  * Group By
    * Status
  * Order By
    * Completed Date + Scheduled Date + Transit Task ID
  * Button
    * New Transit Task



Details don't matter. Duane will reconfigure anyway
