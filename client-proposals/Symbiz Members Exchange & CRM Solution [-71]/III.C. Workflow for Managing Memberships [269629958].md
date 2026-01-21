3.3. Workflow for Managing Memberships

  


Requirements

The following is a basic description of how to manage memberships:

  


Note that while the person is considered to be a Member immediately upon their application being marked as approved, they do not have an Active Membership until the initial payment is received. In addition, their 1-year "membership clock" does not start until they have been added to a Growth Ring Group. 

  


Initial setup for a new Member: 

  * Note that an address is required for all Members.
  * In the Membership Details section of the Members Contact record:
    * Check the "Initial Invoice Sent" checkbox when the invoice has been sent. 
    * Check the "Online Member" checkbox if the Member will have access to the Members Exchange. 
      * Note that you can manually create and connect the new Member's user profile to give them login access, or you can wait until you click the "Activate Membership" button after the initial payment has been received to do this automatically. 
      * Note that an email address is required for an Online Member.
    * Check the "Confidentiality Agreement" checkbox when it has been received. 
      * Note that this step is not required to activate the Membership.
    * Set the "Account Name" as needed by selecting the appropriate Organization from the list. 
      * Note that this step is not required to activate the Membership.



  


To activate a membership: 

  * Check the "Initial Payment Received" checkbox when the payment has been received. This makes the Activate Membership button visible. 
  * Click the "Activate Membership" button. 
    * Note that clicking this button gives the Member an active membership, though their Paid Membership Start Date isn't set until they join a Growth Ring Group. 
    * Note that clicking this button also sets up the User Profile for Online Members, if they did not already have access. 
    * Note that you will need to refresh the page to see the updated information after clicking "Activate Membership".
    * The Members Exchange Welcome Email is sent automatically to the Online Members at this point. This email contains the information they need to log into the Members Exchange for the first time.



  


 To add a Member to a Growth Ring Group: 

  * Open the Growth Ring Groups report by doing one of the following:
    * On the Member's Contact record, click "Find Group" in the Personal Details section.
      * This will open filtering options to find a specific Group. You can also leave the filter options as they are and click "Continue" to open a report of all Growth Ring Groups.
    * On the Members menu, click "All Growth Ring Groups" in the Members & Groups section.
    * On the Admin menu, click "Find Group" in the Growth Ring Group Management section.
      * This will open filtering options to find a specific Group. You can also leave the filter options as they are and click "Continue" to open a report of all Growth Ring Groups.
  * Click on the desired Group Description to open that Group's record.
  * Click "Edit" in the top left hand corner.
  * In the "Group Members" section, click the "Add" button to add a new row to the table.
  * Select the desired Member from the resulting drop list.
    * Note that you can start typing the Member's name to filter down to find them.
  * Click "Yes" when asking if you wish to Save.
  * Close the pop-up child screen and refresh the page.
  * The new Member will be added to the Group and the Group Description will be displayed in the Member's Personal Details section.
    * Note that you will need to refresh the Member's Contact record to make and save any new edits.



  


To deactivate a membership: 

  * If the Member is a Regional Rep, remove them from the Region record(s):
    * In their Contact record, click the name of the Region in the "Regional Rep for:" field in the Personal Details section.
    * In the resulting report, click the name of the Region again.
    * Click the "Edit" button in the top left corner.
    * Choose a new Regional Rep from the drop list.
    * Click "Save" in the top left corner.
  * If the Member is a Facilitator, remove them from the role on the Growth Ring Group record(s):
    * In their Contact record, click the name of the Group in the "Facilitator for:" field in the Personal Details section.
    * In the resulting report, click the name of the Group again.
    * Click the "Edit" button in the top left corner.
    * Uncheck the "Facilitator" checkbox in the Group Members section.
    * Check the "Facilitator" checkbox for the desired new Facilitator.
    * Click "Save" in the top left corner.
  * On the Member's Contact record, click the "Deactivate Membership" button in the Membership Details section to end their membership.  
    * Note that clicking this buttons removes the Member from any Growth Ring Groups of which they are a member, so that does not need to be done manually. A separate automatic process will remove the member from future meetings for their Group(s). Any incomplete Goals will simply remain. 
    * Note that clicking this button also deactivates the Member's User Profile, so the Member no longer has access to the Members Exchange. 



  


To renew a membership for a Member: 

  * Note that the renewal process can be done when the "Next Renewal Date" is within 30 days from the current date, or when it is in the past. 
  * On the Member's Contact record, click "Edit" in the top left corner.
  * In the Membership Details section, check the "Renewal Invoice Sent" checkbox when the invoice has been sent.
  * Check the "Renewal Payment Received" checkbox when the payment has been received.
  * Click "Save" in the top left corner.
  * Other Notes:
    * The "Next Renewal Date" can be edited by Super Admin if there is not a pending renewal. 
    * The membership will remain active until it is ended via the "Deactivate Membership" button, even if the Renewal Date is in the past. This allows for easy handling of a "grace period" and eliminates undesired automatic deactivations. 
    * How to give a grace period: Simply bump out the Membership Year Start date of the new year/row and leave a gap between the "Next Renewal Date" of the previous year and the start of the current year. The membership will stay active, but there will be a gap in their paid membership period.



  


To reactivate a membership for a Member whose membership was previously ended: 

  * On the Members Menu, click "Contacts" in the Contacts section.
  * In the top left corner of the resulting report, click "Contacts" to open filtering options.
  * Search for the desired inactive Member.
  * Click their Name to open their Contact record.
  * Click "Edit" in the top left corner.
  * Fill the "Initial Payment Received" checkbox if it has been cleared. 
  * Click the "Reactivate Membership" button.
    * Note that clicking this button will automatically do the following:
      * Re-fill the Active Membership checkbox
      * Reactivate the linked User Profile if one is linked
      * Create a new active User Profile and link it to the Contact if none is linked and "Online Member" is set to "Yes"
      * Clear the Paid Membership Start date
      * Clear the Membership End Date
      * Display the reactivation message: "Please review and confirm that the renewal dates and payments are correct, and reset the Next Renewal Date if needed. Add the member to a Growth Ring Group to reset the Paid Membership Start date and clear this message."
  * Review and confirm the information above. 
  * Add the Member to a Growth Ring Group, as for a new member, by using the steps in the "To Add a Member to a Growth Ring Group" section above.
    * Note that the Member will need to clean up any old Goals (marking them as incomplete, or reusing them).



  


Development Specification

Change Requests: 

  * Tim Reitz 04/08/2024: This job and child jobs: [[[IN9581](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9583&)]] - ZSB - Contact Record - (Simplified) Clean up Renewal Process & Fields: Main Job


