11.2.6. Contact - Contact Details Section

  


Requirements

Contact Details section: 

  * Preferred Name (plain text)
  * Hold Solicitations Until (checkbox)
  * (unlabeled date field; visible if "Hold Solicitations Until" is checked; editable; defaults to the current date)
  * Review All Emails (checkbox; defaults to not checked; if checked, all emails related to the Contact have the "Ready to Send" checkbox set to not checked when they are created, regardless of the email's "Level" or recipient) 
  * Email Instructions (small memo field; visible and required if the "Review All Emails" checkbox is checked; used for documenting the reason for checking the checkbox / action to take when emails are held from sending) 
  * EITC (checkbox; visible if Contact Type = "Business")
  * Eligible for SPE (checkbox; visible if Contact Type = "Business" or "Individual")
  * Anonymous Donor (checkbox; defaults to not checked; visible if "EITC" or "Eligible for SPE" checkboxes are checked) 
  * Postcard (checkbox; visible if "EITC" or "Eligible for SPE" checkboxes are checked; automatically checked if "Eligible for SPE" is checked; automatically unchecked if "Eligible for SPE" is unchecked")
  * Eligible to Receive SPE Donations (checkbox; visible if Contact Type = "School")
  * Special Education School (visible if Contact Type = "School"; checkbox; defaults to unchecked)
  * Communications Tile (plain text; visible if Contact Type = "Individual" and if a User ID is selected in the "User ID" field at the bottom of the record)



  


Development Specification

TODO_NM: 

  * There is section break between the "Hold Solicitations Until" checkbox and the corresponding date field, so they do not line up.
  * Communications Title should be wider.
  * Preferred Name could be wider.



  


  * Coding note for Review All Emails and Email Instructions fields: Also move the conditionally-visible date field for the "Hold Solicitations Until" checkbox to be directly to the right of its checkbox (currently it displays on the next row).


