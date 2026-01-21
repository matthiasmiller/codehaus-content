7.2.7. Contact - Member Details Section

  


Requirements

The Contact record also includes the following custom section and fields: 

  


  * Member Details section (visible if Contact Type = Member): 
    * Member ID (required; plain text field; used as an internal identifier for the Members, and is displayed on Delivery Tickets, printouts, etc.; normally 2-3 letters, but may be up to 4; with the following additional behaviors: 
      * entered letters are automatically capitalized; 
      * validate that this only contains letters and is 2-4 characters long - error message on the field: "Must only contain letters and be 2-4 characters long."; 
      * validate against duplicates across all Member-type Contacts; 
      * editable for users with the "Manage Financials" Permission; 
      * note that if the Member ID is changed, it will update on lists throughout the Solution, but will not update on Delivery Ticket #s, for historical reporting purposes) 
    * Default Member Payment Terms (required; drop list of "Member" Payment Terms items; used to set the default option for this Member on Delivery Tickets, etc.; defaults to blank; editable for users with the "Manage Financials" Permission) 
    * Sales Commission % (required; number; 2 decimals; with the following details / behaviors: 
      * this is used to calculate the amount of commission that the Salesperson earns from each Delivery Ticket for this Member, as a % of the "Total Buyer Payment $" (post-discount); 
      * visible to and editable for only users with the "Manage Financials" Permission; 
      * note that in the future this could be changed to an embedded spreadsheet, if the Solution needs to support multiple Salespeople) 
    * Delivery Tickets by Member (link; opens the "Delivery Tickets by Member" report, filtered to this Member)



  


Development Specification

Tim Reitz 10/15/2024: Member ID capitalization done via on change expression.

  


Ellis Miller 12/16/2024:

[ ] Member ID has some validation. Note that this is mostly used for readable delivery ticket numbers, but isn't actually used for linking purposes. We use the Contact list for that.

[ ] Clear fields on save if type is not Member.

BID: 6 HOURS
