11.6.4. Family - Contact Information Section

  


Requirements

Contact Information section:

  * Phone (plain text; auto-formats if ten digits long)
  * Email (plain text)
  * Send Email (visible if Email is not blank; opens the default email client)
  * Address (plain text)
  * City (plain text)
  * State (unlabeled; drop-list of state abbreviations; defaults to PA)
  * Zip (unlabeled; number)
  * County (drop-list of PA counties; required)
  * School District (drop list of all active School Districts)



  


Additional Behaviors:

  * When in the record is non-edit mode:
    * Phone is a clickable link that opens the default phone client.
    * Email is a clickable link that opens the default email client.



  


Validation:

  * Error on save if School District is blank and the family has an application with a school year of 2024 or later: "A School District is required because this family has an application for 2024 or later."
  * Warning on Save if School District is blank and the family does not have a family application with a School Year of 2024 or later: "There is no School District selected."
  * Warning on Save if County does not match School District: "County does not match the County for the School District (County Name)."



  


Development Specification

Change Requests: 

  * Tim Reitz 09/04/2024: [[[IN9946](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9948&)]] - XFB - Unlink School Districts and Counties 
  * Tim Reitz 09/13/2024: [[[IN10439](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10441&)]] - XFB - Family record - Swap field locations


