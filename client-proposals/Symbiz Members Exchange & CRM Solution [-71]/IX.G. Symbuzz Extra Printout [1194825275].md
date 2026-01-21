9.7. Symbuzz Extra Printout

  


Requirements

Purpose/Overview: This is a custom PDF printout of all Posts within a specified date range, based on the Post Entry Date. This can be printed in a Monthly or a Weekly format. For offline members without email, this is printed once a month and mailed out, containing all posts from the past month.

  


Printed From / Included In: 

  * Symbuzz Extra Posts Report 
  * Admin | Symbuzz Extra | Print Symbuzz Extra (Weekly) 
    * Workflow: 
      * Selecting this menu option opens a page with prompts matching the filters on the Symbuzz Extra Posts Report, with the filters set to match the defaults. 
      * The user sets the prompts as desired or leaves them defaulted, then clicks Continue. 
      * The Solution generates the corresponding PDF, which the user can then view, download, or print. 
  * Admin | Symbuzz Extra | Print Symbuzz Extra (Monthly)
    * Workflow: The same as for the Admin Weekly version above, except that the Format filter is set to "Monthly" and the Post Entry Date range is defaulted accordingly. 
  * Print Symbuzz Extra (Monthly) User Notification
    * Note that this is the same date range as described in the Admin Monthly version above.
  * Members Menu | Members & Groups | Print Symbuzz Extra  
    * Workflow: The same as for the Admin Weekly version above. 



  


File Format/Name: 

  * PDF: 
    * Monthly (if the Format filter = Monthly): Symbuzz Extra (Monthly) (<Current date in mm-dd-yyyy>) 
    * Weekly (if the Format filter = Weekly): Symbuzz Extra (Weekly) (<Current date in mm-dd-yyyy>) 
    * Custom (if the Format filter = Custom): Symbuzz Extra (Custom) (<Current date in mm-dd-yyyy>)



  


Fields to be Filled: 

  * Letterhead (included on only the first page) 
  * Symbuzz Extra (<Monthly / Weekly / Custom Date Range>) 
  * Edition: 
    * If the Format filter = Monthly: <Current month in "MMMM YYYY" format>
    * If the Format filter = Weekly: <Current date in "MMMM DDDD, YYYY" format>
    * If the Format filter = Custom: <Current date in "MMMM DDDD, YYYY" format>



  


  * For each Group/Meeting (repeated multiple times, once for each Group with a Post Entry Date within the selected Post Entry Date range, sorted like the report - by Meeting Date, with the most recent date at the top): 
    * Group: <Growth Ring Group Description> 
    * Meeting Date: <Meeting Date> 
    * Meeting Secretary: <Meeting Secretary> 
    * Resource: <Development Resource Title> (<Author / Creator>) 
    * Growth Ring News: <Growth Ring News Post contents> 
      * Visible if the Post field has an entry
    * Prayer Requests: <Prayer Requests Post contents> 
      * Visible if the Post field has an entry
    * Networking Requests: <Networking Requests Post contents> 
      * Visible if the Post field has an entry



  


  * Footer: 
    * Symbuzz Extra (<Start Date> \- <End Date>) 
      * Normally this date range corresponds to the settings of the Post Entry Start and End Date filters, but if the results are narrowed based on one or both of the Meeting Date filters, this will display the narrowest date range. 
    * Powered by Silverloom 



  


Template: N/A

  


Handling Page Breaks: Break as needed between rows

  


Other Notes:

  * Note that If a Meeting does not have any posts entered, that meeting will be excluded from the printout (as when an individual post has no entry). 
  * Note that if there are no posts for a selected date range, the printout simply generates as a blank page.
  * Smaller text and narrower margins could be considered in the future to help reduce the page count if it gets really large. 



  


Sample(s): [https://docs.google.com/document/d/1q4qjvcRljTtYV5TrsX4jtiJ18GDTJh2f/edit](https://docs.google.com/document/d/1q4qjvcRljTtYV5TrsX4jtiJ18GDTJh2f/edit)

  


Development Specification

Change Requests: 

  * Tim Reitz 04/11/2024: Added with [[[IN8960](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8962&)]] - ZSB - Add Features for Symbuzz Extra (prev. called Cross Network Forum).
  * Tim Reitz 04/11/2024: [[[IN9417](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9419&)]] - ZSB - Symbuzz Extra - Revisions (#1)


