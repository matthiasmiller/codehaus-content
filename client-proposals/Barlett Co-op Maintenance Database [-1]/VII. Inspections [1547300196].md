7\. Inspections

  


Requirements

Inspections Report

The Inspection report will prompt for Inspection Type, Location, Equipment Type, Inspection By. Users can select one or more of any of these options.

  


It will also have options for:

Show completed inspections - checkbox defaults to checked to include completed inspections

Completed in past [___] days - defaults to past 30 days. Blank will include all completed inspections

Show open inspections - defaults to checked

Show upcoming inspections - defaults to checked

Due in next [_____] days - defaults 30 next 30 days. If blank, it will show any upcoming inspections

  


The report will have three groups:

Completed Inspections

Open Inspections

Upcoming Inspections

  


It will default to being sorted by Date (most recent completed date for completed items and first due dates for open/upcoming items). The due date is based on the inspection schedule defined on the Inspection Template. Users can click sort by other column values (e.g. Location). 

  


The report will have columns for:

  * Equipment Type
  * Location
  * Equipment Name
  * Status - Upcoming, Open, Closed
  * Date - Due date for open/upcoming inspections, completed date for completed inspections
  * # Notes - Number of notes entered, alerting the viewer that there is interesting information in the inspection
  * # Work Orders - The number of work orders. A link displaying the number of work orders. Clicking the link will display the work orders with their status.
  * Inspection By - Name of person doing inspection.
  * Inspection Type



  


Inspection Record

  * Inspection by: Name of person doing inspection, defaults to the current user's name. Can be modified.
  * Date: Defaults to the date the inspection was created, can be modified if needed.
  * Status: list defaulting to "Open" with options for "Cancelled" and "Complete". When "Complete" is specified, a Completion Date is filled in and the record becomes read-only.
  * Inspection Type:  Inspection template name (e.g. "Anhydrous Tank Inspection")
  * Equipment: Equipment name if equipment-specific. Will be filled in automatically when creating inspection. This will be a link to display the equipment record.
  * Current mileage/hours displayed ("90,000 miles as-of 04/10/2017"). If this is more than a week old, show a red label "Please update the mileage/hours on the equipment record."  If the equipment piece tracks mileage/hours, don't allow completing the work order if the record is more than a week old.



  


We will display a list of work orders from this inspection, with open work orders at the top of the list. This list includes work orders created for specific questions (see below). We will include a link to create a general work order for this inspection because sometimes an issue may be noticed that is not related to a specific question.

  


List of questions (from the inspection template). Each question will have:

  * Label
  * Prompt (text box for numbers, strings, and dates, two checkboxes for Yes/No, listbox for lists).
  * Notes field
  * New Work Order -- this link will display a new work order for this equipment piece. If a work order is already created, it will show text "Pending Work Order" or "Closed Work Order" based on the work order status. When creating the work order will have a link back to the inspection and the work order title will be filled in with the "Inspection Issue: " \+ Question Issue. For example: "Inspection Issue: Brake lines OK?"



  


Development Specification

Need a hidden ask prompt for Equipment ID so that we can add an "Inspections" link to the equipment and be able to click into it.

  


Upcoming Inspections is tricky. This report will actually be a New Record spd.

  


"New Work Order" link should be hidden when not in edit mode.

  


  


Could have multiple form types for a given inspection type.

Search inspections by Inspection Type, Location, Equipment Type

  


Inspection Status: Open vs Closed (probably checkbox)

  


  


We need "Add Work Order" for the entire record and may create multiple. (possibly Add button to create the work order on each line item from inspection). We want a list of work orders on the inspection record along with their status. In the inspection report, highlight inspections with outstanding work orders.
