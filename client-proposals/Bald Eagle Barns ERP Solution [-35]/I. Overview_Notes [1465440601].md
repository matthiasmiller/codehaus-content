1\. Overview/Notes

  


Requirements

Bald Eagle Barns (BEB) is a storage barn company in Arkansas. They have 3 entities under 1 enterprise:

  * Bald Eagle Barns (dealer / sales aspect; face of the enterprise)
  * Benchmark Buildings (manufacturing)
  * Bald Eagle Transit (delivery / logistics)



  


There are also independent dealers involved. These dealers don't own the inventory -- they just provide the spot to set it on, then sell on a commission basis. All proceeds from building sales go back to BEB; BEB then pays the dealer their commission every 2 weeks.

  


Jason Miller is the main point of contact. His father and brother started the business; his brother Nathan was here until he left to start the RTO company (separate entity, but a partner company). 

  


What they have now: 

  * Currently have database that syncs with QuickBooks enterprise 
  * Built in Alpha5, Microsoft SQL; hosted on local server
  * They switched from MySQL to MSSQL to harness more of the server
  * Built in 2012, works well
  * BEB owns the code for it, but are the only ones using it
  * Currently using Synergration OpenSync to sync with QuickBooks (but that is now defunct)



  


The problem: 

  * Only one developer mainly; relies on him and he's moving onto other things and doesn't have time to continue developing it
  * Getting a second phase and ongoing maintenance is difficult
  * Wanting to add functionality pieces to it at a later time
  * Surprised there isn't anything off the shelf
  * Not snappy
  * Multiple seconds to populate
  * It is frustrating trying to pull up information and dealing with the lag
  * The file is very large (the SQL database), looking to keep the system lightweight



  


Other options they've looked at:

  * NetSuite - other shed companies using it, along with accounting software
  * ShedSuite - Similar but has quite a ways to go til it has the functionalities we want
    * We had put our name on their list of future users
    * They weren't following their roadmap so we withdrew 
  * ShedApp - Also has promise but still has a ways to go to be customizable for what we want it for 
  * EBMS - Sales rep didn't feel it would be a good fit; no way to have task-driven projects that would give us a



  


From Jason, here's what they're looking to achieve:

  * User friendly, easy to learn
  * Scalable - more drivers, more dealers
  * Various pieces all work together - sales entry, customer management, accounting, inventory, and deliveries; one action correspondingly affects/syncs with all others
  * Can have things added to it along the way
  * Stable and secure
  * Responsive
  * Full ERP - one scalable system; start to finish of the process for our business
  * Centralized dashboard to see a summary of where everything is at



  


  


*Done.

  


Development Specification

Notes about BEB's current process: 

Quote/Order Generation:

  * Customer comes in or calls, or a lead is generated online via IdeaRoom
  * Salesperson writes up a quote and gathers information. The sales quote is collecting information from the customer, base price from the builder, features of the building, and options the customer wants.
    * If it’s a stock order, they generate a blank work order. The blank work order has no customer associated with it, except stock work order, and it gets completed and put into finished inventory
    * Then once it’s there, it can be sold through a sales quote.
    * It cannot be sold from a sales quote until it’s in finished inventory.
  * When the customer accepts, they convert the quote to a sales order & a work order
    * Work Order takes the customer name, options, and building price.
    * Tasks are created for the various pieces of constructing the building. Examples of tasks:
      * Building Trusses
      * Cut Out Building
      * Framing Building
      * Framing Inspection
      * Install Trim
      * Caulk Building
      * Paint the Building
    * The creation of the work order also means these tasks have been assigned to this work order, and have been sent out.
  * Electronic work order is pushed to the shop.
  * Each task is completed by a builder (the builders are paid per task/piece).
  * As tasks/pieces are completed, they show up on the dashboard



  


Construction:

  * They have an assembly line process:
  * Each builder has their department -- the cut man has his department, a framer has a framing department, then the painter, and then the roofer
  * Each one of those is a separate department
  * When the work orders get sent over the shop, they’re in a list. They shop manager has access to all tasks, but the cut man only has access to the tasks for his department
    * Print his work order, showed as printed, and in progress
    * The marks as having cut the building out, then it unlocks the framing one
    * They mark their task and inspection, any extras, then it unlocks the roofing
    * But they have GENERAL TASKS -- the one who builds the trusses, and who does some of the preliminary parts
    * Then they have DEPARTMENT TASKS -- in the sequential order
  * The shop manager has to sign off on the final inspection, before it gets put into finished inventory



  


They have their piece-work base pay:

  * Basically, it has a different price point that the piece work is figured off of
    * The structural tasks are off the base pay
    * There are options that require extra work, but each line item might have its own actions with it
    * Subtable/subassembly
  * Each option
    * Can affect the structural price
    * Can also have tasks with that, along with a price that those are based on



Installing a window might be part of a base price, but it’s a separate task for installing the window

  * Can configure each subassembly 
    * 12x16 Utility - will manually set up all the tasks for that assembly -- and can use the task for an option assembly
    * Make assemblies for each model, and each subitem
  * He really wants to just go show us the old system here


  * Catchall
    * Custom work -- whatever price they put in their, the builder gets a 15% of the line item
      * Somebody wants a dog door installed
      * They charge $150
      * The man gets 15% of that
  * Tasks can be fixed price, percentage based, or price per square foot
    * etc



  


Software is not calculating lead time -- manually setting the delivery date at the sale

  * Internal calendar to mark it as built
  * Using Google calendar to find the delivery spots and to organize it
  * They don’t have a date that it needs to be started by, but it’s up to the shop manager to make sure that it’s completed by the required time.
    * Example: A building that’s scheduled to go out in 2 months; the shop manager might have it built anytime in there, but his responsibility is to make sure that it’s built and ready to go by the delivery date.
  * They can deliver a certain amount each day -- they monitor to make sure the salesmen don’t overload.



  


  


  


Feedback on the High-Level Design: 

Ellis: Data model looks solid. I think you can be pushing forward with this. I wonder if there is any way to do a staged rollout so that we don't wait to deploy a HUGE system? I would love to see this split into at least 2 (maybe more) deliverables.

SIgnificant Pieces:

  * QB syncing (MYS)
  * Payments record -- is this a std module?
  * Buildings record
  * Sales Quote / Order -- presumably a custom record?
  * Invoicing
  * Layout Editor -- significant
  * Shop Workstations -- significant
  * Restricted Data
  * Data Migration(!)



My gut instinct is that it is larger than Weaverland, but I'm not sure. There are also a lot of simple pieces. If I'd have to ballpark, I'd guess maybe 100K to 200K, but if a lot more complexities come, I could see it climb beyond that.

  


Matthias: I don't have anything to add here. Sounds about right. Tim, let's talk about staged deliverables, and perhaps see whether we've communicated potential price with them.

  


Tim Reitz 07/07/2021: Thanks for the review and the input! That sounds good. 

As far as the payments records, it might become a std record. We would have needed to handle payments somehow in the ZPP Ads project, and I could see it being a request we get more often. 

Invoicing might not be a very significant piece, but that's an unknown at this point. 

Data migration might be huge; we probably should plan for it to be. Might be a good candidate for T&M, like we talked about briefly yesterday??

  


Ellis: Yes, T&M for Data Migration makes sense. We may be able to provide a ballpark.

Tim Reitz 01/27/2022: Made a note about T&M in the Data Migration section of the proposal.
