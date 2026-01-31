3.3. Configure Publication Detail

  


Requirements

The Configure Publication Detail page will be used to set up publications. As with the Configure Publications Report, only the Full Admin and the Publication Admins for a given publication will be able to edit these configuration settings.

  


Each publication record will include the following: 

  


General Configuration Section: 

  * Publication Name (required; text field)
  * Publication Code (required; text field; validate against duplicates; used to distinguish Contacts, )
  * Number of Active Users (display number of Standard and Publication Admin Users assigned to the publication)
  * Run By (required; drop list of Ad Size, Column Inch; for now only show Ad Size option and default to it)
  * Invoice Description (expression field; used for configuring what details from the Available Ads embedded spreadsheet show up in the invoice description lines for ads; warn on save if empty; if no description is set here, have a generic message on the invoice line items such as "No invoice description defined") 
    * CodeCrafters/CodeHaus will provide assistance is setting up the Invoice Description using this expression, and may provide instructions for doing it. 



  


Schedule Section: 

  * Repeat By (required; drop list of "Day of Month" and "Day of Week")
    * Day of Week would be used for Daily, Weekly, and Bi-Weekly publications
    * Day of Month would be used for Monthly and Yearly publications
    * Either one could be used for Custom (depending on the need)
  * Schedule (required to define Start On Date):
    * Months (for Day of Month and Day of Week; multi-choice checkboxes of months and Every Month)
    * Weeks (if Repeat By = Day of Week; multi-choice checkboxes of First, Second, Third, Fourth, Last, Every Week, and Every Other Week)
    * Weekdays (if Repeat By = Day of Week; multi-choice checkboxes of weekdays Monday-Saturday and Every Day)
    * Days of Month (if Repeat By = Day of Month; multi-choice checkboxes of dates 1st-31st and Every Day; handle changing the dates 29th-31st that aren't in months)
  * Start On Date (required; calendar/date picker; sets first Publication Date; selected date must match results set in Schedule)
  * Upcoming Publication Dates (automatic; read-only list of next 8 Publication Dates; "Month dd, yyyy" format; based off of Schedule and Start On Date; first/next publication date should be at the top, future dates below; list should keep updating as time goes on)



  


Development Specification

Data Restrictions:

  * Full Admins: Full access
  * Publication Admins: Full access for assigned publication
  * Standard Users: No access



  


TODO_CH: For standard users, I think when you say "No Access", you mean "No Editing". Publication users will only be able to see their own records. PubAdmins can modify it, but standard users can only view it. We need to have the data unrestricted for standard users so that features work correctly. We could potentially hide a few fields on the detail screen if you wish, but restricting fields gets tricky.

  


Invoice Description Expression: We should have a macro that takes an Ad ID and an expression and returns the value to allow referencing ad information from the context of the schedule RGs.

  * In Apphosting.zone Settings, define a default message to use if no description is entered in this expression.



  


Ellis Miller 04/20/2021: 

Basic detail screen:

[ ] validation on publication code.

[ ] macro for NumberActiveUsers

1 day with data restrictions.

  


[ ] Expression Field. 1 day.

  


Schedules Entry:

[ ] Hidden RG's for Months, Weekdays, And DaysOfMonth.

[ ] Visible fields for the 6 Weeks options.

[ ] About 40 macros that add/remove rows to the hidden RG's:

[ ] PubOnMonthDay1 macro that is defined as IsPubOnMonthDay(1) that is defined as HasRG(PubOnMonthDays, PubOnMonthDay = vDay). The OnChange will Add/Delete rows from the RG as needed.

3 days.

  


Calculation Schedules

Ellis wants to code this for fun in 8 hours using functions to make this testable.

Bid at 3 days for Ellis.

Bid at 2 days for a dev to write tests beforehand(?) (Ellis will give guidelines).
