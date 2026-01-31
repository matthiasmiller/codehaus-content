5.4.10. Event - KPIs (Internal) Section

  


Requirements

*Documented 

  


"KPIs (Internal)" section: (visible for all Event Types; visible only to Regional Reps and Super Admins; used to track various key performance indicators related to the Event) 

  


  * Info Meeting KPIs: 
    * Leads Registered (visible if Event Type = Info Meeting; auto-set and read-only; with the following details: 
      * displays the number of Event Registration records that match the following criteria: 
        * Registrant Type = "Lead" 
    * Leads Attended (visible if Event Type = Info Meeting; auto-set and read-only; with the following details:
      * displays the number of Event Registration records that match the following criteria: 
        * Registrant Type = "Lead" 
        * Attended = "Yes" 
    * Attendance Rate [  ] % (visible if Event Type = Info Meeting; auto-set and read-only; number rounded to the nearest 1 decimal place; includes the % symbol after the value; displays the percentage of registered leads who actually attended; calculation: <Leads Attended:> / <Leads Registered> * 100)
    * Leads Converted (visible if Event Type = Info Meeting; auto-set and read-only; with the following details: 
      * displays the number of Event Registration records that match the following criteria: 
        * Registrant Type = "Lead" 
        * Attended = "Yes" 
        * Paid Membership Start Date for the Contact is set and = within 90 days of the Event Date 
    * Conversion Rate [  ] % (visible if Event Type = Info Meeting; auto-set and read-only; number rounded to the nearest 1 decimal place; includes the % symbol after the value; displays the percentage of attending leads that became members; calculation: <Leads Converted> / <Leads Attended> * 100) 



  


  


Note that additional KPIs can be added for Info Meetings or other Event types in the future.

  


Development Specification

Ellis Miller 06/21/2024: 

  


4 Hours, Nahian can give guidance on macros
