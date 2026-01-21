20\. OLD / complex approach to Freight tracking

Tim Reitz 11/11/2024: Up until today in the IDD process, we've been working toward tracking multiple data points for freight, and handling calculations (which turn out to be very complex) within the software.

  


However, the client realized today that we don't need to handle all of those in the software at this point. It's rare enough for GemWood to broker freight that the client is fine with doing the complex calculations outside of the software and inputting the final amount manually into an "Other Line Items" RG.

  


So I'm moving the Freight-related spec here, in case we need/want to reference it in the future.

  


\---------------------

  


Glossary: 

  * GemWood Freight Brokerage Fee: A fee that GemWood charges to Members for the brokerage of shipping for a load of lumber. Currently (as of the time of Phase 1 design), this is 2% of the amount that GemWood pays for the freight.



  


\---------------------

  


  


Calculations / Process:

  


TOD_VA: Tim Reitz 11/06/2024: Per Client today: freight will be treated like any other service provided by GW:

[X] Freight will now be included as a line item on the invoice to the Buyer, and also on the Buyer Grade Report.

[ ] Freight will be included in the total amount and have the 4% taken off of it like the lumber $.

[X] If GW brokers the freight, there will be an extra 2% for that.

[ ] If the Buyer claims the Early Pay Discount, the discount would be taken off of that as well.

TOD_DD: Tim Reitz 11/11/2024: How should this be handled with partial / multiple Buyer Payments for the same Ticket? (where the first one has the early pay discount, but the second one doesn't) Do we need to apply the discount to a certain proportion of the freight $ and take it off that way, or is there a simpler way that we could do it? 

  


TOD_VA: Tim Reitz 11/11/2024: Another new approach to freight:

[X] No longer handling any special calculations for freight (Freight Brokerage, etc.)

[ ] Add a "Include Freight in Member Payment" (checkbox; if the linked PO has a non-zero "Buyer Freight Provided", this is editable, defaulting to checked; otherwise, read-only, defaulting to not checked)

[ ] If GW is not brokering the freight, this stays checked and the Buyer Freight Provided is included in the Member Payment, and handled just like (and along with) the lumber funds (no special handling for fees for just the freight)

[ ] If GW is brokering the freight, this gets manually unchecked, and the Buyer Fright Provided $ is not included in the Member Payment. GW would manually handle the calulations outside ofthe Solution, then add them back in as a custom fee/credis.

[ ] Add an RG for "Other Line Items" (auto-add a row for Freight if applicable; also can be used for custom + / - items):

  * Type
  * Amount
  * Date
  * Description



  


  


TOD_VA: Incorporate here or in another sub-section: 

Freight Cost: There are 3 main ways that freight is paid for: 

  * The Member brokers or provides the shipping, and GemWood never sees the details. 
  * The Buyer includes a set amount per load for the freight in their payment to GemWood, the Member brokers or handles the shipping, and GemWood passes the freight portion of the Buyer Payment along to the Member by adding it to the Member Payment (after having taken out the 4% "Lumber Brokerage Fee", and the 2% "Early Pay Discount" if applicable).  
  * The Buyer includes a set amount per load for the freight in their payment to GemWood, GemWood brokers the shipping, and passes along the full cost to the Member with a markup by deducting it from the payment to the Member (after having taken out the 4% "Lumber Brokerage Fee" from the freight portion of the Buyer Payment and an additional 2% "Freight Brokerage Fee", and the 2% "Early Pay Discount" if applicable).



  


WIP formula: {[("Buyer Freight Provided $" * [1 - decimal value of "GemWood Lumber Brokerage Fee %")] - ["GemWood Freight Cost" * (1 + decimal value of "GemWood Freight Brokerage Fee %")]} * (1 - decimal value of "GemWood Early Pay Discount %")

Sample calculator: 

1\. Baseline

[2,000 * (1 - 0.04)] - [1,800 * (1 + 0.02)]} * (1 - 0.02) = 

[(2,000 * 0.96) - (1,800 * 1.02)] * 0.98 = 

(1,920 - 1,836) * 0.98 = 

84 * 0.98 = 

82.32

  


2. 

2,000 * (1 - 0.04)] - [1,800 * (1 + 0.02)]} * (1 - 0.02) = 

[(2,000 * 0.96) - (1,800 * 1.02)] * 0.98 = 

(1,920 - 1,836) * 0.98 = 

84 * 0.98 = 

82.32

  


Examples: 

  * Example 1: 
    * Starting Numbers: 
      * Buyer Freight Provided $ = 2,000.00,
      * Lumber Brokerage Fee % = 4.00;
      * GemWood Freight Cost $ = 0.00;
      * Freight Brokerage Fee % = 2.00;
      * Early Pay Discount % = 2.00
    * Summary: Member has brokered & paid for the shipping, and GemWood passes the Buyer Freight Provided on the Member, after fee and discount, as applicable. 
    * Results: 
      * IF GemWood takes the Early Pay Discount: 
        * THEN "Freight $ for Member" = +$1,880 
        * Calculation: (2,000 - 80) - 40 
      * IF GemWood does not take the Early Pay Discount: 
        * THEN "Freight $ for Member" = +$1,920 
        * Calculation: 2,000 - 80 



  


  


  * Example 2: 
    * Starting Numbers: 
      * Buyer Freight Provided $ = 2,000.00,
      * Lumber Brokerage Fee % = 4.00;
      * GemWood Freight Cost $ = 2,200.00;
      * Freight Brokerage Fee % = 2.00;
      * Early Pay Discount % = 2.00
    * Summary: GemWood has brokered/paid for the shipping, and the Buyer Freight Provided did not cover the full amount. GemWood charges the Member for the balance of $200 \+ the 2% "Freight Brokerage Fee" of the full GemWood Freight Cost:  
      * THEN "Freight $ for Member" = -$244 
    * Results: 
      * IF GemWood takes the Early Pay Discount: 
        * THEN "Freight $ for Member" = __ 
        * Calculation: 2,000 - __ 
      * IF GemWood does not take the Early Pay Discount: 
        * THEN "Freight $ for Member" = __ 
        * Calculation: 2,000 - __ 
          * 


TOD_DD: Tim Reitz 11/11/2024: Do you take the Early Pay Discount off of the Freight to Member if it is $0 or negative (charging the Member for extra expense)? 

  


TOD_DD: Tim Reitz 11/11/2024: Do you apply the 4% lumber brokerage fee to the $2K if it is all used up with nothing left to pass on to the Member? 

TOD_DD: Tim Reitz 11/11/2024: What about if there is only a little left? (i.e. Example 5) 

  


  * Example 3: 
    * Starting Numbers: 
      * Buyer Freight Provided $ = 2,000.00,
      * Lumber Brokerage Fee % = 4.00;
      * GemWood Freight Cost $ = 1,800.00;
      * Freight Brokerage Fee % = 2.00;
      * Early Pay Discount % = 2.00
    * Summary: GemWood has brokered/paid for the shipping, and there is surplus from the Buyer Freight Provided. GemWood keeps the remaining $200, which covers the Freight Brokerage Fee, and does not charge the Member anything extra:  
      * THEN "Freight $ for Member" = $0
    * Results: 
      * IF GemWood takes the Early Pay Discount: 
        * THEN "Freight $ for Member" = __ 
        * Calculation: 2,000 - __ 
      * IF GemWood does not take the Early Pay Discount: 
        * THEN "Freight $ for Member" = __ 



  


  


  * Example 4: 
    * Starting Numbers: 
      * Buyer Freight Provided $ = 2,000.00,
      * Lumber Brokerage Fee % = 4.00;
      * GemWood Freight Cost $ = 2,000.00;
      * Freight Brokerage Fee % = 2.00;
      * Early Pay Discount % = 2.00
    * Summary: GW has brokered/paid for the shipping, and the Buyer Freight Provided has been used up with no surplus or balance. GW charges the Member 2% Freight Brokerage Fee:
      * THEN "Freight $ for Member" = -$40
    * Results: 
      * IF GemWood takes the Early Pay Discount: 
        * THEN "Freight $ for Member" = __ 
        * Calculation: 2,000 - __ 
      * IF GemWood does not take the Early Pay Discount: 
        * THEN "Freight $ for Member" = __ 



  


  


  * Example 5: 
    * Starting Numbers: 
      * Buyer Freight Provided $ = 2,000.00,
      * Lumber Brokerage Fee % = 4.00;
      * GemWood Freight Cost $ = 1,975.00;
      * Freight Brokerage Fee % = 2.00;
      * Early Pay Discount % = 2.00
    * Summary: GemWood has brokered/paid for the shipping, and there is a small surplus from the Buyer Freight Provided, but not enough to cover the full Freight Brokerage Fee of $39.50. GW charges the Member the difference of the balance and the 2% Freight Brokerage Fee ($39.50 - $25):
      * THEN "Freight $ for Member" = -$14.50
    * Results: 
      * IF GemWood takes the Early Pay Discount: 
        * THEN "Freight $ for Member" = __ 
        * Calculation: 2,000 - __ 
      * IF GemWood does not take the Early Pay Discount: 
        * THEN "Freight $ for Member" = __ 



  


  


NOTE: If the Member Terms includes an Upfront Payment (i.e. initial 75%), GW does not include the Freight amount in the upfront payment (the final Member Payment is the remainder of the load - fees + freight).

  


\---------------------

  


Silverloom Settings:

  * GemWood Freight Brokerage Fee % (required; number; 2 decimals; defaults to 2.00; used for documenting and calculating the % of the freight cost, which GemWood charges Members for brokering shipping for loads of lumber)



  


\---------------------

  


Delivery Ticket | Member Financials section:

  


  * GemWood Lumber Brokerage Fee % (number; 2 decimals; defaults to the corresponding value from Silverloom Settings as of the time that the Delivery Ticket record was created and does not automatically change if the setting is updated; for users with the "Edit Financial Settings" Permission, this is editable and required; for all other users, this is read-only) 
  * GemWood Lumber Brokerage Fee $ (auto-calculated and read-only; number; 2 decimals; displays the rounded value of "GemWood Lumber Brokerage Fee %" * "Final Ticket Value $"; auto-updates based on changes to the fields from which it is calculated; displays in gray italicized text with "(Pending)" suffix until Delivery Ticket Status = "Closed" or "Canceled", at which point it displays in standard black text)



  


  * GemWood Freight Cost $ (required; number; 2 decimals; must equal 0 or a positive number; defaults to 0.00; used for documenting the amount that GemWood spent for freight costs for this load; if this is positive, it means that GemWood has brokered the freight for the load and will be charging their Freight Brokerage Fee in addition to the general Lumber Brokerage Fee) 
  * GemWood Freight Brokerage Fee % (visible if "GemWood Freight Cost $" is set to a positive value; number; 2 decimals; defaults to the corresponding value from Silverloom Settings as of the time that the Delivery Ticket record was created and does not automatically change if the setting is updated; for users with the "Edit Financial Settings" Permission, this is editable and required; for all other users, this is read-only) 
  * GemWood Freight Brokerage Fee $ (visible if "GemWood Freight Cost $" is set to a positive value; auto-calculated and read-only; number; 2 decimals; displays the rounded value of "GemWood Freight Cost $" * "GemWood Freight Brokerage Fee %"; auto-updates based on changes to the fields from which it is calculated)
  * Freight $ to Member (auto-calculated and read-only; number; 2 decimals; with the following special notes:
    * this is the amount to charge or credit to the Member; may be positive (in the case that the Buyer pays for freight and GemWood incurs no extra cost) or may be negative (in the case that the Buyer pays for freight and GemWood brokers the shipping and incurs extra cost to pass along to the Member; or if the Buyer does not pay freight and GemWood pays it and passes it on the to Member);
    * displays the rounded value of the following:
      * {[("Buyer Freight Provided $" * [1 - decimal value of "GemWood Lumber Brokerage Fee %")] - ["GemWood Freight Cost" * (1 + decimal value of "GemWood Freight Brokerage Fee %")]} * (1 - decimal value of "GemWood Early Pay Discount %");
    * example 1 (GW's cost is less than the Buyer Freight Provided)
      * {[2,000 * (1 - 0.04)] - [1,800 * (1 + 0.02)]} * (1 - 0.02) = [(2,000 * 0.96) - (1,800 * 1.02)] * 0.98 = (1,920 - 1,836) * 0.98 = 84 * 0.98 = 82.32;
      * if:
        * Buyer Freight Provided $ = 2,000,
        * Lumber Brokerage Fee % = 4.00;
        * GemWood Freight Cost $ = 1,800;
        * Freight Brokerage Fee % = 2.00;
        * Early Pay Discount % = 2.00)



TOD_DD: (email) Tim Reitz 11/09/2024: Is this correct?

  * example 2 (GW's cost is more than the Buyer Freight Provided):
    * (2,000 * (1 - 0.04)) - (2,200 * (1 + 0.02)) = (2,000 * 0.96) - (2,200 * 1.02) = 1,920 - 2,244 = -324;
    * if:
      * Buyer Freight Provided $ = 2,000,
      * Lumber Brokerage Fee % = 4.00;
      * GemWood Freight Cost $ = 2,200;
      * Freight Brokerage Fee % = 2.00)  



_VA: Tim Reitz 11/08/2024: And take take off the 4% main brokerage fee, and any 2% early pay discount. 

TOD_DD: (email) Tim Reitz 11/09/2024: What to do if the amount to the member is negative (passing on extra expense to the Member)?? Presumably simply disregard it for the negative freight portion?

  


TOD_VA: Tim Reitz 11/09/2024: Need to update the examples in the "Member Payments Overview" section, to account for the 4% fee and the 2% early pay discount.
