8.2. Unpaid Vendor Yard Tallies Alert

  


Requirements

Overview/Purpose: This is an internal alert in the Solution that is sent when there is at least one Yard Tally with a Source of Vendor that has not been Closed within 5 days of the Creation Date. Note that this is the same as the Unpaid Vendor Yard Tallies Email (redundancy seems helpful for this alert).

  


Title: Unpaid Vendor Yard Tallies 

  


Sent via: A report alert that runs soon after 12:00am every day where the above condition exists. It will disappear soon after older tallies are closed. 

  


Action: Link opens the Yard Tallies Report with the Status filter set to "Open" and "Confirmed" and Source filter set to "Vendor". 

  


User(s) to notify: All Administrators

  


Other Notes:

  * N/A



  


Development Specification

Use a Yard Tallies Alert report that uses the YardTalliesOlderUnpaid subset from the Email above. Make this AutoPush into the Yard Tallies report then as outlined above.

  


BID: 4 HOURS
