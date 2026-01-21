16\. Josh's notes

Members become users in DB. Username+password login. Restricted users.

  


# Packs goes in Load Itemization section.

  


Don't allow adding thickness/species/grade values that aren't on the PO. 

  * Correct. Only BF entry would be great.
    * The member should see:
      * Ticket #
      * Delivery to address
      * Buyer
      * Buyer PO
      * Load Itemization
      * # of Packs



  


1 delivery ticket = 1 shipment

  


When does it show up on the tablet?

  * When it is assigned (member is set in the GemWood PO RG on the Buyer PO record) and status is "Ready to Send" or "Awaiting Delivery Ticket".



  


How is it marked as sent? We think that it's when the Delivery Ticket is created.

  


What fields on the Delivery Ticket need to be filled in?

  * "All the info the member sees, plus the rest of the info from members and buyers that goes with the DT."



  


Custom option: how much variation is allowed?

  * No custom option.



  


Josh Nisly 11/03/2025: When creating the delivery ticket:

Line 1: Ticket # must consist of only the Member ID and 4-5 numeric digits. (Field: TktNum) (Record: New Record)

Line 1: The Member ID portion of this Ticket # is not valid. (Field: TktMember) (Record: New Record)

Line 1: "Member Payment Terms" is a required field. (Record: New Record)

Line 1: "Ticket #" is a required field. (Record: New Record)

Line 1: "$/BF" is a required field. (Record: New Record)

  


  


Josh Nisly 11/05/2025: 

  * How do we handle POs with no requested BFT values? Josh Nisly 11/05/2025: I'll just ignore these for now.



Niccolas Miller 11/06/2025: From the client:

  * There are several reasons we might want zero in that field. 


  * The PO bf is basically a place holder and has little bearing on the load shipped.  We will never be held to specific quantities.
  * Often the buyer will leave that at zero
  * Often there are several PO’s with a BF qty representing several truckloads, we haven’t tested this to see how the PO to the member breaks those down per PO. 



                                                                              i.        I just tested this and it does divide up the bf per PO so we will start filling those in.

  


  * I still don't understand the Status in the PO RG. (Show "ready to send" or "awaiting delivery ticket", i.e. all GW POs assigned to member that do not have a linked delivery ticket)



  


  * Let's talk through the delivery ticket creation process. These appear to be created manually right now.
    * Ticket #. Talk through how I'm handling this.
    * Other required fields (Member Payment Terms, for example)
    * Do we default the $/BF automatically? It's required. Niccolas Miller 11/06/2025: See above.



Niccolas Miller 11/06/2025: From the client:

  * The Buyer terms should be automatically pulled from the buyer info [ContactDefaultBuyerPaymentTerms].  We can modify that here but not in the field [i.e. member cannot modify; ZGW can].


  * Only a small portion should be filled out by the member… basically selecting the line item from the PO and filling in BF
  * Yes the $/bf should default to the PO $



  


  


  * Template export for delivery ticket
    * Is there a design for this? Has it been done?



Niccolas Miller 11/06/2025: From client:

  * I don’t have anything right now… we can make it look like the DT and call it Bill of Lading. 


  * Add a field for the shipper (member info)
  * BOL # can be the DT #
  * Signature block
  * Omit species table
  * No Pricing



We may want to make available to the specific members another option to print the dt with pricing and totals.  Or at least display this on the Handheld.  This would be enabled on a case by case basis.

  


  * Update on printing.


