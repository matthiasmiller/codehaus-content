4.8.2.3. Device - Agreement Details Section

  


Requirements

  * Agreement Details section (visible if the Managed checkbox is or previously was checked):



TODO_JM: Tim Reitz 09/07/2023: OK for these to become read-only if the Managed checkbox is un checked?

TODO_EM: Tim Reitz 09/07/2023: Are you OK with that? (to avoid requiring unnecessary things)

TODO_IDD: Tim Reitz 09/07/2023: If yes to read-only, make sure to update all instances. 

  * Managed Service Agreement (required; default to blank; drop list of all active Managed Service Agreements for the selected Customer; warning on Save if changed: "The linked Managed Service Agreement has been changed.")
  * Agreement Renewal Date (auto-set and read-only; sets to the current Agreement Renewal Date field on the selected Agreement record)
  * View/Edit Agreement (link; visible if a Managed Service Agreement is selected; opens the corresponding Agreement record)
  * New Managed Service Agreement (link; visible if no Managed Service Agreement is selected; opens a new blank Managed Service Agreement record with the Customer defaulted)



  


  * Install Date (date; required if Device Status = Active; default to the current date; error on Save if blank: "Install Date is required."; clears if Customer is cleared or changed) 
  * Device Cost $ (required; number field to 2 decimals; auto-set to the Default Device Cost of the selected Device Model; editable in case it needs to be overridden)
  * Activation Fee $ (visible and required if Type = Leased Other; number field to 2 decimals)
  * Initial Invoice # (see details below:)
    * Phase 3: optional; plain text field; warning on Save if blank: "Initial Invoice # is required."; used for manually tracking the initial invoice number. 
    * Phase 4: auto-set and read-only; there would be a process to create the initial invoice with a $0 charge for the Device Cost; details to be determined. 
  * View Invoice (Phase 4; link to open the corresponding Invoice record)
  * Create Initial Printer Invoice (Phase 4; button; visible if there is no linked invoice; clicking the button creates an invoice and sets the Initial Invoice Field:
    * If Type = Customer Printer or Leased Printer:
      * Line item: "<Device Description>"
      * Amount: 0.00
      * Status: Paid
    * If Type = Leased Other:
      * Line item: "Activation Fee - <Device Description>"
      * Amount: <Activation Fee>
      * Status: Invoiced
  * Special Terms (memo; supports expressions; any text entered here is included in Section B of the Managed Service Agreement Printout)



  


Development Specification

TODO_ IDD: Tim Reitz 09/07/2023: Clean up - move / copy Phase 4 items to Phase 4 section.
