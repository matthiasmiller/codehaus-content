22.2.2. Classic Accounting Address Record (Read-Only)

  


Requirements

Overview: This is a hidden record type that mirrors the addresses in Classic Accounting and is used for syncing between the two programs.

  


Accessed via: The Classic Accounting Addresses report (see corresponding section of this proposal)

  


Sections and Fields: (all are auto-set and read-only)

  * Address ID
  * Org ID (to link to Contact)
  * Record Exists (true if record still exists in Classic Accounting)
  * Address Type (BILLTO, SHIPTO; imported into AppHosting Address Type, see "Syncing with Classic Accounting")
  * Active (inactive addresses are excluded from the AppHosting contact)
  * Is Default (checkbox, used when importing addresses onto the AppHosting contact) 
  * Address Name (not imported to the AppHosting Contact)
  * Street 1
  * Street 2
  * City 
  * State
  * Zip
  * Country (not imported to the AppHosting Contact at this time)
  * Created Date/Time (not imported to the AppHosting Contact)
  * Modified Date/Time (not imported to the AppHosting Contact)



  


Data Access: 

  * Visibility: Admin Only
  * Editability: Import Only



  


Other Notes: N/A

  


Development Specification

Mockups: None needed; to be auto-generated

  


DB Level:

[ ] CA_Org_Address

  


CA_Org_Address fields:

[ ] CA_Org_Address__AHZID (auto-number)

[ ] CA_Org_Address__AHZRecordExists (checkbox, OnInit: True)

[ ] CA_Org_Address__AddressType (user-customizable list)

[ ] CA_Org_Address__GenAddrID (number)

[ ] CA_Org_Address__Active (checkbox) 

[ ] CA_Org_Address__AddrName (string)

[ ] CA_Org_Address__TxtCity (string)

[ ] CA_Org_Address__TxtCountry (string) 

[ ] CA_Org_Address__CreateDate (string)

[ ] CA_Org_Address__ModDate (string)

[ ] CA_Org_Address__TxtState (string)

[ ] CA_Org_Address__Street1 (string)

[ ] CA_Org_Address__Street2 (string)

[ ] CA_Org_Address__TxtZip (string)

[ ] CA_Org_Address__IsDefault (checkbox) 

[ ] CA_Org_Address__OrgID (number)

  


Ellis Miller 08/30/2022:

[ ] Add simple record (Custom DB Level) and fields.

[ ] Add detail screen with no behaviors

[ ] Editable: InImport OR CanEditCAInteractively

Add a label visible CanEditCAInteractively if across the top of the screen: "This record is editable for developers."

  


BID: 3 hours
