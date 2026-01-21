7.2.10. Contact Record - Annual Goals Section

  


Requirements

  * Annual Goals custom section (visible if Contact Type = Member; visible to and editable for the corresponding Member and all his uplines):
    * Annual Goals Instructions (read-only; from the memo AppHosting.Zone Settings) 
    * Year (automatic and read-only; from the Year for the corresponding row on the table on the View All Annual Goals child screen - see details below; defaults to the current year when opening the Contact record, if there are multiple years on the table)
    * Set Date (same as the corresponding field on the View All Annual Goals child screen)
    * Review Date (same as the corresponding field on the View All Annual Goals child screen)
    * Faith Goal (same as the corresponding field on the View All Annual Goals child screen)
    * Family Goal (same as the corresponding field on the View All Annual Goals child screen)
    * Friends Goal (same as the corresponding field on the View All Annual Goals child screen)
    * Fitness Goal (same as the corresponding field on the View All Annual Goals child screen)
    * Finance Goal (same as the corresponding field on the View All Annual Goals child screen)
    * Other Goal (same as the corresponding field on the View All Annual Goals child screen)
    * Left/right arrows (buttons; used to cycle forward and backward through the Years to display the corresponding goals from the child screen onto the main screen)
    * New Year (button; adds a new row to the embedded spreadsheet, displayed on the record screen as a new Year and corresponding set of blank goal fields)
    * Delete Year (button; deletes the currently selected row with all of its goals for that year, after a confirmation)
    * View All Annual Goals (button; opens a child screen with the following:)
      * Goals (embedded spreadsheet with the following; used to store all annual goals; each row represents the goals for one year; note that each row appears on the screen as a set of fields as mentioned above): 
        * Columns: 
          * Year (when a new set of goals is added, auto-set to the year after the latest existing year on the table (max existing year + 1); read-only; validate against duplicate Years / more than one set of goals for the same Year - validation error message on the field: "There is already a set of goals for the specified Year.")
          * Set Date (required; date; default to the current date)
          * Review Date (required; date; default to 12/31 of the Year; validate against setting a date more than 13 months into the future - validation message on Save: "Review On date must be within 13 months of today."; when this date = the current day, the Review/Update Annual Goals alert is sent) 
          * Faith Goal (required; multi-line plain text) 
          * Family Goal (required; multi-line plain text) 
          * Friends Goal (required; multi-line plain text) 
          * Fitness Goal (required; multi-line plain text) 
          * Finance Goal (required; multi-line plain text) 
          * Other Goal (optional; multi-line plain text)
        * Automatically sorted by: Year (latest at the top)
        * Show 6 rows without scrolling



  


Development Specification

Change Requests:

  * Tim Reitz 04/09/2024: [[[IN9134](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9136&)]] - ZSB - Contact - Annual Goals Section - Visibility for "New Year" Button
  * Tim Reitz 04/09/2024: [[[IN9565](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9567&)]] - ZSB - Contact Record - Clarify Visibility & Editability
  * 


  


  


  


Ellis Miller 05/05/2023: 

  


BID: 4 HOURS
