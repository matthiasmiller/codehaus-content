4.5. (New) Time Card Record

  


Requirements

TODO_IDD: Tim Reitz 01/21/2026: I think we'll want to put together a Snippet for the standard Time Card records (time for speccing that out maybe would be tracked separately from this IDD time). Then we can use that Snippet for this. 

  


  


_HLD: Tim Reitz 12/03/2025: Could we have a high-level description of how lat & long are set?

TODO_IDD: Matthias Miller 12/03/2025: Hidden fields set in the WSGI

  


TODO_IDD: Tim Reitz 12/11/2025: Would this include time off requests / tracking? (And if yes, would that integrate with the Calendar Events for days off?)

  


This uses the standard Silverloom Time Cards feature, with customizations. This is the digital replacement for paper time cards, capturing who worked, on which job, for how long, and (for prevailing wage jobs) what type of labor they performed.

  


Customizations include: 

  * Entries
    * Shop Time Category (list of Shop Time Categories)
      * NOTE: Shop Time and Job ID are mutually exclusive.
    * Job ID
    * Crew (editable if Job ID is set)
    * Prevailing Wage List (editable of Job ID is prevailing wage)
    * Approved by Foreman (checkbox)
      * This locks the entry once the foreman has reviewed it, so employees can't make changes after approval and payroll has a clean handoff.
    * Latitude (number; 6 decimals)
    * Longitude (number; 6 decimals) 
      * This captures the device location at clock-in, giving you a simple verification layer if questions ever come up about where someone was.



  


NOTE: Overtime rate calculates based on actual entries passing 40 hours for a week.

  


\------------------

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1908881419#gid=1908881419](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1908881419#gid=1908881419)

TODO_VA: Tim Reitz 12/04/2025: Let's add this if we have a mockup for our standard Time Card screen. If we don't, touch base with me and we can determine whether it's worth mocking up. 

Austin Priest 12/09/2025: There is a mockup of the standard time card, And I added the customizations but I think we might need to do some more work on this mockup. You can take a look.
