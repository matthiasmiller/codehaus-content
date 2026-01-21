7.7.4. Vehicle - Additional Details Section

  * Additional Details section 



  


  * Miles Driven (Past 365 days) (read-only macro; number; rounded to the nearest 1 decimal place; displays __ for the past 365 days, including the current day)



_VA: Tim Reitz 10/09/2025: Suggested by the client today. Based on data reported from the device(s) from Traccar. Past 365 days. 

TODO_JB (research): The client has interest in displaying miles driven in the past 365 days on the Vehicle record in Silverloom. I'm wondering if there's an easy way to field this in Silverloom (or if it's something to defer for a Phase 2 or optional future item).

  * Vehicle Photos (embedded spreadsheet with the following; to be used to store photos for quick identification of the vehicle, or for storing a photo of the vehicle information sticker; possibly could eventually be used in alerts, reports, etc.: 
    * Columns: 
      * File Name (read-only macro; displays the uploaded file name) 
      * Upload Date (auto-set and read-only; date field; sets to the upload date)
      * Upload Time (read-only macro; displays the upload time)
      * Download (link to download file; displays as "Link"; opens the file in a new tab) 
      * Delete (link; displays as "Link"; opens a screen to confirm deletion of the file)  
    * Automatically sorted by: N/A (retains the upload sequence) 
    * Show 6 rows without scrolling
  * Add Attachment (link; exits edit mode for the page after prompting to save any unsaved changes and opens the upload screen that allows a file to be dragged into the browser window to add it to the Attachments table; note that this upload screen includes a link back to the record screen for easy access) 



_VA: Tim Reitz 10/03/2025: Added today, per suggestion from client.

_GZ: Tim Reitz 10/22/2025: What is the use case for this? 

_VA: Tim Reitz 10/23/2025: Per client today, mainly for quick identification of the vehicle. Also could be for storing a picture of the vehicle information sticker from inside the vehicle. 

He'd like to keep it fairly basic & simple. 

Maybe eventually we could display a thumbnail image in alerts / reports / list. 

  


_GZ: Tim Reitz 10/22/2025: How many photos / pictures do you think would be added per vehicle? Thoughts on noting a suggested limit to prevent too many? 

_VA: Tim Reitz 10/23/2025: Per client today, it wouldn't have to be a lot. Maximum of 3 is plenty. 

  


_GZ: Tim Reitz 10/22/2025: Should this be cleared automatically at any point, like when the Owner changes? Or should the person changing the owner be prompted to review the pictures?

_VA: Tim Reitz 10/23/2025: Per client today, a prompt like this would be fine. Some of the pictures would stay the same. 

Tim Reitz 12/10/2025: Added a warning on save (on the Owner History RG). 

  


_GZ: Tim Reitz 10/22/2025: Fine with using the term "photos" vs. "pictures"?  

_VA: Tim Reitz 10/23/2025: Per client today, not a big preference. Fine with "photos". 

  


_EM.: [for above notes] Tim Reitz 10/24/2025: I'm thinking this would warrant S3 storage, given the number of vehicles that could end up the system. I'm thinking about suggesting this as a possible future item or an option add-on. Approximately how much does S3 integration add to the upfront cost & maintenance? 

_VA: Tim Reitz 10/31/2025: Yes, S3. $500 setup + $25/month

TODO_: Tim Reitz 12/09/2025: Let's spec this: 

[X] RG spec here 

[ ] S3 integration spec section 

[ ] Note the cost: $500 setup + $25/month

_EM.: Tim Reitz 12/10/2025: Actually, I think the client will want to be able to see thumbnails for these photos (rather than clicking the links in the RG every time). Nic thinks that displaying thumbnails in the detail screen from S3 is impossible or hard or would burden the server. 

What about a report? (could do a bottom report on the Vehicle record) 

Or what about just storing the photos in a memo after all, maybe with a note cautioning the user to not upload more than X photos per Vehicle? 

TODO_: Tim Reitz 12/11/2025: Per Ellis today:

  * A couple of possible options:
    * Option 1:
      * Paste the image into a memo
      * Use a field change or an onchange to save the image as a thumbnail and clear the memo
      * Never save the full version of the image
    * Option 2: Use S3:
      * Add a "thumbnail" column to the S3 RG
      * Concatenate the thumbnails to display
    * Option 3 (via email): Jonathan create a WSGI to let them drop in pictures. They land as thumbnails on a separate record. Can explain more on a call.



_EM.: Tim Reitz 12/11/2025: Ellis made a note to discuss with Josh.

Tim Reitz 01/05/2026: Ellis pinged Josh about this today. 

TODO_VA: Tim Reitz 01/20/2026: Per Ellis, Josh thought this could be $2,000-3,000 to add support for thumbnails to the S3. 

[ ] Let's add an optional add-on for thumbnails for S2 linking. 

TODO_: Tim Reitz 12/10/2025: Depending on complexity, note as a possible future / optional add-on (and remove S3-related spec). 

  


  * View Linked Event(s) (with the following details: 
    * link; opens the "Traccar Events by Vehicle" report, filtered to this Vehicle; 
    * note that __) 



TODO_: Tim Reitz 01/15/2026: Note visibility, once we have that specced out on the Device record (+ report?).
