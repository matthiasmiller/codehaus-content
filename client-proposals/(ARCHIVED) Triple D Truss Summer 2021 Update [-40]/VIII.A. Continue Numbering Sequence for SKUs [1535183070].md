8.1. Continue Numbering Sequence for SKUs

  


Requirements

It would be nice to have a way to continue the numbering sequence we set up for Lumber and Metal SKUs to avoid manually checking every time a new SKU is created.

  * Make the change to find the last SKU number for the corresponding category and use the next number for the SKU being created.



  


Time Estimate: 1/2 day

  


Development Specification

From [[[IN4589](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-4591&)]] - ZTD - Misc Items: 

Continue Numbering Sequence for SKUs: This is not specifically from deployment, but is there a way to continue the numbering sequence we set up for Lumber and Metal SKUs so they don't have to manually check every time they create a new SKU? 

Tim Reitz 04/23/2021: I think this was a question from the client. 

Tim Reitz 04/23/2021: Design question for CCI: 

From Matthias: Dev Spec - Can we find everything RightOf("-"), remove dashes, convert to a number....then create an index of SKUs based on category and autonumber? Then, add a Generate Unique Sku button that converts the category to uppercase, finds the next autonumber, and formats it as CATEGORY-000-000

Ellis Miller 06/11/2021: Yes, included in subscription.

Tim Reitz 06/29/2021: Design from Ellis: OnChange button visible if category is set. Use list substitute to find the highest number for that category (RemovePrefix, remove hyphens, call Value). Add one to get the next one. 

Estimate: 4 hours.
