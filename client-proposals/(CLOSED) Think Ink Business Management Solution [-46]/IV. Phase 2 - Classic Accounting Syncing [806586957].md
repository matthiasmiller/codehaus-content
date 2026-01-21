4\. Phase 2 - Classic Accounting Syncing

  


Requirements

TODO_CH: Tim Reitz 02/16/2023: archive this section (I think).

  


The following will be included in Phase 2, which is to be deployed with Phase 1. 

  


There will be two imports to update contacts from Classic Accounting:

  * The first import should update the main Contact record.
  * The second import should update an Addresses table on the Contact record.



  


Development Specification

Tim Reitz 09/12/2022: See [[[IN6696](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-6698&)]] - ZTK - Classic Accounting Contact Imports.

  


[ ] We'd need to index on date/time so that we can quickly skip records that have not been updated. This will be running frequently. -- Record to Update uses Contact Classic Account ID Ndx Find. Skip Input Line would use CAIDAndLastMod.ndx.  

[ ] Use an x30list for the Contacts -- the first import skips any items that are current, and the second import deactivates any items that are not in the input file \-- only imports OrgID from the input file, matches on that field, no change expressions, set Advanced "unmatched records" to Update with Subset of:

Not IsNA( ContactCAID) AND ContactActive

Change expression: 

ContactActive = false

4 hrs.

[ ] Always import all addresses regardless Modify Date/Time. (We can always optimize it in the future if the X30 is too slow.)

[ ] Make sure that the record isn't updated if none of the address data has changed. Test this by opening the record in edit mode with a few changes, run an import that contains address data that record. If the data changes the open detail screen should say "You cannot save your changes". If the data doesn't change, you should be able to save.

4 hours

  


Sales Rep tie-in is coded already and took us 0.29 days.
