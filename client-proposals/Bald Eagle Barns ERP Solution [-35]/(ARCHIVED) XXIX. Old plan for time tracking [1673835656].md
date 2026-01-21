29\. Old plan for time tracking

  


Requirements

The AppHosting Time Cards module would be included, with some changes. The main changes are to accomplish the following:

1\. To handle the Thursday-Wednesday work week.

2\. To handle daily tracking in addition to hourly tracking.

  


This would include PTO tracking on the time cards. 

  


This would also include the Mileage Reimbursement feature.

  


BEB's pay periods are 2 weeks, starting on Thursday and ending on Wednesday. As mentioned above, the Time Cards (both hourly and daily) would reflect this.

  


Overtime tracking looks at the hours worked in the work week (Thursday-Wednesday).

  


Note that for paid days off where a member also works (gets paid double), the Time Card will track double time for that day in the Hours section (for Hours) and the Summary section (for Hours and Worked Days). For example, Worked Days will still show "1" for the Partial Day and "1" show in the PTO row below, and have both show in the Summary.

  


All BEB Time Cards will have the following custom rows added to the Summary section:

  * Task $ (total amount of the current member's completed Tasks in the selected work week) 
  * Days Worked (hidden for hourly; sum of the number of days worked/partial days)



  


  


For members who are paid hourly/need to track hours, the Time Card would be the same as the standard AppHosting Time Cards, with the added features.

  


  


For members whose Compensation is set to Salary or Daily, the Time Card would display the Worked Days feature. This would be used to track days (full and partial) that the members work, as well as their PTO.

  


The Worked Days Time Card would look almost the same as the regular Time Cards, with a few differences:

  * The "Time Worked" section would be replaced with a "Days Worked" section. This would have an embedded spreadsheet with the following: 
    * Columns: 
      * Day (list of days of work week, Thursday-Wednesday) 
      * Worked (checkboxes; fills the Partial Day with "1" if checked; remains/becomes unchecked if Partial Day is 0 or is changed to 0)
      * Partial Day (drop list of 0, .25, .5, .75, 1) 
      * Notes (plain text field, like the Notes section on the standard Time Card) 
    * Sorted by: Date
  * The following sections would be hidden:
    * Hours (at the top)
    * Paid Time Off (below Days Worked)



_CH: remember why we were going to hide this? I think we would still want it (he wants it for hourly)

  


  * The Summary section would have the following (the other lines would be hidden):
    * Task $
    * Paid Time Off (_CH: can we have this show the days amount?
    * Days Worked
    * Effective (_CH: can we have this show the total days -- worked plus PTO?
    * Mileage $



  


  


All Time Cards in the BEB database would have a bottom report of completed tasks for the selected Time Card user.

  


This would be the Tasks by Assignee Report, filtered down to the selected Time Card user and the selected Work Week.

  


Development Specification

From Matthias regarding Thur-Wed work weeks: I think the most sensible, long-term design is to support this natively in time cards. Otherwise, we run into weird issues with overtime etc, and I think it's arguably correct to let time cards mirror the work week.

  


From what I see, this would require us to:

* Add a system switch called "Work Week Starting Day" that defaults to Sunday.

* Create a StartOfWorkWeek macro, and make sure that gets used in the time card catalog, all customizations, and all reports.

* Possibly rename StartOfWeek to StartOfCalendarWeek.

* Change the "Hours" section to show the days in the order of the work week

* Make sure the time slots get sorted by date, not by weekday

* Maybe even stomp the starting weekday onto a hidden field on the time card itself. This way, if we change the work week, everything can continue to work as expected.

  


Include the Mileage catalog. 

[ ] Note that CH should be paid for this.
