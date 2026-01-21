7.5.1. Changes to Calculating Check-In Dates/Months for Phase 3a

  


Requirements

The Solution uses the following to automatically calculate check-in dates/months: 

  


Check-In Date: With the switch to scheduling check-ins by month, the Solution no longer scheduled a specific date for a check-in. However, the user can use the incident's standard "Due Date" field to specify a target date to do the check-in. Also, as already mentioned, the Solution continues to look at the Incident Closed Date as the official Check-In Date. 

  


To calculate the Last Check-In Month: The Solution will find the Month + Year of the latest Closed date of all closed Check-In Incidents for the Contact.

  


To calculate the Next Check-In Month: The Solution will use the Next Check-In Month from the Contact's linked Region.

  * When creating a new Check-In Incident from an existing Check-In, the new Scheduled Check-In Month would be calculated based on the following "Month" row in the Region's "Future Check-Ins" embedded spreadsheet.



  


Handling unusual situations: There are some uncommon scenarios that the Solution needs to be able to handle: 

  * Off-schedule Check-ins: If an extra check-in happens in between scheduled check-ins, the Solution should simply continue to bring up check-ins on the established schedule and not regard off-schedule / extra check-ins. 
  * Late Check-Ins: If a check-in is completed later than planned (i.e. after the Scheduled Check-In Month), or is not closed until soon before the next scheduled check-in, it can be caught by the user via the "Recent Check-In" column on the Customers Needing Check-Ins report. The user can then decide whether to do another check-in right away or to wait.
  * Canceled Check-Ins: If the user simply closes the Check-In, it will be counted as a check-in in the system. If the user doesn't want to count it as a check-in, they can do one of the following: 
    * Change the Incident Type to something more generic (perhaps "Internal") and close out the incident (note that the Incident Type is required, so the user cannot simply set the Type to blank). 
    * Delete the incident.



  


Development Specification

Tim Reitz 08/16/2023: Adapted from [[[IN8276](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8278&)]] - ZTK - Incidents - Changes to Check-In Calculations

  


  


Last Check-In Date: ContactLastCheckInDate is already coded. Can add ContactLastCheckInMOnth

  


Create a RegionGetNextCheckInDate( vDate) that goes through the next check-ins list and returns the first date value that is greater than vDate. ListSubstitute to get all future ones and take first future one.

  


BId: 1 day, possibly with cleanup
