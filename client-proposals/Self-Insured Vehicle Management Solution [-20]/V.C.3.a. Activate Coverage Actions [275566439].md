5.3.3.1. Activate Coverage Actions

  


Requirements

High-level notes: When the "Activate" button is clicked for any coverage, rows are added to the "Fees and Credits" and "Coverage History" embedded spreadsheets for the corresponding Coverage Type.

  


Actions: 

  * "Date Entered" for the Coverage: sets to the current date;
  * "<Coverage Type> Coverage Is Active" for the Coverage: sets to "Yes";
  * I. In the "Fees and Credits" embedded spreadsheet:
    * (1). A row is added for the Entry Fee (note that this only applies to "Collision" and "Cargo" (there are no Entry Fees for Liability coverage), and only if the Solution has the "Plan: Collision: Uses entry fees" / "Plan: Cargo: Uses entry fees" System Switches set to "Yes"): 
      * "Client Name" = Owner's name; 
      * "Fee Date" = current date; 
      * "Coverage Type" = the Coverage Type of the current section ("Collision" or "Cargo");
      * "Fee Type" = "Entry"; 
      * "Agent = current agent of the client in "Client Name"; 
      * "Fund" = current fund of "Agent"; 
      * "Invoice" = N/A; 
      * "Amount" =
        * if "Coverage Type" = "Collision": sets to the value of <"Collision Entry Fee %" from the current "Vehicle Type"> * <"Coverage" amount>, prorated based on "Start Date" and "End Date";
        * if "Coverage Type" = "Cargo": sets to the value of <"Cargo Entry Fee %" from the current "Vehicle Type"> * <"Coverage" amount>, prorated based on "Start Date" and "End Date"; 
      * "Billing Action" = "Invoice";  
      * "Status" = N/A; 
      * "Start Date"
        * if the current date is on or after the "Current Period Start Date": sets to the "Activation Date"; 
        * otherwise: sets to the "Current Period Start Date"; 
      * "End Date" = "Current Period End Date"  



  


  


  * (2a) One or two rows are added for the Premium (note that two rows are added if the coverage is activated in May or June, to renew the coverage for the upcoming Period Year): 
    * "Client Name" = Owner's name; 
    * "Fee Date" = current date; 
    * "Coverage Type" = the Coverage Type of the current section ("Liability" or "Collision" or "Cargo"); 
    * "Fee Type" = "Premium";
    * "Agent = current agent of the client in "Client Name"; 
    * "Fund" = current fund of "Agent"; 
    * "Invoice" = N/A; 
    * "Amount" =
      * if "Coverage Type" = "Liability": sets to the "Premium Amount $" from the selected "Vehicle Type"; 
      * if "Coverage Type" = "Collision" and "__" for the selected "Vehicle Type" is checked: sets based on "<Alternate text for Collision - Short label> Premium $" and/or "<Alternate text for Collision - Short label> Premium %" from the selected "Vehicle Type", depending on the Solution's settings for the "Plan: Collision Premium: Uses % fees" and "Plan: Collision Premium: Uses flat fees" System Switches, prorated based on "Start Date" and "End Date"; 
      * if "Coverage Type" = "Cargo" and "__" for the selected "Vehicle Type" is checked: sets based on "<Cargo Premium $" and/or "Cargo Premium %" from the selected "Vehicle Type", depending on the Solution's settings for the "Plan: Cargo Premium: Uses % fees" and "Plan: Cargo Premium: Uses flat fees" System Switches, prorated based on "Start Date" and "End Date";
    * "Billing Action" = "Invoice";  
    * "Status" = N/A; 
    * "Start Date" =
      * if the current date is on or after the "Current Period Start Date": sets to the "Activation Date"; 
      * otherwise: sets to the "Current Period Start Date"; 
    * "End Date" = "Current Period End Date".  



  


  


  * (2b) Special behaviors if the current date is within the months of May or June when the coverage is activated: 
    * if "Deactivation Date" for the Coverage is blank: adds an additional row to both "Fees and Credits" and "Coverage History" for the upcoming Period Year; 
    * if "Activation Date" for the Coverage is in the past: adds an additional row both "Fees and Credits" and "Coverage History" for the upcoming Period Year; 
    * if "Activation Date" for the Coverage is in the previous Period Year: adds two additional rows to both "Fees and Credits" and "Coverage History" \- one for the previous Period Year and one for the upcoming Period Year.



  


  


  * II. In the "Coverage History" embedded spreadsheet:
    * (1) If the coverage being deactivated is the last active coverage for the Vehicle: One or two rows are added for the coverage(s) -- usually one row, but two rows if Activation is in May/June and an automatic renewal happens: 
      * "Date" = the current date; 
      * "Owner" = the new "Prior Owner"; 
      * "Vehicle Deactivation Reason" = blank  & editable;  
      * "Vehicle Deactivation Reason (Other)" = blank & read-only; 
      * "Client Deactivation Reason": 
        * if the Vehicle is the last active Vehicle for the new "Prior Owner" = blank & editable; 
        * otherwise = blank & read-only; 
      * "Client Deactivation Reason (Other)" = blank & read-only. 



  


TODO_CCI1: Tim Reitz 08/15/2025: Could you give this section spec a quick review to make sure it all looks correct? Thanks!

Murshid Rahman 08/20/2025: I could not test is myself but looks correct to me on the first glance. I am taking a note and I will review this again once I am back. Thanks.

  


Development Specification

Change Requests: 

  * Tim Reitz 08/23/2025: Tim Reitz 08/23/2025: [[[IN9943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9945&)]] - ZWA - Pre-ZWW - Vehicle Record - Fees & Credits - Add "Dismiss" Option for Fees


