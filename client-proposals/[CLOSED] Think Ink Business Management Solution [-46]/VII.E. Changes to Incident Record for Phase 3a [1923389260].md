7.5. Changes to Incident Record for Phase 3a

  


Requirements

The following change(s) are to be made to the existing Check-In Type Incident records for Phase 3a:

  


Existing Check-In Incident Details custom section: 

  * Scheduled Check-In Month (previously called / replaces Check-In Date; with the following behaviors:) 
    * required if there is a Due Date set for the Incident or if Incident Status = Closed; 
    * drop list of Months in the following format: "<Month> <Year>"; shows the current month at the top, then 12 more calendar months into the future, for a total of 13 months; 
    * auto-set based on the Customer's Region's Check-In Schedule for incidents created from the Customers Needing Check-Ins Report or the "Schedule Next Check-In" link on an existing incident; 
    * defaults to blank for manually-created new records to allow for scheduling additional custom check-ins; 
    * if blank when a Due Date is set, auto-sets to the month of the Due Date; 
    * if blank when the incident Status is set to Closed, auto-sets to the month of the Closed Date; 
    * warning on the initial Save if there is another open Check-In Incident for the same Customer and same Month: "This customer already has an open Check-In for the same month: <INXXXX>."; 
    * note that a Customer may have multiple Check-In Incidents with the same Month) 



  


  * Next Check-In: <Month Year> (if there is one or more existing Check-In incidents for the same Customer and a future month, displays as a link to open the incident for soonest incident; if there is not an existing Check-In incident, displays read-only text of the month & year that the Customer is due for their next scheduled Check-in) 
  * Schedule Next Check-In (link; opens a new Check-In-type incident with Contact and the Scheduled Check-In Month set - see Calculating Check-In Dates/Months in this proposal; Assignee should be defaulted to the contact's sales rep) 



  


Validations:

  * Warning on Save if the incident has been closed without another Check-In being scheduled for a future Month: "This customer does not have a future check-in scheduled."



  


Other Notes:

  * A user can use the Due Date to set a more detailed date for scheduling and sorting.
  * The Solution continues to look at the Incident Closed Date as the official Check-In Date.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2062440072](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2062440072)

  


All of this ONLY applies to check-in incidents.

  


[ ] Naming fields/macros: ScheduledCheckInMonthDate is the FirstCalDay. And ScheduledCheckInMonth is the string display ("MMMM YYYY").

  


[ ] Drop list is ListSubstitute( NumericPipelist(0,12), FirstCalDay(Today, Value(CurrentItem))

  


For: auto-set based on the Customer's Region's Check-In Schedule for incidents created from the Customers Needing Check-Ins Report;

[ ] NewRecord:Init:

  


1 day
