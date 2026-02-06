3.4.1. Manage Sales Items Report

  


Requirements

This is the standard report, with the addition of a Publication column and a Publication filter for Full Admin Users. It can be used to view all Sales Items and to create new Sales Items. This report will have a "New Sales Item" button at the top to set up a new item.

  


Publication Admin Users will only be able to see, create, and edit Sales Items for the publication to which they have access. Full Admin Users will be able to see, create, and edit Sales Items for all publications. Standard Users can only view, not edit or create Sales Items for the publication to which they have access.

  


Columns: 

  * Code (link to the Sales Item detail)
  * Description
  * Category
  * Taxable?
  * Unit Price
  * Active?
  * Publication (Full Admin only)



  


Filters: 

  * Code 
  * Category (list of Categories; default to blank = all)
  * Description
  * Active Items Only (checkbox; default to filled)
  * Publication (Full Admin only)



  


Grouping/Sorting: 

  * Group by Active/Inactive (if showing both), then by Category
  * Sort by Code



  


Development Specification

Standard report customizations: Use conditionally included columns ("System include if:") for the customized columns and custom macro for report subset (custom ask prompt).

  


TODO_CH: Just a note that we have "Support system-specific settings" feature that lets us add columns or buttons that are only sent to specific clients based on a "System include if" setting). You can delete this comment after reading it, but it makes it simpler than adding several custom macros for a new column.

  


adding column and custom ask prompt (the ask prompt can be at the bottom of the screen). 

1 day
