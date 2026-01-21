1.5.2. Changes to Incident Record

  


Requirements

The following changes are to be made to Incident records as part of this customization: 

  


General changes: 

  


  * Add the following behavior(s): 
    * Disallow "grandchild" incidents (only parent and child incidents are needed)
    * New Child link (when creating a new child incident from this link, also default the Contact and Assignee from the parent incident; note that the original behavior only defaulted the parent incident, type, and workflow)



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1Hks1tTQjdnymInK23UzzDXrY3aRrCnxRkN9dUOnYjwo/edit#gid=569310505](https://docs.google.com/spreadsheets/d/1Hks1tTQjdnymInK23UzzDXrY3aRrCnxRkN9dUOnYjwo/edit#gid=569310505)

  


Config_IncidentNestingLimit -- List of 0, 1, and or blank. WIth description of "Maximum levels of incidents (if 0, no child incidents; if 1, child incidents cannot have children; if blank, unlimited levels of children)"

[ ] Warn on parent record if we have too many levels: "Child incidents are not supported: IN0000" or "Incidents cannot be a child of a child: IN0000"

[ ] Validation on child (error when attempting to set, warning if it happened previously). Could use same message

[ ] Test all combinations

Bid: 2 days

  


Change default incident behavior to always default Contact and Assignee for child jobs. If anyone complains we will add a switch.

Bid: 2 hour
