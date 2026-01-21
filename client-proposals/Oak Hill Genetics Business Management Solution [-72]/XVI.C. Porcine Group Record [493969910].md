16.3. Porcine Group Record

Overview: In the current software, pigs are handled separately from dogs and do not have their own records. In general, pigs are handled in groups rather than individually. In the new Solution, the plan is for pigs to each have their own Animal record (with Type set to "Porcine"), but for most of the actions to be done in batch form. This Porcine Group Record is used for tracking groups of pigs and performing batch actions to a group. Pigs can also be entered into the system in batches.

  


Sections/fields:

  * Serial In
  * USDA ID
  * DOB
  * Actions (embedded spreadsheet)
  * Customer
  * Sold Date 
  * View/Edit Pigs (link to open an editable report to view all pigs in the group and to make mass changes)
  * Add Pigs (link to open a page to add pigs)



  


  


Other Notes:

  * Pigs have two numbers: "Serial In" (number that they are tagged with at birth) and "ID" (USDA number), and these numbers are linked together in the software.
  * Pigs arrive at Oak Hill at about 3 weeks of age in batches of about 200; as they get bigger they are separated into smaller groups, but they can still be tracked together as a group.
  * Currently Oak Hill is selling about 5K pigs/year to research, but are producing many more than that (maybe 10K; the extras go into the meat market and don't need to be tracked). We could shed the extra records after a certain number of months (if a pig hasn't been sold for research by the time it's 6 months old, it probably will be going to the meat market). (TBD in in-depth design)


