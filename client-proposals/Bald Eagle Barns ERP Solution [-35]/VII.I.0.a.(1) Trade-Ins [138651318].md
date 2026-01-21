7.9.0.0.1. Trade-Ins

TODO_TR / DONE_CH: this needs work and thought... 

  


More “buy-backs” than trade-ins. But sometimes it is done as a literal trade-in. We would need to show a credit to the customer for the trade-in value (this could be done as a line item discount on the new building’s SO). 

DONE_CH: how should this happen on the technical side? 

  


  


  


Process: 

One member values the building and makes the customer an offer. 

DONE_CH: Maybe set a value on a prompt? This maybe could be done as a reverse SO (selling the building back to BEB), with a negative balance to the customer. NOTE: currently cannot sync a negative number to QB.

Matthias Miller 01/12/2022: This is a field on the BB/TI work order. Sounds like MSRP doesn't need to change?

  


TODO_JM: When the salesperson values the building, is that the buy-back amount or the new sales price? Or both? If not the same, is there a standard mark-up? If a standard mark-up, we should add a setting for that. 

  


  


When BEB purchases the trade-in, normally write a check to the customer and buy it back. 

Financial side (writing a check) is handled in QB,

Ownership changes from the customer to BEB 

Building is put into inventory 

DONE_CH: (we would use a SO/WO; currently they’re doing this through a bug in the system - “undelivering” the building). 

Classified as “Trade-Ins”. Not included on the SRB report; included in Inventory report.

  


It can be sold like a lot building. If sold as an RTO, RR buys it from BEB (if it’s an SRB, RR does not buy it because they already own it).

  


  


TODO_TR:

  * Add a credit field after total, before balance
  * This needs to sync to QB
  * For a trade-in, add a negative credit to the Buy Back, then use that credit on the subsequent purchase



  


  


  


Matthias Miller 01/12/2022: Proposal:

  * Have a "Trade-In" Work Order (requires delivery and changes ownership)
  * Then manually add a line item to the new sales order, or have accounting write a check
  * Does this work, or do we need to track the financials of this?



  


Or, if you wanted to take it further, you could allow designating it as a Trade-In or Buy Back, then automatically creating a check for the Buy Back (if needed) or automatically applying it as a line item on their next invoice (linked directly to the WO; column in the line items RG?)

  * Note that there will be two fields -- buyback value and MSRP
  * Must validate against using buyback multiple times



  


  * Or we could do buybacks manually (for QB)


