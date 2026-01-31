7.4. Changes to Contact Record for Phase 3a

  


Requirements

The following changes are to be made to the existing Contact records for Phase 3a:

  


Existing Customer Details custom section: 

Change the following existing field(s) to this new design: 

  * Sales Rep (if the Customer is linked to a Region: auto-set and read-only, displaying the Sales Rep for the selected Region; if the Customer is not linked to a Region: optional; drop list of Employee Contacts; defaults to blank for new manually-created records; for imported records, continue to default to the imported Sales Rep) 



  


Add the following new fields: 

  * Region (optional; drop list of active Regions; warning on Save if changed from one Region to another: "You are about to change this customer's Region. Do you want to continue?")
  * View/Edit Region (visible if a Region is selected; link; opens the corresponding Region record)



  


Existing Check-In Details custom section: 

Change the following existing fields to this new design: 

  * Scheduled Check-Ins (checkbox; auto-set and read-only; checked if the Customer is linked to a Region)
  * Check-In Schedule (previously called / replaces "Check-In Frequency"; visible if "Scheduled Check-Ins" is checked; auto-set and read-only; displays the Check-In Schedule from the linked Region) 
  * Remove "Check-In Start Date"
  * Last Check-In (previously called / replaces Last Check-In Date; displays the Month of the last check-in incident for the Customer; uses the following format: "<Month> <Year>")
  * Next Check-In (previously called / replaces Next Check-In Date; displays the Month of the next scheduled check-in for the Customer's Region; uses the following format: "<Month> <Year>")



  


Additional custom validations:

  * Require that all Customers have at least one Billing address - error on Save: This Customer does not have a Billing-type address set."



Tim Reitz 09/04/2024: Removed in [[[IN9687](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9689&)]] - ZTK - 3a Post-Deploy Issues.

  * If the "Allow manual editing of Contact records by Administrator users" system switch is set and the current logged-in user is an Admin and the record is being edited interactively:
    * A banner will be displayed across the top of the Contact screen: "All fields are currently editable due to system switch settings."
    * Show a warning message on Save: "The "Allow manual editing of Contact records by Administrator users" system switch is set. Changes you save here may be overridden on the next Contacts import from CA. Please turn off the system switch when done."



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1529895558](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1529895558)

  


Custom Details (Sales Rep / Region)

[ ] Change SalesRep to be a macro with a NonRegionSalesRep field.

[ ] Clear field when region is set.

[ ] Use OnChange macro.

[ ] If we need indices for this, we'll have to combine two -- a ContactsByNonRegionSalesRep.ndx and ContactsByRegion.ndx

1 day

  


Check-in Details

Fairly simple, but may trickle to various reports.

1 day

  


Additional Custom

[ ] Billing address is record validation with HasRG(AddressType = "Billing")

[ ] Adding system switch and using it for CanEditRecord

[ ] Adding display banner

[ ] Adding warning on save

1 day
