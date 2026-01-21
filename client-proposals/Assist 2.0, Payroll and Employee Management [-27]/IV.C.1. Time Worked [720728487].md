4.3.1. Time Worked

  


Requirements

This would automatically populate to:

Day| Start| -| End| Duration| Notes| Reference| Non Prod Hours  
---|---|---|---|---|---|---|---  
Monday| 0:00|   
| 0:00| 0:00|   
|   
|   
  
Tuesday| 0:00|   
| 0:00| 0:00|   
|   
|   
  
Wednesday| 0:00|   
| 0:00| 0:00|   
|   
|   
  
Thursday| 0:00|   
| 0:00| 0:00|   
|   
|   
  
Friday| 0:00|   
| 0:00| 0:00|   
|   
|   
  
Saturday| 0:00|   
| 0:00| 0:00|   
|   
|   
  
  
  


For quick entry, leave the Start time at 0:00 and set the End time to the duration (total time for the entry/day). If more accurate times are required, simply enter the start and end times, allowing the duration to automatically calculate.

  


The duration will automatically exclude any clocked in times that overlap with break times (see Break Times section below).

  


If a day has multiple entries, click the Add button to add another row for that day.

  


Assist will not automatically populate the time worked for salaried employees and employees without hourly equivalents. It will warn against entering time for salaried employees without an hourly equivalent.

  


Development Specification

Overriding Module

This requires the following changes to the provided Time Cards module:

  * Reverse the sort order of the Time Worked RG to match the time card. ConfigTimeCards_AscendingTimeSlots boolean system switch. Change the sort order to respect this. Test that time cards work well in both directions. Consider just hiding the PunchedIn checkbox if Ascending.
  * Change the weekday to default to blank instead of the current weekday, and the start time to midnight instead of the current time. This allows easily adding new entries for days that have multiple entries.  Create macros in the base catalog that we override in ZFP: ConfigTimeCards_DefaultWeekday expression of list weekdays. In base catalog, we define it with a CurrentWeekDayStr. ConfigTimeCards_DefaultStartTime expression of int -- in base catalog is set to to CurrentTimeNoSecond. ConfigTimeCards_DefaultEndTime expression -- default to NA in base and 0 in this catalog.



  


Bid: 12 hours in case of fallout

  


Auto-populating x30 import

We will have a "Std Populate Time Cards.x30" that creates time cards for all active employees (type is Employee, ContactIsActive). The x30 has an ask prompt for the target time card date (default to start of week for Today).  Only create them if they are missing.

  


For hourly employees, create a row per day for Monday to Saturday. Don't create any rows if there are already rows present. Can use a FillRGFromPipeList to fill in weekdays. The times will autopopulate.

  


Josh will manually set up a scheduled task to run this each week.

  


Bid: 4 hours.
