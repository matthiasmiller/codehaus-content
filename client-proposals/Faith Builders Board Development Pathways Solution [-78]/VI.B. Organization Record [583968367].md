6.2. Organization Record

Overview: The Solution probably will use the standard AppHosting Organization Contact record, with customizations.

  


Accessed via: (TBD in IDD)

  


Sections and Fields: 

  * Standard fields, including: 
    * Name (required; plain text)



  


  * Custom fields: 
    * Organization Type (single-selection drop list of Organization Type list items)
    * Board Rep First Name (required; plain text field)
    * Board Rep Last Name (required; plain text field)
    * Organization Login (drop list of Board Representative User Profiles) 
      * User Profile based on the Organization, not individual
    * Login Email (auto-set and read-only; set to the selected the User Profile login email) 
    * Organization City (required; plain text)
    * Organization State/Province (required; drop list of U.S. State and Canadian Province abbreviations) 
    * Organization Country (rquired; drop list of U.S., Canada, Mexico, and possibly others)
    * FB Managed (checkbox; defaults to unchecked; details to be determined in IDD)
    * Subscriptions (link to report OR bottom report of Pathway subscriptions for this Organization)
    * New Subscription (should be an easy way to sign up for a new Pathway, with a different number of participants; details to be determined in IDD)
    * All Participants (embedded spreadsheet of the following:)
      * Columns: 
        * Active (checkbox; defaults to checked)
        * First Name (required; plain text)
        * Middle Name (optional; plain text) 
        * Last Name (required; plain text)
        * Method of Delivery (required; drop list of: Email, Fax, Mail; conditional on the participant's country)
        * Email (required if Method of Delivery is Email, otherwise optional)
        * Fax (required if Method of Delivery is Fax, otherwise optional)
        * Mailing Address (separate columns for Address Line 1 and Line 2; required if Method of Delivery is Mail) 
      * Automatically sorted by: First by Active / Inactive, then by Name (alphabetical)
      * Buttons to append/remove rows: "+" / "-"
      * Show 10 rows without scrolling.
    * View Payments (link; opens a report of payments by this organization)



  


Data Access: (TBD in IDD)

  


Special Considerations: (TBD in IDD)

  * Copy Record: 
  * Delete Record: 
  * Merge Record: 



  


Other Notes (details to be determined in the IDD): 

  * The following is a way for a Board Representative to hand over the account:
    * Current Representative changes the Representative and Login Email (option to select from current participants or add a new one) 
    * Solution gives the Representative a prompt asking if he is staying on the board/as a participant or not
    * Solution updates the User Profile
    * Solution sends an email to the new Representative - welcome, link to change UN/PW
  * The Board Representative should be able to go in and change who goes in and change who gets the next lesson. The new person should pick up after the last person left off. 
  * It could be nice to have a feature to allow an alternate / secondary user to access the account in addition to the Board Rep, or at least another person to receive regular email updates. 



  


Other Notes:

  * There is no need for the same Organization to be able to have multiple active Pathways at the same time. If an organization would wish to do this, they would create a separate account for each additional Pathway that they would want to have going at the same time. 
  * The following will be available as delivery options for people in various countries:
    * USA: Email, fax, print  
    * Canada: Email, print 
    * Elsewhere: Email only
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).


