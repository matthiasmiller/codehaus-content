7.2. Updating Assist from ActiveCampaign

  


Requirements

There are two ways Assist will be updated based on changes in ActiveCampaign:

  


  * Webhooks. This will run whenever an ActiveCampaign contact is modified.



  


  * Nightly Sync. This will run every night to make sure that all ActiveCampaign contacts are in the database.



  


AppHosting will maintain a replica of the ActiveCampaign contact list at all times. Every time the AppHosting system is updated with an ActiveCampaign contact, it will:

  


  * Update the ActiveCampaign contact with the new information.



  


  * Look for all AppHosting contacts that are not associated with an existing ActiveCampaign contact. Link this to the new ActiveCampaign contact if the email address matches.



  


  * Look for all AppHosting contacts that are associated with an existing ActiveCampaign contact (includes the newly-linked item above), and update the email and phone number, if it has changed. (This means that if there are multiple AppHosting contacts for the same ActiveCampaign contact, they will all be updated to reflect each other.



  


Development Specification

This is implemented here in the live system:

  


UserDir::\Shared\Dealer Portal WSGI\Service ActiveCampaign Sync.x30list

  


[ ] TODO_NM:

Add an X30: UserDir::\Shared\Dealer Portal WSGI\Service ActiveCampaign Sync - C - Update Contacts.x30 to the above x30list

  * Find all contacts matching the ActiveCampaign ID
  * Ensure that the email is the only primary email address in the RG
  * Ensure that the phone (if specified) is the only primary phone number. If there is no phone number, uncheck the Primary checkbox on any phone numbers


