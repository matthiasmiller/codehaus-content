5.2.7. Salesperson (Non-member)

  


Requirements

The detail screen for a Salesperson (Non-member) contact will have the following custom section and fields: 

Salesperson (Non-member) Details section:

  * Salesperson Initials (required; entered manually; allow for up to 3 characters, normally the initials of their first and last name; error on save if the same initials are used for another active Member contact or Non-member Salesperson contact; used for reporting to show who sold the building)
  * Dealer (required; default to blank for non-members; field is cleared when Contact Type is changed)
  * Sales Report (link to the Sales by Salesperson Report, filtered to the current Salesperson)



  


Other notes:

  * Note that non-member Salespeople do not receive compensation directly from BEB. They are paid by their Dealer.
  * Each non-member Salesperson should have a Contact record and a User Login set up in the database, and should have their User Login ID linked with their Contact record.
  * The Contact record should have a warning on Save if an active non-member Salesperson contact does not have a User ID associated with the contact record. This warning should say, "This Salesperson (Non-member) type contact is missing its linked User ID."
  * If a Salesperson stops being a salesperson, an admin should deactivate both the Contact and the User Login.
  * The Salesperson contact would always be an Individual.



  


*Done.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1704430071](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1704430071)
