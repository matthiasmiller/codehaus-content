5.1.2. Species Record

  


Requirements

Overview: The Species record is used to configure information about individual log species, such as White Oak, Walnut, etc. This information can then be referenced by other records in the Solution, such as the Yard Tally and Export Tally. 

  


Accessed via: Configure Species Report 

  


Sections and Fields: 

  * Active (checkbox; defaults to filled)
  * Species (auto-set and read-only; displays the log condition as it is displayed on lists, etc., elsewhere in the Solution, in the following format: <AB> \- <Description>", where "AB" is the Abbreviation) 
  * Description (required; plain text; validate against Species records with duplicate Descriptions - validation message: "The Description is used for another active Species record. Please enter a different description.")
  * Abbreviation (required; plain text; validate against Species records with duplicate Abbreviations - validation message: "The Abbreviation is used for another active Species record. Please enter a different abbreviation.") 
  * Hotkey (numeric string; if the first digit is 0, it must be two digits, so 00-09, otherwise it must be a single digit, so 1-9 - validation message: "The Hotkey must be a number between 1 and 9 or between 00 and 09."; validate against active Species with duplicate Hotkeys: "The Hotkey is used for another active Species record. Please enter a different hotkey."; note that not all Species will have a Hotkey) 
  * Pricing (used to determine the "Price" for a log of a given Species and Grade, and therefore to calculate the Log Value on the Yard Tally records; embedded spreadsheet with the following:) 
    * Columns: 
      * Grade (auto-set and read-only)
      * $/mbf (required; number with no decimal places)
    * Automatically sorted by: Grade
    * This embedded spreadsheet will automatically include a row for each Grade from "00" to "49". 
    * Veneer grade (Base Grade 5) pricing would not be included on the Species record. 
    * Rows cannot be added or removed from this embedded spreadsheet. 
    * Show 25 rows without scrolling



  


Data Access:

  * View record: All users (specifically to allow users to view Description, Abbreviation, Hotkey in lists, records, etc. throughout the system)
    * View Pricing: Users with the "View Tracts, Yard Tallies, and Pulpwood Loads" permission 
  * Edit and delete full record: Administrators



  


Other Notes:

  * The Species would be displayed in lists throughout the Solution as "<AB> \- <Description>", where "AB" is the abbreviation.
  * There should be one Species record for "Misc.", to be used to identify species that Eby's doesn't normally work with or that don't fall into their regular parameters. 
  * Eby's will take care of setting up all Species records at deployment.



  


Development Specification

Mockup:

  * Google Sheets: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=2046987196](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=2046987196)
  * Designer: [https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D2&SinglePane=true&MainReportPath=MainDir%3A%3A%5CStandard%5CDesigner%5CStd+Designer+Overview.r20&State=Tr1GcI4u7tA](https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D2&SinglePane=true&MainReportPath=MainDir%3A%3A%5CStandard%5CDesigner%5CStd+Designer+Overview.r20&State=Tr1GcI4u7tA)



  


  


Ellis Miller 12/15/2022:

[X] DONE_CH: Is the underlying Species list, showing the concatenated "<AB> \- <Description>"? Can we display that on screen as a readonly "Species Name" or just "Species"?

Tim Reitz 01/05/2023: Done. 

[X] DONE_CH: Matthias, will we use restricted data to hide the pricing RG from non-financial users or just hide it on the detail screen? Are there any OnChange statements or similar logic in other parts of the system (e.g. when filling in tallies) that make so that other users need to have the pricing accessible under the hood? For example, when the Scaler specifies a grade, do we copy the price onto another record at that time? If so, we should hide, but not restrict, the price RG.

Matthias Miller 12/27/2022: I think this is a visibility thing, since we will need to access this RG in other parts of the system.

Ellis Miller 12/28/2022: OK, we won't use restricted data, just visibilty.

  


Going forward, Ellis would like to push for "openness by default" wherever we can. Performance and development becomes much more expensive when we do this. We should document this as a design principle.

Tim Reitz 01/05/2023: Explanation: Determine the appropriate level of protection for the situation (Example: locks on door vs. security system vs. concrete walls and razor wire - the security level goes up, but so does the cost of implementing and maintaining). By default we should use lower levels of restrictions, and try to use higher levels strategically. In most cases, lower levels are sufficient and most users won't or don't know how to access data behind the "locks". 

 DONE_TR/NM

  


Ellis Miller 12/15/2022:

BID:

[ ] Record type and basic detail screen: 2 HOUR

[ ] Validate against duplicate fields. Pseudocode: ListSubstitute(Species, if (SpeciesField = vThisField AND NotThisListNumber, SpeciesIDOrListNum, ''), 2 HOURS

[ ] Validate that Hotkey is a numeric string in the acceptable range. Add unit tests for this. 1 HOUR

[ ] Pricing RG: Use OnInit to fill in the RG rows. Don't allow adding/removing rows. 2 HOURS

[ ] Create a GradesNonVeneerList macro that returns grades that aren't veneer grade. It could be hardcoded to use InRange(Value(ListSubstituteItem), 0, 49)

[ ] Test that copying a record doesn't duplicate the rows.

[ ] Add validation against duplicate grades. This would prevent us from saving a record with some weird bug that gives duplicate rows. 

[ ] Add restricted data rule for pricing? Need to confirm.

  


Tim Reitz 01/19/2023: Note that no development is needed for the "Misc." species. 

  


Total: 1 Day
