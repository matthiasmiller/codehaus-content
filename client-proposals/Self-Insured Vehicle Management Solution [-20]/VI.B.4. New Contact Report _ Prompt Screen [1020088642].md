6.2.4. New Contact Report / Prompt Screen

*Done.

  


Overview: This is a special custom report that creates a new Contact record, based on selected prompts.

  


Accessed from: Home | Contacts | New Contact (opens a prompt screen with the below prompts)  

  


Title: New Contact

  


Prompts: 

  * The new contact is a driver for an existing client (required; drop-list of "Yes" / "No"; defaults to blank; if set to "No", clicking "Continue", the Solution creates a new blank Contact record; if set to "Yes", the following additional prompts are displayed on the same screen)
  * Client (visible and required if "The new contact is..." = "Yes"; drop-list; with the following details / behaviors:
    * for Admin users: includes all active Clients that have more than one Household Driver;
    * for non-admins: includes all active Clients of the current logged-in Agent that have more than one Household Driver)
  * Driver (visible and required if "The new contact is..." = "Yes"; drop-list of Household Drivers for the selected Client; is cleared "Client" is cleared)
  * Copy address from existing household (visible and required if "The new contact is..." = "Yes"; drop-list of "Yes" / "No"; defaults to blank)
  * Claims and high-risk driver fees will be transferred to the new contact. (visible if "The new contact is..." = "Yes"; label)



  


When all prompts are set, clicking "Continue" causes the report to create a new Contact record, setting the specified fields.
