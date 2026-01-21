7.5.2.3. Member Payment - Payment on Ticket Section

  


Requirements

  * Payment on Ticket section:
    * Note that the labels for the fields in this section are above the fields, to provide a similar layout to the table in the "Applied Overpayments" section.



  


  * Payment Type (read-only macro; displays the "Payment Type" for the Payment) 
  * Ticket # (read-only macro; displays the "Ticket #" for the Delivery Ticket for the Payment; displays as a link to open the corresponding Delivery Ticket record)
  * Ticket Date (read-only macro; displays the "Ticket Date" for the Delivery Ticket for the Payment)
  * Total Member $ (read-only macro; displays the "Total Member $" for the Delivery Ticket for the Payment)
  * Member Balance $ (auto-set and read-only; displays the "Balance Due to Member $" for the Delivery Ticket for the Payment, as of the time that the "Ticket #" was selected on the Payment record)
  * Applied $ (required; sets to the "Balance Due to Member $" for the Delivery Ticket for the Payment, as of the time that the "Ticket #" was selected on the Payment record; otherwise (i.e. if there is no "Balance Due to Member $), defaults to blank; warning on Save if = "0.00": "Applied $ is set to 0.00 for one or more applied overpayments.")



  


Development Specification

Change Requests: 

  * Tim Reitz 03/12/2025: [[[IN11201](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11203&)]] - ZGW - Delivery Ticket - Remove "Next $ Due to Member"


