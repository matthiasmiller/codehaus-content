9\. TODO_Josh (Feedback from Nic)

Niccolas Miller 12/23/2025: Questions for Josh:

App:

[X] All screens in the app have a Back/Cancel button except for the ready to print screen. It isn't necessary, but would be nice for consistency.

[X] Do we want a screen header for all screens similar to the "Print Delivery Ticket" header?

[X] The "H" in LoadHawk on the main screen should be capitalized.

  


Silverloom:

[ ] Pack record: Is is correct that the PO ID is the GW PO ID, not the buyer PO ID? If so, can I safely rename without breaking anything app-related? There only ID stored in the field in the test system is a GW PO ID.

[ ] Delivery Ticket Updated by Member Alert: Is this in the works? Did we decide to ditch it?

"ZGW will receive an alert in Silverloom when the member uploads a delivery ticket input/modifies a delivery ticket."

  


Niccolas Miller 01/07/2026: 

[ ] I removed a Choice Select button (r499441) from Std Delivery Tickets.r20 which was causing an "Invalid Button" error when the new record link action was used. You had added the choice select it in r493430. Please advise.

Josh Nisly 01/14/2026: Sounds fine.

  


Niccolas Miller 12/24/2025: I think we might need to clarify linking somewhat.

Linking as I understand it:

  * Packs linked to GW PO
  * Load Requests linked to Buyer PO
  * Delivery Tickets linked to GW PO (groupings 2-4 in app are Delivery Tickets)


