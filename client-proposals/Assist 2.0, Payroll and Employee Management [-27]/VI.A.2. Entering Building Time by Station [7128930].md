6.1.2. Entering Building Time by Station

  


Requirements

When selecting a company in the left pane that tracks by station, show the following spreadsheet in the right pane:

Invoice #| Date| Start Time| End Time| Hours Worked| No. of Builders| Total Previous Worked Hours| Previous Work Dates| Total Station Hours| Total Building Hours  
---|---|---|---|---|---|---|---|---|---  
Station Name|   
|   
|   
|   
|   
|   
|   
|   
|   
  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
  
|   
|   
|   
|   
|   
|   
|   
|   
|   
  
Station Name|   
|   
|   
|   
|   
|   
|   
|   
|   
  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
(blank)|   
|   
|   
| (auto)|   
| (auto)| (auto)| (auto)| (auto)  
  
|   
|   
|   
|   
|   
|   
|   
|   
|   
  
Etc.|   
|   
|   
|   
|   
|   
|   
|   
|   
  
  
|   
|   
|   
|   
|   
|   
|   
|   
|   
  
  
|   
|   
|   
|   
|   
|   
|   
|   
|   
  
  
  


The invoice numbers would be manually entered.

  


The hours worked will automatically exclude production break times.

  


The Total Previous Worked Hours (total man hours) and Previous Work Dates would auto-fill with data from previous work that was done on the building. This would help to ensure that information doesn't get double-entered.

  


The Total Building Hours includes all man hours spent across all stations.

  


Assist will warn if the building had already been completed as of the specified date.

  


Development Specification

Report

Editable Report for time entry if we are entering by station.

  * The report should do a FillRGFromPipeList to append 10 blank rows for each station. Something like:



FillRGFromPipeList(

      Concat( "|",

          ConcatRGAdvanced(  CompanyProdTimeStation, true { KeepBlanks} ),

           ConcatRG( CompanyStations, ListSubstitute(NumericPipeList(1,10), CompanyStation))

)

  * Create a ProductionTimeEntryBlankRows system switch that is set to 10 (replace the  NumericPipeList 10 above with this switch).
  * The report is grouped by Station.
  * HoursWorked is CompanyProdTimeHours
  * PreviousWorkedHours is CompanyProdTimePrevHours -- see below.
  * PreviousWorkedDates is CompanyProdTimePrevDates -- see below.



  


Most of the behavior should already have been coded in the RG in the detail screen. The report should basically just work, but test that this works smoothly. Bring in Nahian or Ellis if you encounter confusing behavior.

  


Bid: 12 hours

  


PrevHours Macros

CompanyProdTimePrevHours and PrevDates is evaluated on the current Company record so that we see modified RG data. Bring Ellis in if this is not clear.

  


Pseudo-code:

{ returns a pipe list if previous hours worked or dates }

CompanyProdTimePrevHoursOrDate( vInvoiceNumber, vDate, vStartTime, vReturnHours)

  


Assign vBaseDateTime = DateTimeSortString(  vDate, vStartTime);

Assign vPrevFromBuilding =

LookupLevelField( BuildingRecordFromInvoiceNumber

     ConcatRG( BuildingProdTime, 

Assign vThisDateTime = DateTimeSortString(BuildingProdDate, BuildingProdStartTime);

if ( vThisDateTime < vBaseDateTime, 

if (vReturnHours, String(BuildingProdTotalHours), DateSortString( BuildingProdDate), NA));

Assign vPrevFromRG = 

ConcatRG( 

CompanyProdTimeDate, 

Assign vThisDateTime = DateTimeSortString( CompanyProdTimeDate, CompanyProdStartTimeVal);

if ( CompanyProdInvoice# = vInvoiceNumber AND

     vThisDateTime < vBaseDateTime,

   , if (vReturnHours, 

      String(CompanyProdTimeHours), DateSortString(CompanyProdTimeDate))

, '')

     );

  


Concat("|", vPrevFromBuilding, vPrevFromRG)

  


CompanyProdTimePrevHours will call HoursOrDate(true) and do a SumPipeList on the returned list.

  


CompanyProdTimePrevHours will call HoursOrDate(false) and do a SortPipeList, then use:

PipeListSubstitute( vList, DateFormatString( DateValue( ListSubstituteItem, "MM/DD"), ", ")

This should give you something like:

10/25, 10/28, 10/31

  


Bid: 8 hours
