1.5.3. Changes to Time Card Record

  


Requirements

The following changes are to be made to the Time Card record as part of this customization (blue font represents changes to existing design / implementation): 

  


  * Time Worked embedded spreadsheet: 
    * Svc. Run (custom for Good's Ag; located between "View" and "Notes"; drop list of Daily Service Run Numbers (#1 - #9); with the following behaviors: 
      * drop list is visible and editable for all Travel Time-type incidents and for all Work Order-type incidents where Service Location is not "Shop"; for other incidents, displays as blank and read-only; 
      * validation warning Save if empty: "Svc. Run must be specified for <Incident ID>."; 
      * for new rows where it is visible, the Service Run is intelligently defaulted to the most recently-used Service Run # for the current user's time card for the current day, or to "#1" for the first Service Run of the current day).
    * Travel Time (custom for Good's Ag; located at the far right; auto-set and read-only; time field; with the following behaviors: 
      * for Work Order-type incidents with a Service Run selected and have travel time allocated to them: displays the amount of time from the corresponding Svc. Run allocated to this row (total amount of tracked time on the Travel Time incident for the Service Run divided by the number of Work Order incidents for the Service Run); if a Work Order has multiple time slots with the same Service Run, this travel time is displayed on the first entry, and the rest are blank; 
      * for all other incidents: displays as blank) 



  


  * Footnote in black italicized text below the Time Worked embedded spreadsheet to explain the Billing Time field for the selected Time Worked row:
    * If the selected row is for a Travel Time-type incident: "Tracked time: <H:MM>. Total travel time of <H:MM> for Svc. Run #<X> is divided between <Y> work orders."
    * If the selected row is for a non-Shop Work Order-type incident: "Tracked time: <H:MM>. Travel time: <H:MM> (Svc. Run #<X>)."
      * If the incident has multiple time slots for the same Service Run, also includes the following: "For incidents with multiple time slots on the same Service Run, the travel time is included in the earliest time slot."



  


  * Additional Validations: 
    * Error on the ID field if a user tries to track time on an incident with the Billed checkbox checked: "This incident already has been billed, so time can no longer be tracked on it. Please create a new incident."



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1Hks1tTQjdnymInK23UzzDXrY3aRrCnxRkN9dUOnYjwo/edit#gid=398750334](https://docs.google.com/spreadsheets/d/1Hks1tTQjdnymInK23UzzDXrY3aRrCnxRkN9dUOnYjwo/edit#gid=398750334)

  


NOTE: We intentionally leave the stored number populated so that if the Service Location is modified after time slots are added, we automatically have a reasonable default for the Svc Run.

  


Ellis Miller 11/01/2023:

[ ] Use a hidden TimeSlotStoredSvcRun that is initialized OnInit for a new row by looking at the most recent TimeSlotSvcRun for today or 1 if not available

[ ] Add a visible TImeSlotSvcRun macro that returns the stored macro if TimeSlotUsesSvcRun

[ ] Add a macro TimeSlotUsesSvcRun evals IncidentIsTravelTime OR IncidentIsNonShopWorkOrder

[ ] Add a macro IncidentIsTravelTime -- returns true if Incident Type is "Travel Time" 

[ ] Add a macro IncidentIsNonShopWorkOrder -- Type is "Work Order" AND service location is not Shop.

[ ] Add the warning

8 hours

  


Before Coding: Discuss approach with Matthias

  


We 

  * ZFP overrides CustomTimeCards_SlotHours to dynamically calculate hours.
  * TimeCardCategoryTotalMins doesn't respect this calculation since it uses the time stored in the NdxKey
  * Here we need to decide how we handle that. We could potentially store the adjusted time on the time card. This will allow TimeCardCategoryTotalMins to be fast and accurate. I don't know if this will work for ZFP. We could add a switch to specify whether to store the time on the NdxKey. If we don't store it there, then we'd have to calculate it each time (tricky and slow -- esp since we have an RG-row specific NdxKey, but we don't even know which RG row to access to calculate the time).
  * Consider how this is billed for ZFP vs ZGA. 



  


[ ] Consider changing the Duration to always show the actual duration and conditionally show an Adj Time that shows the adjusted time (based on Config_TimeCardShowCalcHoursOverride. Perhaps only if it is different from Duration?

  


[ ] Override CustomTimeCards_SlotHours to spread the time correctly:

  * If we have a service run, count the number of incidents for this service run. Count the total travel time for this svc run.
  * If there are no incidents, the time does not get spread.
  * Otherwise the time gets spread by the # of incidents. Any rounding goes to the first or last incident. 
  * Note if there are multiple entries for the same incident for the same day, only the first one gets the extra minutes.



[ ] TimeCardCategoryTotalMins needs to be changed to reflect the right time (and it just became slower).

Ellis + Nahian (4? hours). Bill as 2 days.

  


Fear, Uncertainty, Doubt. 

Example: The billable hours macro is currently not respecting Custom_TimeCardsSlotHours. This is because we are trying to extract time from the time card. We will have to change 

2 Days.

  


[ ] Add formatted footnote. Add Custom_TimeCardsDtlSlotFootnote

2 hours
