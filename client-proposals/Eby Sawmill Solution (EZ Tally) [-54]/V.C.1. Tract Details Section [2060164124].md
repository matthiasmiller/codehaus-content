5.3.1. Tract Details Section

  


Requirements

Tract Details section:

  * Status (auto-set and read-only; Quote, Archived, Contract Signed, Harvest Started, Harvest Paused, Harvest Complete)
  * Tract Name (required; plain text - usually the last name or LLC of the landowner, with a number manually added to the end if there are multiple; unique identifier for the tract record; used to identify tracts on drop lists, etc.; validate against duplicate tract names - error on Save validation message: "Duplicate Tract names are not allowed: <name>")
  * Tract ID (auto-set and read-only; auto-assigned numeric ID used as part of the Payment ID of linked Payment records)
  * Location Type (required; choice of Address / Coordinates; default to Address)
  * Address fields (visible and required if Location Type = Address):
    * Address 1 (text; required)
    * Address 2 (text)
    * City (text; required)
    * State (list of US state abbreviations; required)
    * Zip (number; required)
  * Coordinates (visible and required if Location Type - Coordinates; editable; formatted "Latitude, Longitude", e.g. "52.811468, -98.061405")
  * Latitude (hidden field; number; 6 decimals)
  * Longitude (hidden field; number; 6 decimals)
  * County (drop list of Counties from PA, MD, VA, WV; filters down as you type; default to blank)
  * Contract Signed (drop list of Yes, No, blank; default to blank; read-only if the "Harvest Started" checkbox is filled; see details about Tract Status in Other Notes below)
  * Signature Date (date; visible and required if "Contract Signed" = "Yes"; default to today; date the contract was signed; will be cleared if Contract Signed is switched to No or cleared)
  * Expiration Date (date; visible and required if "Contract Signed" = "Yes"; required; date the contract ends; will be cleared if Contract Signed is switched to No or cleared)
  * Harvest Started (checkbox + editable date; editable if "Contract Signed" = Yes and "Harvest Paused" is not filled and "Harvest Ended" is not filled; filling the checkbox sets the date to the current day; entering a date fills the checkbox; clearing one clears the other; when this checkbox is filled, this tract will show as an option for Yard Tallies)
  * Harvest Paused (checkbox + editable date; editable if the "Harvest Started" checkbox is filled and "Harvest Ended" checkbox is not filled; filling the checkbox sets the date to the current day; entering a date fills the checkbox; clearing one clears the other; when this checkbox is filled, this Tract will be hidden from the options for Yard Tallies; when cleared, this tract would again show as an option)  
  * Harvest Ended (checkbox + editable date; editable if the "Harvest Started" checkbox is filled and "Harvest Paused" checkbox is not filled; filling the checkbox sets the date to the current day; entering a date fills the checkbox; clearing one clears the other; when this checkbox is filled, this tract will be hidden from the options for Yard Tallies)
  * View Yard Tallies (link; opens the Yard Tallies report, with the "Tract" filter set to the corresponding Tract) 
  * New Pulpwood Load (link; opens a new Pulpwood Load record in a new tab with Tract defaulted; also, Logger and Location will be defaulted if there is only one for the Tract) 



  


Other Notes:

  * Tract Status: The Status will be set automatically based on the following criteria:
    * Quote: If "Contract Signed" = blank (this is the default status on creation of the Tract record)
    * Archived: If "Contract Signed" = "No"
    * Contract Signed: If "Contract Signed" = "Yes"
    * Harvest Started: If the "Harvest Started" checkbox is filled
    * Harvest Paused: If the "Harvest Paused" checkbox is filled
    * Harvest Complete: If the "Harvest Complete" checkbox is filled
  * If the Location Type field is changed, the previously entered Address or Coordinates fields are hidden and will be blanked out on save.



  


Development Specification

NICCOLAS:

We are planning to code the counties feature separately.

  


  


Ellis Miller 12/15/2022: 

CCI:

[ ] These can be lookup records because we have a name, but we also will want an assigned numeric ID.

[ ] NOTE: Tracts cannot be merged because we rely on their numeric ID's. 

  


[ ] Basic screen work: 2 HOURS

[ ] Add numeric auto-incrementing TractID -- 1 HOUR

[ ] Add index for lookups and for assigning new TractID

[ ] Clear TractID On Copy

[ ] Add TractStatuses readonly list (unsorted)

[ ] Add TractStatus macro with ifs statement: 1 HOUR

[ ] Add field change expressions to clear address/coordinate fields based on type. 1 HOUR

[ ] Clone/refactor logic for GPS coordinate fields from contact record. 2 HOUR

[ ] The Harvest checkboxes can be macros

[ ] Validation / visibility as defined above. 8 HOURS

  


TOTAL: 1.5 DAYS
