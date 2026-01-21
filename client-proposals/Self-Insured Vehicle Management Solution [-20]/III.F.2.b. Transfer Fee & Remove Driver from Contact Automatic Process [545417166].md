3.6.2.2. Transfer Fee & Remove Driver from Contact Automatic Process

  * Name: "Transfer Fee & Remove Driver from Contact" 
    * Description: This process completes the setup of a new Contact created from a Household Driver of an existing Contact, transferring over pertinent information.
    * Prompts: 
      * N/A (not specced here) 
    * Initiated:
      * When the "Transfer" button is clicked on the Contact record.
    * Action(s): 
      * 1\. Transfer all (both paid and unpaid) Contact / HRD fees for this new Client from the "parent" Contact to the new Contact, based on the "Household Driver" name; 
        * note that if there are any unpaid invoices for an HRD fee, those invoices will remain under the "parent" Contact, and the agent can manually change the invoice to the new Contact if needed 
        * (Std Transfer Fees to Driver Contact Import.x30); 
      * 2\. Transfer Claim records from the "parent" Contact to the new Contact: All Claims for which the new Contact is set as the Driver have the following changed:
        * "Client": set to the new Contact;
        * "Originating Owner": sets to the "parent" Contact;
        * "Stored Claim Driver ID": sets to "1" for the new Owner;
        * "Stored Claim Driver Name": sets to the "Display Name" for the new Owner; 
        * (Std Claim Update Client Import.x30) 
      * 3 Update any Vehicles belonging to the "parent" Contact for which the new Contact was set as the "Primary Driver"; the following field(s) are changed:
        * "Primary Driver": set to the "parent" Contact;
        * (Std Vehicle Update Primary Driver Import.x30) 
      * 4\. Remove the corresponding driver from the "parent" Contact's Household Drivers embedded spreadsheet
        * (Std Remove Driver from Contact.x30); 
      * 5\. __ (Std Remove Parent Contact from Contact.x30) 



_CCI1: Tim Reitz 08/20/2025: I apparently forgot to ask about this one previously. Could you give a brief summary of this one too?

Murshid Rahman 09/03/2025: We have 2 hidden fields ContactParentContact and 

ContactDriverIDInParent. When the transfer process starts, we set the values for linking purposes. Then as soon as the household driver becomes new contact (transfer process ends), we remove the values set on these fields via this x30. Please let us know if this is confusing. Thanks.

TODO_CCI1: Tim Reitz 09/15/2025: Yes, I think that makes sense. I'll summarize what I'm understanding, and you can confirm / correct it as needed:

Fields on the Contact record: 

  * Parent Contact (hidden; drop list of Contact records; when a new Contact record is created with "The new contact is a driver for an existing client" = "Yes", this sets to the the Contact selected in the "Client" prompt, then this is cleared when the "Transfer Fee & Remove Driver from Contact" automatic process is run) 
  * Driver ID in Parent Contact (hidden; number field; 0 decimals; when a new Contact record is created with "The new contact is a driver for an existing client" = "Yes", this sets to the "Driver ID" for the selection in the "Driver" prompt, then this is cleared when the "Transfer Fee & Remove Driver from Contact" automatic process is run) 



Column in the Household Drivers RG: 

  * Driver ID (hidden column; number; 0 decimals; auto-set and read-only) 



How does this look to you?

Sagar Sagar 12/10/2025: Yes, this looks correct.
