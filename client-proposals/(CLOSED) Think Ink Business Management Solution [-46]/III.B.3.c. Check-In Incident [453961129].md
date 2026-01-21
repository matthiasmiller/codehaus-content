3.2.3.3. Check-In Incident

  


Requirements

The Check-In-type incident would include the standard fields for the AppHosting incidents and standard Think Ink-specific fields, plus the following custom section and fields:

  


Check-In Incident Details section:

  * Check-In Date (required; default to blank)
  * Check-In Notes (multi-line text field; plain text to allow editability in reports)
  * Schedule Next Check-In (link; opens a new Check-In-type incident with Contact and Check-In Date set - see Calculating Check-In Dates in this proposal; Assignee should be defaulted to the contact's sales rep) 
  * Badger ID (optional; editable only on import; hidden if blank; used for identifying check-ins imported from Badger) 



  


The Contact field should be required for Check-In-type incidents.

  


The Check-In incident is considered complete when the incident is closed. If follow-up is required, a new incident can be created and the incidents can be cross-referenced.

  


Validations:

  * Warning on Save if the incident has been closed without another Check-In being scheduled for a future date: "This customer does not have a future check-in scheduled."



  


Other Notes: 

  * For the sake of consistency, the Solution will use "Check-In" (with a hyphen and a capital "I") for all references to check-ins and Check-In-type incidents.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2062440072](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2062440072)

  


[ ] Several simple fields.

[ ] ContactLatestCheckInDate macro that we can use to calculate the next checkin date

[ ] "Schedule Next Checkin" auto-push report (we'll either have to require SaveRecord or need to pass in the CheckInDate from this detail screen into the auto-push report).

[ ] Additional warning on save

Bid: 6 hours

 

CCI: Tim Reitz 06/21/2022: Note that there might be some instances of "Check-in" in the proposal and/or mockups, but we should use "Check-In" (capital "I") in the Solution.
