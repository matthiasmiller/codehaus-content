13\. Data Migration

  


Requirements

The process of importing and cleaning up migrated data will be done by CodeCrafters in coordination with Symbiz. CCI/CH will provide spreadsheet templates to facilitate the importing of data from Salesforce and other sources into the Solution. Symbiz and CCI/CH will work together to do the actual migration of data, and an initial test with real data may be done in a separate "deploy" system if desired.

  


The following data will be migrated into the Solution: 

  * Contacts (from Salesforce) 
    * Leads 
    * Members 
    * Organizations 
  * Growth Ring Groups (from Salesforce)



  


Symbiz is anticipating the following numbers for imports at the time of deployment of Phase 1:

  * Leads: 250
  * Members: 500
  * Growth Ring Groups: 70



  


Following is the anticipated sequence for running the imports for migration:

  * Run the Organizations import
  * Configure the Industries. (An industry must be created for every unique Industry listed on the import files.)
  * Run the Leads import
  * Run the Members import
  * Run the Set Member Organizations import
  * Run the Groups import (the "Facilitator" column sets the first row of the Members tables) 
  * Run the Add Members to Groups import



  


Possible Imports:

  * Development Resources (from a spreadsheet)
  * Development Resource Reviews (from a spreadsheet)



  


This proposal includes 24 man hours of data migration time by CCI/CH. Additional time may be billed on a per-hour / T&M basis.

  


Other Notes:

  * N/A



  


Development Specification

Ben Reitz 06/15/2023: Folder of import spreadsheets: [https://drive.google.com/drive/u/0/folders/1ums2RA_Fg8cOPPhBv9xw6cD_Aj-aLhsg](https://drive.google.com/drive/u/0/folders/1ums2RA_Fg8cOPPhBv9xw6cD_Aj-aLhsg)

  


  


  


\---------------------------

  


Tim Reitz 12/12/2023: Data migration sequence (current as of today): 

  * Set up Lead Sources 
  * Set up Industries 
  * Set up Church Affiliations 
  * Run the Organizations import Std Migration - Organizations
  * Run the Leads import Std Migration - Leads
  * Prepare the Members import: 
    * Run diffcheck on Member Home vs Mobile numbers to make sure we aren't missing any.
    * Copy Group Member Since date into Paid Membership Start date column
  * Run the Members import Std Migration - Members
  * Set up Regions (so that the Groups import can set the required Region field)
    * Include a generic "Placeholder Region"
  * Make sure the Region column on the Groups import file is filled in 
    * _IDD: tbd
  * Run the Groups import Std Migration - Growth Ring Groups (the "Facilitator" column sets the first row of the Members tables)
  * Run the import to add members to growth ring groups Std Migration - Add Members to Growth Ring Groups (to set the rest of the rows of the Members tables in the Groups; does not re-add a row for the Facilitator)



  


Jonathan Bergen 12/11/2023: Notes and questions for data migration:

  * The Contact is Active column is only set for a few contacts. I'm ignoring this, and setting all imported contacts to active.
    * Tim Reitz 12/12/2023: This sounds good. 
  * DONE_IDD How do we know which members are online members? The Internet Access column is empty.
    * _JB: Tim Reitz 12/12/2023: Good question. I guess we should ask the client if they are able to set the field in Salesforce before doing the full/final migration. 
    * Tim Reitz 12/12/2023: We've asked the client, and they said they'd take care of it. 
  * DONE_IDD How is the region for each group specified?
    * _JB: Tim Reitz 12/12/2023: They apparently aren't tracking this yet (regions are relatively new). Two options I'm seeing: 



1\. Can we make Region field on the Group record not required for imported records (but have a warning on save instead)? That way we can import the Groups without the Regions, then the admins can fill them in later (and maybe we could give them an editable report to fill them in faster). 

2\. We could include the column on the import file, and have the client fill in the column before we import it (or we could fill it in with a generic "Placeholder Region" for all Groups, that would be changed later). 

Tim Reitz 12/12/2023: Per Ellis, let's do #2. 

  * Since we don't have the saleforce ID listed for the facilitators on the grg import file, we'll have to check manually that we can match on first and last name alone.
    * _JB: Tim Reitz 12/12/2023: Ok. Or would it be faster to find the Salesforce ID for each facilitator and manually put that into the import file? 
    * Tim Reitz 12/12/2023: Jonathan confirmed that the Facilitators do all have unique names, so we should be able to just go with that. 
  *  We don't have the info to fill in the membership details section. If we import the contacts and fill the ContactMembershipIsActive box in the import, I foresee issues with how our renewal logic works. It would be awesome to have real values to fill in for the Initial Invoice Sent date field, etc.
    * Tim Reitz 12/12/2023: List of fields that we will import (all other client: 
      * Paid Membership Start (date) (default to the Group Member Since date) 
      * ?Renewal Payment Received date (imported from QuickBooks)
      * ?Membership End Date (required field)
      * ?Initial Payment Received (default to the Group Member Since date) 
    * DONE_JB / DONE_EM: Tim Reitz 12/12/2023: Should we try to import renewal information for members who have been members for more than 1 year? Or just start out all members as if this were their first year?
      * Tim Reitz 12/12/2023: Ben is emailing the client to ask if they currently track the Renewal Payment Received Date (or some other date to mark the renewal). 



_IDD: Ben Reitz 12/13/2023: Client said that they're currently tracking this in QuickBooks.

Ben Reitz 12/20/2023: We probably should ask them to give us an export of this (columns for the Member's name, Salesforce ID [or whatever they use to keep track of contacts between the 2 systems], and Renewal Payment Received Date. 

  


TR: Do we also need a date for the upcoming renewal? 

DONE_EM: Ben Reitz 12/20/2023: Should we pursue this or just import all Members as first-year members?

Tim Reitz 12/21/2023: Per Ellis, let's just base the renewal date off of the original start date. 

  * DONE_JB / DONE_EM: Tim Reitz 12/12/2023: Should we try to import historical (inactive past) members? Or only import currently active members? 
    * Tim Reitz 12/12/2023: Ellis thinks they will want to have this. Ben is emailing the client to ask them to make sure all inactive (past) members are marked as inactive, and asking if they can provide a membership end date to go along with the status. Anything not marked as inactive will be imported as active (including blank entries). 



_IDD: Ben Reitz 12/13/2023: Client said that if they have the correct status column, it should be very current, as they have gone through and cleaned it up.

Ben Reitz 12/20/2023: TR: We probably should make sure we're looking at the same / correct column. Have they cleaned it up since they sent us the file or had they already cleaned it up when they sent us the file? If it was before they sent us the file, then we're probably not looking at the same column.

  * Tim Reitz 12/12/2023: Also ask the client if they are fine with us defaulting all imported members' Initial Payment Received date to the existing Group Member Since date. 



_IDD: Ben Reitz 12/20/2023: Client: I don't see why it would hurt to change the initial payment to that date even if it's not entirely accurate. Some joined and paid later as we didn't quite have our system in place. Maybe one of the others would have a different thought.

_JB: Ben Reitz 12/20/2023: You can go ahead and make this change.

  * There a handful of contacts that are missing addresses, or have an invalid email address. I'll plan to note all of these contacts when doing the import, and let Symbiz update them in the live system.



_IDD: Ben Reitz 12/20/2023: Client: We are working on this currently, but I can assure you, some of this will not be available because it is not existent. Could you please send a list of emails that bounced?

_JB: Tim Reitz 12/12/2023: Since we'd be doing the full/final import later, I think my vote would be to get a list of the names and ask the client to update them in Salesforce prior to giving us the final export file.

_EM: Ben Reitz 12/20/2023: Are you fine with a warning instead?
