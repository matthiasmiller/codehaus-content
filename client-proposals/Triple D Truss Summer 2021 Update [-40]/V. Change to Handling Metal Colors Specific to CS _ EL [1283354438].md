5\. Change to Handling Metal Colors Specific to CS / EL

  


Requirements

Some Central States metal colors are only available for their Prime or Ultra lines (e.g. Crimson). After some discussion of ideas, the plan is to take the simple approach of adding a suffix such as "(Prime)" or "(P)" to the end of the items on the current list. However, the current main colors lists not editable.

  * Make changes to allow users to control both the Central States and Everlast colors lists.



  


Time Estimate: 1 day

  


Development Specification

From [[[IN5018](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-5020&)]] - ZTD - Metal Colors Specific to CS / EL: 

Some Central States metal colors are only available for their Prime or Ultra lines (e.g. Crimson). After some discussion and CH sharing some ideas, John was fine with the simple approach of adding a suffix such as "(Prime)" or "(P)" to the end of the items on the current list. 

However, the current main colors lists are shipped and they can't edit/delete the items. Let's drop the shipping and allow them to control both the Central States and Everlast colors lists. These are currently simple lists. 

  


Tim Reitz 06/29/2021: From Ellis: 

  * Prefix each of the list items with Changeable: to make so that the user can modify / delete them.
  * Change the two color lists to be lookup lists with an Active checkbox.  Disallow deleting referenced lookup items.
  * Change helper lists to only show active ones.



Estimate: 1 day for all of this. 

(If needed) We should have instructions on how to clean up / add items to the lists after the update.
