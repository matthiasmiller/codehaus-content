7.1.10. Event Type Record

  


Requirements

Overview: Event Types are configured on this configuration record and viewed on a Event Types report. They are used to specify the type for Event records, and to determine certain fields that are conditionally visible on the Event record based on the Type.

  


Due to the various things that depend on these Event Types, the records are fully read-only / uneditable in the Solution; any changes require coding work by CCI. 

  


The following Event Types are included ("shipped") in the Solution (see the corresponding sections of the spec for details regarding how fields should be set for each one):

  * Annual Summit
  * Industry Forum 
  * Info Meeting 
  * Launch Meeting



  


Accessed via: "View Event Types" report

  


Sections and Fields: 

  * Active (checkbox)
  * Event Type Name (required; plain text)
  * Default Event Visibility (optional, drop list of Event Visibility list items; the item selected here is set on Event records when the corresponding Event Type is selected)
  * Requires Food Notes if Scheduled (checkbox; if checked, Events of this Type require an entry in the "Food Notes" field if "Event Status" = "Scheduled" unless the Event's "Event Format" = "Virtual") 
  * Always Requires Registration Deadline (checkbox; if checked, Events of this Type require an entry in the "Registration Deadline" field from creation, rather than the default -- see corresponding section of the spec)
  * Displays Region & Rep (checkbox; if checked, Events of this Type display the "Region" and "Regional Rep" fields)



  


Data Access: See the Data Access Controls section of the proposal for details. 

  


Special Considerations: 

  * Copy Record: N/A
  * Delete Record: Prevent deletion "This is not editable."
  * Merge Record: N/A



  


Other Notes:

  * Note that the sequence of these Types should be static and lists / instances of these names should always appear in this sequence.
    * Note that currently the desired sequence is the same as alphabetical order, so no special coding is needed to handle this at this point. If other Types are desired in the future, a Sort Order field could be added to accommodate proper sorting.
  * Note that adding additional Event Types requires consideration of which sections & fields should be visible (or added), as well as other changes that might be required to reports, printouts, etc.



  


Development Specification

Change Requests:

  * Tim Reitz 06/04/2025: Added in [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Add Events Feature (Info Meetings, etc.)


