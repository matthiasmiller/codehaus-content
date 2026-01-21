5.2. Phase 2 - CRM

It's worth exploring whether we can implement a basic CRM as a secondary Phase without derailing Phase 1. These are some partially formulated ideas.

  


In the future, we will need to look at:

  * Integrating the Book Bill process
  * Tracking & reporting on creation date
  * Having the sales manager assign leads by territory
  * Tracking the date and time of the first call
  * Tracking when it goes into estimating, and when it's back in the salesperson's court for presenting



  


Contact Types:

  * Salesperson
  * Customer
  * Integrator
  * Contractor/Dealer
    * pricing level



  


Goal record:

  * Time frame
  * Goal participants
  * Goal
  * Achieved
  * Percent achieved



  


Stage record:

  * Stage name (Class 1, etc.)
  * Stage Status (Won, Lost, Open)
  * Max number of days in Stage



  


Opportunity record:

  * Title (used to store the building description)
  * Workflow (Table Egg, Non-Table Egg, Non-Poultry)
  * Stage
    * Class 1 (asking for a product not being sold)
    * Class 2 (tire kicker)
    * Class 2.5 (potential future lead; follow up in 2 months)
    * Class 3 (ball's in our court)
    * Class 4 (lost)
    * Class 5 (will close in 30 days)
    * Class 6 (old)
  * Date Estimate Sent to Salesman (origination/creation date)
  * Date Last Worked
  * Status
  * Linked Salesperson
  * Linked Customer
  * Linked Project Manager
  * Lead Source
  * Location
  * Integrator
  * Subcategory (workflow-specific)
  * Package Type
    * Package
    * Turnkey
  * Notes
  * Embedded spreadsheet of the following:
    * Meeting Description
    * Date
    * Time
  * Job Status; list of:
    * RFQ Scheduled
    * Contract Meeting Scheduled
  * 5k Deposit (checkbox)
  * 15 Week Bird Date
  * Hostetler Committed Date
  * Contract Amount (number)



  


  


Reports

  * Status for Book Bill --
  * Quoting Queue
  * Leadership Scorecard
  * Department Scorecard
  * Salesperson Scorecard (incl. individual act vs. goal)
  * Sales vs Goal (requires further design)
    * Annual
    * 1st Qtr
    * 2nd Qtr
    * 3rd Qtr
    * 4th Qtr
  * Outdated Leads (leads in a status longer than the max number of days; turning red past the date)
  * Active Leads
  * Additional reports listed in the "Customer Journey / Leads" section


