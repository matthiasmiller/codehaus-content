2.10. Rescheduling Missed Stops

  


Requirements

Every day, find all prior stops that were unfulfilled. Add a note to the instructions: "(This stop was rescheduled because it was missed on [scheduled date].)". Update the scheduled date to the next week that has availability on the same weekday (considering holidays).

  


In addition, when a Stop's status is changed to Attempted and it was requested on or before today, add a note to the instructions: "(This stop was rescheduled because it was attempted on [attempted date].)". Reschedule it for the next available week on the same weekday (considering holidays).

  


Development Specification

Macros

[ ] Add an HolidayIsOnDate(Date) macro that's a Holiday macro. It should evaluate the holiday for the past year, current year, and next year, and see if any match. This is important since holidays can be observed on the prior or following day.

[ ] Add Unit Tests to mock up a holiday with a prior day and following day observance to test this.

  


[ ] Add an RouteIsHoliday(Date) macro that iterates over the RG, using the new HolidayIsOnDate macro

  


[ ] Add a ConfigRoutes_RescheduleInterval (of RoutesRecurringSchedules list). Default to "Daily", but override to "Weekly" for ZNH.

[ ] Add a ConfigRoutes_MaxRescheduleDays. Default to 30. No override for ZNH.

  


[ ] RouteNextAvailableDate macro:

  * Take a vAsOfDate.
  * Task a vRescheduleInterval (list of RoutesRecurringSchedules)



  


  * vStartDate = vAsOfDate+1
  * vEndDate = vStartDate + ConfigRoutes_MaxRescheduleDays
  * Do a DateRangePipeList from vStartDate to vEndDate, respecting the vRescheduleInterval (every 1 or 7 days)
  * Keep all items if they are on the route's schedule and are not a holiday (see prior Validate macro that we added)
  * Return the first item from that list, or vEndDate if there are none. (We bump it out into the future to avoid continually adding footnotes.)



  


[ ] Add a RouteStopNextAvailableDate macro and pass in ConfigRoutes_RescheduleInterval

  


X30s

  * Create an x30 ("Std Routes Daily - Rescheduled Unfulfilled Stops.x30") to reschedule unfulfilled routes (stop type = "unfulfilled" and RequestedDate < Today). Append footnote to Instructions field per the spec. Use the RouteStopNextAvailableDate(Today-1) macro for the new requested date.
  *  Create a "Std Routes Daily Maintenance.x30list" that runs the above x30.



  


OnChange

  * The second footnote should be an OnChange when the stop's status is set to Attempted. Append footnote to Instructions field per the spec. Use the RouteStopNextAvailableDate(Today) macro for the new requested date.


