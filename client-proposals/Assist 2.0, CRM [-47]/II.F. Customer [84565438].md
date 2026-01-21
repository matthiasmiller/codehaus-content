2.6. Customer

  


Requirements

Customer (visible to everyone)

  * First Name
  * Middle Name
  * Last Name
  * Phone Number (embedded spreadsheet allowing multiple phone numbers a free-form notes field; include a primary checkbox that sorts one of the phone numbers to the top)
  * Address
  * City
  * State
  * Zip
  * Email (allowing multiple, just like phone number)
  * Round Robin fields (used to manage the round robin)
    * Round Robin District (list of districts)
    * Round Robin Dealer (list of dealers; if specified, the lead is part of a dealer round robin; otherwise, it's part of a district round robin)
    * Round Robin Salesperson (list of salespeople; this is the originally assigned salesperson; leads that directly contact the salesperson will not be part of a round robin)
  * Assignee
    * District (automatic)
    * Dealer (automatic)
    * Salesperson
    * Claimed (checkbox)



  


Round Robin

Leads will assigned based on their source. For example:

  * Emails to [email@district.com](mailto:email@district.com) will be assigned to a District round robin
  * Emails to [saleslot@district.com](mailto:saleslot@district.com) will be assigned to a District/Dealer round robin
  * Emails to [salesperson@district.com](mailto:salesperson@district.com) do not become part of the round robin.



  


Salespeople do not currently have their own direct phone number. If an email is directly sent to a salesperson, the contact will be assigned and automatically claimed by the receiving salesperson.

  


For voicemails/emails to the district/dealer, sort all active salespeople in the district/dealer (depending on the source). Find the salesperson having received the most recent round robin assignment at the respective district/dealer level, then assign it to the next one in alphabetical order.

  * For example, a salesperson may receive two leads at the same time, if it's that salesperson's turn in the district's round robin, and it's their turn in the dealer's round robin.



  


If the originally assigned salesperson does not respond to the lead, it will become available to the other salespeople on the sales lot. If no salesperson at the sales lot responds to the lead, it will become available to the entire district. (The time spent at each level can be configured. See below.)

  


Sales Portal

A salesperson can only edit a contact and their opportunities if they have claimed the contact. In addition, the phone number and email will be hidden. This is used to manage the round-robin approach and to make sure no two salespeople respond to the lead at the same time.

  


The Contact will have a Claim/Unclaim button. It would also have a button called "Assign to Dealer/Salesperson" that would assign it to a dealer. This can be assigned to a specific salesperson, but it would default to a round robin assignment. 

  


NOTE: The Claim button can be abused by salespeople (for example, claiming a lead but waiting a long time to get back to them). This behavior can be managed by training and team culture. It's important that we make sure that two people do not follow up with the same lead at the same time

  


Duplicate Contacts (Sales Portal)

This will include an embedded table of duplicate contacts (matching address, phone, or email) showing:

  * (Checkbox)
  * Contact Name
  * Contact Address
  * Contact Phone
  * Contact Email
  * Assigned Salesperson
  * Last Communication Date



  


When one or more items are selected, it will show a "Merge Contacts" button. This will prompt for name, address, phone, and email. Each of these will show a list of values from all the contacts that are being merged. This will reassign all opportunities for old contacts to the new contact, then will delete all of the old contacts.

  


This should maintain the old assignee for the contact.

  


This will also have a checkbox for "Not a Duplicate". This will suppress it from the weekly duplicates report.

  


Development Specification

Use "Contacts_EnablePrimaryPhone"

  


I think you could just have an RG of "Additional Emails".

  


Original Point of Contact can be editable NOT InDetailScreen. To clarify, there is ONE district, ONE dealer, etc.

  


For the assignee, derive the district/dealer from the salesperson.

  


For duplicate contacts, I think we want a subset to find duplicate contacts. Once we code the sales portal, we should add a link to the Contact Record that goes to the sales portal to resolve duplicate contacts (only visible if there are possible duplicates). The "Not a Duplicate" checkbox can still be added.
