4.1.1.10. Configure Holidays

  


Requirements

Assist will track also holiday dates on a per-company basis. Each company will have an editable embedded spreadsheet. It will have the same columns as the universal holiday dates, but the values will be company-specific.

  


Embedded spreadsheet with the following:

  * Columns
    * Start date (single-line plain text field)
    * End Date (single-line plain text field)
    * Reason (droplist of Closed, Add new item to list)
    * Paid Time Off (checkbox)
  * Automatically sort by: Start Date (show oldest first)
  * Buttons to add and remove rows ("+"/"-")
  * Show 6 rows without scrolling



  


These dates will automatically be respected when calculating lead times.

  


Development Specification

Seth Miller 06/14/2021: I think these dev specs are fairly out of date. I'm just coding this like the RG in AppHosting.zone Settings (as the mockups suggest).

  


  


See also [[File:2020 Holidays.pdf]]

  


Josh: I think for the sake of simplicity, we should stop using the built-in holidays. I think instead, we should have something in AppHosting.zone settings, if we want company-wide blackouts.

  


CCI: We will use the IsDateBusDay function to determine whether a date is a business day. Copy the DaysAsHolidays and DaysAsBusinessDays system switches from PerformSmartBase into ZFP so that ZFP can modify the dates. 

  


Create a "View System Holidays" report in the Admin menu. It will prompt for the year (default to current year). Show a list of holidays. The expression is something like this:

  


DateRangePipeList( [1/1/2020], [12/31/2020])

Assign vRepeatDate = DateValue( RepeatListItem );

  


InRange( Weekday( vRepeatDate), 2, 6) AND

NOT IsDateBusDay( vRepeatDate)

  


Sort by DateValue( RepeatListItem)

  


Column Contents formatted as "DDDD, MMMM D, YYYY".

  


Add a footnote:

Dates can be added or removed from this list by modifying the DaysAsHolidays and DaysAsBusinessDays system switches.

  


We can use the DaysAsBusinessDays and DaysAsHolidays system switches for global dates. Most likely, we want to nix the Veteran's Day, President's Day, etc.

  


This will be used to populate the time off RG and for lead times. Because of this, we do not need to store historic holidays.

  


Bid: 4 hours
