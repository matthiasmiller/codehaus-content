3.2. Configure Publications Report

  


Requirements

The Configure Publications Report is a report of all publications being managed in the database. 

  


This report will be available only to Admin users, but with these distinctions between Full Admins and Publication Admins: 

  * Only the Full Admin will be able to see the full list of publications and open/edit them all. They will also be able create new publications. 
  * Publication Admins will only be able to view the publication that they are assigned to. They will be able to open the Configure Publication detail for that publication from this report. They will not be able to create new publications.



  


This report should have the following columns: 

  * Publication Title (link to open the Publication Detail)
  * Publication Code
  * Number of Active Users
  * Next Publication Date ("Month dd, yyyy" format)



  


Grouping/Sorting: 

  * It would be grouped by number of active users: Publications with one or more active users would be at the top; publications with zero active users would be at the bottom. 
  * It would sort by Publication Name, and it would not have any filters. 



  


This report would have a "New Publication" button at the top for setting up additional publications. As mentioned above, only Full Admins will be able to use this feature.

  


If a publication has zero active users, it will show in gray text on this report.

  


Development Specification

Date Format: The date format used throughout the ads management system should be "Month dd, yyyy" (or "Month d, yyyy" if the day has only one digit). This is the same format used in PNP's current newsletter system.

  


Data Restrictions on Publication Record: 

  * Full Admins: Full access
  * Publication Admins: Full access for assigned publication
  * Standard Users: No access



  


TODO_CH: We will hide the report for a standard user, but a user could always find the report or create their own. If they do, they will only see their own publication. Is this OK?

  


1 Days for report
