2.1. On the Trusses embedded spreadsheet

  * Add a column without a column heading, but internally called "Request Print": 
    * This would be a column of checkboxes, defaulting to cleared. 
    * It should be located between "Description" and "Unit Price". 
    * Filling a checkbox will show a "Pending Truss Print Request" memo and the "Truss Request Preview" underneath the Trusses spreadsheet when that row is selected. 
    * A user can select multiple checkboxes to initiate requests, then go between the requests by selecting the row for the truss they wish to work on. 
  * Add a column called "View Sketch": 
    * As long the platform can generate an image with good enough quality, this will show an ellipsis button in the row that will open a child screen with the sketch. If no sketch exists, the ellipsis button will either be hidden (if possible) or open a blank image.
    * If necessary, this column may use an "Open Link" for each row. This would open the image in a new tab. If no sketch exists, the link would either be hidden (if possible) or the link would open a new tab with a blank sketch.
    * Located to the right of "Unit Price". 
  * Add a column called "View Print": 
    * This would have an "Open Link" cell that opens the most recent print generated for that row. (If possible, the link will be hidden for items that do not have a print.)
  * Add a hidden read-only column called "Truss Print Request Date". This will be used to track the order of the requests.
  * Add a hidden read-only column called "Truss Print Request": 
    * This is the Truss Print Request memo for the corresponding row. 
    * (Technical details: use a hidden field for the memo, with a read-only MRG expression with the RichTextExpression behavior for the MRG) 
  * Add a hidden column called "Truss Print Pending Revision #": 
    * This is a number that defaults to 1. 
  * Add a hidden column called "Truss Print Completed": 
    * This would be a column of checkboxes, defaulting to cleared. 
    * These checkboxes would only be visible for the designer/user in the Truss Print Request View. 
    * This would be tied to a hidden "Truss Print Completed Date"


