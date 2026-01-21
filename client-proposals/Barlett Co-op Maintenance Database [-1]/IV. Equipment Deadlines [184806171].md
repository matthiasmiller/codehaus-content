4\. Equipment Deadlines

  


Requirements

Equipment Deadlines

We will display a table of deadlines on the equipment record. It will be displayed in deadline order. Deadlines with overdue hours/miles will be displayed first, followed by items with a date < 30 days in the future, followed by any deadlines without a date, and finally deadlines more than 30 days in the future. 

  


Each deadline will include:

  * Deadline label
  * Next Deadline Date -- shows the date if specified, yellow if within 30 days, red if overdue.
  * Next Deadline Hours/Miles -- entered by the user for deadlines that are based on the tracked hours/miles. Red if overdue.
  * Last Completed
  * Completed By



Every deadline needs to either specify a date or Hours/Miles.

  


There will be an option complete a deadline. When selected, it fills in the completion date, Completed By, and allows entering optional notes. The due date is advanced if we know the deadline frequency, otherwise it is blanked out so that the user can enter the next deadline.

  


There will also be an option to edit an existing deadline. 

  


A "View Completed Deadlines" link displays all completed deadlines with dates, completed by, and entered notes.

  


We will need an interface for making a deadline as complete and adding notes (if desired).

  


Development Specification

Do we always lookup Deadline labels from the type record? let's look up for upcoming deadlines, but archive it for completed deadlines.

  


What happens when a new deadline is added and information is not filled in on each equip record? I think we treat it as currently due.

  


What happens if someone deletes a deadline? I think we remove it from upcoming deadlines for all equipment.
