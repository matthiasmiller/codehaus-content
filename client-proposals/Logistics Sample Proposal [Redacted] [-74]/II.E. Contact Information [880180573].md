2.5. Contact Information

  


Requirements

Pickup & Delivery Guests will be assigned a special "Pickup & Delivery Guest" contact type by default. Stops can only be assigned to these contacts, and these contacts can never be employees. These contact records will only be visible to administrators and Pickup & Delivery users.

  


This is important to protect the privacy of contacts and employees. If an employee would like to have a pickup or delivery, they must have a second Pickup and Delivery contact that is used strictly for pickup and delivery.

  


For a Pickup & Delivery Guest, the last name will not be required. When attempting a save without a last name specified, the last name will autofill to "[456]" where 456 is a unique number identifying the guest. (This allows importing prior information if needed in the future, as well as entering stops with partial names.)

  


The Contact should have the following fields:

  * Name
  * Building (choice of "Single-Family Home" and "Apartment/Lot")
  * Apartment/Lot # (conditional based on above selection)
  * Address
  * City
  * State
  * Zip
  * Mobile
  * Home
  * Work
  * Email
  * Latitude (internal only)
  * Longitude (internal only)



  


Development Specification

[ ] In ZNH, override ConfigRoutes_ContactType a new "Pickup & Delivery Guest" in the ContactTypes list.

[ ] Add a SelectRouteContacts subset that respects ConfigRoutes_ContactType. (This will be used by the integration.)

  


In ZNH:

[ ] Add a new ContactAddressBuilding list that has the options for "Single Family Home" and "Apartment / Lot". 

[ ] Change the Apt / Lot # to be visible based on that, rather than the ContactAddressType.

[ ] Remove the AddressTypes list modifications and the Contacts detail screen modifications from the AppHosting Routes catalog.

  


For Matthias:

[ ] The easiest way to do Geocoding is just having a JavaScript process that does it when we load up the Routes schedule. Alternatively, we could use a webhook and do it automatically.

[ ] Save the new record with a random ID, then update it with the actual list value.

[ ] In the integration, hardcode client-code for the Building, etc
