8.1.4. View Non-Business Days Report

  


Requirements

Overview: This is standard Silverloom report of non-business days, used to set which days to exclude from business day-related calculations (i.e. for discount windows and payment due dates).

  


Accessed from: Advanced | Configuration | View Non-Business Days (opens the report directly, bypassing the filter screen)

  


Title: "Non-Business Days (Excluding Weekends)"

  


Columns: 

  * Date 
  * Description 



  


Footnote: "Non-holidays can be treated as holidays by specifying the date in the Holidays system switch. Additionally, holidays can be treated as business days by specifying the date in the Business days system switch. In the value of these switches, enter one or more dates separated by a space." 

  


Grouped by: N/A (none)

  


Sorted by: Date (earliest at the top) 

  


Filters: 

  * Year (required; number; defaults to the current year) 



  


Buttons: 

  * N/A



  


Menu Visibility: 

  * All users



  


Other Notes: 

  * The default list includes the following US bank holidays: 
    * New Years Day
    * Martin Luther King Jr Day
    * Presidents Day
    * Good Friday
    * Memorial Day
    * Juneteenth
    * Independence Day
    * Labor Day
    * Columbus Day
    * Veterans Day
    * Thanksgiving Day
    * Christmas Day
  * Customizing holidays / business days can be done on a year-by-year basis: 
    * Non-holidays can be treated as holidays by specifying the date in the Days as Holidays system switch. 
    * Additionally, holidays can be treated as business days by specifying the date in the Days as Business Days system switch. 
    * In the value of these System Switches, enter one or more dates separated by a space.



  


Development Specification

Mockup: N/A 

  


Tim Reitz 12/31/2024: See a user version of this report in the demo system: [https://demo.silverloom.io/Reports/User/Shared/Government_Holidays_(Non-business_Days)?Asks=...&State=ISwSvCyE0ts](https://demo.silverloom.io/Reports/User/Shared/Government_Holidays_\(Non-business_Days\)?Asks=...&State=ISwSvCyE0ts).

  


Tim Reitz 12/31/2024: The two System Switches mentioned in the report footnote need to be added to Silverloom Base: 

  * Holidays system switch
  * Business days system switch



  


Ellis Miller 12/16/2024: 

[ ] BD: Make the report standard.

[ ] BD: Copy DaysAsBusinessDays and DaysAsHolidays to Silverloom Base.

[ ] USA: Change the report Column 2 so that it says "Custom" if the target date is in the DaysAsHolidays list (compare with DateValue in case the date is formatted differently).

  


BID BD: 2 HOURS

BID US: 2 HOURS
