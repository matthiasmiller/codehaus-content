19.6. Improvements for Linking & Accessing Change Orders

  


Requirements

_VA: Tim Reitz 07/03/2025: Client wants to move forward with this for Phase 1.

  


  


The following feature could be added to facilitate easier access to linked Change Orders from their Source Proposal.

  


[ ] Estimated Cost: $150-300

_EM: Tim Reitz 07/03/2025: The link was actually already specced on the Proposal record, with details about a filtered report that it would open. So should we skip adding this $$ to the total price estimate? 

_VA Ellis Miller 07/03/2025: That's fine.

  


Initial Spec: 

  


[X] Part 1: Link on Proposal record:

  * View X Change Order(s) (link; with the following behaviors / details:
    * visible if "Proposal Type" ≠ "Change Order" and there is one or more "Change Order"-Type Proposals in the Solution that share the same "Numeric ID" \+ "Revision Suffix";
    * opens the "Change Orders for Proposal" report;
    * in place of "X", displays the number of corresponding Change Orders) 



  


[X] Part 2: "Change Orders for Proposal" report:

Overview: This is the All Proposals Report, filtered to display Change Orders for a single Proposal.

  


Accessed from:

  * "View X Change Orders" link on the Proposal record



  


The following filter(s) are set differently from the main report:

  * Source Proposal #: Defaulted to the record from which the report is opened
  * Proposal Type: Set to "Change Order"



  


Development Specification

Tim Reitz 06/26/2025: I don't remember if the client wanted a price on this one, but it's small enough that I think it would be worth giving a price while pricing the others.
