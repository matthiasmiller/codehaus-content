14\. Sales Opp Notes

CodeHaus Receptionist 12/15/2022: 

  


Alex Mast

Valley View Transport

Office: (330) 359-8500

Cell: (330) 473-9035 - preferred

Email: [alexm@shipvvt.com](mailto:alexm@shipvvt.com)

Meeting Scheduled: Tuesday December 20th at 2:30pm

  


Valley View Transport is a logistics company. Alex is looking for a software to be built to help with labeling and organizing. He does have access to internet and has 20 employees.

  


Ian Miller 12/20/2022: 

Called, he wasn't available for our scheduled call. Sent email w/ link to reschedule.

  


Ian Miller 1/6/2023: 

Called, he wasn't available for our scheduled call. Sent email w/ link to reschedule.

  


Ian Miller 01/06/2023: 

  


Tell me a little more about your business--what do you do, what services do you provide? 

  * We are a blanket wrap furniture shipping company. 
    * We pick up furniture from manufacturing companies and deliver them to retail stores across eastern United States. 
    * We handle about $1.2 million of furniture each week. 
    * We have internet and have 20 employees. 
  * We want to build a system that helps us ensure that each piece is delivered with its group of other pieces. 
  * We would envision a bar code system, with a unique bar code on each piece. Bar codes are generated in groups, depending on how many pieces are in each group. 
    * For example: A table would need 3 bar codes
      * For the table top
      * For the components
      * For the leaves
  * We check the furniture into our warehouse and apply the bar code label
  * We check the furniture out of the warehouse when we load the pieces onto the truck; at this point we need to ensure each piece from the set is loaded onto the truck. 



  


Key questions for Matthias and Ellis

  * Is this something that is feasible and that you feel comfortable pursuing further? 
  * Is this something that's going to be a $20-50k? Or is this $50-100k? 
  * Are there other specific questions you'd want me to ask him before encouraging him towards the high level design? He sounds very interested in the high level design but I don't want to encourage him that route until I know you feel comfortable and confident moving that direction. 



  


Follow up:

[ ] Ian - Send follow up email with call notes and other documents

[ ] Ian - Send call notes to head designer

[ ] Ian - be in touch with Alex after hearing back from head designer; possibly schedule a follow up call to discuss details and questions.

  


Matthias Miller 01/16/2023: Josh - Rubico project, except Ellis wants this as a strategic project

  


  * Barcode generation + reading = client-side
  * Hardware (?)
    * Bluetooth + Tablet ($400)
    * [https://www.amazon.com/MUNBYN-Barcode-Scanner-Inventory-Warehouse/dp/B0911X86Z2/ref=sr_1_9?keywords=phone+barcode+scanner+attachment&qid=1673904172&sprefix=barcode+attachment%2Caps%2C119&sr=8-9](https://www.amazon.com/MUNBYN-Barcode-Scanner-Inventory-Warehouse/dp/B0911X86Z2/ref=sr_1_9?keywords=phone+barcode+scanner+attachment&qid=1673904172&sprefix=barcode+attachment%2Caps%2C119&sr=8-9)
  * Printing
    * Raspberry Pi w/ next thing to print (CUPS + kind of printer)



  


Need to bill a higher amount of support + higher level of development + documentation for hardware requirements

  


Scanning - $70 scanner + tablet + time  ($300 for Josh)

Printing - do some research + buy printer -

TOTAL - $1000 for Josh for technical possibility

  


Matthias Miller 01/16/2023: Definitely doable. Our HLD is normally $3500, which does not include hardware-related design and research. The full price for the HLD (including hardware) is $4700.

Looks simple on the surface but could have complications that weren't expected. Don't anticipate it being the upper end of 75-100k but there are so many variables.

  


Ian Miller 01/23/2023: 

  * What you're wanting looks doable on our end
  * We would bring someone else into this who has experience in the hardware side of things
  * High Level Design would be $4,700 because of the hardware / software implementation research needed
  * Looks simple on the surface and seems like this will fit in the small project range ($20-50k)
  * Of course, there is always the possibility that we will discover complexities that weren't expected which would impact the project investment



  


Follow up:

[ ] Alex will talk with others about this and will get back in touch with Ian when he's ready

  


Ian Miller 02/09/2023: Called to follow up w/ Alex. Left VM

  


Ben Reitz 04/19/2023: Sent an email to Alex to see if this is something he's still interested in. Setting the follow up date for 2 weeks.

  


Ben Reitz 04/20/2023: Alex replied to my check in email:

  


Thanks for checking in Ben. We’re going to sit on it for a bit until we decide how and when we want to move forward.

  


Setting the follow up date for November and setting as Backburner.

  


Ben Reitz 11/06/2023: Since the rest of the year is filled up for us, I'm removing the follow up date and will see about reaching out again in the beginning of 2024.

  


Ben Reitz 05/16/2024: Sent Alex an email to see if he's found anything yet.

  


Ben Reitz 05/16/2024: Alex said they're still looking at this point. I offered a call with Ellis.

  


Ben Reitz 05/21/2024: Alex said he'd like a call with Ellis. Offered May 30th at 3:00pm ET.

  


Ben Reitz 05/22/2024: Call is confirmed for the 30th.

  


Ben Reitz 05/30/2024: Ellis and I had our call with Alex. Here are the call notes: [https://docs.google.com/document/d/1ORDM-lIyAxjNw80dYgzJg8-mgEu52YerZ448jxqfJvM/edit](https://docs.google.com/document/d/1ORDM-lIyAxjNw80dYgzJg8-mgEu52YerZ448jxqfJvM/edit)

  


Overview:

Summary:

  * Alex had talked with Ian back in 2022
  * Located in Mt. Hope, OH
  * Furniture transportation company
  * Specializing in blanket wrap
  * Using QuickBooks for accounting
  * Using HighJump ([https://www.koerber-supplychain-software.com/en/supply-chain-solutions/transportation-management-system](https://www.koerber-supplychain-software.com/en/supply-chain-solutions/transportation-management-system) ) to put together routes
  * Looking for improvements in the following areas:
    * Dispatching: current dispatcher is really good but she’s the only one who knows how her system works, so it’s hard for someone to fill in for her
    * Cubing: currently calculations for truck space are done by hand. It would be nice to have a more automated way to do this
    * Avoid manual errors with furniture: sometimes items are put on the wrong truck. Having something (especially a barcode system) would help a lot
  * Have about 100 furniture suppliers / manufacturers
    * Most of them do not have internet access
  * Orders are called, faxed, or emailed and then VVT goes out and picks them up
  * Bulk of calls come in on Monday or Friday but 1,000 - 1,500 orders are called in per week
  * ~12 semi-truck trailer loads come through per week
  * Covering the eastern half of the country for deliveries
  * A week at VVT:
    * Monday noon is when the orders need to be called in for that load week
    * Usually the finish shops and manufacturers are the ones calling in the order
    * Orders are received several different ways: actual invoice, general bill of lading, etc.
    * Orders are physical paper copies that are stored in bins that are assigned to different regions
    * Dispatcher then uses the papers from the bins to generate the routes
    * Tuesday is when the very first load is loaded for the next week
    * Wednesday - Friday/Monday is when a bulk of the loads are loaded, minimum of 3 loads loaded each day
  * Everything is typed into QuickBooks manually to create the bill of lading and invoicing



  


Thoughts from Ellis:

  * Something like this should probably be done in phases
  * We would love to work with you and would like to offer a HLD



  


Next Steps:

  * Ben will send the Project Design Overview and System Screenshots
  * Alex will consider the HLD offer and will get back to us



  


Ellis Miller 07/11/2024: Left a message.

  


Ben Reitz 08/20/2025: SALES CALL: Talked with Alex. They're still looking for a solution. He's been shopping through a lot of different software providers. Customized software is appealing but the cost is something that kinda holds them back. 

  


Since our call last year, they started using a new dispatching software but would be open to either having Silverloom integrate with it, or moving away from it entirely if we can do what it does.

  


Some questions that he asked me:

  * When would you be able to have a software built for us? That really depends on the size of the system and complexity of the design, but with our current pipeline, I would think that probably in 8 months or so.
  * How often are you able to meet a client's request vs telling them that you can't do it or that it will cost a lot? I would say that 98% of the time, we're meeting the client's needs. Occasionally they'll ask for something that we simple aren't capable of but that's rare. Sometimes they'll also ask for a change that we can do, but it will cost them a good bit to be able to do it. However, we work hard to make sure that the software matches the client's workflow, rather than making the client change their workflow for the software.



  


Alex said that after all the shopping around he's done, he really feels like he needs to go with the customized route. I set up a call with Ellis for September 9th at 3:00pm ET / 2:00pm CT.

  


Ben Reitz 09/09/2025: Ellis and I had our call with Alex today. Notes can be seen at the bottom of this doc: [https://docs.google.com/document/d/1ORDM-lIyAxjNw80dYgzJg8-mgEu52YerZ448jxqfJvM/edit?tab=t.0](https://docs.google.com/document/d/1ORDM-lIyAxjNw80dYgzJg8-mgEu52YerZ448jxqfJvM/edit?tab=t.0)

  


Alex would like to move forward with a HLD, so I'm checking with Matthias see when he could do that.

  


Ellis 09/09/2025: Order entry -- how that should happen

  


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

  


Ellis 09/10/2025: Matthias said  he can do design in October. Let's tell the Alex we can do design in October but Matthias is preparing for an expo, so we'll let him work out the schedule later this month. If he gives 50% down (2500), we'll reserve his place as the next design.

  


Ben Reitz 09/10/2025: I've invoiced Alex for the $2,500 and informed him that if he pays by the due date, that will reserve his spot for an October design.
