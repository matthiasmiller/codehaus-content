7.9.9. Event - KPIs (Internal) Section

  * "KPIs (Internal)" section: (visible for all Event Types; visible only to Regional Reps and Super Admins; used to track various key performance indicators related to the Event) 



  


  * Info Meeting KPIs: 
    * Leads Registered (visible if Event Type = Info Meeting; with the following behaviors / details: 
      * read-only macro; 
      * displays the number of Event Registration records that match the following criteria: 
        * Registrant Type = "Lead") 
    * Leads Attended (visible if Event Type = Info Meeting; with the following behaviors / details:
      * read-only macro; 
      * displays the number of Event Registration records that match the following criteria: 
        * Registrant Type = "Lead" 
        * Attended = "Yes") 
    * Attendance Rate [  ] % (visible if Event Type = Info Meeting; with the following behaviors / details: 
      * read-only macro; 
      * number rounded to the nearest 1 decimal place; 
      * includes the % symbol after the value; 
      * displays the percentage of registered leads who actually attended; 
      * calculation: <Leads Attended:> / <Leads Registered> * 100)
    * Leads Converted (visible if Event Type = Info Meeting; read-only macro; with the following details: 
      * displays the number of Event Registration records that match the following criteria: 
        * Registrant Type = "Lead" 
        * Attended = "Yes" 
        * Paid Membership Start Date for the Contact is set and = within 90 days of the Event Date) 
    * Conversion Rate [  ] % (visible if Event Type = Info Meeting; with the following behaviors / details: 
      * read-only macro; 
      * number rounded to the nearest 1 decimal place; 
      * includes the % symbol after the value; 
      * displays the percentage of attending leads that became members; 
      * calculation: <Leads Converted> / <Leads Attended> * 100) 



  


  


Note that additional KPIs can be added for Info Meetings or other Event types in the future.
