7.2.1. Contact Record - Standard Sections & Fields

  


Requirements

The Contact record will include standard contact sections and fields, such as (but not limited to) the following. Note that there are some of these fields with some custom behaviors.  

  


  * Active Contact (checkbox; defaults to filled; includes the following validations:) 
    * Custom: Editable for Super Admins only.
    * Custom: Validate against deactivating the Contact record if the Contact Type = Member and the Active Membership checkbox is filled -- error on the field: "The Contact cannot be deactivated because this Member has an active membership." 
    * Custom: Validate against deactivating the Contact record if the contact is a Regional Rep or Facilitator -- error on the field: "The Contact cannot be deactivated because this Member is a Regional Rep and/or Facilitator." 



  


  * Contact section (visible to all users with some further restrictions as noted; custom behavior for all fields in the section: Editable for Super Admins only)
    * Contact Type (required; drop list of Contact Types; includes the following validations:) 
      * Custom: Technically this is editable for all users on new records, to allow for cleaner creations of Contact records. However, non-Super Admn users cannot create new contacts.
      * Custom: Validation warning when changing the Contact Type if the Contact Type = Lead - warning on the field: "You are changing the Contact Type from Lead to another Type, which will result in the lead details being lost. To cancel, refresh the page without saving your changes."
      * Custom: Validate against changing the Contact Type if the Contact Type = Member and the Active Membership checkbox is filled - error on the field: "The Contact Type cannot be changed because this Member has an active membership."
      * Custom: Validate against changing the Contact Type if the Contact Type = Member and the Contact is listed as a member of one or more Growth Ring Groups - error on the field: "The Contact Type cannot be changed because this Member is part of the following Group(s): <GroupDescription1>, <GroupDescription2>, <etc.>."
      * Custom: Validate against changing the Contact Type if the Contact Type = Member and the contact is a Regional Rep or Facilitator - error on the field: "The Contact Type cannot be changed because this Member is a Regional Rep and/or Facilitator."
    * First Name (for individuals; required) 
    * Middle (for individuals; optional) 
    * Last Name (for individuals; required) 
    * Organization Name (for organizations; required) 
      * Custom: Validate against duplicate Organization Names (via the ConfigContacts_AllowDupOrgNames system switch) - error message on Save: "There is already a <Member Organization / Other Organization> with the same name."
    * Summary (for individuals and organizations; optional; plain text field) 
    * Organization (for individuals; standard; embedded spreadsheet that allows the Contact to be linked to multiple organizations/businesses)
    * Date of Birth (date field)
      * Custom: Optional field; corresponding member and all uplines can view the full date; other standard members can only view the month and date. 
    * Gender (drop list of blank, Female, Male) 
      * Custom: Optional field; corresponding member and all uplines can view; field hidden for other standard members.



  


  


  * Address section (standard) (custom behavior for all fields in this section: Editable for the corresponding member and all uplines.): 
    * "(<X> of <Y>)" (visible in the section heading, after "Address", if more than 1 address exists for the Contact; "X" represents the item number of the current address; "Y" represents the total number of addresses) 
    * "🡄" & "🡆" (visible if there are more than one address entered; buttons in the section heading; to cycle through the entered addresses) 
    * Type (optional; visible and editable if there are more than one address entered; drop list of Address Type list items, and the option to add a new item to the list) 
    * Address (optional; for "line 1"; plain text field) 
    * Address 2 (unlabeled field; optional; for "line 2"; plain text field) 
    * City (optional; plain text field) 
    * State (unlabeled field; optional; drop list of US state & territory abbreviations) 
    * Zip (unlabeled field; optional; plain text field) 
    * Google Maps (link; visible if at least one of the address-related fields has data entered; opens the entered address in Google Maps) 
    * Export Address (link; visible if at least one of the address-related fields has data entered; opens a prompt screen to export the address (i.e. for printing on an envelope)) 
    * View All (button; opens the "View All Addresses Child Screen" - see spec below) 
    * New (button; adds a new address item)  
    * Delete (visible if there are more than one address entered; button; deletes the currently-visible address) 



  


  * View All Addresses Child Screen: 
    * Embedded spreadsheet with the following: 
      * Columns: 
        * Type (column always visible; otherwise the same as the corresponding field on the main screen) 
        * Address (same as the corresponding field on the main screen)
        * Address2 (same as the corresponding field on the main screen)
        * City (same as the corresponding field on the main screen) 
        * State (same as the corresponding field on the main screen) 
        * Zip (same as the corresponding field on the main screen) 
        * Country (same as the corresponding field on the main screen)
        * Export (link; displays as "Link"; same behavior as the "Export Address" link on the main screen) 
      * Automatically sorted by: N/A (rows remain in the order in which they were entered)
      * Buttons to insert/append/remove rows: "+" / "-" 
      * Show 12 rows without scrolling 
      * Other Notes: 
        * The first / top address is considered to be the "Primary" address. 
        * Custom: If Contact Type = Member, require there to be an address with Type = Primary, and validate that there is only 1 Primary address - validation error message on Save: "Member-type contacts must have 1 Primary-type address." (note that this will be a warning instead of an error for imported records)
        * Note: As mentioned elsewhere, this can handle Canadian addresses. 



  


  


  * Phone section (visible to all users with some further restrictions as noted; custom behavior for all fields in this section: Editable for the corresponding member and all uplines.)
    * Phone Number (standard embedded spreadsheet; standard version can handle Canadian phone numbers since they use the same format as US numbers; standard also considers the top number to be the primary)



  


  * Email section (visible to all users with some further restrictions as noted; custom behavior for all fields in this section: Editable for the corresponding member and all uplines.)
    * Email (standard field & embedded spreadsheet; can track multiple email addresses, and one or more can be designated as "Primary")
      * Custom: If Contact Type = Member and Online Member = Yes, have validation against duplicate email addresses - validation error message on Save: "This email address is already being used for another member (<Name>)." (Note that this means than multiple offline members can share the same email address.) 
      * Custom: If Contact Type = Member and Online Member = Yes, validate that the Contact has at at least 1 email address - validation error message on Save: "This Contact must have at least one email address specified since they are designated as an Online Member."  (note that this will be a warning instead of an error for imported records) 



  


Other Notes: 

  * Custom: The following section(s) / field(s) are hidden in this Solution: 
    * Notes (standard memo) 
    * Executive Notes (standard memo)



  


Development Specification

Change Requests: 

  * Tim Reitz 03/13/2024: [[[IN9344](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9346&)]] - ZSB - Misc. Minor Changes & Bugs (01/23/24)
  * Tim Reitz 04/09/2024: [[[IN9081](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9083&)]] - ZSB - Contacts - Change Validations for Imported Member-type Contacts
  * Tim Reitz 04/09/2024: [[[IN9565](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9567&)]] - ZSB - Contact Record - Clarify Visibility & Editability
  * Tim Reitz 04/10/2024: [[[IN9074](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9076&)]] - ZSB - Contact Types - Handle Organizations more cleanly
  * Tim Reitz 09/12/2024: [[[IN9639](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9641&)]] - ZSB - Allow Duplicate Email Address for Offline Members
  * 


  


  


[ ] Add a Custom_ContactValidateActive macro and override it.

[ ] Add a Custom_ContactValidateType macro and override it.

  


[ ] Email validation, just rip through all contacts (no ndx), skipping this lookup number, looking for a duplicate.

[ ] Test if you rename the lookup name

  


[ ] Validate address

  


  


BID: 6 Hours
