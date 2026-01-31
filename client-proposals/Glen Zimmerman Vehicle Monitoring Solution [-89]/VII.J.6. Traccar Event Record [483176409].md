7.10.6. Traccar Event Record

  


Requirements

Overview: This is a custom record type, used to store information about "Events" from Traccar. This is a special "sync record", with certain details set via the sync with Traccar (not editable interactively in Silverloom), and other details editable interactively in Silverloom (but not synced back to Traccar).

  


Accessed via: 

  * The "Traccar Events" report(s) 
  * "Device Events" embedded spreadsheet on Device records 



  


Sections and Fields: 

  * Traccar Event Details section (all fields in this section are set from Traccar): 
    * Traccar Event ID (auto-set and read-only interactively; number; no decimals; corresponds to the "ID" in Traccar)
    * Event Type (auto-set and read-only interactively; plain text field; corresponds to the "Type" in Traccar)
    * Traccar Event Time (auto-set and read-only interactively; UTC date & time in the ISO 8601 format (i.e. "2019-08-24T14:15:22Z"); corresponds to the "Event Time" in Traccar)
    * Event Time Zone (auto-set and read-only; __



TODO_JB (research): Tim Reitz 10/25/2025: I think we'd have to look at the Event location (Position ID?) to determine this. 

  * Event Date (read-only macro; displays the date from the "Traccar Event Time" field, in the "MM/DD/YYYY" format, based on the "Traccar Event Time" and the "Event Time Zone") 
  * Event Time (read-only macro; displays the date from the "Traccar Event Time" field, in the "HH:MM:SS AM/PM" format, based on the "Traccar Event Time" and the "Event Time Zone")
  * Traccar Device ID (auto-set and read-only interactively; number; no decimals; corresponds to the "Device ID" in Traccar)
  * Traccar Position ID (auto-set and read-only interactively; number; no decimals; corresponds to the "Position ID" in Traccar; link to the corresponding Traccar Position Record in Silverloom) 
  * Traccar Coordinates (auto-set and read-only interactively; number; no decimals; corresponds to the __ in Traccar) 



TODO_JB (research): Tim Reitz 01/27/2026: Is there something like this on the Event, or is it derived from a linked Position? (I'm seeing an option in the left-hand column of Events report in Traccar: ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAfCAYAAACh+E5kAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAOLSURBVFhH7ZdLSyNNFIafxCtGQ0AxXiKSiIyKRIUoKIKooIKCuhd006Au3PsfslaIURdu48KNuhMvKN5QIgZcxAhBRMVbq1nEmJ5N0nT6m/kgncwMgs+q6PPWod46VadoXTgclvjC6NUfvhrfBv413wZ+xdLSEtPT09zc3KhDaSftBl5eXgiFQgDc398TiUTUkrSiS0cbjUaj7OzssL+/z+PjY0IsIyOD+vp6urq6KC4uToilg5QNiKLIwsICt7e38reCggIKCgq4vb3l8/MTAL1ez9DQEM3NzYrZqZOSgdfXV2ZmZnh+fsZsNtPZ2Ul1dTV5eXkQq8zNzQ2Hh4ccHBwgSRLDw8O0tLSoU2lGswFJkpidnSUYDGKxWBAEgezsbLVM5ujoiOXlZXQ6HZOTk1gsFrVEE5ov8enpKcFgEKPRyNjYmLx4URQ5Pj5ma2sLv98v6x0OB+3t7UiSxOrqqiJTamg2sLu7C8Dg4CAGgwEAr9eL0+nE4/GwtraG2+1mbm5O7kS9vb2YTCYCgQB3d3cJ+bSiyUAkEuH6+hqDwUBtbS3Edt7j8fDx8ZGgvby8ZGNjA4DMzEwaGxsBuLi4SNBpJSkD4XAYl8uFy+VCkiRKS0vR6XQA+P3+/yw+ztnZmTyurKwEYHt7G5fLxd7enkKZPEkZ+Pz8JBAIEAwGIdbj47y/vyuUiby9vcnj+HF7fX0lEAjw8PCgUCZPUgZycnIQBIHR0VEAnp6e5Fh5eblCmYgyFn/o7HY7giDQ2tqqUCZPUgb0ej02m42amhqMRiN3d3c8Pz8DYLVaqaqqUk8BoKenRx7Hz/6PHz+w2WwUFhYqlMmTlAElDQ0NoOhGACMjI7S2tmIymcjOzsZqtTI+Pk5FRQXELrrX6yUrK4u6ujp5XipofshEUcTpdCJJEhMTE5SVlaklCUiSxPz8PH6/n46ODvr6+tQSTWiugNFoZGBggEgkgtvt5vz8XC2REUWRxcVF/H4/JSUldHV1qSWa0VyBOJubm6yvrwNgNptpa2ujqKgIgI+PD05OTjg7OyMajVJcXIwgCOTn56uyaCdlA8Re4JWVFfk/4Fc4HA76+/vJzc1Vh1IiLQaI7bbX6+Xq6gqfz0coFMJms2G1Wmlqakq52/yOtBlQsrS0hM/nY2pqitLSUnU4rWi+xP+H3W6nu7s7rWf9d/yRCvxN/kgF/ibfBv41X97ATzyrayuRh5pKAAAAAElFTkSuQmCC) (see [https://x6rildfvs.traccar.com/reports/event](https://x6rildfvs.traccar.com/reports/event)) 

  * Google Maps (link; opens the location of "Coordinates" in Google Maps) 
  * Apple Maps (link; opens the location of "Coordinates" in Apple Maps)
  * Traccar Geofence ID (auto-set and read-only interactively; number; no decimals; corresponds to the "Geofence ID" in Traccar; link to the corresponding Traccar Geofence Record in Silverloom; note that this is not in use for Phase 1)
  * Traccar Attributes (auto-set and read-only interactively; __ field; corresponds to the __ in Traccar)



TODO_VA (later): Tim Reitz 01/27/2026: Spec once we have info on the User attributes from JB.

  


  


  * <Service Name> Details section (some fields in this section are editable interactively, allowing Upline Providers to make "override" notes) : 
    * Device Description (auto-set and read-only; defaults to the "Device Description" for the Device record matching the "Traccar Device ID", when this record is created) 
    * Device Account (auto-set and read-only; defaults to the "Account #" of the current "Account" on the corresponding Device record when this record is created)
    * Stored Device Primary Driver (hidden; auto-set and read-only; defaults to the "Contact ID" of the "Primary Driver" on the corresponding Device record when this record is created) 
    * Device Primary Driver (read-only macro; displays the current "Display Name" of the "Stored Device Primary Driver") 
    * Override Driver (optional; plain text field; for a user to type in another name if another person was reported as driving the vehicle at the time of the Event) 
    * Override Driver Notes (optional; plain text field; for the user to document additional notes related to "Override Driver") 
    * Device Primary Vehicle (auto-set and read-only; defaults to the "Vehicle Description" of the "Primary Vehicle" on the corresponding Device record when this record is created)   
    * Owner at Time Event (auto-set and read-only; defaults to the "Display Name" of the "Current Owner" when this record is created) 
    * Override Vehicle (optional; plain text field; for a user to type in another VIN if another vehicle was reported as having the Device at the time of the Event) 
    * Override Vehicle Notes (optional; plain text field; for the user to document additional notes related to "Override Vehicle") 



  


  


  * Record History section (visible only to "Upline Provider Roles" for the linked "Account"): 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (visible only to users with the "Full Access" Permission; link to open the report for the record) 



  


  


Data Access: 

  * Visibility: Visible to all users. 
  * Editability: Editable for "Upline Provider Roles" users of the linked Account. 



TODO_GZ: Tim Reitz 01/15/2026: Visibility: Is it fine for all providers to see all Events in Silverloom? Or should we limit it to only uplines?

If we limit to only uplines, we would need to determine how to limit it: Based on Device / Account / Driver?

  


Special Considerations:

  * Copy Record: Disallowed
  * Delete Record: Disallowed
  * Merge Record: Disallowed



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=260329509#gid=260329509](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=260329509#gid=260329509)

  


  


  


TODO_: How to specify the speed limit?

Tim Reitz 07/23/2025: I'm assuming this would be for the "Speed limit exceeded"-type Event

Tim Reitz 01/14/2026: This probably should be deferred to a "Possible Future Item", rather than include the complexity here?? Unless it's simple. 

TODO_BR: Tim Reitz 01/14/2026: Once the devices are up and running, how does the "Speed limit exceeded" Event work in Traccar?
