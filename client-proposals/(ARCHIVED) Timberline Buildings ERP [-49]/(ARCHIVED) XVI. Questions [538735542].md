16\. Questions

  


Requirements

TODO_SS: Tim Reitz 01/25/2022: Question for the clients: What do you mean by “link back to our supplier portal” (in the context of pricing)?

Matthias Miller 02/01/2022: Their pricing would comes from lists that are in spreadsheets.

  


  * Main Supplier has their interface that they work with
  * And they have a backside they can go in and put in the orders themselves
  * In that same interface, they can download the current pricing lists (Excel sheet, 40K items) keep it in a central location in Dropbox, and most of them link back to that sheet, then copy/paste
  * They use supplier SKUs for just about everything, but they also have an internal list for items they stock in their shop -- the way they separate is the code in the shop starts with a *
  * The stuff that they stock, are thigns that they pull on a job-to-job basis, some of it will be purchased -- it's the way that he handles the information within his material list system, so he uses that to print out a picking list, where items can be pulled from the list..
  * Basically just used as a picking list
  * Use two separate SKUs \-- supplier and internal sku



  


  


  * Imagines a module that allows him to subcontract \-- here are my labor hours, and here's what I figure with a subcontractor
    * He just needs to be able to point to a number that covers labor for subcontractor. It won't affect the sale price. he wants to pull consistent numbers
    * It can be in the background, and look up subcontractor allocation for this scope of work.
      * Broken down by phase
      * Global Setting for Subcontractor Rate
    * Subcontractor child screen
      * Editable control for Subcontractor rate
      * Shows totals per pahse,a long with a grand total.



  


  


TODO_SS: Are you tracking “Referred By” for customers? If yes, what info and how should this database handle it? (Tim noticed it in the “General Notes” document you sent over)

  * They're tracking referrals, but they don't have a tracking spreadsheet for that
  * Lead Source
  * Tracking down referrals are a pain to track down, so it's not important. Sometimes they are referred by 2-3 friends. (Not necessary)



  


Migration:

  * What data do they want to migrate across, beyond customers? Past orders? Current orders?
    * Leads / opportunities?



Matthias Miller 02/01/2022: 

  * Complete customer list
  * Organize the customer folder structure to match the names of the spreadsheet, then have a way to mass-attach these to the contacts
  * Material SKUs (?)



  


  


  


  * “Box” SKUs - do you mainly have standard boxes, or mainly custom boxes? 



Matthias Miller 02/01/2022: For the building themselves -- starts off with a box price, but there isn't any SKU attached to the building style and size

  * None of the buildings are the same (they're custom builders, and everything gets customized)
  * Right now, the way the BOX gets priced, is that you have your BOX price, and for a 32x40 is a common size (and it's a box), but if anyone wants to go longer, you build a longer building by adding sectiosn
    * Maybe you have your box and your sections -- Your section is 8ft, and broken 2ft sections
    * They're trying to standardize those selections as much as possible



  


  * Have 1 box per width
    * Then add sections to extend the length



  


Matthias Miller 02/01/2022: 

  * Would like templates of the buildings
    * You could have these under a special customer, then they could copy it over to a new quote
    * For example, "Advertised Buildings"
    * Matthias Miller 02/01/2022: Main thing is that it's easy to set these up by template.



  


  * Currently, every time the pricing changes, they end up having to run all his pricing again, they have to go back to the updated TPS, and restart a whole new proposal...
    * Matthias Miller 02/01/2022: If a customer calls in 4 months / etc - "Refresh to current pricing." "Proposal price differs from current pricing by $X." with a refresh button. (Note from Ervan, that SmartBuild almost matches what...if you take a template, you assign a customer to it, it holds the pricing for the job, and you can update.)



  


  


  * Separate invoice and contract, or does the contract act as the invoice as well? 



Matthias Miller 02/01/2022: Separate invoice, manually created in QB, from information off the contract.

  


  


  * Does TOS need to track separate/multiple payments from the customers? (presumably yes - down pmt vs. final pmt; change orders, etc.) 
    * If yes, how should the payments work / what information do they need to track?  
    * Also if yes, should TOS handle refunds and/or credits? 



Matthias Miller 02/01/2022: Typical project today will come in with a 25% deposit at signing, 65% due when starting, 10% retainage at final completion

  * What they're doing on Change Order, and 50% on acceptance, and 50% on completion -- if they're going to automate it a little more, paid when that phase is complete
  * When a Change Order is executed in the system, it would push those numbers into the invoicing to get invoiced at the right time



Matthias Miller 02/01/2022: Final invoice would show everything, and all the payments, so they end up with  the ending balance.

  * The invoicing is set up to mimic the payment schedule on the contract
    * Deposit - 25%
    * Construction Draw - 65%
    * Final Invoice - has the full balance



  


  * What reports do you want?



Matthias Miller 02/01/2022: 

  * Sales by Salesman - broken down by category (new building / change order) -- summarize the totals and push it to graphs
  * Be able to set targets and pull up reports (YTD vs Goal vs Prior Year / Years)
  * Lead Management - track lead volume / conversion rates / # of contracts
  * Another one from their job costing - Profitability Target / Job have been met or not
  * Profitability by Crew
    * TODO_CH - need to have fields to put -- each time card would have the job code on it, as the crews are working, payroll is biweekly, so when payroll picks up the time cards and enters them for the payroll, she's also going to charge those hours to job codes
    * Jobs would be assigned to the same forman, but you wouldn't have all the jobs on-site. Assigne it to a crew would give you a general overview how each crew is performing, but it's not something that he would get too hung up on
    * The source of truth for job costing, hours, would come right from payroll, based on the hours charged to that job.
    * The whole idea of that, is to recapture as much billable time as possible per job -- they're paying to and from the job site, and that time is billed to the job 
    * Matthias Miller 02/01/2022: If you do this, you need to sync to time sheets.
  * Matthias Miller 02/01/2022: Would ned to be able to see that this job was a subcontractor crew
    * Matthias Miller 02/01/2022: Can sub out by job
      * Perhaps a contact type of Subcontractor with a default rate
      * Checkbox per phase for subbing it out, default the rate, allow changes, and allow entering subcontractor hours.
      * My guiess is that the profitabilty by labor should be different for eomployee vs contractor
      * Even for subcontractor hours, running a report on total hours per year, it would help to forecast future needs -- could lose a lot of subcontractor hours, if they don't actually track them, but it would be hard to put a finger on to how much they've helped (for example, if they have a sub whos; moving out of town, they could calculate the deficit that it will create, and predict what they need from there)
  * Profitability by Salesman
  * Inventory Side
    * Some reports printed out for stop correction -- what inventory that they have, sheet they can take into the shop to break down the inventory that they have, and enter in against what they have in the system
    * Other things he expect to be tied in
      * Being able to see how many doors projected for jobs to be stored
    * Uses dscriptiopns and codes to print out tags for stock keeping / kanban system -- he should be able to export an excel sheet with all the information that is needed -- be able to select the fields that you
  * Doesnt'see the learning curve, as long as they can customize it



  


  


  


TODO_SS: Mentioned Job codes - what is your current format? 

Matthias Miller 02/01/2022: Job Name -- not a good system for breaking out phases, not in the system

  * Woudl like to move just beyond job name
  * Don't have a clear picture of what it would look like
  * As far as the results, a job is entered, and as far as phases and costs against that job, when it's entered in queue, processed, and sold, be able to generate POs with codes for every need for that job.
    * Bulk Matieral - AB Martin (preassigned PO number, that woiuld tie into job costing and general ledger, the general ledger being expense categories -- cost code for general supplies is 640, and so they want to generate a PO that includes job costing and general ledger
    * You pay in the invoice, or the AP pushes it based on the assigned codes
    * This would save a good bit of time, right now the cost codes are getting assigned manually based - approve them for payment by assigning cost codes
    * Purchasing, by virtue of issuing a PO, has approved it, and assigned the cost code in advance of 



  


  


  * Job Cost and General Ledger
  * (Labor)
  * Rentals (occasional jobs)
  * Disposal (where getting a portable toilet to the job)
  * COGS -- 
    * job lodging
    * job meals (reimburse per diem)
  * All of those would be assigned to job and GL



  


  * Assigning a PO to the job phase, but that PO would mainly be for TOS
    * Matthias Miller 02/01/2022: Want to be able to generate the CSV, and could take back into TOS, and could assign POs per line item, to get it to be costed to the right phase.
    * 


  


TODO_CH: we need to add this to the Job record...

  


  


  


  


Matthias Miller 02/01/2022: 

  * It's seldom, but it is a scenario --
    * It's pretty rare
    * if you come back in 2-months, we'll cosnider rolling the $2500 as a credit as a next project
    * It's rare enough, as long as they have a process, some manual work is fine
  * Refunds -- the most common scenario (about 4X a year), a customer signs up for a building, gives his deposit, and for whatever reason backs out early on, no materials on the ground, or even some materials are on back order, and in good faith, refunds less costs
  * Discount on the front end
    * On the pricing side, a scenario of a discount in pricing, pre-contract to negotiating -- customer will come in and say, worked with you guys 3years ago, like your work, and would like work with you, 5 miles up the street, like to get the process started, go back and fortha  few times
    * His sales people have up to 3-4% if they can justify it reasonably -- then needs to document it on the quote as a repeat customer discount (all manual), knock 3% off the total -- need bascially to enter a line item and assign off the bottom (done long before it comes to QB, it's just been sold for less than it's potentially worth)
  * Discount on the back end
    * There's "Returns and Allowances" expense codes
    * Common scenario for that, would be the one they talked about backing out early (see above)
    * May have a customer, where they have done everything they were contracted to do, but they go across the customer's yard and destroyed his PVC riser from his sewage line, and they ask if $500 is fair repair -- it normally comes off on the value of thevalue.
    * Comes out of retainage, and it becomes a job cost



  


  


Matthias Miller 02/01/2022: 

  * Being able to add 5% to the system-wide pricing.



  


Matthias Miller 02/01/2022: 

  * Be sure that we've got some provision for seeing job status as it moves through the status, so that you can see at a glance, which department it's moving through



  


Development Specification

TODO_CH: Zones / Counties lists
