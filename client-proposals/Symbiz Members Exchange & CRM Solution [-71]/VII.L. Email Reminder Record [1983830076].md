7.12. Email Reminder Record

  


Requirements

The Solution includes the standard Silverloom Email Reminders module, to allow admin users to set up scheduled email reminders.

  


Accessed via: The Email Reminders report

  


Sections and Fields: 

  * Active Reminder (checkbox) 



  


  * Email Reminder section:
    * Name (required; plain text field) 
    * Schedule (auto-set and read-only; displays the selected schedule from the Schedule child screen) 
    * Ellipsis button; opens the Schedule child screen (see details below) 
    * Next Date (auto-set and read-only; displays the next scheduled reminder date from the Schedule child screen) 



  


  * Schedule child screen: 
    * Schedule section: 
      * Send Reminder (drop list) 
      * Months (labels + checkboxes, one for "Every Month" and one for each calendar month)
      * Repeat by (drop list of "Day of Month" and "Day of Week) 
      * Days of Month (visible if "Repeat by" = "Day of Month"; labels + checkboxes, one for "Every Day" and one for each date of the month, 1-31) 
      * Weeks (visible if "Repeat by" = "Day of Week"; labels + checkboxes for the following: 
        * Every Week 
        * First Week
        * Second Week
        * Third Week
        * Fourth Week
        * Last Week
      * Weekdays (visible if "Repeat by" = "Day of Week" ; labels + checkboxes for "Every Day" and each day of the week, Sunday - Saturday) 
      * Repeat Until (date field; default to blank = N/A) 
    * Upcoming Dates section: 
      * Schedule (
      * Next Date (
      * Future Dates (embedded spreadsheet with the following: 
        * Columns: 
          * Weekday 
          * Date



  


  * Email Contents section: 
    * From 
    * Bcc Sending (checkbox; defaults to unchecked) 
    * To 
    * Subject 
    * Body (memo; allows for expressions) 
    * Send Reminder Now (link; prepares and sends the current Email Reminder immediately; can be used to test the reminder) 



  


  * Attachment section: Note that this does not literally attach files to the Email Reminder. It would be better called "Embedded Report", as it allows the user to embed a selected report from the Solution into the bottom of the Email Body. 
    * Path (expression field; allows the user to select a report path) 



  


Data Access: See the Data Access Controls section of the proposal. Summary: Super Admins can view & edit all Email Reminders (controlled by the "View email reminders" permission). 

  


Special Considerations: 

  * Copy Record: Standard (any user with permission to view Email Reminders can copy)
  * Delete Record: Standard (any user with permission to view Email Reminders can delete)
  * Merge Record: Standard (any user with permission to view Email Reminders can merge) 



  


Other Notes:

  * Note that this record has a link to access Modification History (standard).
  * Note that the "Attachment" section is made visible via the "Show attachment on email reminders" System Switch (see details in the corresponding section of the proposal).



  


Development Specification

Change Requests: 

  * Tim Reitz 04/15/2024: [[[IN8957](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8959&)]] - ZSB - Add Email Reminders Module (prev. Internally created email reminders)


