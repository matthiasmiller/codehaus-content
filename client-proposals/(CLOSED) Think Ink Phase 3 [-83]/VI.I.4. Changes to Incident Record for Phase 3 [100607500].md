6.9.4. Changes to Incident Record for Phase 3

  


Requirements

TODO_IDD: Tim Reitz 11/22/2023: What applies to Phase 3b vs. 3c?

  


TODO_IDD: Tim Reitz 11/22/2023: What is completely new (not in the original scope)?

  


  


The following changes will be applied to the existing Incidents records:

  


Add to the existing Device Details section on all incident types that have it:

  * Device (optional; drop list of Device descriptions for the selected Customer)
    * Validation: warning on save if the device is changed "The Device for this incident has been changed. Are you sure you want to continue?"
  * Serial # (optional and editable if Device is blank; auto-filled and read-only if a Device is selected; if a Serial # is entered that matches an existing Device for the selected Customer, the Device field will auto-fill) 
    * Note that this allows the user to simply document a serial # without creating a Device record if the device is not already in the database.
    * Validation: warning on save if the Serial # is changed "The Serial # for this incident has been changed. Are you sure you want to continue?"
  * New Device (visible if Device is blank; link; opens a new blank Device record in a new tab with the Customer defaulted)



  


  


  


Add to New Service Incident Prompt: 

Tim Reitz 06/23/2022: Change behavior for the Device prompt.

  


  


Tim Reitz 04/20/2023: From call with client today: Might want a more basic/simplified view for Checkin incidents.

  


If Type = Check-In:

  * Customer Temperature Tracking section (visible if Type = Check-In): 
    * (embedded spreadsheet with the following:) 
      * Columns: 
        *       * Automatically sorted by: (e.g. by date, etc, or N/A)
      * Buttons to insert/append/remove rows:
        * If only two options are needed, use "+" / "-" (regardless of whether "+" functions as an Insert or an Append)
        * If three options are needed, use buttons with words "Insert", "Append", "Delete".
      * (If not sorted) Button to insert ("Insert") 
      * (If not sorted) Buttons to move rows up and down (up/down arrows) 
      * Show __ rows without scrolling



DONE_JM: Tim Reitz 07/27/2023: Discuss what additional reporting on Check-Ins you'd like.

TODO_IDD: Tim Reitz 08/03/2023: Client would like to be able to track more information from interactions with customers.

\- Something like ZWA:

\- RG to configure Customer Temperature questions on AppHosting Settings

\- Question

\- Customer Temperature RG that auto-fills on the Check-In

\- Question (auto-set)

\- Answer (optional; drop list of Yes/No/??)

\- Comments (optional; plain text)

\- Customer Temperatures Report:

  * Grouped by Question, then by Answer
  * Columns for
    * Customer
    * Check-In Date
    * Comments



\- Multiple choice; questions like

\- Customer satisfied? (drop list of Yes/No; comments required for No)

-

  


Development Specification

CCI: Tim Reitz 08/15/2023: Ensure we retain manually-entered Serial #'s from before the Device records are added, and that matching ones fill in the Device field.
