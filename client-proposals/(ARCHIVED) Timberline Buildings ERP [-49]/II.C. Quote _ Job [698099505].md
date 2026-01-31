2.3. Quote / Job

  


Requirements

The Quote and Job will be two statuses for the same record. Once the contract for a Quote has been signed by the customer, the Quote will be advanced to a Job.

  


There will be three types:

  * Construction
  * Change Order
  * Warranty



  


The Quote/Job record will track the same information as displayed on the TPS, such as: 

  * Job Code (auto-generated; format to be determined)
  * Customer Details (e.g. name, phone, address, etc.; auto-filled by selecting a customer from a drop list; can add a new customer contact if needed) 
  * Job Details (e.g. date of contract, salesperson, job location, travel info, county, zone, design data, etc.)
  * Building Details (e.g. size, style, doors, windows, eaves, roofing, insulation, concrete, etc., as well as misc items and a notes memo) 



  


It will also have additional fields and features, such as: 

  * Crew Only Notes memo
  * Ability to create & print proposal and contract PDFs from this page



  


Each section will be tied out to one of the following Construction phases:

  * Framing
  * Stone
  * Grade
  * Concrete
  * Gutter
  * Doors
  * Interior
  * Ceiling Ins.
  * Other



  


Each of the phases will have a "Subcontract" checkbox. When selected, it would show a drop list of subcontractors. Selecting a subcontractor would default the subcontractor hourly rate. The hourly rate could be edited as necessary. Subcontract phases would allow entering the number of hours for that phase.

  


Scheduling and Production should have a visual cue that they've activated a phase, and tha an invoice is due.

  


The Quote/Job record will also have an embedded spreadsheet for custom options.

  


The details will become read-only after the contract is signed. To make changes after that, the job will show a "Start Change Request" option. This will make the options editable again. It will generate a new Change Request.

  


It will also need to track progress, such as:

  * Quote Ready for Review
    * The job will almost always move ahead into drafting.
    * At times, it will also go back to sales for further information.
  * Quote Ready for Drafting
  * Quote Ready for Contract
  * Etc



  


It will also track other progress, such as:

  * Customer Permits
  * 1 Call
  * Scheduled Build Date
  * Phase Status (In Progress / Complete)



  


Normally, jobs need to be completed on a first-come, first-served basis. However, in the case of an emergency (fire, etc), the scheduled date needs to be able to be changed or overridden.

  


It will track the progress of special order items. For each it, track:

  * Available Date
  * Delivery Date
  * Delivered On (date)
  * Delivered To (location)



  


Allow a custom SKU for one-off items.

  


Warranty work would include a list of miscellaneous items. It would track customer information. The quote would include remobilization (percentage over book price). This needs to be included in a special warranty agreement.

  


For example, if the customer calls a month after a building is completed and reports that the door latch isn't working, it will be reported in a Warranty Work Order.

  


The job will include a note if pricing differs, such as "Proposal price differs from current pricing by $__." with a "Update Pricing" button.

  


The job will have an embedded spreadsheet to track payments towards the job. Typically, projects are invoiced with a 25% deposit at signing, 65% construction draw (due when starting), and 10% retainage at final completion. The final invoice will show a statement-like view with all charges, all payments, and the remaining balance.

  


Each job will need to track additional expenses besides material and labor, such as:

  * Rentals
  * Disposal
  * COGS (i.e. jog lodging and per diem meal allowance)



These would be linked to a QuickBooks expense category and pushed across to the general ledger.

  


The job will need to support:

  * Refunds (most frequently, a partial refund of the deposit)
  * Discounts Prior to Sale (usually 3-4% by the salesperson for a project worth the investment)
  * Discounts After the Sale (usually to compensate for repairs required by customer; taken from retainage)



  


The Quote/Job record will have the following printouts (see the corresponding sections of this proposal for more details):

  * Quote
  * Initial Contract
  * Change Request
  * Job Work Sheet



  


Development Specification

NOTE: For inventory management etc, I think we'll need a lengthy macro that translates all the fields into a hidden RG with:

  * Contract Version (Perhaps 0 for initial contract, and 1..N for change requests)
  * Phase
  * Qty
  * Item Code
  * Desc
  * Price



  


TODO_IDD - presumably they can change it anytime until the phase is done?

  


DONE_CH: How to handle change orders? (video - around 1:45-47)

TODO_IDD - The change order might not be a record type. We could consider a custom DB level with subtypes for Warranty / Constructrion

  


TODO_IDD: How often do you have jobs out of town that require crew lodging & meals? Is it frequently enough that it would be helpful to track/document those plans/details in TOS?
