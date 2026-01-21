5\. Records

  


Requirements

  


  


Development Specification

\----

  


  * Do we want a way to track which orders are going onto which truck? Matthias Miller 10/07/2025: Via DispatchTrack export and/or API
    * Don't we need to push the Date + Truck + Sequence back into the system for loading? Matthias Miller 10/07/2025: Same as above



  


  * State Upcharge
  * PDF Printout
    * of what will actually be picked up -- these will go out to the warehouse...
    * could see all the orders that should be coming in on this specific trucks...
    * headboard, rails, etc... at that point, you start slapping barcodes on each of those pieces...
      * generated 8 barcodes for this order...
      * it might show that you have 6 pieces on your order, (bed, dresser, 2 nightstands, mirror) but in reality, you have more than 6 parts (mirror might come w/ a separate mirror bracket) -- want the guys to be able to see by scanning that barcode (you have 1 of 9 parts)
    * You would have to punch # of barcodes at time of receiving
    * when checking in... it's probably by DATE + MANUFACTURER ??
    * They do DOCK SWEEPS - some manufacturers, they just showed up & said 'give us everything'
      * their benefit in that  is that the product is there, don't have to get it later, ready to load ASAP
      * Downside is warehouse filled up quicker...
    * Filter down by manufacturer
      * subgroup down by date... (since you might be getting stuff for future)
    * They have pickup lists that they give out.. they've done this long enough.. they know where the shops are... no address info
      * They go to the shop, and tell them they're picking up for these customers... the shop gives them all the stuff..
      * It's the shops responsibility to make sure they give everything ot them.. 
      * At that point they give us the invoice... they hand it in to the driver, then turns all that over to them... that's where the gatehouse is starting to keep track... 
      * as things are coming off, they're checking it 
    * Put thigns down on the 
    * Customer Built Rite - 
      * They need
        * Headboaed / Foorboard/ Rails / Slats
    * Check in all the pieces, if there is something wrong, tyre to follow up right away...
    * Take care of everything and distribute the papers
    * Use the mfg's invoice paper to first check in, to ensure they have it, then it goes to the PULLERS and indicates that it gets loaded on the truck, then it gets loaded into the office -- writes up a BILL OF LADING, cross references to make sure there are no discrepancies, and then put it into QB in a BOL form to send it out to the customer
      * That's creates the manifest for the load
    * 1 of 4 sounds like a better way...
      * Middle way of doing it... 



  


  * As long as they have the pricing, could pull all these orders based on the data, and the %'s it's working off of... could hit send invoice
    * They aren't very pushy w/ their information collection...
    * He wants to get to the point that when he gets the phone call, he gets all the information he needs from that order right away, and if they don't do that to start with, they do that to start with..
    * Started w/ a lot of the features that would need to be put inthere... fierst the order is called in, jot it down on the word doc, generic BOL, and file it...
    * Next stage -- is the backend ... they're getting all these papers in, tkae all those... all confusing, especially for new hires, putting it into QB
      * Sent out as a BOL
    * Invoicing... someeone comes back around, some of it they go after...
      * enter in the totals in QB (change BOL to invoice, then send out ot the invoice, beginning of the week)



  


  * Bill To
  * Ship To
  * PO  \- can we do it without a PO -- sometimes they get orders in without POs, applying a generic PO to something if it doesn't have one -- so they have a way to track it through the system
  * Item + Qty
  * Price gets complicated
    * Finisher
    * Buider
    * Sometimes just a finish price, just a build price..
    * Ultimately you need the total cost on the order...
    * It probably works best if they just had -- maybe they need 3 different values they can input
      * unfinished cost
      * finisher cost
      * total
      * there will be times they might give a piece to the puzzle
        * right away, they need to get to the mfg to get pricing too
        * would love to train them to get that information when it comes in, to avoid those extra steps
    * It is a little complicated too...
      * generally their base value is the % of the wholesale cost (to their area OH, to get indoor furniture, it is a flat 12%, mostly based on state, but there are multiple rates within the same state)
      * Where some complexities lie.. outdoor assembled is 4% (12+4=16%)
      * If they pick up in IN and ship EAST + 2%
      * If they pick up in Lancaster, and ship WEST, it's 2%... ship it WEST, no upcharge
    * Base Rate would automatically be tagged as a specific flow-in
      * if you see that an order is an outdoor-assembled order... tag the +4% is incorporated into the order
      * If it's a pickup in PA
    * They do have a minimum - across the board minimum for $250 for every region except WEST+ -- that moves to a $350



  


  * Export the pickups



  


  


  


  


They do have a new software for dispatching -- if they would find that we can bring something to the table that would work just as well, and would integrate well.

  


  * Currently using Dispatch Tracker -- they compile all the information itno an Excel sheet. Needs a sheet that has:
    * Shipping Location
    * Item (non-critical)
    * Quantity



  


  


  * They use cubes to figure loads, and will be a big part of their order entry



  


  * They do charge different states depending on where they do need to go
    * IN, OH have an upcharge
    * TODO_HLD



  


  * Call / Fax / Email - 90% from the mfg / finish shops, because they have the best grasp of when the product's done. If customers try to call it in, they end up going to a place where the builder isn't ready yet
  * Everything from plain Amish, to more modern Amish, to English
    * The more advanced it is, the easier it is to work with, and tend to be bigger shops
    * The smaller shops will fax in scribbled notes
  * Calls + Emails - are the larger majority, and between those it's a good 50/50 split (mybe 48/48/4 for 4 for fax)



  


  * They won't typically know the cube until they're picked up.
    * Cubic cheat sheet (same one for the past decade), started with that, looks at a paper, and in her head is able to cube it herself -- just knows what it is..
    * That's part of why they set up this spreadsheet...



  


  


  * Most pickups are done with Hotshots (pickup & trailers, etc -- 3-4x/day)
  * Most pickups are 53ft semis



  


\--

  


they pickup the same day that they load

  


  


  


\--

  


  


All comes through their gatehouse, as a pickup checkin, and right now -- they get invoices from ...

  * just a builders / stores invoice & list the
  * all of them have a different paper... looking at so many different papers,makes it hard to just jump from one to the next
  * when they enter the order initially, and IT prints out based on the



  


Go back and find the orders...

  * Looking for a specific piece on the order
  * THe MARKING IT OFF to make sure they don't scan a bunch of items, and have the bunch of items, and forget the last chest...
  * Maybe do one ore 
  * PULLER - taking it to the trailer
  * LOADER - is actually taking it in
  * His handheld would stay upfront where all his paperwork is, look at his order, says he has his bedroom set, and pull pu the headbord, scans it, and then sees that he has 3 parts, goes to his rails for this customer, 



  


  * There are exceptions to to all those rules...
    * share another map..
    * 


  


  


TODO:

  * Some warehouse location tags for the items...



  


Barcoding

  * Do NOT put on a "1 of 4"
  * Tie it out to a BUILDER + CUSTOMER + PO 
  * Optionally (??) tie it out to a specific line item...
    * not the end of the world if it's the wrong line item...
    * ULTIMATELY all he cares about... is 
    * on the back of the paper... that they're looking at, start slapping the equivalent barcodes on, and that's what you would use to match up to the number that you use... could count it out on there, 



  


Zone Assignments (?)

  *  Blocks are numbered
  * It would be nice.. it would be great if someone took a piece back, and started a new pile because there was no pile started.. if they woulc ome back to the checkin person, and they started a customer in A7 and could tie it in...
    * going to pull that order up... if something that would mention A7...
    * and even for putting things away.. might pick up from 4-8 mfgs for 1 customers, but will come in at different times...
    * it would be nice if there WOULD be a pile, could automatically, and could tie to that customer for a temporary time...



  


  


Order stages

  * Scheduled
  * Picked up
  * Routed
  * Loaded
  * On way
  * Delivered



Ever quotes instead?

  


Customer Portal

  * Login
  * All orders
  * Has it been scheduled?
  * See where it is
  * Possibly estimated date
  * 


Barcode Software/Hardware

  


  


Matthias Miller 10/07/2025: 

  * Region
    * Tied to their shipping schedule
    * [https://valleyviewtransport.com/routes-schedules/](https://valleyviewtransport.com/routes-schedules/)
  * Item Category
    * Has to be adjusted by Florida
    * Just a few scattered throughout the different areas had negotiated
  * Unfinished Pine & Alder
    * Typically it's coming from just a specific order
    * Sometimes may need to pick out different tiems
    * COULD POTENTIALLY BE AN OVERRIDE ON AN ITEM LINE ITEM



  


  * ONE BUILDER...
    * Discount 4% because they pay that part+



  


  * PICKUP ONLY...



  


  


  * OUTDOOR FURNITURE -> MFG + REGION



  


  


Matthias Miller 10/07/2025: RECAP

  * Trying to simplify processes for office
  * Wants to take mutiple processes and reduce them down to more workload on the frontend to make everything else run more smoothly
  * Think in terms of all the information flowing through this sofwtare, then being able to pull everything, whether it's an import / export to another software
    * Dispatching, wants her to be able to sort orders based on regions / states
    * Automatically export those into a file, then import them into their dispatching software
    * It would have to have all the information in the software
  * Be able to pull for customers BILL OF LADING
    * Customer Portal
  * Trying to help...making it simple for a stoe (sales reps, etc) to hop onto a computer, log into their account, and immediately they have access to every order that is current status
    * called in & sitting @ mfg
    * moves to another status -> Picked up / Received / Sitting in Warehouse / Scheduled on Route
    * Look at it very quciokly. based on the PO's --
    * If the order isn't on there...
  * Loves to ahve a system that they can log in, but if they can get 80% of their customers to recognize that by logging into an account, they can quickly see what the statuses are in the order, schbeduled to load & ship, and feel like they are just as much in the loop as they are... so that they can avoid them picking up the phone and spending 2 hours/day for each of their ladies int he office answering questions on the order status...
    * TRYING TO CUT DOWN ON TIME SPEND THERE...


