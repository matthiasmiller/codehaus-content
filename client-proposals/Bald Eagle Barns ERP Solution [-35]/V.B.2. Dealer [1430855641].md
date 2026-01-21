5.2.2. Dealer

  


Requirements

The detail screen for an Dealer contact will include the following custom section and fields:

Dealer Details section: (all fields only visible to and editable by admins) 

  * Dealer Code (required; allow up to 4 characters; error on save it the same code is used for another active Dealer; used for tracking sales by dealers and reporting) 
  * Requires Approval (if checked, requires approval for Sales Orders of new buildings and modifications - not lot buildings - by the dealer's salespeople) 
  * Dealer Commission % (number field, whole number; percentage of sub-totals for all Sales Orders that correspond to the Dealer, after discounts but before sales tax)



  


Other Notes: 

  * Each Dealer, including Bald Eagle Barns, should have a Contact record. Dealer Contact records will not have User Logins; there will be a Salesperson Contact with "Dealer" permissions. 
  * If a Dealer ceases to be a dealer for BEB, an admin should deactivate the Contact.
  * As mentioned elsewhere, the Dealer would not have a separate login - the main contact would use their Salesperson (Non-Member) user login, linked to their personal Contact record. 
  * For sole proprietor dealers, there would be both a Dealer and Salesperson (Non-member) contact set up. The business (Dealer) name could be the same as the personal (Salesperson) name, but would be differentiated, such as with a manually entered asterisk or a suffix. The Salesperson contact would then be linked to the Dealer contact. 
    * Example: Sometimes a person is a salesperson selling buildings off the BEB property, but they are not under BEB as their dealer. The Dealer contact name could be "John Doe*" or "John Doe (Dealer)" or "John Doe (Sole Prop)", and the Salesperson contact name could be "John Doe". BEB can determine what approach they would like to use for this naming.
  * The Dealer contact would default to being an Organization, but could be changed to an Individual if needed. 



  


*Done.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=881903758](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=881903758)

  


  


"IN TRANSIT" dealer contact would not be Investortools-owned.

Tim Reitz 11/23/2021: I think this is now irrelevant.

  


DONE_AP:Austin Priest 03/03/2022: Mock up

[https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=881903758](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=881903758)

DONE_TR Austin Priest 03/03/2022: Should this have first name last name or just one name field like an organization.

DONE_AP: Tim Reitz 03/08/2022: Good question. See my new notes above (bottom bullet point). So it would normally just be one field. Does that sound good to you?

Austin Priest 03/10/2022: DONE_TR Should contact records have the organization checkbox? Right now they do not.

TODO_AP: Tim Reitz 03/21/2022: That depends on the setting of the Contact Type - whether it supports Individual and/or Organization types (see example: [https://testweaverland.apphosting.zone/Detail/Edit/2?RecordType=ContactTypes&NumberID=-13&State=ISwSvCyE0ts&](https://testweaverland.apphosting.zone/Detail/Edit/2?RecordType=ContactTypes&NumberID=-13&State=ISwSvCyE0ts&)). If the Contact Type is set to support both, then the Org checkbox would be visible on the Contact record. If only one, then it would only show the name field(s) for the one that it supports.

So for BEB mockups, you can add the checkbox for the ones that support both. Let me know if you need any more explanation on this. Thanks!

Austin Priest 04/07/2022: Ok I will clean this up if we continue the project.
