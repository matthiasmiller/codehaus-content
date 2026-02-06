4\. Method to Differentiate Between CS and EL Trim Items

  


Requirements

Triple D would like a way to differentiate between Central States and Everlast trim items. 

  


This involves some coding work and some cleanup and migration of data. 

  


  


SKUs: 

  * Add "CS" and "EL" as suffixes to Central States and Everlast SKUs, respectively. 
  *  If a SKU does not have either suffix, it will be considered a "general" metal item. 



  


Quote/Order page: 

  * Have the Central States and Everlast checkboxes above the Metal order control which SKUs are available on the Description drop list - show the corresponding items (based on their suffixes) plus all general items.
  * Make the Central States & Everlast checkboxes be read-only after one item of the corresponding type has been added to the order. But still allow switching the checkbox if only general items have been added.



  


  


Time Estimate: 2 days

  


Development Specification

Tim Reitz 08/06/2021: See [[[IN4410](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-4412&)]] - ZTD - Method to Differentiate Between CS and EL Trim Items (in MYS).

  


John wondered if there could be a way to differentiate between Central States and Everlast trim items. They have different prices. 

  


We should: 

  * Create a SKU export
    * 2-4 hours (CCI) 
  * Add an Active column to the export/import
    * 2-4 hours (CCI) 
  * Cleanup & Migration (CH)
    * Export the current SKUs list
    * Rework things in Excel (creating 2 new SKUs to replace each one that needs to be deactivated/replaced). 
    * Deactivate the unneeded SKUs
    * Re-import the (new) list
    * 1 day for data cleanup & migration (CH)  



Misc: 

  * We would need their new list(s). John said there would be about 50 items currently. 
  * We would need to do some cleanup/rearranging of the new list. 
  * We'll need to coordinate a day or so where they don't make changes in their system. 



  


  


Additional Design: 

  


SKUs: 

  * Add "CS" and "EL" as suffixes to Central States and Everlast SKUs, respectively. 
  *  If a SKU does not have either suffix, it will be considered a "general" metal item. 



  


Quote/Order page: 

  * Have the Central States and Everlast checkboxes above the Metal order control which SKUs are available on the Description drop list - show the corresponding items (based on their suffixes) plus all general items.
  * Make the Central States & Everlast checkboxes be read-only after one item of the corresponding type has been added to the order. But still allow switching the checkbox if only general items have been added.



  


  


Todo CH: 

  * Export all SKUs from live system
  * Pull out Metal SKUs
  * Identify and separate the items that are to be the general items
  * Duplicate the rest of the list and have one copy for EL and one copy for CS
  * Add suffixes to the duplicates: 
    * "\- CS"  for Central States
    * " \- EL" for Everlast 
  * Re-import all Metal items



  


ZTD will take care of cleanup in their live system (deactivating the unwanted new ones)

  


Tim Reitz 08/19/2021: Time estimate: 2 days.
