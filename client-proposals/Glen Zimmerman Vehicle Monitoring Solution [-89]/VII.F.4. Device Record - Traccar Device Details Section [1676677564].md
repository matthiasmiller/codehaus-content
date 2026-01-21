7.6.4. Device Record - Traccar Device Details Section

  * Traccar Device Details section (this section displays details from Traccar about the linked Device):
    * Traccar Connection Status (read-only macro; displays the most recent "Status" from Traccar, displaying items from the "Online / Offline" list) 



TODO_JB: Tim Reitz 01/13/2026: Sync point from Traccar. Thoughts on how this would work? How frequently it would update?

  * Last Connection (read-only macro; displays the most recent "Last Update" date & time from Traccar)
  * View Device in Traccar (link; opens the corresponding Device screen in Traccar)



TODO_JB: Tim Reitz 12/04/2025: can we do this? 

Tim Reitz 01/16/2026: I'm thinking something like the following: 

\- Set up Device record in Silverloom 

\- x30 creates the "Traccar Device" sync record 

\- Sync sets up the Device in Traccar 

\- Sync brings back the Device record # from Traccar and saves it on the "Traccar Device sync record (or Silverloom / the WSGI keeps track of the next # in line, to save it when the Traccar Device sync record is created)

\- Hidden macro on the Silverloom Device record to set the URL 

  


TODO_VA: Tim Reitz 01/16/2026: Include any of the "Connections" fields from Traccar??
