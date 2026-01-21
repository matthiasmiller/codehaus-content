11.12. SPE Online Submission Record

  


Requirements

Accessed from: Faith Builders SPE | Member Applications | Online Submissions

  


TODO_AP: Tim Reitz 02/24/2025: Bring in the Record Snippet for the standard pieces for this overview section. Also update the record sections below as able/needed.

  


Development Specification

Ellis Miller 02/08/2021: 

  


Linked Contact with Matching Logic:

[ ] These are OR'ed together

[ ] Do exact match on name

Target: 1 day

  


Online Submission Contact Fields:

[ ] Lookup macros from Linked Contact

[ ] Font formatting on matched values

Target: 1 days

  


Create Contact / Update Contact button: 

[ ] Sets LinkedContact="Frank Smith (from Online Submission #1317)" via on OnChange button. The contact will be auto-created on save. When the user clicks the Update Contact, an x30 finds "(from Online Submission)" records and copies data in, fixing up the contact name, etc.

Target: 2 days

  


School Spreadsheet: Target: 4 hours

  


Contact Applications

[ ] The Contact Applications RG is a virtual RG showing applications for the linked contact.

[ ] Virtual RG (sorted by date). 

[ ] RepeatList: Call on ApplicationsByContactNdxConcat with DateSortString+ApplicationID, then SortPipeList to sort by date, then ListSubstitute to extract the ApplicationIDs from the sorted list.

[ ] Columns are just LookupLevelFIelds using the RepeatListItem.

Target: 1 day

  


Create Application:

[ ] Let's have this launch an auto-push report with a New Record button that pops up a new detail screen with values defaulted. If we do an AutoSave on the button the report could run directly against this record. Otherwise you need to pass all the values via ask prompts into a None level report.

Target: 1 day
