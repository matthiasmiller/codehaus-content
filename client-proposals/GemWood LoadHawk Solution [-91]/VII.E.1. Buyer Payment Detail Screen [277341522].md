7.5.1. Buyer Payment Detail Screen

  


Requirements

Overview: The Buyer Payment Detail Screen is used to track details about payments from Buyers to GemWood. A single payment from a Buyer may contain multiple "sub-payments" (funds for multiple Delivery Tickets).

  


Note that the Buyer Payment does not depend on the Buyer Grade or the Delivery Ticket, but is simply a documentation of funds received from the Buyer (and most times, this will already to be in the bank by the time the Payment record is set up).

  


Accessed via: 

  * Buyer Payments reports 
  * "New Buyer Payment" links/options in the following locations:
    * Delivery Ticket record
    * Buyer A/R Aging report
    * Main Menu | Data Entry | New Buyer Payment (opens a blank new Buyer Payment record) 
  * Links on Delivery Ticket records 
  * Etc. 



  


Sections and Fields: The sections and fields for this detail screen are specced out in subsections below.

  


Additional Validations: 

  * Warning on save if any edits are made when Status = "Complete": "You are making changes to a completed payment."
  * Warning on save if any edits are made when Status = "Canceled": "You are making changes to a canceled payment."



  


Other Notes: 

  * The "Close Delivery Ticket from Buyer Payment" automatic process runs on the first Save after the "Complete" checkbox is checked.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=364718168#gid=364718168](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=364718168#gid=364718168)

Tim Reitz 01/09/2025: Updated

  


Change Requests: 

  * Tim Reitz 02/28/2025: [[[IN11186](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11188&)]] - ZGW - Delivery Ticket - Clarifications for Auto-Closing Delivery Tickets



  


  


  


TODO_CCI: Tim Reitz 11/07/2024: Per Ellis, for the "Set / Update" button: use SuppressX30SuccessMessage.
