7.9.4. Event - In-Person Event Details Section

  


Requirements

  * "In-Person Event Details" section (visible if Event Format = In-Person or Hybrid; visibility for users based on the "Event Visibility" field selection): 



  


  * Venue (optional; plain text; can be used to track the name of the venue/location; defaults to blank)
  * Address (includes the following fields; all default to blank; all are required if Event Status = Scheduled or Complete and Event Format = In-Person or Hybrid: 
    * Street
    * City
    * State/Province 
    * Zip)



  


Development Specification

Tim Reitz 06/26/2024: Per Ellis: If we want custom behavior [i.e. conditional requirements for address fields based on Event Status and/or Event Format], we'll put it on the Event Type record (e.g. we could have a "Require Address Immediately"). This could be a future change request.
