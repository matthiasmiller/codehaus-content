5.3.1.2.1. Transfer Vehicle Actions

  


Requirements

*Done. 

  


High-level notes: 

  * Transferring a vehicle to a household member (i.e. if "Transfer coverage to household member" = "Yes"):  
    * active Liability coverage is transferred for free for the New Owner (they are not charged for the remaining portion of the Premium for active coverage(s)), and the Prior Owner does not get any refund; 
    * active Collision coverage is transferred for free for the New Owner (they are not charged for the remaining portion of the 5-year Entry Fee (if applicable) or the remaining portion of the current Period Year's Liability), and the Prior Owner does not get any refund, unless the the "Collision Coverage Amount" is decreased for the New Owner; 
    * coverages are technically deactivated for the Prior Owner and reactivated for the New Owner, but no refunds are generated for the Prior Owner for any coverages (even if a coverage is being canceled or the Vehicle is becoming a No-Charge Vehicle).
    * active Cargo coverage is deactivated and not transferred to the New Owner (and the Prior Owner does receive a refund for any remaining portion of the Entry Fee (if applicable) and Premium). 



 

  * Transferring a vehicle to a non-household member (i.e. if "Transfer coverage to household member" = "No"): 
    * any active coverages are deactivated for the Prior Owner, appropriate refunds are generated for the remaining portion of each; 
    * all coverage information and most vehicle information is cleared, to start with a clean slate for the New Owner. 



  


  * Who can initiate a transfer:
    * All agents can transfer any Vehicle, but can only transfer it to one of their own clients.
    * Admins can transfer a vehicle owned by any client.



  


  * Transferring an inactive Vehicle: Only ownership is changed, and no new rows are added to any embedded spreadsheet ("Guidelines Compliance", "Fees and Credits", "Coverage History", or "Deactivation History")



  


  


  * Transferring a No-Charge Vehicle: 
    * Prior Owner Charge + New Owner Charge: 
      * Standard procedure, as specced out below.  
    * Prior Owner Charge + New Owner No-Charge: 
      * All "Amount" rows for the New Owner are set to "0.00". 
      * If Collision Coverage Amount is increased in the Transfer process, there is no extra fee for the New Owner.
      * Refunds are generated for the Prior Owner for all active coverages.
    * Prior Owner No-Charge + New Owner No-Charge: 
      * All "Amount" rows for the New Owner are set to "0.00". 
      * If Collision Coverage Amount is increased in the Transfer process, there is no extra fee for the New Owner.
      * No refunds are generated for the Prior Owner for any coverages.
    * Prior Owner No-Charge + New Owner Charge: 
      * If Collision Coverage Amount is increased in the Transfer process, an additional fee is generated for the New Owner. 
      * No refunds are generated for the Prior Owner for any coverages.



  


  


Spec for standard coverage transfer (this is for Vehicles that start the transfer process with at least one active coverage, and than have the "No-Charge Vehicle" checkbox not checked; see "Transferring a No-Charge Vehicle" and "Transferring an Inactive Vehicle" notes for exceptions): 

  


Transferring Liability Coverage:

  * I. In the Fees and Credits embedded spreadsheet:
    * 1. If "Transfer coverage to household member" = "No":
      * (1). Row(s) are added for the Prior Owner, for refunds for unused portions of the old coverage (note that two rows are added if the Vehicle is transferred in May or June, after the coverage has already been renewed for the upcoming Period Year): : 
        * "Client Name" = Prior Owner's name; 
        * "Fee Date" = current date; 
        * "Coverage Type" = "Liability"; 
        * "Fee Type" = "Premium"; 
        * "Agent = current agent of the client in "Client Name"; 
        * "Fund" = current fund of "Agent"; 
        * "Invoice" = N/A; 
        * "Amount" = negative amount, prorated based on the remaining portion for the prior owner for the corresponding Period Year; 
        * "Billing Action" = "Invoice" (for a refund);  
        * "Status" = N/A; 
        * "Start Date" = "Start Date" of the fee row being refunded; 
        * "End Date" = current date) 
      * (2). Rows are added for the New Owner (note that two rows are added if the Vehicle is transferred in May or June, to renew the coverage for the upcoming Period Year):  
        * "Client Name" = New Owner's name; 
        * "Fee Date" = current date; 
        * "Coverage Type" = "Liability"; 
        * "Fee Type" = "Premium"; 
        * "Agent = current agent of the client in "Client Name"; 
        * "Fund" = current fund of "Agent"; 
        * "Invoice" = N/A; 
        * "Amount" = prorated Premium amount for the remaining portion of the corresponding Period Year; 
        * "Billing Action" = "Invoice";  
        * "Status" = N/A; 
        * "Start Date" = current date; 
        * "End Date" = Period End Date.  
    * 2. If "Transfer coverage to household member" = "Yes":
      * (1). Rows are added for the Prior Owner, for refunds for unused portions of the old coverage (see spec above), with the following difference: 
        * "Amount" = "0.00"; 
      * (2). Rows are added for the New Owner, for the current Period Year, and upcoming Period Year, if transferred in May or June, (see spec above), with the following difference: 
        * "Amount" = "0.00". 



  


  * II. In the Coverage History embedded spreadsheet:
    * 1. If "Transfer coverage to household member" = either "Yes" or "No":
      * (1). The currently-active row for the Prior Owner: "Status" is changed from "Active" to "Used";
      * (2). If the transfer happens in May/June and any row exists for the Prior Owner for the upcoming Period Year: "Status" up the upcoming row is changed from "Active" to "Canceled";
      * (3). A row is added for the new Owner, with the following set:
        * "Date" = the current date; 
        * "Owner" = the new "Owner"; 
        * "Coverage Type" = "Liability"; 
        * "No-Charge" = based on the "No-Charge Vehicle for New Owner" prompt; 
        * "Start Date" = the current date; 
        * "End Date" = the "Current Period End Date"; 
        * "Status" = "Active"; 
      * (4). If the transfer happens in May/June: A row is added for the new Owner for the upcoming Period Year, with the following set:
        * "Date" = the current date; 
        * "Owner" = the new "Owner"; 
        * "Coverage Type" = "Liability"; 
        * "No-Charge" = based on the "No-Charge Vehicle for New Owner" prompt; 
        * "Start Date" = the "Next Period Start Date"; 
        * "End Date" = the "Next Period End Date"; 
        * "Status" = "Active". 



  


  * III. In the Deactivation History embedded spreadsheet:
    * 1. If "Transfer coverage to household member" = either "Yes" or "No":
      * (1). If the Vehicle is the last active vehicle for the Prior Owner: A row is added with "Owner" = the Prior Owner and "Date" = the current date. 



  


  


Transferring Collision Coverage (see "Transferring a No-Charge Vehicle" and "Transferring an Inactive Vehicle" notes for exceptions):

  * I. In the Fees and Credits spreadsheet: 
    * A.If "Collision Coverage for New Owner?" = "Yes":
      * 1. If "Transfer coverage to household member" = "No":
        * a. If the Vehicle had Collision coverage for the prior owner: 
          * (1). Rows are added for the Prior Owner, for refunds for unused portions of the old coverage: 
            * If the Solution uses Collision Entry Fees: Entry Fee: 
              * "Client Name" = prior owner's name; 
              * "Fee Date" = current date; 
              * "Coverage Type" = "Collision"; 
              * "Fee Type" = "Entry Fee"; 
              * "Agent = current agent of the client in "Client Name"; 
              * "Fund" = current fund of "Agent"; 
              * "Invoice" = N/A; 
              * "Amount" = negative amount, prorated based on the remaining portion for the prior owner, as of 5 years from the "Start Date" for their Entry Fee; 
              * "Invoice Action" = "Invoice" (for a refund);  
              * "Status" = N/A; 
              * "Start Date" = current date; 
              * "End Date" = blank; 
            * Premium (note that two rows are added if the Vehicle is transferred in May or June, after the coverage has already been renewed for the upcoming Period Year): 
              * "Client Name" = prior owner's name; 
              * "Fee Date" = current date; 
              * "Coverage Type" = "Collision"; 
              * "Fee Type" = "Premium"; 
              * "Agent = current agent of the client in "Client Name"; 
              * "Fund" = current fund of "Agent"; 
              * "Invoice" = N/A; 
              * "Amount" = negative amount, prorated based on the remaining portion for the prior owner for the corresponding Period Year; 
              * "Invoice Action" = "Invoice" (for a refund);  
              * "Status" = N/A; 
              * "Start Date" = "Start Date" of the fee row being refunded; 
              * "End Date" = current date) 
          * (2). Rows are added for the New Owner: 
            * If the Solution uses Collision Entry Fees: Entry Fee: 
              * "Client Name" = New Owner's name; 
              * "Fee Date" = current date; 
              * "Coverage Type" = "Collision"; 
              * "Fee Type" = "Entry Fee"; 
              * "Agent = current agent of the client in "Client Name"; 
              * "Fund" = current fund of "Agent"; 
              * "Invoice" = N/A; 
              * "Amount" = calculated based on the "Collision Coverage Amount" and settings in the selected Vehicle Type, for the standard 5 year Entry Fee; 
              * "Billing Action" = "Invoice";  
              * "Status" = N/A; 
              * "Start Date" = current date; 
              * "End Date" = blank; 
            * Premium (note that two rows are added if the Vehicle is transferred in May or June, to renew the coverage for the upcoming Period Year): 
              * "Client Name" = New Owner's name; 
              * "Fee Date" = current date; 
              * "Coverage Type" = "Collision"; 
              * "Fee Type" = "Premium"; 
              * "Agent = current agent of the client in "Client Name"; 
              * "Fund" = current fund of "Agent"; 
              * "Invoice" = N/A; 
              * "Amount" = prorated Premium amount for the remaining portion of the current Period Year; 
              * "Billing Action" = "Invoice";  
              * "Status" = N/A; 
              * "Start Date" = current date; 
              * "End Date" = Period End Date.  
        * b. If the Vehicle did not have Collision coverage for the Prior Owner: 
          * (1). No rows are added for the Prior Owner (since there was no coverage to refund); 



(2). Rows are added for the New Owner, for the current Period Year, and upcoming Period Year, if transferred in May or June, (see spec above)

  


  * 2. If "Transfer coverage to household member" = "Yes":
    * a. If the Vehicle had Collision coverage for the Prior Owner: 
      * (1). Rows are added for the Prior Owner, for refunds for unused portions of the old coverage (see spec above), with the following difference: 
        * "Amount" = "0.00", unless "Collision Coverage Amount" for the New Owner is less than for the Prior Owner, in which case the "Amount" here is the prorated amounts of the difference of the Entry Fee (if applicable) and Premium for the remaining portion of the fees; 
      * (2). Rows are added for the New Owner, for the current Period Year, and upcoming Period Year, if transferred in May or June, (see spec above), with the following difference: 
        * "Amount" = "0.00"; 
    * b. If the Vehicle did not have Collision coverage for the Prior Owner: 
      * (1). No rows are added for the Prior Owner (since there was no coverage to refund); 
      * (2). Rows are added for the New Owner, for the current Period Year, and upcoming Period Year, if transferred in May or June, (see spec above)



  


  * B. If "Collision Coverage for New Owner?" = "No":
    * 1. If "Transfer coverage to household member" = either "Yes" or "No":
      * a.If the Vehicle had Collision coverage for the Prior Owner: 
        * (1). Rows are added for the Prior Owner, for refunds for unused portions of the old coverage (see spec above). 
        * (2). No rows are added for the New Owner. 
      * b. If the Vehicle did not have Collision coverage for the Prior Owner: 
        * (1). No rows are added for the Prior Owner (since there was no coverage to refund); 
        * (2). No rows are added for the New Owner. 



  


  


  * II. In the Coverage History spreadsheet:
    * A. If "Collision Coverage for New Owner?" = "Yes":
      * 1. If "Transfer coverage to household member" = either "Yes" or "No":
        * Same as items (1), (2), (3), and (4) under "II. In the Coverage History embedded spreadsheet" for Liability coverage above.



  


  * B. If "Collision Coverage for New Owner?" = "No":
    * 1. If "Transfer coverage to household member" = either "Yes" or "No":
      * a. Same as items (1) and (2) under "II. In the Coverage History embedded spreadsheet" for Liability coverage above.



  


  * III. In the Deactivation History spreadsheet:
    * A. If "Collision Coverage for New Owner?" = either "Yes" or "No": 
      * 1. If "Transfer coverage to household member" = either "Yes" or "No":
        * (1). If the Vehicle is the last active vehicle for the Prior Owner (and if a row is not already being added by deactivating Liability coverage): A row is added with "Owner" = the Prior Owner and "Date" = the current date. 



  


  


Transferring Cargo Coverage: N/A -- Cargo Premium and Entry Fee (if applicable) are never transferred (Cargo coverage is always canceled in the process).

  


Development Specification

TODO_: Tim Reitz 07/28/2025: Follow up here once we have this settled - see [[[IN11925](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11927&)]]. Update the transfer actions spec below too if needed.  

  * Transferring a vehicle to a household member (i.e. if "Transfer coverage to household member" = "Yes"):  
    * active Liability coverage is transferred for free for the New Owner (they are not charged for the remaining portion of the Premium for active coverage(s)), and the Prior Owner does not get any refund; 
    * active Collision coverage is transferred for free for the New Owner (they are not charged for the remaining portion of the 5-year Entry Fee or the remaining portion of the current Period Year's Liability), and the Prior Owner does not get any refund, unless the the "Collision Coverage Amount" is decreased for the New Owner; 
    * ...



  


  


  


Change Requests: 

  * Tim Reitz 08/18/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident
  * Tim Reitz 08/23/2025: Tim Reitz 08/23/2025: [[[IN9943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9945&)]] - ZWA - Pre-ZWW - Vehicle Record - Fees & Credits - Add "Dismiss" Option for Fees


