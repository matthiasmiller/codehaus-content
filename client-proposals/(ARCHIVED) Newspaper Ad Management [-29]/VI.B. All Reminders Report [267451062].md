6.2. All Reminders Report

  


Requirements

This report would show all set, due, overdue, and dismissed Reminders for the selected publication.

  


The report should include the following columns:

  * Reminder Title (link to the Reminder detail)
  * Customer
  * Associated Task
  * Send To
  * Due Date (mm/dd/yyyy format)
  * Due Time
  * Publication (only visible for Full Admins)



  


Filters:

  * Status (multi-choice of Overdue, Due, Set, and Dismissed; default to blank = all)
    * Overdue
    * Due - sent
    * Set - created but not sent yet
  * Send To (list; default to blank = all)
  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Grouping/Sorting:

  * Group by Overdue, Due, Set, and Dismissed
  * Sort by Send To



  


Development Specification

Tim Reitz 02/03/2021: The Publication prompt should be available in a SelectPublications subset
