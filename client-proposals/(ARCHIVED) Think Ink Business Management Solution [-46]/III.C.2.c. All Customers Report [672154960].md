3.3.2.3. All Customers Report

  


Requirements

This is a custom report of all Customer-type contacts. 

  


For Phase 1, this will be a simple 1-pane report. In the future, this will be a multi-pane report, with the customers in the top pane, and the past purchased items for the selected customer in the bottom pane.

  


This would be accessed from an "All Customers" menu option on the Home Menu. 

  


A mobile interface can be added as part of a future phase. 

  


Title: All Customers

  


Columns:

  * Customer Name (link to record)
  * Street Address 
  * City
  * State
  * Phone
  * Email 
  * Last Check-In Date
  * Check-In Frequency
  * Next Check-In Date
  * Next Check-In Notes
  * Sales Rep
  * Google Maps (display "Link"; links to open in the Google Maps App)



  


Grouped by: Active (at top), Inactive (at bottom) 

  


Sorted by: Customer Name

  


Filters: 

  * All of the filters on the standard contacts report, with the exception of Name (see replacement below) 
  * Name (text field; ignore punctuation in results) 
  * Check-In Frequency (drop list of Check-In Frequencies; default to blank = all)
  * Last Check-In Date Range (looks at the Check-In Date; start date field defaults to blank = all; end date field defaults to blank = all)
  * Next Check-In Date Range (looks at the Check-In Date; start date field defaults to blank = all; end date field defaults to blank = all)
  * Sales Rep (drop list of all Employee Contacts; default to blank = all)



  


Buttons: N/A

  


Menu Visibility: All users

  


Other Notes: N/A

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1408803107](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1408803107)

  


Note that this is a fully custom report (not using the standard AppHosting Contacts report).

  


Split on spaces and search first name, last name, and contact override.Split on spaces and search first name, last name, and contact override.

  


BID: 1 day.

  


DONE_CH: Tim Reitz 06/18/2022: Do we need to clarify this? Will it look at all Sales Reps on contacts in the Solution?

Ellis Miller 06/20/2022: We will make Sales Rep a list field so that we can report on the list. We'll create a process to clean up old unused list items.
