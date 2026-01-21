27.13. Internal Fee Payout Contact Changed Report Alert

  


Requirements

Sean Miller 04/29/2025: Moved to [[[IN11431](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11433&)]] - ZGW - Internal Fee Payout Contact Changed Report Alert

  


  


Estimated Cost: Approximately $500

  


Spec:

  


Overview/Purpose: This is an internal report alert that notifies users that a Contact listed on the "Internal Fee Payouts Configuration" embedded spreadsheet in Silverloom Settings has been deactivated or has been changed to a different Contact Type. 

  


Details: 

  * Title: "Internal Fee Payout Contact Changed - Remove from configuration list" 
  * Displays within 20 minutes of: 
    * Contact listed on the "Internal Fee Payouts Configuration" embedded spreadsheet in Silverloom Settings is marked as Inactive or has its Contact Type changed to something other than "Internal". 
  * Action: Open the Silverloom Settings page
  * User(s) to notify: 
    * Users with the "Manage Financials" Permission 
  * Dismiss type:  
    * Auto-dismiss when all items are resolved



  


Other Notes:

  * N/A



  


Development Specification

Mockup: N/A

  


Ellis Miller 12/24/2024: A simple Auto-push report that checks

[ ] Std Alert Invalid Fee Payout Contacts.r20

[ ] Report runs on Silverloom Settings record. Subset does a HasRG on Internal Fee Payout Contacts

BID: 4 HOURS
