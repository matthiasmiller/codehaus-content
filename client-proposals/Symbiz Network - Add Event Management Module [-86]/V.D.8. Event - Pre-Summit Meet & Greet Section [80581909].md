5.4.8. Event - Pre-Summit Meet & Greet Section

  


Requirements

*Documented 

  


"Pre-Summit Meet & Greet" section: (visible if Event Type = Annual Summit; visibility for users based on the "Event Visibility" field selection, with some fields visible only for Regional Reps and Super Admins): 

  


  * Meet & Greet Date (date field; required if Event Status = Scheduled or Complete; defaults to blank)
  * Meet & Greet Time (time field; required if Event Status = Scheduled or Complete; defaults to blank, showing the following gray hint in edit mode if blank: "e.g. 6:30 PM"; 
  * Meet & Greet Details (memo)
  * Meet & Greet Notes (Internal) (memo; visible to Regional Reps and Super Admins)
  * M & G Registrants (Internal) (link; displays the total sum of all M & G registrants, based on the "Registrant Attending M & G" and "Guest Attending M & G" fields on Registration records for the Event; link displays in the following format: "<#> Registrant(s)"; opens the "Meet & Greet Registrations Report" report; visible for Regional Reps and Super Admins)
  * M & G Food Note (Internal) (plain text; defaults to blank; visible for Regional Reps and Super Admins) 
  * M & G Food Contact (Internal) (optional; drop list of all active Contacts; visible for Regional Reps and Super Admins) 
  * View Contact (Internal) (link; visible in Edit mode if a Food Contact is selected; opens the selected Contact record; visible to Regional Reps and Super Admins)



  


Other Notes:

  * Note that the Pre-Summit Meet & Greet could eventually become its own Event Type. In that case, the details from previous Meet & Greet events could be copied out of their corresponding Annual Summit records to create new records for them.



  


Development Specification

Ellis Miller 06/20/2024: 

[ ] Add an EventIsAnnualSummit macro to use for these conditions

[ ] Remember to add EventIsAnnualSummit for all Required

  


Bid: 3 hours
