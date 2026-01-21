11.12.1. SPE Online Submission - Online Submission Section

Online Submission:

  * Linked Member Contact (drop-list; with the following details / behaviors: 
    * drop list of any Contact records that match on one or more of the following: 
      * EIN (if both left/right sides are businesses)
      * SSN (if both left/right sides are individuals)



_EM: Tim Reitz 02/19/2025: Currently it does not show options for matching SSN (and I'm assuming the same for EIN). 

TODO_BR: Tim Reitz 02/19/2025: Write up a CR for Jonathan or Seth to chase this. Here's the macro for them to look at: SubmissionLinkedMemberContactsList. 

  * Name (if full name matches) 
  * Phone Number (if it matches with a Primary phone number) 
  * Email (if it matches with a single Primary email address) 



TODO_BR: Tim Reitz 02/19/2025: Maybe these those match on any email / phone, not just primary? 

  * defaults to blank) 


  * Create Contact (button; visible if Linked Member Contact is blank; creates a blank contact record with the Business Name and sets Linked Member Contact)
  * Update Contact (button; visible if Linked Member Contact is not blank; runs an import that updates the linked contact with the relevant fields; does not return an error if Linked Primary Contact is blank)
  * Application Date (uneditable)



  


Additional behaviors: 

  * If the Linked Member Contact is a business, Linked Primary Contact is set to the primary related contact for the selected Linked Member Contact when it is set.
  * When the Create Contact button is clicked, Linked Member is set to (this creates a contact):
    * For businesses: <Business Name> (member from Online Submission # <Submission ID>)
    * For individuals: <Last Name>, <First Name> <Middle Name> '<Preferred Name>' (member from Online Submission # <Submission ID>)



  


Validation:

  * Error on save: if the type of the Linked Member Contact does not match Type in the Member Information section.
    * Error Message: "Member type '<SPESubmissionMemberType>' does not match with the selected linked member contact type."


