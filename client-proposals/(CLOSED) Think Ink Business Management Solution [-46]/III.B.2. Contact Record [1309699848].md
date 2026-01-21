3.2.2. Contact Record

  


Requirements

Overview: The Contact record will be a customized version of AppHosting's standard Contact record. The Solution will use Contact Types to differentiate between different types of contacts (see the corresponding section of this proposal).

  


Contacts will be synced manually via exports from CA and imports into AppHosting (automated syncing may be built out in the future). The synced fields will not be editable interactively, and will only be updated via the import from Classic Accounting. Classic Accounting will be the "source of truth" for contacts. Contacts will not be able to be created interactively in the Solution - they must be created by the import.

  


Accessed via: 

  * The various Contacts reports
  * The contact's name on invoices and other records



  


Sections and Fields: 

All Contact records, regardless of type, will track the following information:

  * Contact (standard section) 
    * Note that this will include the following field (not currently in the standard section):
      * Tags (see details in the corresponding section of this proposal) 
    * Note that First and Last names should not be required for records created from the CA sync.
  * Address (standard section)
    * Note that this will include the following links (not currently in the standard section): 
      * Google Maps (opens the corresponding location in Google Maps - browser or app) 
      * Apple Maps (opens the corresponding location in the Apple Maps app) 
    * Add a custom "Default SHIPTO" checkbox that is visible for addresses with the "SHIPTO" Address Type. 
      * Note that this field will be read-only on the detail screen (editable via the import). 
      * Tim Reitz 09/04/2024: Not required. See [[[IN9687](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9689&)]] - ZTK - 3a Post-Deploy Issues. 
    * Warn on Save if more than one SHIPTO address is flagged as Default. 
      * Error message: "Only one SHIPTO address can be set as Default"
    * Sort the addresses in the Addresses list in the following sequence:
    * Default SHIPTO address
    * Other SHIPTO addresses, Sorted by State + City + Line 1. 
    * BILLTO address
    * The Solution will always consider the first address on the list to be the "Primary" address (which it displays on Service Incidents, etc.). 
    * Note that the Solution will handle this sorting automatically, and no special sorting is needed for the import from CA. 
    * If there is a BILLTO address, display it at the bottom of the Address section after a "Billing Address" label. 
    * The Address Types list in AppHosting should contain the following items:
      * BILLTO
      * SHIPTO
  * Phone (standard section)
  * Email (standard section)
  * Incidents (standard section, with the following customizations): 
    * New Sales Opportunity (link; opens a new incident with Contact and Type defaulted; Assignee should be defaulted to the contact's sales rep)
    * New Check-In (link; opens a new incident with Contact and Type defaulted; Assignee should be defaulted to the contact's sales rep; Check-In Date will be blank)
    * New Service Incident (link; opens a new incident with Contact and Type defaulted; Assignee should be defaulted to the contact's sales rep)
  * Notes (standard section) 



  


All Contact records, regardless of type, will have the following custom section/fields:

  


  * Classic Accounting Notes (custom section): 
    * Read-only memo (filled with the notes from the CA contact)
    * CA Contact ID (Think Ink-specific; stores the Org ID from Classic Accounting)
      * Note that this is being done prior to the main Phase 1 development.



  


All CUST-type Contact records will also have the following custom section/fields: 

  * Customer Details (custom section): 
    * Sales Rep (read-only; automatically determined from CA Sales Rep ID)
    * Preferred Contact Method (optional; drop list of Email, Fax, Mail, Phone)
    * Preferred Invoicing Method (optional; drop list of Email, Print)
    * Changes for CA (Think Ink-specific; editable multi-line plain text field that shows 3 rows; used for documenting changes that should be made in CA, since the CA-specific fields are read-only in the Solution) 



  


  * Check-In Details (custom section): 
    * Scheduled Check-Ins (checkbox; default to cleared)
      * Note that in the future this can be auto-filled if the customer is an MPS customer. 
    * Customer Check-In Frequency (visible and required if Scheduled Check-Ins is filled; drop list of Monthly, Quarterly, Annually; all based on the Start Date; default to Quarterly)
    * Check-In Start Date (visible and required if Scheduled Check-Ins is checked)
    * Last Check-In Date (auto-filled and read-only; see Calculating Check-In Dates in this proposal for calculations)
    * Next Check-In Date (auto-filled and read-only; see Calculating Check-In Dates in this proposal for calculations)
    * Next Check-In Notes (multi-line text field; auto-filled and read-only; based on the Check-In Incident for the Next Check-In Date above)
    * Check-In Documentation (read-only memo; auto-filled with text from the 4 most recent closed Check-In incidents for this customer; displayed in the following format:) 



TITLE: 

Sample

 

NOTES:

Sample 

\---------------------------------------------------------

TITLE:

Sample

 

NOTES:

Sample

\---------------------------------------------------------

  


Also include:

  * Created (user ID, date, and time; auto-filled and read-only) 
  * Last Modified (user ID, date, and time; auto-filled and read-only) 
  * Modification History (link to report)



  


Data Access: All users can view and edit

  


Other Notes:

  * The addresses will be geocoded, allowing the user to click a link to open the address in Maps (Google and Apple).
  * Note regarding duplicate names: The AppHosting Contacts module does not currently allow for more than one contact with the same name. Previously CA had allowed duplicate names, but is now moving away from allowing it. With this in mind, duplicate names should be avoided/cleaned up in CA to ensure a clean syncing process. To differentiate between contacts with the same name, an identifier suffix can be added to one of the name fields to make a distinction.



  


Development Specification

Austin Priest 01/20/2023: [[[IN7289](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7291&)]] - ZTK - Rename Contact Types

Austin Priest 01/20/2023: [[[IN7193](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7195&)]] - ZTK - Changes to Addresses and Address Types

Austin Priest 01/20/2023: [[[IN7190](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7192&)]] - ZTK - Contacts - Changes to Preferred Contact & Invoicing Method Fields

  


  


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1529895558](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1529895558)

  


All fields synced from CA would be read-only in the Solution.

Spec: We will add multiple Custom_ContactCanEditFieldName(vInDetailScreen, vInEditableReport, vInImport) parameterized macros so we can specify that fields can only be edited in imports. This would always be in addition to any other conditions we have (base should always return true). 

  


Also, users can't create contacts interactively. 

Bid: 1 day

  


Note that First and Last names should not be required for records created from the CA sync.

Spec: For Contact individuals, we will add a switch Config_ContactPersonRequireFirstLastName. If this is false, we will not validate and will not automatically populate the Contact ID. We will treat it as an Override all of the time and the user needs to enter an ID manually.

[ ] Add switch

[ ] Change validation

[ ] Always treat as Override

[ ] Never populate

BID: 0.5 Days

  


Geocoding Module: 

TODO_JN:

  * For the geocoding, we will need to tie in a webhook.
  * In AppHosting: 
    * Add a "Google Maps" link to the Contact between the Address buttons and the Export Address link.
    * Add a system switch to enable Apple Map Links. If enabled, show a link underneath the Google Maps link for "Apple Maps". 



Ellis Miller 06/14/2022: GeoCoding module that uses a separate GeoCodedAddresses DB Level. Look up by ini format (Josh decides if he wants to standardize addresses). A DB trigger will fill in these records. Consider using an MD5 hash to determine the addresses that need geocoding. The Config_ContactShowAddressCoordinates(?) switch becomes 3 way -- No, Manual, Automatic GeoCoding. Do we need a way to override the geo-code?

Ellis Miller 06/20/2022: We will charge this as a module (folding $250 into proposal and adding $25 / month). Also bidding 1 day of Seth's time for address tie-in if needed.

  


Map Links

'[http://maps.apple.com/?ll=%(lat)s,%(lng)s&daddr=%(addr)s&dirflag=d&address=%(addr)s'](http://maps.apple.com/?ll=%\(lat\)s,%\(lng\)s&daddr=%\(addr\)s&dirflag=d&address=%\(addr\)s') 

'[http://maps.google.com/maps?ll=%(lat)s,%(lng)s&daddr=%(addr)s'](http://maps.google.com/maps?ll=%\(lat\)s,%\(lng\)s&daddr=%\(addr\)s') 

  


Proposal:

  * Add a parameterized macro GoogleMapUrl( vAddressIni) where vAddressIni is our standard address INI.
  * Add a parameterized macro AppleMapUrl( vAddressIni) where vAddressIni is our standard address INI.
  * Add a system switch Config_ContactShowAppleMapUrl (default to false). We'll always show Google Maps.



BID: 1 day for CCI

  


Incidents:

  * 3 auto-push reports that populate fields using New Record.



BID: 0.5 days CCI

  


Classic Accounting Notes & Customer Details (custom section): 

  


BID: 0.5 days CCI

  


Check-In Details (custom section): 

  * Need CheckInByDate ndx for Incidents. 2 hours
  * Lookup macros for last and next -- 4 hours



  


Ellis Miller 06/20/2022: DONE_TR: Matthias believes that we should use the Check-in Start Date for the first check-in and then after that base our calculations on the last check-in. Can wait until later to confirm, but I'd like to confirm that with you.

DONE_CCI: Tim Reitz 06/21/2022: Confirmed with the client that that's their preference too. See note for Check-In Date in the Check-In Incident section. 

  


DONE_CCI: Tim Reitz 06/23/2022: Note that I changed the CA Org ID and CA Contact Notes to be for all types of Contacts, not just the Customer type, since I think that reflects how it actually will be. 

Also, I changed Tags to be for all types of Contacts, not just the Customer type, since I think that is simpler and more practical (and I think the client might end up requesting it at some point if we don't do it now). 

Ellis Miller 07/02/2022: Agreed on both.

  


TOTAL: 4.25 (Round up 5 days)
