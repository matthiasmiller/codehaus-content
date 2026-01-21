9.2. Update the "Glossary" Notes

  * Purchase Order: Purchase Orders are an integral part of the LoadHawk software. 
    * Buyer Purchase Order: A Purchase Order (PO) that is submitted by the Buyer and contains the various lumber items that the Buyer needs. These are tracked as their own record type.
    * GemWood Purchase Order: A PO that GemWood generates, based on a Buyer Purchase Order record, to request lumber from a Member sawmill. Note that one or multiple GemWood POs may be created for a single Buyer PO. Note that GemWood POs are tracked entirely on their "parent' Buyer PO, and not on their own record type. Also note that there is a 1-to-1 relationship between GemWood POs and Delivery Tickets. 
    * Purchase Order Close Types: There are two main approaches to setting a PO so that the Solution knows when the PO should be marked as "Closed": 
      * "Date-Based": The PO is essentially a blanket purchase order from the Buyer, requesting as many loads of a certain type of lumber as GemWood can broker, at a certain rate; the Buyer will provide notice of when they wish to stop receiving those loads, or send a new Date-Based PO for a new type of lumber and/or different price. When a new Date-Based PO replaces an existing one, it is documented and handled on the new Purchase Order record, and the old PO is closed automatically after being selected on the new one. It can also be closed sooner on the Purchase Order record. Note that the same Buyer might have multiple Date-Based PO's open at the same time, for different types of lumber, etc. 
      * "Load-Based": The Buyer requests a certain amount of lumber on a purchase order, and a corresponding target number of truckloads is specified for the PO. When the target number is reached, the PO is automatically closed from a linked Delivery Ticket. It can also be closed sooner on the Purchase Order record.


