2\. Delivery Record

  


Requirements

Delivery Section:

  * Will Call (checkbox; this is used to indicate that the customer will call back to schedule; have a warning on save if this is set to confirm that the user actually wants to mark it for Will Call; "This delivery is marked as Will Call.")
    * Dev Spec - This is an editable macro based on schedule date
  * Schedule Date (date field; required if Will Call is not checked; blank if Will Call is checked; defaults to the current date; on the Calendar view this updates as the delivery is moved around on the calendar; warning on the field if the entered date is in the past - validation message: "Schedule Date is set to a date in the past.")
  * Schedule Sequence (sequence within the day; number; hidden field used by drag and drop; on save, set to the next number in the sequence)
  * Customer (text field; same as "Contractor" in original spreadsheet)
  * Job (text field) 
  * Area (text field) 
  * Item (required; text field) 
    * Note that this is replacing "Amount" and "Span" from the old sheet 
  * Lum Pkg (checkbox; used to indicate a lumber package)
  * Mtl Pkg (checkbox; used to indicate a metal package)
  * Time (text field) 
  * Info (text field) 
  * Priority (checkbox; shown in red on calendar)



  


Logistics section:

  * Trailer:
    * Drop list of numbers (simple list; to be provided by Triple D; must be configured outside the calendar view; use natural sorting to sort these numerically)
    * Other Trailer (text field; visible of drop list is blank; to be used for custom items)
  * Trucker:
    * Drop list of truckers (simple list; to be provided by Triple D; must be configured outside the calendar view)
    * Other Trucker (text field; visible if drop list is blank; to be used for custom items)
  * Truck:
    * Drop list of trucks (simple list; to be provided by Triple D; must be configured outside the calendar view)
    * Other Truck (text field; visible if drop list is blank; to be used for custom items)
  * Board Feet (number; 0 decimals)



  


Production Hours

  * Production Hours (string field; no validations)



  


Status section:

  * Set (checkbox)
  * Drop (checkbox)
  * Permit (checkbox)
  * Escort (checkbox)
  * Called (checkbox; have editable date visible in detail screen)
  * Confirmed (checkbox; have editable date visible in detail screen)
  * Made (checkbox; have editable date visible in detail screen)
  * Status (automatic) 
    * In Progress (if the Made checkbox is not checked) 
    * Made (if the Made checkbox is checked but Schedule Date is today or in the future) 
    * Delivered (if Made checkbox is checked and Schedule Date is in the past)



  


Development Specification

  * Lists:
    * Trailers
    * Truckers
    * Trucks



  


  * System Switches:
    * Calendar Schedule History (# of Weeks)


