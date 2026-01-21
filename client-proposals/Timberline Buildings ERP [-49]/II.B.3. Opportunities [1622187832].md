2.2.3. Opportunities

  


Requirements

The Opportunity would be its own record type and would store basic information about a job lead. Each Opportunity can have multiple Quotes/Jobs linked to it. 

  


The Opportunity would track/show:

  * Read-only information from the Contact. (These would have links to open a local phone or email application, just as in the Contact.)
  * Site Address



  


The following information would be read-only, shown based on the zip code:

  * Site Township
  * Site County
  * Design Data
    * Snow Load
    * Wind Speed
    * Frost Depth
  * Lead Source (user-customizable list?)
  * Lead Status (either blank or list option)
    * Interested Prospect
    * Unqualified Prospect
  * Opportunity Notes (used for job-related notes)
  * Followup Notes (used for internal sales notes)
  * Followup Date (?)



  


The Opportunity will also show an embedded spreadsheet of emails related to this opportunity.

  


Development Specification

TODO_IDD: I (Matthias) am thinking that we restrict emails to those that are linked to an opportunity, or those that are sent to the current user. The current user could link threads/emails to a specific opportunity if they wanted to. We could also check for ones that are sent to something tos@____ and make them be unrestricted.

  


TODO_IDD: We can also do reporting based on last modify date (or based on when the note was last changed). Either one could be pulled from activity history.
