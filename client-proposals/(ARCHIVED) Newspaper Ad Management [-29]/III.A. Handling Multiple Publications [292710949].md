3.1. Handling Multiple Publications

  


Requirements

The database will be set up to be able to manage ads for multiple different publications. These publications will not be associated with each other and will require separate logins for Standard Users and Publication Admin Users to access them (Full Admin Users will have access to all publications on the database). Separate publications will still share a common Wiki section, but other data on the system such as Contacts, Ads, Invoicing, and Reports will be separated. 

  


Each publication will have a label at the top of the menu screens to help identify which publication is currently open. It would display a message such as, "You are viewing ads for ___ publication." Note that this label will not be on reports and detail screens. 

  


In the event that a publication would be sold, all parties would work together to develop a plan and a price for removing the publication from the database and migrating it to a new, separate database with a new subscription for the buyer.

  


Development Specification

Data restrictions notes on all record types.

  


Contact Restriction -- Add a Custom_ContactRecordPermitted macro that calls PublicationIsPermitted( ContactPublication).

1 day for contacts. Other items handled in their specific record types.
