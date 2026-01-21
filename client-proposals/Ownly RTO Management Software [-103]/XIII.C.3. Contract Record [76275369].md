13.3.3. Contract Record

Overview: This is a custom record type, used to keep track of individual Contracts for a given Customer. This is the main record of the solution, which brings together details from Contacts, Assets, Payments, Contract Entry, and more.

  


Accessed via: 

  * Contracts | Contract | Search Contracts



  


Sections and Fields: 

  * Rental Contract section 
    * Transfer Contract checkbox (visible and editable after Contract Start Date)
      * On Save, if the transfer checkbox is checked and if the primary or secondary customers changes, save the old values in a new row in the RG; also clear the checkbox; just use a Field
    * Primary Customer (required; drop list of active customers; editable on/before Contract Start Date OR if Transfer Contract is checked)
      * view/edit link
      * Primary Tags (read-only memo; one tag per line) 
    * Secondary Customer (optional; drop list of active customers; same editability as above)
      * view/edit link
      * Secondary Tags (read-only memo; one tag per line)
    * Customer History  (button/ child RG; not editable interactively; visible if there are any rows)
      * Transfer Date (defaults to Today's date)
      * Primary Customer
      * Secondary Customer



  


  * Asset section (Note: An Asset can only be tied to 1 pending/active contract at a time)
    * view/edit (link; opens corresponding Asset record)
    * Product (drop-list of product descriptions; Note: only shows Assets not already tied to a pending/active contract)
    * Product Tags ( read-only macro; displays the Asset Tag(s) set on the corresponding asset record; see corresponding spec) 
    * Manufacturer (auto-set; link; opens contact record for the Manufacturer; pulled from the Asset record)
    * Primary ID (auto-set; read-only macro; displays the Primary ID for the asset)
    * Secondary ID (auto-set; read-only macro; displays the Secondary ID for the asset)
    * Cost (auto-set; read-only macro)



  


  * Contract Details section:
    * Rental Company (drop-list of active Rental Companies; cannot add to list; default to active Rental Company if there is only one; editable before the contract start date OR if the user has a superadmin permission)
    * Rental Contract Type (RTO vs RTR; required; editable before the contract start date OR if the user has a superadmin permission)
    * State (drop list of States; based on availiabilty from contract definitions; required; editable before the contract start date OR if the user has a superadmin permission)



Matthias Miller 07/30/2025: After the contract start date, only someone with highest permissions can edit Rental Company, Rental Contract Type, and State. TODO_PERMISSIONS - figure this out

  * Contract Status (list field; editable; required; list of Contract Statuses) 
    * Waiting to be Built
    * Waiting to be Delivered
    * Active
    * Pending Retrieval
    * Complete
    * Canceled
  * Contract ID (text field; required)
  * Entry Date (OnInit: Today; read-only)
  * Start Date (required if Contract Status = Active)
  * Salesperson (auto-calculated and read-only; the salesperson from the linked product)
  * Dealer (auto-calculated and read-only; the salesperson from the linked product)



  


  * RTR/RTO Contract Details section



  


  * Rental Fees (a formatted display of fees due and fee balances)
    * Due Date (auto-calculated) 



  


  * Rental Fee Due (auto-calculated)
  * Late Fee Due (auto-calculated)
  * DWF Due (auto-calculated)
  * Total Due (auto-calculated)



  


  * Payments (auto-calculated)
  * Rent Balance (auto-calculated)
  * Late Fee Balance (auto-calculated)
  * DWF Balance (auto-calculated)
  * Balance (auto-calculated)



  


Niccolas Miller 01/07/2026: TODO_MM/TODO_DB: Rethink contract status and contract resolution and how they work together.

  * Contract Resolution
    * Contract Resolution (drop-list of the following contract resolution types:)
      * Early Payoff
      * Payout
      * Return (i.e. voluntary)
      * Retrieval (i.e. involuntary)



  


  * Fees and Payments section



  


  * Documentation Section
    * References; Embedded Spreadsheet of:
      * Type (user-configurable list)
        * Landlord
        * Reference
      * Name
      * Email 
      * Phone Number (plain text; auto-formats when ten digit phone number is entered)
    * Attachments; embedded spreadsheet (S3)



  


  * Notes section 
    * "This record must be saved before creating a linked note." (label, visible for new unsaved records)
    * New Note (opens a new note record; populates the Type + Linked Record, visible if the record has been saved)
    * View Notes (report link; opens the My Notes report)
    * Notes (read-only memo that concats based on record Type + record ID, sorted in order of Note ID; newest first) 



  


Modification History: This contains the following standard feature for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

TODO_PERMISSIONS: Document based on Permission, rather than User Groups. 

  


Special Considerations: TODO_PERMISSIONS: 

  * Copy Record: __ (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: __ (think: allow deletion? under what circumstances?)
  * Merge Record: __ (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)


