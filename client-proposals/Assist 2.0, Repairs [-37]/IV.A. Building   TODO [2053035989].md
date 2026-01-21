4.1. Building   TODO

On the Building's Location RG:

  * Add a "Type" of "Repair"
  * Rename Hauler to "Primary Hauler"
  * Add a "Secondary Hauler" (same list of haulers)
  * Add a "Scheduled Time" (i.e. "4:20 PM")
  * Job Status (user-customizable list)
  * Invoice Date



  


For repairs, add:

  * Description (plain text, multi-line input)
  * Photos (S3)
  * Supplies - child RG of:
    * Qty
    * Repair Item
    * Price (defaulted to Repair Item's cost)
    * Amount (Qty * Cost)
  * Travel Start Time
  * Travel End Time
  * Repair Start Time
  * Repair End Time
  * Truck (link to truck)
  * Notes (multiline)



  


NOTE:

  * This will be able to attach documents (PDFs, images, etc)



  


TODO_BTI: Which fields are required?

TODO_BTI: What validation?

TODO_BTI: Are they OK losing the calendar input?
