4.2. Imports

  


Requirements

TODO_CH: Tim Reitz 02/16/2023: Update sections:

level 1. Imports (include General Notes, if applicable)

level 2. Importing Contacts

level 2. Importing Addresses

level 2. Importing Check-Ins from Badger (existing section, currently called "Importing from Badger")

  


  


Importing Contacts: The Contact import will start importing the following additional fields as new columns on the import file:

  * Sales Rep ID
  * Modify Date
  * Modify Time



  


Note that contacts deleted in CA should be marked as inactive in the AppHosting Solution.

  


Importing Addresses: There will be a new Addresses import that should include the following fields:

  * Organization ID
  * Address ID
  * Address Modify Date/Time
  * All Address fields



  


Note that addresses deleted in CA should be removed from the corresponding Contact in the AppHosting Solution.

  


General Notes:

Each import would have a prompt called "Only Import Updated Contacts" (or addresses). This would be checked by default, but it could be unchecked to force a full import.

  


The date/time will be imported from a single column. The milliseconds (i.e. ".806") can be disregarded. It will be formatted as one of the following:

  * 2018-08-20 17:49:19
  * 2022-08-26 11:12:11.806



  


The Classic Accounting query that feeds the import file will use something like the following for the timestamp: 

  


GREATEST(createdate, moddate) 

  


The import can be run using the Curl or Powershell options in [https://think.apphosting.zone/Services?Name=Import&](https://think.apphosting.zone/Services?Name=Import&). For details for other HTTP clients, see the "REST API" tab after hitting "Generate Command", or contact Matthias for support.

  


Development Specification

Ellis Miller 09/22/2022: Address x30 finds contacts based on Org ID (Classic Accounting ID). RG Import that matches on the Address ID. Deletes unmatches rows from the record.

  


Once this is ready, remove the address fields from the Contact import. 

  


Let's make both the Contact Import and the Address Import use Non-Fixed Headers. Go ahead and enumerate all columns and all change expressions stay the same. This will avoid problems if columns mismatch.
