5.3.3.2. Deactivate Coverage Actions

  


Requirements

High-level notes: When the "Deactivate" button is clicked for any coverage, refund rows are added to the "Fees and Credits" embedded spreadsheet for the corresponding Coverage Type and the corresponding row in the "Coverage History" embedded spreadsheet is updated accordingly.

  


Actions: 

  * "Date Entered" for the Coverage: is cleared;
  * "Activation Date" for the Coverage: is cleared;
  * "<Coverage Type> Coverage Is Active" for the Coverage: sets to "No";
  *  I. In the "Fees and Credits" embedded spreadsheet:
    * (1). A row is added to refund the remaining portion of the Entry Fee (note that this only applies to "Collision" and "Cargo" (there are no Entry Fees for Liability coverage), and only if the Solution has the "Plan: Collision: Uses entry fees" and/or "Plan: Cargo: Uses entry fees" System Switches set to "Yes", and only if the current date is within 5 years of the "Start Date" for the Entry Fee for the Coverage): 
      * "Client Name" = Owner's name; 
      * "Fee Date" = current date; 
      * "Coverage Type" = the Coverage Type of the current section ("Collision" or "Cargo"); 
      * "Fee Type" = "Entry"; 
      * "Agent = current agent of the client in "Client Name"; 
      * "Fund" = current fund of "Agent"; 
      * "Invoice" = N/A; 
      * "Amount": sets to the prorated (unused) portion of the Entry Fee for the remainder of the 5 years from the Entry Fee Start Fee;
      * "Billing Action" = "Invoice" (for a refund);  
      * "Status" = N/A; 
      * "Start Date"
        * if the current date is on or after the "Current Period Start Date": sets to the "Activation Date"; 
        * otherwise: sets to the "Current Period Start Date"; 
      * "End Date" = "Current Period End Date"  



  


  * (2a) One or two rows are added to refund the remaining portion of the Premium (note that two rows are added if the coverage is deactivated in May or June after having been renewed for the upcoming Period Year): 
    * "Client Name" = Owner's name; 
    * "Fee Date" = current date; 
    * "Coverage Type" = the Coverage Type of the current section ("Liability" or "Collision" or "Cargo"); 
    * "Fee Type" = "Premium"; 
    * "Agent = current agent of the client in "Client Name"; 
    * "Fund" = current fund of "Agent"; 
    * "Invoice" = N/A; 
    * "Amount": sets to the prorated (unused) portion of the Premium for remainder of the "Period Year";
    * "Billing Action" = "Invoice" (for a refund);  
    * "Status" = N/A; 
    * "Start Date" =
      * if the current date is on or after the "Current Period Start Date": sets to the "Activation Date"; 
      * otherwise: sets to the "Current Period Start Date"; 
    * "End Date" = "Current Period End Date".  



  


  * II. In the "Coverage History" embedded spreadsheet:
    * "Status" for the corresponding coverage row: Changes from "Active" to "Used".



TODO_VA: Tim Reitz 10/23/2025: I think we also need to note that "End Date" is updated if needed. 

  


  * III. In the "Deactivation History" embedded spreadsheet:
    * If the Vehicle does not have any remaining active coverages: A row is added with "Owner" = the Prior Owner and "Date" = the current date.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/23/2025: [[[IN9943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9945&)]] - ZWA - Pre-ZWW - Vehicle Record - Fees & Credits - Add "Dismiss" Option for Fees


