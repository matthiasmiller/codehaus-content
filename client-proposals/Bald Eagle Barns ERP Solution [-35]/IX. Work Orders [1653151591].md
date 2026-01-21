9\. Work Orders

TODO_TR: clean this up 

  


  


The work order would be a separate record type. 

For Customer Buildings, this would be created when the sales quote is changed from Quote to Order. 

For Lot Buildings, ___ 

In both cases, creating the Work Order would trigger the assignment of the Serial Number and lock the fields related to the Serial Number and Building Price.

  


DONE_CH: The materials price on a WO should be up-to-the minute, then frozen when it's completed.

TODO_TR: Just note this, and perhaps in the Dev Spec that we should have both stored and calculated values.

  


TRIGGER FOR CREATING THE WORK ORDER FOR A NEW BUILDING: When the serial number is generated. 

TODO_TR

  


Work orders can be created from the Building record, from the menu, or from a Sales Order. Different Types of Work Orders will be created from different places:

TODO_TR

  


All work orders must be tied to a building. 

TODO_TR: is this still right?

  


DONE_CH: Can there be multiple work orders per Sales Order?

TODO_TR: Probably not, unless a work order was canceled. Can we get away with just not creating an additional work order if one already exists?

  


  


DONE_CH / TODO_TR: linking between Sales Order records and Work Order records (should go both ways). Which should be stored on which? 

  * Work Order should point to the building.
  * SO finds WO's for its building
  * WO finds SO's for its building



  


DONE_CH: when doing a change order, where should the details be entered - on the SO or the WO? E.g.: adding Options, like additional windows. This affects materials and tasks, and is a sale. It feels so complicated - is there a way to simplify this? 

TODO_TR:

  * have a "Pending Change Order" on the building record with options
  * The SO pulls this information for a quote
  * When the quote is finalized, the Pending Change Order items get pushed into the main options RG, and those options get tied out to the Sales Order.



TODO_TR

Matthias Miller 12/01/2021: Have an RG of options on the building record with an optional column for Work Order. If it's blank, it means it's pending and gets copied onto new quotes. Once a quote goes final, all pending options get deleted, a work order gets created, and the options are added onto the building and linked to the work order. (The Work Order then shows a read-only virtual RG of options based on the building record.) Note that this will allow for 2-way editing.

  


TODO_TR: Make sure that materials costs get frozen on the WO so that Assembly (and other) reporting works properly. (also noted to do the same in Tasks)

  


  


Does repairs

  * Get scheduled in Google Calendar
  * Not tied into the software at this point -- it would be helpful to tie it into the software
  * They have a building that’s been sold 2 years ago, then they write up a service ticket -- they have a history on the building, but also show that X date they replaced the door, window, etc…
  * Can be in-warranty, or not in-warranty



  


  * There are a lot of secondary moves that happen -- this building was moved from this location to the other location
    * This becomes a transit expense
    * The goal is to be able to have a full tracking of Lot 
  * Not wanting to chase down in Google calendar etc
  * Put a place to put in big red letters, DO NOT MOVE AGAIN



  


Service man job desc:

  * Inventory check -- make sure that the buildings are on the lots they’re supposed to be on, and do maintenance on the chains broken, doors adjusted, knobs fixed
  * Escorting for over-sized loads
    * He does this in Google calendar -- it would be nice to have a secondary assignee
  * The other problem that happens is that sales people schedule these in two opposite directions….



  


  


Matthias Miller 06/03/2021: For the work order, would prefer that it stays as an original work order is differently...

  * Service Call -- may have options
  * Sometimes it will be installed in a task option, but in a non-tasked option
  * One challenge is a building that's 2 hours away, then schedules for it have doors and windows added out there...but you can't send your serviceman to do this...this can be part of the approval process
  * As far as dealer progress, would like to see if the building is started


