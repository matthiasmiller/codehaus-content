7.1. Renew All Vehicles Prompt Screen

  


Requirements

*Done. 

  


Overview: This is a prompt screen that allows an Admin user to initiate the "Renew All Vehicles" automatic process, to renew Coverages for all selected Vehicles, or if none are specified, all active Vehicles.

  


Accessed from: Admin | Renewals and Printing | Renew All Vehicles

  


Filters / prompts:

  * Renew for Period Start Date: July 1, <current calendar year> 



_CCI1: Tim Reitz 08/12/2025: Is this correct that it always displays July 1 of the current calendar year?

Murshid Rahman 08/18/2025: Yes, that is correct. This is July 1 of current year. 

_CCI1: Tim Reitz 08/12/2025: Is this date actually used in the import in any way, or is it simply included as a point of reference for the user?

Murshid Rahman 08/18/2025: We do not renew a coverage if its already renewed. 

With this date, we look for coverages within current period start date and current period end date and then we renew if no coverages were found. Please let us know if this is confusing. Thanks.

TODO_VA: Tim Reitz 09/02/2025: Follow up. 

  * Vehicle(s) (Blank=All) (multi-select list of active Vehicles, displayed in the following format: "<Vehicle Owner Display Name> <Vehicle Year> <Vehicle Make> <Vehicle Model> <Vehicle VIN/Serial 3>"; defaults to blank/none = all) 



  


Informational label below the prompts: 

"Clicking Continue will renew the selected vehicle(s) that have not been renewed already

or that do not have a Deactivation Date before the above Period Start Date."

  


Button: 

  * Run Import (clicking this button initiates the "Renew All Vehicles" automatic process based on the prompt(s) -- see corresponding automatic process spec) 



  


Menu Visibility: Admin

  


Development Specification

TODO_VA: Write up a CR to change the "Run Import" button to something more user-friendly? Probably "Confirm" or "Run Renewal Process" or something like that (Also update the wording of the informational label to match -- currently that says "Continue".)
