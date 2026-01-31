4.6.2. Online Submissions

  


Requirements

AppHosting will provide an online application form for new members. This is detailed in a separate section.

  


When the form is submitted, it will create an Online Submission record. This record should include an application date.

  


Show a drop-list at the top, showing all contacts that match on:

  * EIN (if both left/right sides are businesses)
  * SSN (if both left/right sides are individuals)
  * Name
  * Phone Number
  * Email



  


The list would show the list of possible matches:

  * Mullet, Joseph R. #0010
  * Mullet, Joe #0134
  * Mullet, J. R. #0407
  * Mullet, Joseph Reagan #0391



  


The list would also include a blank item (in case none of the existing contacts are the right one).

  


The Member Information section would be in a two column layout:

Person/Business Information from Online Submission (see Online Member Application section).  
These will be editable to allow corrections as needed.| Show the corresponding fields from the contact record. Both sides should be bold and purple if they match between both sides.  
---|---  
  
  


Show a button called "Create Contact" (if no linked contact is selected). This would create a new contact, then update the online submission with the new contact. If a linked contact is selected, show an "Update Contact" button to update the contact with the information from the application.

  


The SPE will be responsible for updating and correcting any information from the online submission before updating the contact.

  


The School Designations section would include an embedded spreadsheet of member applications for the selected contact and calendar year.

Application Status| Application Date| Application Amount| Link to View  
---|---|---|---  
  
|   
|   
| (Open)  
  
  


The School Designations would be an embedded spreadsheet:

SPE School Name  
| SPE School County| Application School Name| Application School County| Application School Contact Name| Application School Contact Phone| Application School Contact Email  
---|---|---|---|---|---|---  
If Matching| If Matching|   
|   
|   
|   
|   
  
  
|   
|   
|   
|   
|   
|   
  
  
  


Once the submission has been linked to a contact and all designations have been linked to SPE schools, show a button called "Create Application". This would create an application for the selected contact. (The online submission is never used to update an existing application. However, it may be used for existing members to submit new applications when applying for additional amounts.)

  


The Online Submission will have a "Closed" checkbox that will allow archiving the submission once it has been processed or noted as a duplicate.

  


Development Specification

Ellis Miller 02/08/2021: 

[ ] TODO_CH: Not seeing application date in mockups

  


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
