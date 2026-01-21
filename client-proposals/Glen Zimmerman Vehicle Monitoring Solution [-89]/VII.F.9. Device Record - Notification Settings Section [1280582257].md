7.6.9. Device Record - Notification Settings Section

TODO_VA: Tim Reitz 09/12/2025: I think we need to work more on the Notifications themselves before going too far here. 

Tim Reitz 11/20/2025: It looks like Traccar has configuration options for: 

[ ] Notification records 

[ ] Notifications linked to Devices (in "Connections") 

[ ] Notifications linked to Users (in "Connections") 

  


TODO_: Tim Reitz 12/04/2025: Maybe two sections for SIlverloom and Traccar? 

Tim Reitz 12/08/2025: Or maybe just Traccar, since Silverloom notifications will be pre-determined as emails. 

But are the alerts in Traccar defined on the Device or the Account or the User? 

  


TODO_: Tim Reitz 09/12/2025: Alerts are a big (important) piece. Alerts can be customized on a per-device basis: i.e., "for this Device, what alerts are received by what users and in what method".

Some (i.e. vehicle maintenance, etc.) are optional, but some are mandatory. 

  


  * Notification Settings section:
    * Device Notification Settings (__
      * User (list of all administrators and users associated with the linked Account)



TODO_: define these roles more.

  * Phone (read-only)
  * Email (read-only)
  * Critical (text or email; blank = none)
  * Warning (text or email; blank = none)
  * Information (text or email; blank = none)



TODO_EM : Tim Reitz 09/12/2025: We need to think through this -- it looks like the idea here was for the user to be able to specify which level of urgency they want to assign to each alert. 

TODO_: Tim Reitz 07/24/2025: There must be an alert for at least the Account Manager.
