11.3.1. Business Application - Business Application Section

Austin Priest 09/27/2024: _TR The name on the menu and the report is "Direct Business Application" but the first section on the record and in various places in the spec we call the record just "Business Application"

This causes me to sometimes feel like I am not sure if I'm at the right place.

TODO_EM: Tim Reitz 10/01/2024: Should we rename additional "Business Application" references to "Direct Business Application", for consistency? We've already changed the menu options and the report title.

Examples to change:

  * First section heading on the record
  * Contact | EITC Reports section: "Business Applications" link
  * Contribution record | Contribution Section : Business Application drop list
  * Additional references in the living spec



  


Business Application:

  * ID (auto-set and read-only; business + year + type + commitment + state application number (if not blank): e.g. "Business Name #123: 2025 K-12, Year 1 of 1, 2025070161862")
  * Business (drop-list of active businesses)
  * Commitment (drop-list)



List items:

  * "Year 1 of a 2 year commitment"
  * "Year 2 of a 2 year commitment"
  * "Year 1 of a 1 year commitment"


  * Filing Schedule (drop-list; required if Submitted Application to State is not blank)



List items:

  * "May 15 to June 30"
  * "July 1"


  * Year (number; required)
  * Type (drop-list; required if Submitted Application to State is not blank)



List items:

  * "K-12"
  * "OSTC"
  * "Pre-K"


  * Amount (number; two decimals; required if Submitted Application to State is not blank)
  * SPE Application (visible if the Business Application is entered in the SPE's Business Application field on an SPE Application record; opens the linked record)



  


Validation:

  * Error: if Year is not a valid year. (Number between 1000 and 4000)
    * Error Message: "Please enter a valid year."
  * Error on save: if Amount is blank and Submitted Application to State is not blank.
    * Error Message: "Amount should be specified if the application is submitted to state. (Field: Amount)"



  


Additional behaviors:

  * If the selected Commitment does not match the Filing Schedule (see notes below), Filing Schedule is cleared.
  * If there is only one Filing Schedule option for the selected Commitment, Filing Schedule is auto-filled.



  


Other Notes:

  * Two year commitments, whether first or second year, are on the May 15 to July 1 filing schedule, one year commitments are on the July 1 filing schedule.


