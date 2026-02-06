4.3.3. Changes to the "GemWood Financials" Section

(Not all fields included here.)

  


  * Salesperson (read-only macro; with the following details / behaviors: 
    * displays the following: 
      * if "Legacy Stored Salesperson" is blank: displays the "Salesperson" on the linked Purchase Order record; 
      * otherwise: displays that (this ensures that the Salesperson is displayed correctly for Delivery Tickets created prior to the field being added to the "Salesperson" field being added to the Purchase Order record; 
      * displays as a link to the corresponding Salesperson's Contact record) 
  * Legacy Stored Salesperson (hidden; list field of all Internal-type Contacts; this retains the selected Salesperson for Delivery Tickets created prior to the "Salesperson" field being added to the Purchase Order record) 
    * with the following behaviors and details: 
      * required and editable if "Commission Paid" checkbox is not checked; 
      * visible to all users; 
      * drop list of all Internal-type Contacts; 
      * defaults to the "Default Salesperson" from Silverloom Settings at the time that the Delivery Ticket record is created)


