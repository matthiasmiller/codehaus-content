2.1. Glossary

  


Requirements

Overview: The purpose of this glossary is to provide a description of key terms referred to in this proposal. These are listed below, in approximate order of appearance in this proposal: 

  


  * Member: A sawmill that has signed up as a GemWood member, and provides wood to Buyers through GemWood's brokerage.
  * Buyer: A company that buys wood from one or more sawmills through GemWood.
  * Purchase Order: Purchase Orders are an integral part of the LoadHawk software. 
    * Buyer Purchase Order: A Purchase Order (PO) that is submitted by the Buyer and contains the various lumber items that the Buyer needs. These are tracked as their own record type.
    * GemWood Purchase Order: A PO that GemWood generates, based on a Buyer Purchase Order record, to request lumber from a Member sawmill. Note that one or multiple GemWood POs may be created for a single Buyer PO. Note that GemWood POs are tracked entirely on their "parent' Buyer PO, and not on their own record type. Also note that there is a 1-to-1 relationship between GemWood POs and Delivery Tickets. 
    * Purchase Order Close Types: There are two main approaches to setting a PO so that the Solution knows when the PO should be marked as "Closed": 
      * "Date-Based": The PO is essentially a blanket purchase order from the Buyer, requesting as many loads of a certain type of lumber as GemWood can broker, at a certain rate; the Buyer will provide notice of when they wish to stop receiving those loads, or send a new Date-Based PO for a new type of lumber and/or different price. When a new Date-Based PO replaces an existing one, it is documented and handled on the new Purchase Order record, and the old PO is closed automatically after being selected on the new one. It can also be closed sooner on the Purchase Order record. Note that the same Buyer might have multiple Date-Based PO's open at the same time, for different types of lumber, etc. 
      * "Load-Based": The Buyer requests a certain amount of lumber on a purchase order, and a corresponding target number of truckloads is specified for the PO. When the target number is reached, the PO is automatically closed from a linked Delivery Ticket. It can also be closed sooner on the Purchase Order record.
  * Delivery Ticket: A document or record containing all of the necessary information pertaining to the order. This is the main common thread used to track an order to completion. 
  * Grade: A value in the grading system that GemWood (and Members and Buyers) use for grading the quality of lumber. See "Grades" for more information regarding grades.
  * Board Feet (abbreviated as "BF"): A standard unit of measure for logs and lumber, with 1 BF = 144 cubic inches, the equivalent to a piece of wood measuring 12" long x 12" wide x 1" thick.
    * Note that all lumber pricing in the Solution is done in $/BF (as opposed to $/MBF), with dollar values going to 3 decimal places.
  * Buyer Payment: A payment made by a Buyer to GemWood for lumber and/or other expenses. In the Solution, these are tracked on special "Buyer Payment" records, which can contain "sub-payments" for multiple Delivery Tickets. 
  * Buyer Settlement Date: The date of the latest Buyer Payment linked to a "Closed" Delivery Ticket. This is used as the reference point for Member Payments that use "Buyer Settlement Date" as their date baseline. 
  * National Hardwood Lumber Association (abbreviated as "NHLA"): An organization that promotes and establishes standards for grading and trading hardwood lumber.
  * Claim: Any deviation from the invoiced amount that the Buyer doesn't pay. This normally is a result of the Buyer Grade Report giving a lower total value that then Member's. NHLA rules are that the Buyer should always pay if their grade is within 4% of the sawmill's grade (note that claims are not the same as a discount) 
  * Member Payment: A payment made by GemWood to a Member, passing on payment from the Buyer. In the Solution, these are tracked on special "Member Payment" records. 
  * GemWood Lumber Brokerage Fee: A fee that GemWood charges to Members for the brokerage of the lumber sale. Currently (as of the time of Phase 1 design), this is 4% of the amount that the Buyer pays for the load of lumber. 
  * GemWood Division: A division or branch of GemWood, as defined by role or activity (sales, marketing, office/administrative, etc.). Each internal GemWood contact (employee, contractor, or business) is assigned a Division for Internal Fee Payout tracking, etc.
  * Internal Fee Payout: A payment to an internal GemWood contact (employee, contractor, or business), calculated as a percentage of the GemWood Lumber Brokerage Fee for a Delivery Ticket.



  


Development Specification

Change Requests:

  * Ben Reitz 10/09/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature


