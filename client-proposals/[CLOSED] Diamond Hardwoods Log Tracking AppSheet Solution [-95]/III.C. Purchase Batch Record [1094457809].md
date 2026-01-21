3.3. Purchase Batch Record

Overview: The Purchase Batch record tracks information about an individual batch of purchased logs. 

  


Accessed via: 

  


Sections and Fields: 

  * Batch ID (auto-set and read-only; __) 



TODO_AP: Tim Reitz 11/05/2024: What auto-set options do we have for unique IDs? We maybe could simply do an auto-number, or maybe auto-number with a "B" prefix. 

  * Description (auto-set and read-only; "<Log Buyer> \- <Date> \- <Supplier> \- <Location> \- <Batch Notes>"; used as a visual identifier for the Batch)
  * Log Buyer (required; list based on users; defaults to the current user) 



_DD: fine for this to be a list based on users? or do you really need to track other info for the Buyer? 

TODO_AP: Tim Reitz 11/01/2024: Yes, that's good. 

TODO_AP: Tim Reitz 11/05/2024: Fine to default to the current user?

  * Supplier (required; drop list of Suppliers) 
  * Location (optional; defaults to the Defaults Location for the selected Supplier) 
  * Batch Notes (optional; plain text field) 
  * Date (required; defaults to the current date) 
  * Logs (read-only embedded spreadsheet; displays several rows with several columns: 
    * Tag #; 
    * Species; 
    * Length; 
    * Grade) 
  * Add (button; opens the camera to scan the QR code, then opens a new log record - see corresponding spec) 
  * View (button; opens the report of logs) 
  * Total # of Logs (auto-set and read-only; total number of logs linked to the Purchase Batch) 
  * Batch BF (auto-calculated and read-only; sum of "BF" values for all logs linked to the Purchase Batch)
  * Total Batch Value $ (auto-calculated and read-only; sum of "Log Value $" values for all logs linked to the Purchase Batch) 
  * Batch Closed (button / checkbox; __



TODO_AP: Tim Reitz 11/04/2024: What capabilities do we have with this in AppSheet? Could we make it read-only when this is set? And then require a confirmation if a user would try to open it again? 

  * Generate/Print PDF (button; __



TODO_AP: Tim Reitz 11/04/2024: Is it simple enough to directly print from the app, rather than have a PDF in between? Or can we create a PDF and print without saving? Client doesn't think they'll normally need to go back to the PDF itself (and it could get confusing to have multiple file versions for the same batch). 

  


Data Access: N/A (all users can access)

  


Special Considerations: TODO_AP: Tim Reitz 11/04/2024: Is this something to consider for AppSheet?  

  * Copy Record:
  * Delete Record:
  * Merge Record:



  


Other Notes:

  * N/A


