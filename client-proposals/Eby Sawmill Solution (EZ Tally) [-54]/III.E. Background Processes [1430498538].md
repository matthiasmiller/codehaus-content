3.5. Background Processes

  


Requirements

The Solution includes the following background processes. These are configured in the Solution at deployment by CH/CCI.

  


1\. Create and Link Single Payment: 

  * Overview: This background process links "Open Unpaid" Payment records with a single Pulpwood Load or Yard Tally record (setting the Payment ID field). If no "Open Unpaid" Payment record exists, this process creates a new one before linking. 
  * Schedule: 
    * When the "Create Payment" link is clicked on Yard Tally records
    * When the "Create Payment" link is clicked on Pulpwood Load records
    * From the Yard App, when a Yard Tally is saved after the user marks it as "Confirmed"
  * Actions:
    * Creates a single Payment records for Landowner, Logger, or Vendor, depending on whether it is run from a Yard Tally or a Pulpwood Load (Std Create Single Payment.x30)
    * For Yard Tally records, sets the Payment ID for Landowner and/or Logger, or Vendor (Std Yard Tally Set Single Payment ID.x30) 
    * For Pulpwood Load records, sets the Payment ID for Landowner and/or Logger (Std Pulpwood Load Set Single Payment ID.x30)
  * Command(s):
    * N/A (no Scheduled Task is needed for this since it is always run via a button, and any items that are missed will be caught by the "Create and Link All Payments" background process the next time it is run) 



  


  


2\. Create and Link All Payments: 

  * Overview: This background process looks at multiple records (Tract, Yard Tally, and Pulpwood Load) and links "Open Unpaid" Payment records to them, creating the Payment records if needed. 
  * Schedule: 
    * When the "Create Missing Payments" button is clicked on the Payments Due reports
    * Nightly at 3:00am (via a Scheduled Task with the same name -- see "Command(s) below) 
  * Actions: 
    * Searches Tract records (for Down Payment & Expense Withholding items), Yard Tally records (Landowner, Logger, & Vendor payments), and Pulpwood Load records (Landowner and Logger payments), eliminates duplication if there is any, and creates Payment records as needed. (Std Create Unpaid Payments.x30)
    * For Tract records, sets the Payment ID for Down Payment and Expense Withholding items. (Std Tract Set Payment IDs.x30) 
    * For Tract-sourced Yard Tally records, sets the Logger Payment ID. (Std Yard Tally Set Logger Payment IDs.x30)
    * For Tract-sourced Yard Tally records, also sets the Landowner Payment ID. (Std Yard Tally Set Landowner Payment IDs.x30)
    * For Vendor-sourced Yard Tally records, sets the Vendor Payment ID. (Std Yard Tally Set Vendor Payment IDs.x30) 
    * For Pulpwood Load records, sets the Landowner Payment ID. (Std Pulpwood Load Set Logger Payment IDs.x30)
    * For Pulpwood Load records, also sets the Logger Payment ID. (Std Pulpwood Load Set Landowner Payment IDs.x30)
  * Command(s): 
    * import "Standard/Std Create and Link All Payments.x30list"



  


  


3\. Daily Payment Emails:

  * Overview: This background process runs automatically via a Scheduled Task to send out various emails. 
  * Schedule:
    * Daily at 7:00am (via a Scheduled Task with the same name)
  * Actions:
    * Sends the Landowner Flat Payments Due Email; see details in the corresponding section of the proposal (Std Landowner Flat Payments Due Email Merge.r20) 
    * Sends the Unpaid Vendor Yard Tallies Email; see details in the corresponding section of the proposal (Std Unpaid Vendor Yard Tallies Email Merge.r20) 
  * Command(s)
    * email "Standard/Std Landowner Flat Payments Due Email Merge.r20" \--maximumemails=1000
    * email "Standard/Std Unpaid Vendor Yard Tallies Email Merge.r20" \--maximumemails=1000



  


  


4\. Service Yard Tallies: 

  * Overview: This background process is initiated from the Yard App, and runs to update Yard Tally records in the main system, based on changes made in the Yard App. 
  * Schedule: 
    * When the "Save Tally & Return" button is selected in the Yard Scaling portion of the Yard App. 
  * Actions: 
    * Marks a Yard Tally as unconfirmed, if the "Confirmed" checkbox was unchecked in the Yard App (Std Service Yard Tallies - 1 - Unconfirm.x30);  
    * Creates a new Yard Tally record, or updates an existing one, with data entered in the Yard App (Std Service Yard Tallies - 2 - Changes.x30); 
    * Marks a Yard Tally as Confirmed if the "Confirmed" checkbox was set to checked in the Yard App (Std Service Yard Tallies - 3 - Confirm.x30). 
  * Command(s): 
    * N/A (no Scheduled Task is needed for this since it is always run via a button) 
  * Other Notes: 
    * This is referred to internally as "STD SERVICE YARD TALLIES.X30LIST". 



  


  


5\. Service Export Tallies: 

  * Overview: This background process is initiated from the Yard App, and runs to update Export Tally records in the main system, based on changes made in the Yard App. 
  * Schedule: 
    * When the "Save Tally & Return" button is selected in the Export Scaling portion of the Yard App. 
  * Actions: 
    * Marks an Export Tally as unconfirmed, if the "Confirmed" checkbox was unchecked in the Yard App (Std Service Export Tallies - 1 - Unconfirm.x30);  
    * Creates a new Export Tally record, or updates an existing one, with data entered in the Yard App (Std Service Export Tallies - 2 - Changes.x30); 
    * Marks an Export Tally as Confirmed if the "Confirmed" checkbox was set to checked in the Yard App (Std Service Export Tallies - 3 - Confirm.x30); 
    * Fills Load Details section fields on an Export Tally record, including load photos, with data entered in the Yard App (Std Service Export Tallies - 4 - Changes.x30); 
    * Marks an Export Tally as Loaded if the "Loaded" checkbox was set to checked in the Yard App (Std Service Export Tallies - 5 - Load.x30). 
  * Command(s): 
    * N/A (no Scheduled Task is needed for this since it is always run via a button)
  * Other Notes: 
    * This is referred to internally as "STD SERVICE EXPORT TALLIES.X30LIST".



  


Development Specification

Change Requests: 

  * Tim Reitz 02/05/2024: [[[IN9150](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9152&)]] - ZET - Rework Payment ID logic for performance and bullet-proofing 
  * Tim Reitz 09/17/2024: [[[IN9330](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9332&)]] - ZET - Yard App isn't setting Payment Amounts when confirming yard tally
  * Tim Reitz 10/07/2024: [[[IN10236](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10238&)]] - ZET - Rework Payment Linking
  * 


  


TODO_: Tim Reitz 09/05/2023: Use this for documenting scheduled tasks / x30s / etc.

  


Dev Spec notes for the designers: 

  * General info: [[[W0457](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-458&)]] - 170. Scheduled Tasks
  * Wiki page for setting up Scheduled Tasks: [[[W0552](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-553&)]] - Setting Up Scheduled Tasks 
  * [X] Add a note to the deployment incident to set up the Scheduled Tasks


