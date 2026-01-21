5.2.1. Customer

  


Requirements

The detail screen for a Customer contact will include the following custom section and fields: 

Customer Details section:

  * Delivery Latitude/Longitude (text field; editable as a pair such as "35.918221, -91.549139")
  * Google Maps (link; opens Google Maps, with the location auto-set from the Latitude/Longitude)
  * New Building (opens a new building building record, defaulting the Building Contact to the corresponding Customer)
  * Customer's Buildings (link to the Historical Buildings by Customer Report for the current customer - see corresponding section in this proposal) 
  * Customer Referred By (read-only; auto-filled from the customer's most recent Sales Order with a Referring Party; displays the Referring Party's name and the sale date in the following format: "LastName, FirstName mm/dd/yyyy")
  * Customer Payment History (link to the Payments / Refunds by Customer Report - see corresponding section in this proposal)



  


Other Notes:

  * Customers would not have login access to the database.
  * The Customer contact would default to being an Individual, but could be changed to an Organization. 



  


*Done.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=2008998919](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=2008998919)

  


See [https://stackoverflow.com/a/1300922](https://stackoverflow.com/a/1300922) for the Google Maps link. Have two URL system switch prefixes, defaulting to the right value.

  


Validation for Delivery Lat/Long: Split on comma, trim both sides, validate that both are numbers.
