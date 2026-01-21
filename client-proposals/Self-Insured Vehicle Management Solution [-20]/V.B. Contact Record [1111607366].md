5.2. Contact Record

  


Requirements

Overview: The Solution uses the standard Silverloom Contacts module, utilizing the standard Contact record with its contact sections and fields, which may have custom behaviors. Additional custom sections & fields may be added as well. Any customizations are noted as such in the spec. 

  


Accessed via: Various places, such as: 

  * Contacts reports
  * Other records (Vehicles, Claims, etc.)  



  


Data Access:

  * Visible to: All users 
  * Editable by: The Contact's current Agent (when applicable, i.e. for Client-type Contacts) and all Admins



  


Sections and Fields: The sections and fields for this record are specced out in subsections below.

  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (User ID, date, and time stamp) 
  * Last Modified: (User ID, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access:

  * Visibility: Visible to all users (standard). 
  * Editability: Editable for all Admin users and all "In-State Agent"-type users (custom). 



  


Special Considerations:

  * Copy Record: Allowed, and the following fields are cleared (standard): 
    * Contact ID 
    * First Name 
    * Middle Name 
    * Last Name 
    * Date of Birth 
    * Household Drivers (custom)
    * Vehicles (custom)
    * Fees (custom)
    * User ID 
  * Delete Record: Allowed until the record has been referenced by another record, at which point deletion is disallowed (standard). 
  * Merge Record: Allowed if inactive (custom); the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record). 



  


Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked (standard). 
  * If a Contact changes from one Contact Type to another, any fields specific to the previous Contact Type are hidden, and cleared on Save (standard). If desired, this can be changed to retain field information (customization).



TODO_VA: Tim Reitz 11/20/2025: This has been changed for the "Contact Details" section in [[[IN12301](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12303&)]] - ZWA - Contact - Changes to "Member Policy #". 

  


  * The following entire standard section(s) with all included fields are hidden (custom) in this Solution: 
    * __



TODO_CCI: Tim Reitz 11/20/2025: Which sections are hidden completely? 

Sagar Sagar 12/10/2025: I believe there is none.

  * The following individual standard field(s) are hidden (custom) in this Solution: 
    * __



TODO_CCI: Tim Reitz 11/20/2025: Are there any individual fields / macros that are hidden?

Sagar Sagar 12/10/2025: I am listing them below

  * Active Contact - checkbox
  * Contact Inactive Date - beside Active Contact checkbox
  * Contact Summary



  


Development Specification

Change Requests: 

  * Tim Reitz 11/20/2025: [[[IN12301](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12303&)]] - ZWA - Contact - Changes to "Member Policy #" 
  * 


  


  


  


Tim Reitz 08/18&19/2020: Any info here about Snoozed? Do we need to store a snoozed date as well? Do we need Snoozed Reason?  Is Snoozed something big enough to be worth cutting out? 

Matthias Miller 08/20/2020: Snoozing is discussed in the Admin Reports. The Snooze is a date (specified above). No Snoozed Reason. And no, not big enough to cut out.

  


Matthias Miller 07/14/2020: Eventually:

[ ] Could handle clients moving into other household (women getting married after they moved out on their own).

[ ] Future: consider alternate ways of submitting the New Member card.

  


Ellis Miller 08/12/2020: 

  


NOTE: All Required fields should be NOT Import.

  


Enhanced Search Fields (1 day)

 \- Add system switch Config_ContactsSearchMatchFirst -- to match only on beginning

 \- Add a few additional fields to our contact report search

 \- TODO: circle back to Active Checkbox on search

  


Creating a New Contact (2 days)

 \- Add system switch Config_ContactsNewContactAutoPushReport. If this is set, we use this for the "New Contact" button. Otherwise we show our current button.

\- The New Contact report will need conditional ask lists to show Drivers based on clients

  


New Contact Migration (5 days)

TODO: Let's interface the x30 on the menu for admins to transfer any driver.

 \- Add required "Transfer Driver" Yes/No List field. Required If NewRecord. Visible if Yes or if New Record.

 \- If Yes, show fields for ContactMigrateFromClient  / ContactMigrateDriver. If populated, show a "Migrate Data Button" that runs the imports. We'll also have a nightly process to run this

 \- Add index ContactMigrationNeeded

 \- Imports:

 \- Migrate Copy Client Fees.x30 -- (!RG) copies across fee lines

 \- Migrate Delete Client Fees.x30

 \- Migrate Delete Driver.x30

 \- Migrate Update Claims.x30

 \- Migrate Clear Flag.x30

 \- Add warning on save not new record and they have not yet clicked the button "Please click the button!"

 \- Background Task (manually configured)

  


Contact Fields (we need to track): 3 days

 \- Populate the Types list 

 \- Add Config_ContactCanAddTypesInDetail switch

 \- Replace AddressType list with "Primary"

 \- Add validation that only one address is marked as primary. 

 \- Consider a Macro to Sort Address Type so Primary is first.

 \- Entry Date -- just use new "Created" macro

 \- Add a standard "Inactive Date" field that is init if Active is unchecked. This field is editable. Validate that this is in sync w/ checkbox. Make field visible if Inactive or NOT IsNA.

 \- Config_CanEditInactiveDate expression system switch. Overridden as IsAdmin for this client. 

 \- "Snooze Until" Date

  


  


Display Invoices (1 day)

 \- we show invoices already

 \- may need macros to display fees and credits

  


Create Customer Invoice (4 days)

\- x30list button (takes prompt for client):

 \- First x30 has ask prompt that creates invoice for today's date and this client with a "Please Populate Me" hidden field.

 \- Invoice Populate from Contact.x30 -- uses report to populate invoice lines from creates/fees/vehicles

 \- Invoice Update Contact Fees.x30 -- stamps invoice ID on fee rows

 \- Invoice Update Vehicles.x30 -- stamps invoice ID on assoc vehicles

 \- Invoice Finalize.x30 - clears "Populate Me" flag and changes status to Invoiced.

 

Print Unpaid Invoices Link (2 days)

\-- Create PDF merge that takes a list of invoice ID's and our normal PDF template to generate the PDF

\-- Create macro to collect ID's: Uses the InvoicesByContacts and subsets by unpaid to generate list of invoice IDs

  


Deactivate (1 day)

 \- Don't allow "Active" to be unchecked.... Add a Config_ConfigValidationForIsActiveField. 

 \- for vehicles, don't allow making it active unless contact is active.

  


Household Drivers (1 day)

 \- OnInit: Fill in name when adding first row.

 \- Add a Hidden auto-populated incremented DriverNumber. (Max+1)

 \- Drivers are identified by ContactName+ContactDriverNum.

  


Fees (2 days)

 \- Only for High Risk Fees at this point.

 -Assess Fees.x30 -- Prompts for Contact (passed in), Driver, and Fee. The x30 uses change expressions would be in triplicate to add the three rows

  


Cards (1 day) 

\- Add a NewMemberCardTemplate memo field with Expr requirements to the AppHosting settings. We will manually populate this as part of setup, but make sure we know what template to use.

\- Use a simple PDF Export with a size of 5 1/2 x 4 1/4 that evaluates this for the current record.

  


Other Notes (0.5)

 \- Add ValidateRecord to the detail screen for this.
