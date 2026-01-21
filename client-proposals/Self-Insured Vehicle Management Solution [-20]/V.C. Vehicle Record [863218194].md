5.3. Vehicle Record

  


Requirements

Overview: This is a custom record type, used to track vehicles in the database. Each Contact can have one or more Vehicles, and each Vehicle must be associated with a specific client Contact.

  


Accessed via: Various places, including: 

  * All Vehicles report
  * "Vehicles" embedded spreadsheet on the Contact record



  


Sections and Fields: See the following sub-sections of this living spec. 

  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (User ID, date, and time stamp) 
  * Last Modified: (User ID, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access:

  * Visibility: Visible to all users.
  * Editability: 
    * Generally, fields are editable by all Admin users and by the "Current Owner's Agent", with some fields editable only for Admins after the Vehicle is inactive. 
    * Some fields have special editability conditions (i.e. to allow the current agent of a previous owner to make some limited edits). This is done via the "Limited Editing Mode" feature.



  


Special Considerations: 

  * Copy Record: N/A (disabled)
  * Delete Record: Allowed for Admin users if Vehicle is inactive 
  * Merge Record: N/A (disabled) 



  


Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/23/2025: [[[IN11647](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11649&)]] - ZWA - Pre-ZWW - Vehicle Record - Update Record Editability for Non-Admins 
  * 


  


  


  


Matthias Miller 07/14/2020: Future

[ ] Should we transfer actual invoices for high risk driver fees?

[ ] The VIN decoder URL should be a system switch so we don't have to update the URL.

  


  


  


\--------

Ellis Miller 08/12/2020: Vehicles

  


Custom DB Level

  


Section: Vehicle (4 days)

Make and Model are simple lists. We infer Model from Make using a VehicleToMakeAndModel.ndx. 

VIN Validation - Use a 20-byte ndx for VehicleByVINSerial.ndx. Validate that they can't enter more than 20.

  


Activate/Deactivate button (1.5 day)

Default VehicleActive to true

When reactivating, blank out all deactivation fields

Needs OnChange statements to deactivate coverages

Reactivate will not change any coverages, but we shoudl always validate that we have at least one active coverage for an active vehicle.

  


Transferring Ownership 

When clicking the Transfer button, fill in a PriorOwner field that is readonly. Show the field if PriorOwner <> Owner.

  


Note that the "Transfer to household member" field is simply saying whether or not the new Owner is from the same household.

  


Transferring Ownership (5 days)

The Transfer button sets a DetailVariable for Transferring or EditOwner.

  


When clicking the Transfer button, fill in a PriorOwner field that is readonly. Show the field if PriorOwner <> Owner.

  


Note that the "Transfer to household member" field is simply saying whether or not the new Owner is from the same household.

  


Hide the "Create Invoice Now" button if credit amount is < AppHostingSettings.MinimumTransferCredit. See setting: 

"Issue Invoices for Credits Over $"

  


Section: Guideline Compliance (1 day)

Guidelines are defined in AppHostingSettings. This is a virtual RG that fills in a VehicleGuidelinesCompliance RG.

  


Coverage RG (Liability / Collision / Cargo) (3 days for basic RG and MRG fields)

We will have a coverage RG with 3 fixed rows:

 \- Liability (has only annual Premium)

 \- Collision (Entry fee + annual premium)

 \- Cargo (Entry fee + annual premium)

  


We'll show MRG fields below the RG for editing. The MRG fields vary somewhat. 

  


Fields

  * Liability Code - Liability Only
  * Classes  \- Liability Only
  * Premium 
  * Active (macro) 
  * Effective Start Date
  * Effective End Date
  * Date Entered 
  * Coverage Amount - Collision and Cargo Only
  * Current Coverage Period Start -- macro of Max(EffectiveStartDate, AppHostingSettings.CurrentPeriodStart)
  * Current Coverage Period End -- macro of Min(EffectiveEndDate, AppHostingSettings.CurrentPeriodEnd)
  * Next Coverage Period Start --  macro of Max(EffectiveStartDate, AppHostingSettings.NextPeriodStart)
  * Next Period End -- macro of Min(EffectiveEndDate, AppHostingSettings.NextPeriodEnd)



  


  


Coverage Activate Button (3 days)

Rate Calculations: See details in setting screen, the premium are prorated for partial years. Note that because the CurrentPeriod is incremented in May before the July 1 start, the premium could be for 13.9 months.

  


Creates up to three rows and fills in information. We can use a parameterized OnChange. 

  


For Rate calculations, let's create a macro that has a testing report where people can play with calculations.

  


As much as possible, create transparency in calculations.

  


Please involve Ellis in design/implementation.

  


Coverage Deactivate Button (3 days)

When deactivating any coverage for any type of fee:

  * Find all fees since the latest credit
  * Prorate each fee based on the current date vs. the fee's Through Date
  * Add a credit entry for that fee to the RG  ($0 credits can be skipped, since they should always prorate to 0 in the future as well.)



Owner does not matter, because if ownership is transferred, we will create fees. If ownership is not transferred, the new owner could theoretically collect on the entry fee. Maybe check w/ Bruce to confirm?

  


Coverage Renewal Button (2 days)

For coverage renewal, we will use an x30. Let's show a "Renew (admin-only)" button for testing purposes. Renew button is normally triggered by an x30 (you can trigger an OnChange button by using ButtonName = true). If coverage is up to date, it doesn't do anything.

  


Section: Fees & Credits (1 day)

Need an auto-incrementing Sort ID with latest at top.

  


Template Exports:

  


Program Participation Agreement (2 days)

This will be spec'ed out more fully once we have a sample. We'll be exporting some fields, including the table of guideline agreements.

  


Add the contents of the "Vehicle Guidelines" wiki page memo to the end of the template, with a page break before. 

  


Liability Declaration Page (2.5)

  


Loss Payable Clause (2.5)

  


Insurance Card Template (4 days)

Because this is printed on perforated Letter paper, we will want the template to actually include the card 3 times. We will drive this from a merge report that gives us three Vehicle ID's. The report will have 3 columns

  * ColVehicleID1
  * ColVehicleID2
  * ColVehicleID3



  


We'll create a local macro in the report that takes the vehicle number (1-3) and the field to lookup LocField(1, VehicleField). You may want to even wrap this with other macros LocEffectDt(1).

  


Use a DeleteSection if any of the IDs are blank.

  


The template will include a second page for the backs. We will delete sections there if the vehicle numbers are blank or if the ask prompts specified to only print front.

  


Insurance Card Merge Report (1 day + 3 hours Ellis)

We will use the merge report to either print one vehicle or to print lots of vehicles. We'll add prompts for:

 \- Agent

 \- Print: Front Only, Front & Back

 \- Owner

 \- (hidden) Vehicle ID

  


If these are blank, we include all active vehicles. 

  


This report needs to create one row per 3 vehicles per owner. The easiest way to do that may be to make this a vehicle report that is subsetted by the ask prompts and IsActive. It will use a model to rank the vehicles grouped by owner. It will be a totals-only report that groups by Owner + Rank/3. It will put the vehicle in a column based on Rank%3. I would love to help actually create this report. 

  


Section: Deactivation History (1.5 days)

The Deactivation button adds a row (see button desc), we will require the reason to be filled in.
