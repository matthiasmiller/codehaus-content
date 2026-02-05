8.5.4. Device Record - Traccar Device Details Section

  * Traccar Device Details section (this section displays details from Traccar about the linked Device):
    * Linked Traccar Device Sync Record (auto-set and read-only; sets to the "Unique ID" for the linked Traccar Device sync record; sets via __) 



TODO_VA (later): Tim Reitz 01/31/2026: Once we have the linking figured out. Presumably a triggered x30 that runs when the Device record is created. 

  * Traccar Connection Status (read-only macro; displays the "Traccar Connection Status" from the linked Traccar Device sync record, displaying items from the "Online / Offline" list) 
  * Last Connection (read-only macro; displays the most recent "Last Update" date & time from the linked Traccar Device sync record)
  * View Device in Traccar (link; opens the corresponding Device screen in Traccar)



DONE_JB (research): Tim Reitz 12/04/2025: can we do this? 

Tim Reitz 01/31/2026: For the linking & syncing process, I'm thinking something like the following (similar to what we're doing with Users): 

\- Set up Device record in Silverloom 

\- Triggered x30 runs on Save and creates the "Traccar Device" sync record 

\- Sync sets up the Device in Traccar 

\- Sync brings back the unique ID from Traccar and saves it on the Traccar Device sync record (or Silverloom / the WSGI keeps track of the next # in line, to save it when the Traccar Device sync record is created)

\- Hidden macro here on the main Device record to set the URL 

\- Same triggered x30 runs on Save here to update the linked Traccar Device sync record

Jonathan Bergen 02/02/2026: Hmm... I think that this should be the flow:

\- Set up Device record in Silverloom

\- Triggered x30 runs on Save and sets up the Device in Traccar

\- Sync brings back the details from the Device in Traccar and creates/updates the "Traccar Device" sync record

  


Reasoning: A one-way data flow simplifies everything. We can pass some kind of ID to the Device in Traccar when we set it up, something like a Silverloom ID, which will allow us to easily link the two back in Silverloom.

Note: It should be easy to have URL macros that link from Silverloom to things in Traccar.

  


TODO_VA (later): Tim Reitz 01/16/2026: Include any of the "Connections" fields from Traccar??
