5\. Orders

  


Requirements

Overview: The Order record would track details for an order, and would be used to generate cut lists and invoices.

  


Accessed via: 

  * The various orders reports
  * The Orders section on a customer's record
  * A "New Order" menu option that opens a blank order
  * A "Find Order" menu option that prompts for customer, order #, etc. 



  


There are only a few new customers every month, so prioritize order entry for existing customers. The Order will have a New Customer link that can be used to create a new customer. In addition, the Customer will have a link to easily create a new order for that customer.

  


Sections and Fields: 

Order Details section:

  * Order # (auto-set and read-only; this number should start with multiple digits, such as at 1001) 
  * Status (drop list of Quote, Order, Completed, Canceled; default to Order)
  * Customer (required; drop list of Customers, filters down as you type)
  * New Customer (link; opens a new Contact record, defaulted to Customer type) 
  * PO# (text field) 
  * Order Date (required; default to today)
  * Invoice Date (read-only; auto-filled via the QuickBooks sync)
  * ASAP (checkbox)
  * Needed By (date; required if "ASAP" is unchecked)
  * Projected Start Date (auto-set and read-only date; first date with a configurable margin of availability, i.e. 0.25 day)
  * Delivery (required; drop list of:) 
    * Shipped
    * Job Pickup
  * Special Order Request (read-only; shown from Customer record)



  


Order Options section: (apply to ALL drawers on the order; otherwise, write up a separate order):

  * Box Wood Type (required; drop list of Box Wood Types)
  * Bottom Wood Type (required; drop list of Bottom Wood Types)
  * Top Edge (mutually exclusive checkboxes)
    * Square Top (checkbox; checked by default)
    * Radius Top (checkbox)
  * Drawer Box Specs (required; drop list of:)
    * Assembled Unfinished
    * Assembled Finished
    * Assembled Finished Premium
    * Unassembled w/ Bottoms
    * Unassembled w/o Bottoms
  * Inset (mutually exclusive choice between:)
    * Bottom Inset 5/16" (standard) (checked by default)
    * Notch & Drill w/ 1/2" inset for Undermount
  * Drill from Fronts (checkbox)
  * Pull-out Tray Scoop Type (required; drop list of:)
    * Standard Scoop (default)
    * W/O Scoop
    * Big Scoop
  * Pull-out Tray Side Tabs (checkbox)
  * Pull-out Tray Scalloped Sides (checkbox)
  * Logo Branding (checkbox)



  


Drawers section: (embedded spreadsheet; showing up to 22 without scrolling):

  * Columns: 
    * Line # (autonumbered from 1 to N; read-only)
    * Qty (required; number; 1 decimal)
    * Height (required; number; 2 decimals)
    * Width (required; number; 2 decimals)
    * Depth (required; number; 2 decimals)
    * Combination (optional; drop list of items in the Drawer Combinations SKU category) 
      * Selecting this will auto-fill the associated components. And similarly, selecting the correct components(s) will auto-fill the combination.
      * Allow entering an item that is NOT in the list.
    * Components (drop list of components; editable if there is only a single component for the drawer; ellipsis button in an adjacent column for multiple components) 
    * Comments (text)
    * Price (auto-filled and editable) 
  * Buttons to add and remove rows from the embedded spreadsheet ("Add"/"Remove")
  * Buttons to move rows up and down ("Up"/"Down") 



  


Components section: (embedded spreadsheet; reflects components in the Drawers embedded spreadsheet)

  * Columns: 
    * Drawer (optional drop list of Line #'s from above; automatically updates to reflect moved rows in top spreadsheet)
    * Qty (required; number; 1 decimal)
    * Component (required; drop list of components; allow entering an item that is NOT in the list)
    * Price (auto-filled and editable) 
    * Total (auto-calculated and read-only)
  * Buttons to add and remove rows from the embedded spreadsheet ("Add"/"Remove")
  * Buttons to move rows up and down ("Up"/"Down") 



  


Pricing section:

  * Terms (optional; drop list of Invoice Terms) 
  * Discount $ (optional; number; 2 decimals) 
  * Subtotal $ (auto-calculated and read-only) 
  * Tax % (auto-filled from the customer record; read-only)
  * Tax $ (auto-calculated and read-only)
  * Grand Total $ (auto-calculated and read-only)



  


  


Data Access: Available to all users

  


Other Notes:

  * It would be ideal for the Order screen in the software and the Order printout to be very similar in layout, to maximize data entry efficiency.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1OqUDF4OUPjb-Z316DR8yjVsdRxG1O0MgsJmPVcwBhtE/edit#gid=1526134269](https://docs.google.com/spreadsheets/d/1OqUDF4OUPjb-Z316DR8yjVsdRxG1O0MgsJmPVcwBhtE/edit#gid=1526134269)

  


TODO_IDD: How many of these should actually be required, and how many should be warn on save? Reason: If a customer leaves out some info that isn't caught until the order is being entered into the database, we want to be able to save the order while waiting on an answer from the customer.

  


TODO_IDD: Add a section and spec out more

Find Order (opens a prompt page with the following fields:)

  * Customer (drop list of customers; filters down as you type
  * Order #
  * other?



Opens the order directly if only 1 match; otherwise opens the All Orders report, filtered accordingly.
