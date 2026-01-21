4.8.2. Device Record

  


Requirements

Overview: The Solution would use one Device record per printer (or other device / email account) to track details about all of the devices that are managed by Think Ink. Non-managed items also can be tracked, but not all would be.

  


Accessed via: 

  * All Devices Report
  * Devices by Customer Report
  * Home | Devices | New Managed Device (opens a blank new Device record)
  * Home | Devices | New Customer Printer (opens a blank new Device record with Type = Customer Printer; this behavior may change in Phase 4 to accommodate the invoicing process)
  * Etc.



  


Sections and Fields: See following sections

  


Data Access: All users can view and edit

  


Special Considerations:

  * Copy Record: The following sections / fields are cleared / reset to their defaults when a Device record is copied:
    * Serial #
    * Warranty Details section (all fields)
    * Agreement Details section (all fields)
    * Contract Details section (all fields)
    * Page Counts section (all fields)



*TODO_JM: (once we have the record specced out more) Confirm that you want these cleared/reset to default.

  * Delete Record:
    * Prevent deletion if the record is referenced anywhere in the Solution: "This Device record cannot be deleted because it is referenced by another record in the database."
  * Merge Record: N/A



  


Other Notes:

  * If a Device ever was Managed (had the Managed checkbox checked), it should continue show the Managed-specific sections / fields, even if changed to non-Managed. 
  * If a Device started as non-Managed and later is changed to Managed, it does not retain any non-Managed-specific sections / fields.
  * Context for "Initial Invoice": Think Ink buys a printer and when they set it up as a managed device, they create a "sale" to the Customer for $0 so that it can be tracked as a loss (immediate depreciation) for Think Ink. If a managed printer is brought back and deployed for a subsequent (second or more) customer, no expense is tracked.
  * For non-printer Devices (email accounts, wifi hotspots, etc.) the user should select the "Leased Other" type and enter the email address or the IMEI in the Serial # field. 
  * Device IDs are for one serial + customer combination. If the customer cancels, or gets a different device, they get a new Device ID.
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=597400646](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=597400646)

  


TODO_EM: Tim Reitz 07/18/2023: Individual devices should show up as part of the line items on invoices. It would be nice to include managed devices in inventory. If they have a skid of printers in the warehouse, one could be bought outright or given to a customer as a managed device. Should we use a customized SKU / Sales Item record for devices instead of this custom record here? Or can we pull from both SKUs and from Devices for invoice line items?

Tim Reitz 07/19/2023: From conversation with EM today:

Options:

  * Sales Items (no individual records)
  * SKUs (typically for interchangeable goods; costs $150/month)
  * Independent record
  * Accounting Assets (using for AB)



Additional notes

  * Tracking specific devices (calling it "inventory") for managed devices.
  * Not tracking inventory in the warehouse.
  * Managed devices are immediately written off as a loss (totally depreciated).
  * Lots of drop shipping (these items never hitting inventory)



  


  


  


  


Dev Spec for MPS IDs: Index Customer + ID to auto-assign the next sequential number

  


  


  


  


NOTE for CCI: We will need to handle migration from the IncidentDevice text field to the new IncidentDevice list field.

  


HL Est: 24 hours

 Record (lookup or custom?)

  * Adding record: 2 hours
  * 6 simple fields: 2 hours
  * 1 ndx to find the appropriate agreement: 2 hours
  * 5 lookup macros for managed: 2 hours
  * Page count RG (8 fields): 2 hours
  * Prorating macro: 4 hours
  * Report? 4 hours
  * Padding: 4 hours


