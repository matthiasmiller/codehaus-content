5.3.6. Proposal - Documentation Section

  


Requirements

  * Documentation section (all editable fields in this section are editable in limited editing mode): 
    * Proposal Attachments (embedded spreadsheet with the following; this is used to attach jobsite photos and other documents as needed: 
      * Columns: 
        * File Name (auto-set and read-only; displays the uploaded file name) 
        * Upload Date (auto-set and read-only; displays the upload date)
        * Upload Time (auto-set and read-only; displays the upload time)
        * Download (link to download file; displays as "Link"; opens the file in a new tab) 
        * Delete (link; displays as "Link"; opens a screen to confirm deletion of the file)  
      * Automatically sorted by: N/A (retains the upload sequence) 
      * Show 6 rows without scrolling
      * Other Notes: 
        * Not all Proposals will have photos or documents, so no validation to require attachments.) 
    * Add Attachment (link; exits edit mode for the page and opens a new tab that allows a file to be dragged into the browser window to add it to the Attachments table)



  


  * *Deleting an attachment will result in the corresponding link being broken for other proposals in the same family. If needed, first download the file from here and upload it to other proposals as needed prior to deleting it here. (on-screen message in gray font; visible if there is another Proposal in the same "Proposal Family" and with a duplicate file attachment key)



  


  


  * Other Notes:
    * This is always editable, even after other sections / editable fields on a Proposal record have been frozen. This is because users might want or need to upload attachments in later stages, or even after the job has been completed.
    * A copy of the signed Proposal printout can be uploaded via this feature. 
    * Note that all of the editable fields (links / rows) in this section are cleared on new copied Proposals when the "Change Order" button is clicked (but not for the "Revised Proposal" or "Duplicate Proposal" buttons - all links are retained for those).



  


Development Specification

Change Requests: 

  * Tim Reitz 11/25/2025: [[[IN12327](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12329&)]] - ZLP - Phase 1 - Proposal - Documentation Section - Add Message About Deleting Attachment Links 



  


  


Ellis Miller 06/17/2025: 

[ ] S3 RG's like we use elsewhere

3 HOURS
