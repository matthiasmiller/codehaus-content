27.16. Member Payment - Add "Available Overpayment"

Sean Miller 04/29/2025: Moved to [[[IN11434](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11436&)]] - ZGW - Member Payment - Add "Available Overpayment"

  


  


Member Payment record | Applied Overpayments section: Show the total available overpayment, so the user can see the available amount before adding any rows to the Applied Overpayments embedded spreadsheet. 

  


Approximate cost: TBD

  


Spec: 

  


  * Available Overpayment $ (read-only macro; dynamically displays the current available Overpayment $ for the Member, i.e. the sum of all non-zero "Unused Overpayment $" values on Delivery Tickets for the Member, minus the "Applied Overpayments $" for this Member Payment)
    * Note that if this add-on is pursued, additional thought will be needed to make sure "(Pending)" amounts are handled correctly.


