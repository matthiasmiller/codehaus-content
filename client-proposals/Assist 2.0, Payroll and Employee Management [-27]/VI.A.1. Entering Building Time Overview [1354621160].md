6.1.1. Entering Building Time Overview

  


Requirements

Assist will provide an two-pane interface to enter building labor time. It show a list of companies on the left pane. The right pane would allow entering the labor time, based on the company's labor tracking method.

  


Development Specification

Tim Reitz 01/15/2021: How does this get saved? Can we save individual screens on the right side, or do we save the whole page (all companies at once?)

Matthias Miller 01/15/2021: Save individual ones. Looks good.

  


To simplify data entry, we will create an RG of Production Time on the company record and fill it in using these editable reports. A separate process will then move it over to the Building records (see "Stored Calculations")

Nate Kilcrease 01/15/2021: What should this look like in the Company Record?

Matthias Miller 01/15/2021: A "Pending Production Time" button that opens a child RG with the following columns:

  * Station (if using station tracking)
  * Employee (if using employee tracking)
  * Invoice #
  * Date
  * Start Time
  * End Time
  * Number of Builders
  * Break Time (read-oly; calculated)
  * Hours (read-only; calculated)



  


This allows us to enter information on a per-company basis, simplifying the entry process, while still allowing ongoing data entry.

  


Company RG

The company record would have an RG (behind a "Production Time Entry" button). Users will typically enter from the editable report, not from the RG.

  


Each row will specify time either for a station or for an employee:

  


  * CompanyProdTimeStation (list of stations, helper list based on Company record's stations)
  * CompanyProdTimeEmployee (list of contacts, helper list of active employees for this Company)
    * "ErrorOnSave:You cannot specify both a Station and an Employee.



  


  * CompanyProdInvoice# -- simple string field (TODO: Ask Josh about validation for the ID).



  


  * CompanyProdTimeDate
    * "ErrorOnSave:A Date must be specified if a Start Time is specified."
    * "ErrorOnSave:A Date cannot be specified unless a Start Time is specified."
  * CompanyProdTimeStartVal - number field to store time
  * CompanyProdTimeStart - editable string macro for entering time
    * "ErrorOnSave:A Start Time cannot be specified if both Station and Employee are blank."
    * "ErrorOnSave:A Start Time cannot be specified if the Invoice # is blank."
  * CompanyProdTimeEndVal - number field to store time
  * CompanyProdTimeEnd - editable string macro for entering time
    * "ErrorOnSave:An End Time must be specified if a Start Time is specified."
    * "ErrorOnSave:An End Time cannot be specified unless a Start Time is specified."
    * "ErrorOnSave:End Time must be after Start Time."
  * CompanyProdTimeNumBuilders
    * "ErrorOnSave:Number of Builders must be specified if a Start Time is specified."
    * "ErrorOnSave:Number of Builders cannot be specified unless a Start Time is specified."
  * CompanyProdTimeBreaksVal -- macro for time of breaks (see below)
  * CompanyProdTimeHours -- macro, see below



  


A Field Change Expression should Delete any rows that don't have a Start Time specified.

  


Bid: 1 day

  


Time Macros

CalcCompanyBreakTime( vProdStartTime, vProdEndTime) -- this will find the overlap of break times with the StartTime/EndTime range. This will do a SumRG on the CompanyBreakTimes RG summing the overlap of each of the breaks with these times using a new CalcTimeOverlap macro.

  


Create a new CalcTimeOverlap( vStartTime1, vEndTime1, vStartTime2, vEndTime2) macro with unit tests:

Assign vMaxStart = Max( vStartTime1, vStartTime2);

Assign vMinEnd = Min( vEndTime1, vEndTime2);

Max( 0, vMinEnd - vMaxStart)

From [https://stackoverflow.com/questions/36035074/](https://stackoverflow.com/questions/36035074/)

  


CalcCompanyProdTimeHours( vStartTime, vEndTime) is basically:

Sum( vEndTime - vStartTime,

          -CalcCompanyBreakTime( vStartTime, vEndTime))

  


Bid: 1 day

  


  


Multi-pane Report

Multi-pane "Building Time Tracking" report in the Buildings menu.

  


The left pane is simply a list of companies in alphabetical order.

  


We'll use one of two different reports for the right pane depending on the highlighted company (use conditional subpanes):

  * Std Building Time Tracking -- by Station.r20
  * Std Building Time Tracking -- by Employee.r20



  


Pass the company name as an ask prompt to the right pane.

  


Subpanes are defined below.

  


Bid: Basic report. 1 hour.
