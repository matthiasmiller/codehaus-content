4\. Housing Protocol Group (NEW)

  


Requirements

This is a new feature that does not exist in the current software. Oak Hill recent added a new line of business: a housing facility for animals owned by others. Oak Hill is currently running this on Excel, but would like to have this be part of the Solution as well.

  


This would track animals that are being housed, with data points such as: 

  * Housing Group 
  * Entry Date
  * Daily Observation/actions
  * Exit Date
  * Weight
  * Vaccinations
  * Litter
  * Mother
  * Room



  


Ben Reitz 05/03/2023: In a phone call with the client, he expressed interest in doing a smaller system for just the housing side of the business, with the intention of moving their entire system onto our platform sometime in the future. He sent Matthias and I an email with the top 10 things he would like to have in the housing system. They are listed below:

  


  * Create an animal file when they arrive. We will need the ability to attach documents to the animals file.
  * Record daily observations of the animal and its daily health.
  * Record any medications administered.
  * While we need to have individual animal files, we also need to be able to create groups. For example, we may receive five animals for Dr. McCall, and they would be under Protocol # 143.21. We need to be able to receive each animal and then assign them to a “group” or “order” while they are here. Then that group can have an assigned customer name and protocol number etc.
  * We would want mass action entry ability, as most often the group of animals will receive the same daily treatment or records.
  * Billing. Anything we do will be billed for, so anytime we do a daily observation for the day or give a medication that will have a charge.


  * Tim Reitz 05/08/2023: Maybe a "Daily Observation" record or RG that can get linked out to a line item on the invoice? 


  * Send Invoices to QuickBooks.


  * Tim Reitz 05/08/2023: Needs Invoices module and some sort of sync to to QB. 


  * Pen Inventory per room and building, and track which animals are in the facility.
  * Allow customers to login to see data on their account.
  * There will be a small production side of the housing software. There are scenarios where we get a pregnant pig to house her and she ends up birthing her litter here. At that point we would need to create a litter for her and track her piglets separately but still see their history.



  


I'm starting subsections with what I'm seeing that we would need to get this off the ground.

  


Ben Reitz 05/03/2023: Considering that they want groups for their animals, as well as customer logins, I'm wondering if we can possibly copy some of the specs from Symbiz over to this and make our lives easier with that. Or is that too proprietary to Symbiz?

  


Development Specification

*Other System for new line of business* Animal Inventory Tracking / SKUs:

Tim Reitz 03/22/2023: This is a whole other feature that doesn't exist yet. They recently bought a housing facility for their customers. They desperately need software for that as well (currently running on Excel). This is a completely separate feature, but Justin does want to work on design for this now as well as the main software.

Overview:

  * Animals are only housed OR bred and housed
  * Housed:
    * Entry Date
    * Daily Observation/actions
    * Exit Date
    * Vaccinations
  * Housed and litter birthed there:
    * Track mother
    * Track litter
  * Inventory tracking:
    * Facility has 6 big rooms
    * They know approximately how much room each room can hold, but would like to be able to track how many animals each room has and how much space is available (assign an animal to a room and go from there).



  


  


Matthias Miller 03/22/2023: 

  * Housing Order
    * Matthias Miller 03/22/2023: Monthly Cycle
  * Transport to / from
  * Animal records??



  


Matthias Miller 03/22/2023: 

  * When the animal arrives, it gets a 
  * When they are assigned a GROUP, rather than a LITTER, and you can assign medication to that GROUP
    * TODO_HLD: Tim Reitz 03/23/2023: Are group and litter the same record type or separate? It makes sense to treat them as separate. We could design them as separate, and let Ellis speak into it later if he wants them to be combined.
  * You can either SHIP the whole group at the same time, or certain animals ship
  * You have an END DATE of the GROUP



  


  * If you have 10 beagles staying for 3 months, and you bill them 3 times, how is there a way to keep that 3 month period as 1 ORDER, but bill them 3 times, but know it was billed. But doesn't like the idea of a new order appearing...



  


  * There is ALWAYS a match between animals on order, and animals in group -- "Protocol Order" is a great term
    * Ability to create an invoice for the Delta between the last time it was invoiced, and today
    * Two scenarios -- halfway through the month, request that half of the animals get brought back to the facility. The program needs to know that some animals continue, and some
    * You get a pregnant pig, when she farrows and births pigs, and her piglets might get sold and shipped back at varying intervals.
    * Embedded RG of
      * Animal Serial #
      * Arrival Date
      * Departure Date
    * I think the animals are on the group --
  * Matthias Miller 03/22/2023: Animals are billed by per diem rate based on weight, using prior known/recorded weight. This is broken down as a LUMP SUM - Animal ID #1 is X for the month of March.



  


TODO_IDD: Tim Reitz 03/23/2023: global setting: Per Diem per pound for cost
