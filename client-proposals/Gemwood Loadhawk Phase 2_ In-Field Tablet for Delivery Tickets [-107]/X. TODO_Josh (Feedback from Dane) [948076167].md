10\. TODO_Josh (Feedback from Dane)

Silverloom

[Workflow] Buyer PO/Load Request Linking Change:

[ ] We need to be able to “apply” a PO to a load request.  Right now it appears that the only way to connect a load request to a PO is to create a PO from the load request.

Josh Nisly 01/14/2026: They just close the load request out.

  


[Workflow] Load Request Generation (from GW PO, not Buyer PO):

[ ] Also, if we can create a load request from an existing GW PO with an option to connect it to .  When we assign a PO, it should show up in the app.

Josh Nisly 01/14/2026: I don't fully understand this. Let's leave it for now.

  


App

[Workflow] Support Generating Packs Outside of Load Requests/Delivery Tickets:

[ ] The mill needs to be able to add packs without a load request (pack inventory).  So can we have a Packs grouping above Load requests that is something like “Packs” or “inventory” that can be filled out with packs based on thickness, species, grade with bf entered by the operator.  The “packs” grouping should be only packs that aren’t assigned to a Load or PO.

[ ] In the load request card, the mill can either add a pack like it is now or select from the packs already in the packs grouping.

Josh Nisly 01/14/2026: "Unallocated packs". Separate view.

  


Grouping Change (Open Load Requests linked to POs):

[ ] The Load request with PO’s can stay in the “load request” grouping, once it has a PO, the card will need some PO info on the card (customer name – maybe PO# if there is room).  The Load requests without PO’s can be as they are not (with bf applied added).

Josh Nisly 01/14/2026: I think that they didn't realize that you have close the Load Request out when creating a PO manually.

  


Minor - UX:

[X] On the pack screen when you hit + and it takes you to the pack “pack tally” screen, if it could automatically bring up the number pad for entering the bf, I think that would be helpful.

[X] On the home screen on the Load Requests card, the total bf requested is showing.  Can we replace that with the total bf already entered?  We do not need to show the amount of bf requested because it is a truckload

  


  


Question for Packs:

[ ] So when / how do we move packs from “load Request” to “PO’s” in the app?

Josh Nisly 01/14/2026: For now, you just manually select them over.

  


  


Josh Nisly 01/14/2026: 

[X] Wait to show the PO in the app until the email has been sent.

[X] Fix save errors: [https://testloadhawk.silverloom.io/Detail/View/2?RecordType=Save+Attempt&NumberID=698&](https://testloadhawk.silverloom.io/Detail/View/2?RecordType=Save+Attempt&NumberID=698&)

[ ] In pack selection screen, don't show packs that don't match by grade.

[ ] In Load Requests, turn "Internal Notes" into "Public Notes", and show in the app like we do for POs.

[ ] Once enough packs have been entered for a load request, turn it gray instead of blue.

[ ] Idea: make newly-selected pack pulse its background in the underlying list.

  


In pack selection screen, replace BFT with notes.

  


Talk to Ben about getting a printer set up for testing.

Immediately save packs when adding them via the load detail page.
