7.5.2. Member Payment Detail Screen

  


Requirements

Overview: The Member Payment Detail Screen is used to track details about payments from GemWood to Members. A Payment to a Member corresponds to one primary Delivery Ticket, but may also contain "applied overpayments", deducting funds from the Payment to account for overpayment by GemWood on one or more other Delivery Tickets.

  


GemWood may make multiple Member Payments for a single Delivery Ticket (for example, in the case of "Early Pay Option" Terms, or a Ticket that was initially underpaid).

  


Accessed via: 

  * Member Payments reports
  * "New Member Payment" links/options in the following locations:
    * Delivery Ticket record
    * Main Menu | Data Entry | New Member Payment (opens a blank new Member Payment record) 
  * Links on Delivery Ticket records
  * Etc.



  


Sections and Fields: The sections and fields for this detail screen are specced out in subsections below.

  


Additional Validations: 

  * Warning on save if any edits are made when Status = "Complete": "You are making changes to a completed payment."
  * Warning on save if any edits are made when Status = "Canceled": "You are making changes to a canceled payment."



  


Other Notes: 

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=27652506#gid=27652506](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=27652506#gid=27652506) 

Tim Reitz 01/24/2025: Updated.

  


TODO_CCI: Tim Reitz 12/18/2024: Please let us know the format for the Payment Calculations feature once you have that finalized, so that we can document it in the living spec. Thanks!
