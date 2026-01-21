13.2.1. Changes to Incidents for Phase 4

  


Requirements

TODO_TR: 

  


Tim Reitz 06/08/2022: Items for future phases: 

  


  


Tim Reitz 06/08/2022: Current design for eventual Device Details section (when Device records are done): 

Device Details section: custom section to the right of the standard sections; TODO_TR

  * Device (optional; drop list of Device descriptions for the selected Customer) 
  * New Device (link; opens a new blank Device record; once a new device is added for the same customer and saved, it will appear on the Device list)
  * Serial # (optional and editable if Device is blank; auto-filled and read-only if a Device is selected) 
    * Note that this allows the user to simply document a serial # without creating a Device record if the device is not already in the database.



  


DONE_CH: the client probably would like to add additional Billing Details fields (at least the Time Adjustments). Free? How to spec out?

  


TODO_JM: which additional Billing Details fields would you like? (show blank incident)

  


TODO_TR: I'm willing to give everything except Invoices. If they want the Invoices section, I think we should add a column to Invoices for Incident ID that allows tying this out.

  


I think this requires them looking carefully at what we have and figuring out if they like it, or if something needs to change. No estimate on what this will cost until then.

  


Also, is this needed for first iteration?

  


Accessed via:

  * Other reports



TODO_JM: see other reports section and determine which are needed

  


  


  


  * Supplies (embedded spreadsheet with the following:) 
    * Columns: 
      * Date (required; defaults to "today")
      * Item (required; drop list of Sales Items/SKUs of the __ category)



TODO_JM: what category(ies) of SKUs?

  * Qty (required; number field; allow up to 2 decimals)
  * Notes (optional; plain text field)


  * Sorted by: Date (most recent at top)
  * Buttons to add and remove rows ("+" and "-")
  * Show at least 8 rows without scrolling



  


  


  


  


DONE_CH: Can we have the new incident title be generated from the Contact Name + MPS ID ? 

TODO_JM: Customer + ??

TODO_TR: Yes, as long as it's selected in the prompt. 

  


Customer Name - MPS ID: Remaining Title

  


This would be updated when changing the incident title, customer name, device, etc. We could even automatically update on save to handle situations when the contact record itself is renamed.

  


Up to you if you want a warning when changing a device

TODO_TR: Include the MPS ID in the Service incident title

  


Development Specification

DONE_CCI: I think we use Incidents for this. They don't really need a title, but we can negotiate that in the in-depth design. This would let us have standard email integration, and standard time card integrations.

Ellis Miller 11/09/2021: Sure.

DONE_CH: when do we finalize this? 

TODO_TR

Matthias Miller 04/08/2022: Can we try speccing it out that way once?
