5\. Time Off Policies

  


Requirements

We will track all time off by days or (in the case of health) by partial days.

  


We will have the following policies:

  * Vacation (annual allowance)
  * Family Wedding or Bereavement (per-incident allowance)
  * Health leave (monthly allowance)
  * Unpaid Time off (monthly allowance)



  


We will also implement an untracked "Scheduled Day Off" to allow managing thrift store schedules.

  


The time off policies will be used to calculate the number of available days. We will calculate, but not enforce, this in the system. It will remain up to the managers to enforce this.

  


When calculating available vacation days, all prorated days will be rounded up.

  


Here is an example Allowance Schedule for Salaried Staff:

  * Year 1 - 10 days
  * Year 2 - 10 days
  * Year 3 - 12 days
  * Year 4 - 14 days
  * Year 5 - 16 days
  * Year 6 - 18 days
  * Year 7 - 20 days



  


We will document the concept of grandfathering these policies.

  


For salaried staff, total available vacation days (without regard to used days) will be calculated as follows:

  * As of Hire: Prorated by Year 1
  * As of 1st New Year’s: Year 1
  * As of 1st Anniversary: Year 2
  * As of 2nd New Year’s: Year 2
  * As of 2nd Anniversary: Year 3
  * Etc



  


For hourly staff, vacation days will not become available until the following year. For example:

  * As of Hire: No vacation
  * As of 1st New Year’s: Year 1
  * As of 1st Anniversary: Year 1
  * As of 2nd New Year’s: Year 2
  * As of 2nd Anniversary: Year 2



Etc

  


Health is typically tracked on an hourly basis, but we will need to turn it into a daily rate. We will have an option to calculate it based on an 8:00 basis.

  


USER SPECIFICATION

We will define specific Time Off Policies. These will have:

  * The name
  * Dates
    * Pre-determined (i.e. Holidays)
    * Flexible (i.e. Vacation)
  * For Pre-determined  Dates:
    * List of Months+Days
    * Special calculations for Labor Day, Memorial Day, Good Friday
  * For Flexible Dates
    * Time Period
      * Per Year (Vacation)
      * Per Month (Health Leave/Unpaid Time Off)
      * Per Incident (Family Wedding/Bereavement)
    * Tracking (Yes or No?)
      * If tracking, Allowance? (Vacation, Family Wedding, Bereavement)
      * Partial-Year Allowance
        * None
        * Prorated
      * If tracking by allowance, Days Available based on Years
    * Allow partial days? (Health only)
    * Request Deadline
      * 21 days for Vacation, 0 days for Bereavement, etc)
      * # of days -- based on Day of Week and/or Time
  * Who it's for:
    * By role (i.e. specific role or section of org chart)
    * By salary/fulltime/parttime



  


When the office is closed, we will simply need to create 8 holiday entries for Dec 24-31.

  


Development Specification

Matthias Miller 12/06/2017: Can't remember the story but removing this

  * Availability
    * Beginning of Period
    * Earned Monthly


