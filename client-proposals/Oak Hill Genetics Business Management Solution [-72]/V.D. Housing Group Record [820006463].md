5.4. Housing Group Record

Overview: In the current software, pigs are handled separately from dogs and do not have their own records. In general, pigs are handled in groups rather than individually. In the new Solution, the plan is for pigs to each have their own Animal record (with Type set to "Porcine"), but for most of the actions to be done in batch form. This Porcine Group Record is used for tracking groups of pigs and performing batch actions to a group. Pigs can also be entered into the system in batches.

  


Ben Reitz 05/03/2023: It's possible that we would have both dog groups and pig groups. Waiting to hear from the client before making very many changes to this section.

  


Sections/fields:

  * Serial In
  * USDA ID
  * DOB
  * Actions (embedded spreadsheet)
  * Customer
  * Leave Date 



TODO_JB: Ben Reitz 05/03/2023: Would all animals in a single group leave at the same time?

  * View/Edit Pigs (link to open an editable report to view all pigs in the group and to make mass changes)
  * Add Pigs (link to open a page to add pigs)



  


  


Other Notes:

  * Pigs have two numbers: "Serial In" (number that they are tagged with at birth) and "ID" (USDA number), and these numbers are linked together in the software.


