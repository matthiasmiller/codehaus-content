7.10.2. Registration: Registrant Details Section

  * Registrant Details Section (visible to the Registrant, all uplines, and all Regional Reps): 
    * Registrant Name (required; drop list of all active Individual Contacts; when created from a Contact record, defaults to that Contact; otherwise defaults to blank; warning on Save if changed after the first Save: "The selected Contact has been changed. To continue, click Continue. Otherwise, click Cancel and reset the Contact."; validate against multiple Registrations for the same Contact and Event - error on the field: "This contact already has another Registration record for the same Event") 
    * New Lead (visible to Regional Reps and Super Admins in edit mode if Registrant Name is blank, to make it easy to add new leads who register or who were in attendance; link; opens a new Contact record with Type = Lead) 
    * View Contact (visible to the right of the Registrant Name field in Edit mode if a Registrant is selected; link to open the corresponding Contact record) 
    * Registrant Type (auto-set and read-only; displays the Contact Type / Org Role of the selected Contact (Lead, Standard Member, Facilitator, Regional Rep, Super Admin, Other Individual); used for informational tracking and KPI calculations; displays the information as of the time the contact was added to the record, and does not change here if changed on their Contact record; does not display as a link to anything) 
    * Organization Name (auto-set and read-only; sets to the top organization on the Organization table on the Contact record; displays the information as of the time the contact was added to the record, and does not change here if changed on their Contact record) 
    * Phone (auto-set and read-only; displays to the primary phone number (the top non-Fax number first phone number) for the selected Contact at the time that the Registration record was created)
    * Email (auto-set and read-only; sets to the the top primary email address for the selected Contact at the time that the Registration record was created; displays as a link to send an email)
    * Address (auto-set and read-only; sets to the primary address on the Contact record at the time that the Registration record was created; displays in the standard 2-line address format)
    * Industries (auto-set and read-only; comma-separated list of all Industries that are selected on the Registrant's Contact record at the time that the Registration record was created, in the sequence in which they are listed there) 
    * "Note: details are as of the registration date." (informational note in gray font to help clarify that all of this information is static and does not update if changed on the Contact record) 
    * Bringing Guest (required; drop list of blank/Yes/No; defaults to blank)


