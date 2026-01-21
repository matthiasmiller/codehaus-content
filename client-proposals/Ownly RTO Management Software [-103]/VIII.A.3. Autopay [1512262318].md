8.1.3. Autopay

See mockups [https://docs.google.com/spreadsheets/d/1jnDV1EadaIUCQzJZc-U7IAv9kvSzyM7DJey1fND0WAk/edit?gid=1219725344#gid=1219725344](https://docs.google.com/spreadsheets/d/1jnDV1EadaIUCQzJZc-U7IAv9kvSzyM7DJey1fND0WAk/edit?gid=1219725344#gid=1219725344).

  


Seth Miller 11/26/2025: TODO_IDD: Consider a warning/error if autopay is set up in a way in which late fees will be incurred

  


  * Automatic Payment Schedules (section)
    * # of Active Automatic Payment Schedules (autocalculated and readonly)
    * Next Automatic Payment Date (autocalculated and readonly)
    * Next Automatic Payment Amount (autocalculated and readonly; sums if multiple payments occur on the same date)
    * "View / Edit Schedules" (child detail screen)
      * Automatic Payment Schedules (RG)
        * NOTE - Starting Date has to be FUTURE
          * Allow editing as long as the starting date is in the future 
          * If the starting date is today or prior, lock it down EXCEPT for the Active checkbox and the End Date
          * Do NOT allow re-opening a payment schedule after it's been closed (and saved as closed).
          * Validate that starting date is not more than # days in the future (based on a system switch AutopayNumDaysFutureStartDateWarning that defaults to 365 days) 
        * Sort the RG with active at the top (Start Date + End Date + RG Row ID)
        * Frequency (when changed; clears start date, end date, and Frequency-specific fields)
          * One-Time
            * Starting Date (required)
          * Weekly
            * Weekday (S-S; sets to first upcoming Wed, etc; editable if Starting Date is within the next week (Tomorrow + 1 <= Date <= Tomorrow + 7) always reflects Starting Date; required)
            * Starting Date (editable; required)
            * Repeat Every # of Weeks (default to 1; required)
          * Monthly by Day of Week
            * Week (First, Second, Third, Fourth, Last; editable; required)
            * Weekday (S-S; editable; required)
            * Starting Month (list of Months; required)
            * Starting Date (read-only; auto-set from Week, Weekday, and Starting Month fields)
            * Repeat Every # of Months (default to 1; required)
              * Must be a positive integer 
          * Monthly by Day of Month
            * Starting Date (required)
            * Repeat Every # of Months (default to 1; required; must be a positive integer) 
        * Payment Method (list of payment methods for the primary customer; required)
        * Amount (number; two decimals; required)
        * Active (editable if Ending Date is >= Today; on uncheck, sets Ending Date to yesterday)
        * Ending Date (date)
          * If the Ending Date is scheduled for a payment date, show label: "The payment is scheduled to run on the ending date."
        * Note (string)
      * Payment Method (MRG field; list of payment methods for the primary customer; required)
      * Add Payment Method (link)
      * Note (MRG field; string)
      * Preview Automatic Payments (virtual RG of automatic payments until Balance is zero or contract end date [Start Date + Term Length] is reached)
        * Date
        * Amount
        * Balance
        * NOTE - Include some customer & contract information to be able to send to customer
    * View All Upcoming Payments (link; opens a report of the automatic payments preview)



  


  * Events RG
    * Link to the schedule definition 



Seth Miller 12/04/2025: TODO_KS [[PC0187318]]

  


TODO_SETH: The read-only checkbox is confusing. Can we show it as yes/no? Or better yet, should it be editable and set an end date to today
