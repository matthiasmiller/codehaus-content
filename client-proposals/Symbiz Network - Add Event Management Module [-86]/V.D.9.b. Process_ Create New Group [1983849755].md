5.4.9.2. Process: Create New Group

  


Requirements

*Documented 

Tim Reitz 06/05/2025: This looks like a "User-Initiated" automatic process. 

  


Overview: This is a process used to a new Growth Ring Group record from a Launch Meeting, with fields defaulted.

  


Interfaced:

  * Via the "Create New Group" link on the Launch Meeting-type Event record.



  


Action(s): 

  * Creates a new Growth Ring Group record, with the following fields defaulted:
    * Growth Ring Group ID: Defaults to blank, but is required to save the new record 
    * Region: Sets to the Region set on the Info Meeting linked to the Launch Meeting 
    * Regional Rep: Sets based on the Region
    * Info Meeting: Sets to the Info Meeting ID for the Info Meeting linked to the Launch Meeting



  


Scheduled Task Command: N/A

  


Development Specification

Tim Reitz 11/18/2024: Note that this is an auto-push report, rather than an x30.
