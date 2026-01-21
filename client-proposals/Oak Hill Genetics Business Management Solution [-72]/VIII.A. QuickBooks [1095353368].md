8.1. QuickBooks

  


Requirements

The software will integrate with QuickBooks Premier Desktop edition.

  


  * Sales Items, Classes, and Sales Item Tax Designations, and Customers will be automatically synced from QuickBooks into the software.



  


  * Estimates and Invoices will be created in the software, then be automatically synced to QuickBooks. Once the Estimate and Invoice is synced to QuickBooks, QuickBooks will become the source of truth and any further modifications will be synced back to the software.



  


Technical Details:

  


  * This will likely include software that will run on the server, watching for AppHosting events that require a sync to QuickBooks. When this happens, this software will first check for any updates to invoices and estimates in QuickBooks, and will apply them based on the assigned Order #. Then, any new estimates and invoices in the AppHosting system will be pushed to QuickBooks with a custom field that links it back to the order. (We will need to consider custom line item fields, such as PI.)



  


  * All QuickBooks items will be monitored on a configurable time interval to push back into AppHosting.



  


  * The latest sync date/time, as well as success/error information, will be automatically pushed into AppHosting as well.



  


  * During deployment, we will need to make sure we can reasonably reconcile all QuickBooks contacts with preexisting contacts, since that sync has not been working recently.



  


  * Most likely, third-party software will be used as part of the bridge with QuickBooks.



  


Development Specification

The monitor would be set based on activity records for new estimate/invoice records. We'd use an index to make it super-fast -- possibly a QueryRecords call?
