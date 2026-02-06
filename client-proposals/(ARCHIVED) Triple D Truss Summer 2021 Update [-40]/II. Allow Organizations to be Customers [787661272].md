2\. Allow Organizations to be Customers

  


Requirements

There is currently not a way to create a Quote/Order for an Organization (currently Customers can only be individual Contacts). Let's use the new format for Orgs so that we can have Quotes and Orders for Organizations as well. And let's be able to have linked contacts (e.g. reps from the customer businesses) to assign as the reps for the orders. 

  


Changes to contacts: 

  * Use the new format for contacts/organizations. This would allow organization contact types to be customers. 
  * Use the following contact types: 
    * Customer Individual (change from existing "Customer") 
    * Customer Organization
    * Vendor Organization (change from existing "Vendor")
    * Other Individual
    * Other Organization
    * Salesperson (existing) 
    * There will be a custom editable report to change the contact types. 



  


Changes to the contact detail screen: Have a new custom section called "Linked Contacts" . Linked contacts belonging to an organization/business should be stored on the organization contact page (they would not be separate contact records).

  * This would have an embedded spreadsheet that stores the following: 
    * Name (one field for first and last)
    * Phone #
    * Email
    * Active/Inactive checkbox 
    * ID (hidden; auto-assigning) 
    * There should be the option to add linked contacts. 
    * There would not be an option to remove linked contacts (they should be made inactive instead). The reason for this is so that information is not accidentally deleted from orders and printouts. 
    * Sorted by name, with inactive items at the bottom. 
    * Linked individual contact records would not show up on this list. 



  


Changes to the order screen: 

Workflow on the order: First select a business name from the Customer list, then select a name from the Contact list and that person's information would auto-fill into the other fields (or you could just leave the Contact field blank). 

  * The "Customer Name" field in the Customer section of the order details would be a list of all Customer type contacts (individuals and organizations). 
  * If an organization is selected, new fields appear: 
    * Contact (list of linked contacts)
    * Contact Phone (auto-fill)
    * Contact Email (auto-fill)
  * Also 3 buttons: 
    * New (opens a child screen with blank prompts for FN, LN, Phone, Email; clicking Continue adds the person to the list on the Organization record) 
    * Optional/Extra: Edit (opens a child screen with the same prompts plus "Is Active" checkbox, defaulting to the current information; clicking Continue updates the information on the list on the Organization record)
    * If the "Edit" button isn't added here, the user can click on the ellipsis button beside the customer name to make edits to the RG on the Organization page. 
  * If any of the "linked contact's" information is changed on the RG on the Organization, it will update on orders and printouts where it is referenced. 
  * Deactivated names will remain on existing orders and printouts. 



  


  


Changes to printouts: 

  * Both the Quote/Order Sheet and the Packing List should show the phone # and email for both the linked contact and the organization, but Fax for only the organization. 
    * Maybe move the organization's Phone and Fax and Email to the top right of the box, then put the linked contact's Name and Phone and Email underneath that. 



  


Migration Work: CodeHaus/CodeCrafters would provide training and Triple D would do the actual work of switching organizations and setting up linked contacts. 

  


  


Notes: 

  * This would involve switching all company names who are currently Individual contacts to Organizations for all who are of the Customer type (not Vendors). We would probably do a re-import of these as Organizations and delete the duplicates that are in the system as individual Contacts (OR maybe switch them manually/change their contact type).  
  * The Organization would be the Customer on the Quotes/Order reports, etc., and we would not need to display the linked Contact name on those reports.



  


Time Estimate: 3 days

  


Development Specification

Tim Reitz 08/06/2021: From [[[IN4353](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-4355&)]] - ZTD - Allow Organizations to be Customers. 

  


We realized that we don't have a way to create a Quote/Order for an Organization (currently Customers can only be individual Contacts). Let's use the new format for Orgs so that we can have Quotes and Orders for Organizations as well. And let's be able to have linked contacts (e.g. reps from the customer businesses) to assign as the reps for the orders. 

  


Our proposal: 

Changes to contacts: 

  * Use the new format for contacts/organizations. This would allow organization contact types to be customers. 
  * Use the following contact types: 
    * Customer Individual (change from existing "Customer") 
    * Customer Organization
    * Vendor Organization (change from existing "Vendor")
    * Other Individual
    * Other Organization
    * Salesperson (existing) 
    * Let's give them a custom editable report to change the contact types after we have this set up. 



Tim Reitz 06/22/2021: Contact types work is 2 hours. 

Tim Reitz 08/06/2021: I'm increasing this to 4 hours to add some buffer and to make this whole job come out to an even 3 days. 

  


  


Changes to the contact detail screen: Have a new custom section called "Linked Contacts" . Linked contacts belonging to an organization/business should be stored on the organization contact page (they would not be separate contact records).

  * This would have an embedded spreadsheet that stores the following: 
    * Name (one field for first and last)
    * Phone #
    * Email
    * Active/Inactive checkbox 
    * ID (hidden; auto-assigning) 
    * There should be the option to add linked contacts. 
    * There would not be an option to remove linked contacts (they should be made inactive instead). The reason for this is so that information is not accidentally deleted from orders and printouts. 
    * Sorted by name, with inactive items at the bottom. 
    * Linked individual contact records would not show up on this list. 



Tim Reitz 06/22/2021: Adding the RG is 1 day of work. 

  


Changes to the order screen: 

Workflow on the order: First select a business name from the Customer list, then select a name from the Contact list and that person's information would auto-fill into the other fields (or you could just leave the Contact field blank). 

  * The "Customer Name" field in the Customer section of the order details would be a list of all Customer type contacts (individuals and organizations). 
  * If an organization is selected, new fields appear: 
    * Contact (list of linked contacts)
    * Contact Phone (auto-fill)
    * Contact Email (auto-fill)
  * Also 3 buttons: 
    * New (opens a child screen with blank prompts for FN, LN, Phone, Email; clicking Continue adds the person to the list on the Organization record) 



Tim Reitz 06/22/2021: The "New" button work is 1/2 day. 

  * Optional/Extra: Edit (opens a child screen with the same prompts plus "Is Active" checkbox, defaulting to the current information; clicking Continue updates the information on the list on the Organization record)



Tim Reitz 06/22/2021: The "Edit" button is 1/2 day. 

  * If the "Edit" button isn't added here, the user can click on the ellipsis button beside the customer name to make edits to the RG on the Organization page. 


  * If any of the "linked contact's" information is changed on the RG on the Organization, it will update on orders and printouts where it is referenced. 
  * Deactivated names will remain on existing orders and printouts. 



  


  


Changes to printouts: 

  * Both the Quote/Order Sheet and the Packing List should show the phone # and email for both the linked contact and the organization, but Fax for only the organization. 
    * Maybe move the organization's Phone and Fax and Email to the top right of the box, then put the linked contact's Name and Phone and Email underneath that. 



Tim Reitz 06/22/2021: The template work is 1/2 day. 

  


Migration Work: ZTD would do the work; CH would provide training. 

  


  


Notes: 

  * This would involve switching all company names who are currently Individual contacts to Organizations for all who are of the Customer type (not Vendors). We would probably do a re-import of these as Organizations and delete the duplicates that are in the system as individual Contacts (OR maybe switch them manually/change their contact type).  
  * The Organization would be the Customer on the Quotes/Order reports, etc., and we would not need to display the linked Contact name on those reports.



  


Ellis Miller 06/11/2021: There are very few Organizations in their system. We can migrate those over to contacts and flip the switch to use the new organization structure (we'll also have to change orders to work with that).

  


We will do this as part of Premium Subscription T&M.
