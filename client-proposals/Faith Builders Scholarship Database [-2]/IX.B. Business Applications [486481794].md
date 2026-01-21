9.2. Business Applications

  


Requirements

Accessed via: FaithBuilders Scholarship Services | Business | Business Applications

  


Sections and Fields: 

Business Application:

  * ID (auto-set and read-only; business + date + type + year: e.g. "Business Name #123: 2025 K-12, Year 1 of 1")
  * Business (drop-list of active businesses)
  * Commitment (drop-list of "Year 1 of a 2 year commitment", "Year 2 of a 2 year commitment", "Year 1 of a 1 year commitment")
  * Filing Schedule (drop-list of "May 15 to June 30" and "July 1")
  * Type (drop-list of "K-12", "OSTC", and "Pre-K")
  * Year (number; must be a valid year)
  * Amount (number; two decimals)



  


Status:

  * Received Application from Business (date)
  * Submitted Application to State (date)
  * State Application Number
  * State Fiscal Year (read-only; defaults to the value of the "Year" field in the Business Application schedule)
  * Override Status (checkbox; makes Status list editable)
  * Status (drop-list of "Pending", "Approved", and "Denied")



  


Notes:

  * (unlabeled memo)



  


Reports:

  * Renewal Application (opens renewal application PDF for the current business)



  


Other Notes:

  * Unless the "Override Status" box is checked, a status message is displayed underneath the status.
    * If the status is "Pending" and the Submitted Application to State date is empty, a message is displayed in black text: "This application is pending because the application was not submitted from May 15 through July 31."
    * If the status is "Pending" and the above date is not empty, a message is displayed in black text: "This application is pending because no contributions have been postmarked since August 1, <Year>."
    * If the status is "Approved", a message is displayed in green text: "This application was automatically approved because one or more contributions were postmarked between August 1, <Year> through May 1, <Year + 1>."
    * If the status is "Denied", a message is displayed in red text: "This application was automatically denied because no contributions were postmarked from August 1, <Year> through May 1, <Year + 1>."



  


Development Specification

Matthias Miller 04/27/2018:

  * Year 1/2 - May 15
  * Year 2/2 - May 15-June 30
  * Year 1/1 - July 1
  * New App - July 1 -- based on whether or not they were accepted the prior year



  


Matthias Miller 04/27/2018: 

  * Warn on Application and Contribution - if Denied and there's a contribution.



  


Matthias Miller 04/27/2018: When creating new year's application, that will be based on the corresponding prior year's Commitment + Status. i.e. if the prior year was NOT approved, it will go to the late filing if applicable.
