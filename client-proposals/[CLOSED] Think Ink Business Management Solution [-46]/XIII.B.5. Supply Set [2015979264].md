13.2.5. Supply Set

4TODO_EM: Tim Reitz 07/20/2023: The client would like to eventually build out a list of sales items (ink, toner, replacement parts, etc.) for each model. They would use this for promotion (sending reorder forms to customers with active printers of the given model) and for internal use (techs doing repairs, etc.). Currently calling these "Supply Sets". This is on a per-Model basis. There is a different sub-set for Managed vs. Customer-Owned (example: a feed roller should show up for a tech but not for a customer) - maybe have a "customer item" tag on the supply item.

Long term, they would like this to allow them to intelligently determine what other supplies that a Customer-Owned customer might be interested in based on another purchase (i.e. the customer bought this black toner for a printer that we didn't know they have; the solution will look at what supply set that item belongs to and we'll send them a reorder form with that supply set).

TODO_IDD: Tim Reitz 07/20/2023: Add "Supply Sets" to a future phase. Ideas:

\- Maybe an RG on the Model

\- A custom "Configure Supply Set" record type, with a "Supply Set" drop list on the Model to link (this is probably the way to go, so that they don't have to set up the same list for multiple models, etc.)

  


Maybe a supply set RG on both the Model and the supplies, and having the SS record be the link between them. 

Or maybe store all the supplies on an RG on the SS record.

  


  


4TODO_IDD: Tim Reitz 08/03/2023: Where should the system look to generate the reorder forms? The customer's Device records or the customer's invoice line items?

  


4TODO_IDD: Tim Reitz 09/19/2023: 

[ ] Supply Sets are specific to 1 model each (but there is overlap for specific items) 

[ ] fields for Supply items: 

  * Customer item vs. TI item
  * Other columns from Jesse's pricing spreadsheet that he showed us on the call today? (colo, yield, etc.)?


