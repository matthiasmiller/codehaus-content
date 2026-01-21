22.1. Syncing with Classic Accounting

  


Requirements

Overview

The Solution will include a sync from the Classic Accounting software to the AppHosting Solution. This will sync the following:

  * Contacts
  * Addresses
  * Invoices (to be done in a later phase)
  * Sales Items/SKUs (to be done in a later phase)



  


The information from CA would first be synced to the read-only Classic Accounting Contact and Classic Accounting Address records (see corresponding sections of this proposal), then merged into the standard AppHosting Contact records. All fields synced from CA would be read-only in the AppHosting Solution (therefore changes need to be made in CA, then synced over), and the fields specific to the Solution will not be synced back to CA.

  


Interface

There will be a Sync Now menu option in the "Classic Accounting" section on the Advanced menu that will open a simple page with three buttons:

  * Sync Created/Modified Contacts (for all users)
  * Sync Created Contacts (for all users)
  * Sync All Contacts (for admin users only)



  


Behaviors

Duplicate Contact names will produce an error when syncing (and will need to be cleaned up in CA to be successfully synced).

  


The Classic Accounting discriminator (Org Name Extension) needs to match the Contact Type in the AppHosting Solution. If a matching Contact Type does not exist, the sync will automatically create that Contact Type in the AppHosting Solution.

  


Addresses will be imported as follows:

  * If the CA Address Type is "BILLTO", the address is imported as a Billing address. If it is "SHIPTO", it is imported as a Shipping address. Otherwise the AppHosting address type it not set. 
  * Addresses will be ordered as follows:
    * By Address Type: The Billing address(es) will be imported first, followed by the Shipping address(es). Typically there will be only one Billing address. Multiple Billing addresses will be added in the order they were entered in Classic Accounting.
    * By Default setting: If an address is specified as default, it will be first listed within that address type.
    * Entry order: Finally addresses will be sorted by the order they were entered in Classic Accounting (CA Address ID). 
  * Inactive addresses will be excluded from the sync.



  


If a contact is deleted from Classic Accounting, the corresponding AppHosting Contact will be marked inactive. If this was done mistakenly:

  * Create a new contact in Classic Accounting with a new name
  * Sync contacts
  * Merge the old, inactive AppHosting contact with the newly created AppHosting contact
  * Optionally change the name in Classic Accounting back to the desired name and sync again



  


Sync Setup

The Classic Accounting sync will be installed on the local server and will be accessible via a URL that must be configured in the AppHosting system.

  


The sync settings will be controlled by a configuration file C:\Users\<UserName>\AppData\Local\AppHosting.zone\ClassicAccountingSync\ClassicAccountingSync.conf. It will be formatted as follows:

  


[Server]

Host=

Port=8080

  


[AppHosting]

URL=[https://think.apphosting.zone](https://think.apphosting.zone)

Username=classic_accounting_sync

Password=password1234

  


[ClassicAccounting]

Database=classic_accounting_db

Port=1234

Username=postgres

Password=true

  


[Sync]

SyncMinutes=15

  


The Classic Accounting Sync will have a basic installer. It will:

  * Require the AppHosting settings to be configured first.
  * Confirm the Classic Accounting settings
  * Confirm the Server settings
  * Set the "Classic Accounting Sync URL" system switch in AppHosting
  * Configure a Windows service to start automatically on startup



  


Development Specification

CCI's Portion

Create an Std Sync CA to AppHosting.x30list that syncs from the Classic Accounting records in the database to the contacts.

It should run three x30's -- one to create contacts, one to update contacts, one to deactivate contacts.

  


[ ] Create a Std Sync CA - New Contacts.r20 that shows all classic accounting records that do not have a Contact linked to that ID.

[ ] Requires a ContactsByCAContactID.ndx -- that is 4-byte CAContactID + 4-byte Contact ID

[ ] Subset is simply NOT ContactsByCAContactIDNdxFindField(..., true)

[ ] Columns: CA Contact ID, Contact Name

BID: 4 Hours

[ ] Run an Std Sync CA - New Contacts.x30 that creates blank Contact records for all new contacts (uses above report as input).

  * Populate name (to avoid validation).
  * Populate CA Contact ID. -- Add validation that CA Contact ID cannot be duplicated.



BID: 2 Hours

  


[ ] Std Sync CA - Update Contacts.r20 of all Contacts that are out-of-date

  * Create an index of CA Addresses by Org ID CAAddressesByOrgID.ndx -- 4 byte Org ID + 4 byte Address ID.
  * Create an index of all activity for Classic Accounting Contacts (CA ID + Activity ID) ContactActivityByCAContactID.ndx. Skip any activity that is not for CA Contact records.
  * Same for Classic Accounting Addresses AddressActivitybyCAAddressID.ndx



BID: 4 hours.

  


  * Ellis & Nahian will code: Create a Macro CAContactActivityVersion(vCAContactID) that returns the Latest Activity version for vCAContactID based on ContactActivityByCAContactID.ndx, and for all related addresses based on all addresses for org (CAAddressesByOrgID.ndx) and then  ContactActivityByCAContactID.ndx. 



BID: 4 hours (equiv)

  


  * Add a new ContactLastSyncedActivity numeric field not visible on detail screen. BID: 1 hour
  * Report for all contacts where CAContactActivityVersion > ContactLastSyncedActivity with one column for ContactName. BID: 1 hour



[ ] Run Std Sync CA - Update Contacts.x30 that matches on the ContactName column.

  * Sets the Contact Active field to true (any contact in CA is considered active).
  * Uses Change expressions to update all fields by doing an NdxFindField based on the CA ID
  * Repopulate entire Phone/Address/Email RGs 
    * Phone is pretty simple -- blank out the RG, Add row for Phone1 if avail, Phone 2 if avail, Fax if avail.
    * Addresses:
      * Create a AddressRecordFromCAAddress(vIncludeSortOrder) macro that evaluates on a CA Address and calls AddressRecord(...) with the CAAddress fields, leaving Contact/Org blank. If vIncludeSortOrder is true, prefix a SortOrder= line to the address that is formatted for sorting. We can create a CAAddressSortID that is defined something like:



if (CAAddressType="BillTo", 'A', 'B') + if (CAAddressDefault, 'A', 'B') + String(CAAddressID, 10, 0)

  * Create a local macro in the x30 locAddressData that returns a pipe-list of all of the addresses for this contact, using the CAAddressesByOrgID.ndx and calling AddressRecordFromCAAddress.  For safety, have it remove any pipes from the result. Call SortPipeList so that it is sorted by the SortOrder= line.
  * Create local macros that return pipe lists for each of the address fields (e.g. locAddressStates). The macros simply do a ListSubstitute on locAddressData calling AddressRecordState(ListSubstituteItem), etc. This gives us easy values for the FillRGFromPipeList
  * The x30 should blank out all of the addresses and then call FillRGFromPipeList over and over for every field. ContactAddressState = FillRGFromPipeList:locAddressStates
  * Test this carefully with various fields blank. If we fill in City first, what if the first city is blank, etc.


  * Set ContactLastSyncedActivity to CAContactActivityVersion 



BID: 3 days

  


TODO_EM: Correct spec

[ ] Create a Std Sync CA - Deactivate Contacts.x30 that deactivates contacts that no longer have an associated CA Contact record. Let's feed this with a Std Sync CA - Deactive Contacts.r20 that runs on Contact records and checks for:

{ We have a ContactCAContactID that is no longer valid. }

NOT IsNA( ContactCAContactID) AND 

NOT CAContactsNdxFindField( BinString( ContactCAContactID, 4), true) AND 

{ The contact is still active }

ContactIsActive

The report will just have a column of ContactName. The x30 will set the contact as inactive.

BID: 2 hours

  


  


[ ] On Copy Contact, clear the Classic Accounting ID.

  


Matthias's Portion

Matthias's Notes:

[ ] Add a "Service Classic Accounting Setup" x30 that prompts for a URL and updates the URL system switch, and set the AppHostingWsgiHmacKey if it's blank.

  


[ ] Very simple installer that checks for "setup" executable name, and if it's not in the install folder, prompt for a confirmation to install. In that case, copy to the Install folder.

  * Require running as admin - [https://raccoon.ninja/en/dev/using-python-to-check-if-the-application-is-running-as-an-administrator/](https://raccoon.ninja/en/dev/using-python-to-check-if-the-application-is-running-as-an-administrator/)



  


[ ] win32serviceutil ala [https://thepythoncorner.com/posts/2018-08-01-how-to-create-a-windows-service-in-python/](https://thepythoncorner.com/posts/2018-08-01-how-to-create-a-windows-service-in-python/)

\--startup auto

  


[ ] Use HMAC authentication

  


[ ] The Sync Now button should pass an HMAC through with the user ID.

  


Lists to use:

[ ] DetailScreenOrderedFieldNames

[ ] DatabaseLevels

[ ] Create a ClassicAccountingFields list that has the names of all of those fields

[ ] Add catalog validation that all ExpressionCodeLevel is non-blank for each of these fields, and that each field name starts with "Level__"

  


  


  


Indexes:

[ ] Activity-level index (RepeatRG) for all database levels that starts with "CA_" and for all modified field names that end with "__CreateDate", "__ModDate", "__Mod_Date", or "__Create_Date". Use a BinString(ListNum(ActivityLevel),4) + a 23-character date/time (i.e. "2022-08-09 10:37:55.388")

[ ] Create a macro that takes a database level and returns the latest mod/create date directly from the index (without hitting disk)

[ ] Create a "Std Service Classic Accounting Sync.r20". It should be an any-level report, totals and subtotals only, JSON report, that returns:

  * Database Level
  * Fields (pipe list)
  * Last Sync Date (from index above)



  


  


For the syncing process:

[ ] Run the above report

[ ] For each of those levels:

[ ] Find the latest created/mod date in the database. Run a SQL query to pull all records created after the latest one. Import all of those into the Classic Accounting records.

[ ] Do the same thing for addresses.

  


[ ] Run the x30list above

  


[ ] Run the CleanUpList for the SalesRep list

  


[ ] Occasionally do a full sync watching for dropped addresses and contacts and flag them as deleted.
