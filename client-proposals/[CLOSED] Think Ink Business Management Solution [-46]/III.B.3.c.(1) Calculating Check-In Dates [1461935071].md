3.2.3.3.1. Calculating Check-In Dates

To calculate the Last Check-In Date: The Solution will find the latest closed date of all closed Check-In Incidents for the Contact.

  


To calculate the Next Check-In Date: The Solution will use the Contact's Check-in Start Date for the first Check-In, and after that will do the following:

  * If there are any open Check-In Incidents for a Contact, simply look at the earliest Check-In Date.
  * If there are closed (but no open) Check-In Incidents for a Contact, calculate the next Check-In Date based on the Contact's Check-In Frequency and the Closed Date of the most recently closed Check-In Incident.
  * If no Check-In Incidents exist for a Contact, calculate the next Check-In Date based on the Contact's Check-In Frequency and the Contact's Check-In Start Date.
  * When creating a new Check-In Incident from an existing Check-In, the new Check-In Date would be calculated based on today's date and the Contact's Check-In Frequency. This assumes that the existing Check-In Incident normally will be closed the same day.


