4\. Workflow: Processing

  


Requirements

We will have reports available to make it easy to schedule processing. This report is grouped first by calendar week, then by order date, then finally by item type. For easy reading, the totals should be at the top of each grouping. The columns will include:

  * Item Type
  * Item Description
  * Unprocessed Weight
  * Last Processed Date



  


We will also have a kiosk where the meat is processed. The kiosk will:

  * Prompt for the order number
  * Confirm to mark it as processed. It will save a processed date, indicating that the entire order has been processed.



  


Development Specification

Matthias Miller 05/29/2019: Kiosk can show up either as different color or as packaged. Ellis Miller 06/10/2019: I don't understand.

Matthias Miller 06/10/2019: I don't either. I'll have to ask ... ??  

Matthias Miller 06/10/2019: My thoughts:

  * Show giant input for order #
  * When you enter in, it takes you to the correct tab based on workflow, but allows you to switch to a different tab if needed.



  


Ellis Miller 06/10/2019:  Report details:

  * RepeatRG on Items for open orders (PLEASE, one RG so that we aren't doing RepeatForList here!!), filtered by unprocessed items.
  * How to calculate the last processed date? We don't have Max models. We could have a OrderItemsByProcessedDate.ndx and use an NdxMax expression.



  


Detail Validation for Kiosk

  * Error if already marked as processed. Validation on detail screen if InImport?



  


Matthias Miller 06/10/2019: Time:

  * CCI - 1.5 days
  * Matthias - 1 day


