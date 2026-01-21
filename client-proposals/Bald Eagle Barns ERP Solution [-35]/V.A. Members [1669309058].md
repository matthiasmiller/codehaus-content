5.1. Members

  


Requirements

Notes about Members:

  * The contact types with "(Member)" in the name will be used for people who work directly for BEB. BEB does not have any literal employees; they function as a limited partnership, so the workers are referred to as members.
  * Each Member should have a Contact record and a User Login set up in the database, and should have their User Login ID linked with their Contact record.
  * The Contact record should have a warning on Save if an active Member contact does not have a User ID associated with the contact record. This warning should say, "This Member contact is missing its linked User ID."
  * If a Member stops working at BEB, an admin should deactivate both the Contact and the User Login. 
  * If a Member changes roles, an admin should change the Contact Type. Doing so would not automatically change all of the compensation information, so the admin should change that separately in the Member Compensation section. 
  * Admin users can use any of the Member-type Contact Types (their admin status will be set as part of the User Login)



  


Member Compensation custom section: (for all Member-type Contact Types; visible only to the corresponding user and for admins; editable only by admins):

  * Initials (required; entered manually; allow for up to 3 characters, normally the initials of their first and last name; error on save if the same initials are used for another active Member contact or Non-member Salesperson contact; used for QB and for reporting, such as to show who sold a building or completed a Task)
  * Base Compensation (required; drop list of the following:) 
    * Daily + Commission (only option for Salesperson (Member))
    * Hourly (available for Office Worker) 
    * Piecework + Hourly (available for Shop Worker) 
    * Salary (only option for Driver; available for Office Worker and Shop Worker)  
  * Annual Salary $ (visible and required if Base Comp = Salary OR Daily + Commission; number field to 2 decimal places; allow for 0.00; Daily Rate is calculated from this as needed)
  * Daily Rate $ (visible and auto-filled/read-only if Base Comp = Daily + Commission; calculated from Annual Salary $, based on a 260-day work year: Annual Salary $ / 260)
  * Hourly Rate $ (visible and required if Base Comp = Hourly; number field to 2 decimal places)
  * Hourly Rate for Tasks (visible and required if Base Comp = Piecework; number field to 2 decimal places) 
  * Worked Days/Hours (link; opens the Time Sheets Report, filtered to only the current member) 
  * Move Job Rate (%) (visible and required if Contact Type = Driver (Member); number field with whole numbers; only for Move Jobs; % of subtotal after discounts but before tax) 
  * Completed Tasks (link; opens the All Tasks Report, filtered to show only completed tasks for the current member; visible on all Member-type Contacts)
  * Salesperson Commission (visible and required if Base Comp = Daily + Commission; embedded spreadsheet with the following, with the intention that it can be used for a salesperson on a flat rate or a custom tiered rate; if only one row is filled, it is flat rate, if multiple rows are filled, it is tiered and the Salesperson will receive the percentage(s) that correspond with their sales $ for the current Pay Period; the Commission % will apply to sales for the corresponding tier)
    * Columns: 
      * Min. Sales $ (required; number field to 2 decimal places; must be 0 for the first row; for rows after the first row this must be set to 0.01 more than the Max. Sales $ of the previous row)
      * Max. Sales $ (required if subsequent row(s) exist; must be blank for the final row, either flat rate or tiered; number field to 2 decimal places) 
      * Commission % (required; number field to 3 decimal places; percentage of sub-totals for all Sales Orders that correspond to the Salesperson, after discounts but before sales tax)
    * Sorted by: Min Sales $
    * Buttons to add and remove rows ("+" and "-")
    * Show at least 4 rows without scrolling



  


Other custom field(s) for all Member-type contacts:

  * Subscribe to Referral Letter Notification (in the "AppHosting Settings" section of the contact record; visible if there is a User ID for the contact; checkbox; users with this checkbox filled will receive the Customer Referral Letter system notification) 



  


Other Notes about the Member Comp section:

  * The database will not store historical compensation details (other than in Modification History). 
  * As mentioned in the details above, the tiered commission would be based on the pay period, so the Salesperson would start over in the lowest tier when the next pay period begins. (In the future, this calculation may be adjusted to be based on the calendar month or calendar year.)
  * Example of tiered commission for SP:
    * Sample tiers:

Min. Sales $| Max. Sales $| Commission %  
---|---|---  
0.00| 5,000.00| 3.000  
5,000.01| 10,000.00| 3.500  
10,000.01|   
| 4.000  
  
  * Sample sales & commission behavior:
    * SP sells $4,500.00 of merchandise: Receives 3.000% for all of it.
    * SP sells $5,500.00: Receives 3.000% for $5,000.00 and 4.2000% for $500.00.
    * SP sells $12,000.00: Receives 3.000% for $5,000.00, 4.2000% for $5,000.00, and 4.7555% for $2,000.00.


  * All changes to compensation for a member should be applied effective immediately on Save.
  * For Shop Workers:
    * If Base Comp = Salary, the worker does not get paid anything for the Tasks that they complete.
    * If Base Comp = Piecework, the worker is paid exclusively for the completion of Tasks (based on the settings of the Task Type and the Hourly Rate for Tasks).



  


*Done.

  


Development Specification

Tim Reitz 11/23/2021:  

Min. Sales $| Max. Sales $| Commission %  
---|---|---  
0.00| 5,000.00| 3.000  
5,000.01| 10,000.00| 3.500  
10,000.01|   
| 4.000  
  
  


TODO_CCI: The client would like for it to be fairly easy to change this time frame (maybe to a month or a year). My proposal is that we have a macro that, given a date, returns the beginning date of the sales commission period. For now, it goes back to the beginning of the pay period, but this could be adjusted. When calculating commissions, we would calculate the number of prior sales in that period.
