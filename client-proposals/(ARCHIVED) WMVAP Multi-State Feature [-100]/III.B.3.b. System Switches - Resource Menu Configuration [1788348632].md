3.2.3.2. System Switches - Resource Menu Configuration

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Related to Menu options (specifically the Home | Resources menu section): The Home | Resources menu supports one hard-coded menu option for printing the Vehicle Guidelines Sheet, plus up to 10 user-specified menu items that point to specific wiki pages. This allows providing easy access to specific resources for agents.

  


  * Label: Resource Menu Vehicle Guidelines Sheet
    * Code: ResourceMenuGuidelinesWikiID  
    * Field Type: Plain text field
    * Description: "This is used to configure the linked Wiki page for the "Vehicle Guidelines Sheet" menu item in the Resources section of the menu."
    * Default Value: N/A (may be left blank)
    * Set to: As described in the "Deployment - System Switches" section of the proposal.
    * Other Notes: 
      * Note that if this System Switch is configured, the menu option is visible; if this is blank, the menu option is hidden.
      * This is editable in the Solution. 



  


Note that each of the following items should be repeated 10 times, as described below, to allow for up to 10 different menu options. Only one copy is included here in the spec, for sake of space. 

  


  * Label: Resource Menu item 1 Label (note: include a total of 10, from "item 1" to "item 10") 
    * Code: ResourceMenu01Label (note: include a total of 10, from "Code01" to "Code10") 
    * Field Type: Plain text field
    * Description: "This is used to configure the name for the 1st menu item in the Resources section of the menu."
      * Note: include the appropriate ordinal number, from "1st" to "10th". 
    * Default Value: N/A
    * Set to: As described in the "Deployment - System Switches" section of the proposal.
    * Other Notes: 
      * Note that if this is configured, the menu option is visible; if blank, the menu option is hidden.
      * This is editable in the Solution.



  


  * Label: Resource Menu item 1 Wiki action (note: include a total of 10, from "item 1" to "item 10")  
    * Code: ResourceMenu01Action (note: include a total of 10, from "Code01" to "Code10") 
    * Field Type: Drop list of "View Page" / "Page to PDF" / "View Attached File" 
    * Description: "This is used to configure the action that is taken when the 1st menu item in the Resources section of the menu is clicked."
      * Note: include the appropriate ordinal number, from "1st" to "10th". 
    * Default Value: N/A
    * Set to: As described in the "Deployment - System Switches" section of the proposal.
    * Other Notes: 
      * Note that if "Page to PDF" is selected, it should respect the "Include Title in Export" checkbox on the Wiki page) 
      * Note that if "View Attached File" is selected, the menu option opens the last uploaded file (based on alphabetical order) in the Wiki page memo (the Solution looks at the files as a list sorted alphabetically).
      * This is editable in the Solution.



_VA: Tim Reitz 08/11/2025: How does this logic work? (i.e., how does alphabetical order determine which was uploaded last?) Find out and clarify this spec (and other places where this is referenced). 

Tim Reitz 08/26/2025: Pursuing this separately. 

  


  * Label: Resource Menu item 1 Wiki page (note: include a total of 10, from "item 1" to "item 10") 
    * Code: ResourceMenu01Page (note: include a total of 10, from "Code01" to "Code10") 
    * Field Type: Plain text field 
    * Description: "This is used to configure the linked Wiki page for the 1st menu item in the Resources section of the menu."
      * Note: include the appropriate ordinal number, from "1st" to "10th". 
    * Default Value: N/A
    * Set to: As described in the "Deployment - System Switches" section of the proposal.
    * Other Notes: 
      * This is editable in the Solution.



  


Development Specification

Change Requests: 

  * Tim Reitz 05/12/2025: [[[IN11459](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11461&)]] - ZWA - Multi-State Feature - System Switches - Add System Switch for Vehicle Guidelines Sheet Menu Option
  * 


  


Ellis Miller 04/24/2025: This could be coded by another developer since it's a standalone piece.

  


Ellis Miller 09/04/2024: I have a target of total of 8 hours, but am bidding it at 12 hours. We should definitely be able to meet that target.

  


[ ] Add ResourceMenuActions list with options for "View Page" / "Page to PDF" / "View Attached File PDF"

[ ] Create a "Std AutoPush Wiki Page Action.r20" that takes a wiki page ID and a Action. Both are ask prompts that should be required (Ask list of all wiki page IDs, ask list of Actions).  1 hour

[ ] None level report that simply passes answers to the specific action report.

[ ] We'll have a Default AutoPush button that returns one of 3 different r20's based on action:

[ ] If action is View Page, we autopush into the wiki page (we presumably already have an AutoPush r20 to launch an ID).

[ ] If Page to PDF, it's equivalent to clicking the PDF link at the bottom of the wiki page (create a "Std Export  Wiki to PDF.r20" merge that takes a wiki ID and runs the r21 that is at the bottom of the wiki detail screen).  1 Hour

[ ] We also need to code [[[IN10441](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10443&)]] - CORE - Wiki - Add "Include Title in Export" Checkbox 2 Hours

[ ] For View Attached File PDF, create a "Std AutoPush Wiki Page Attached PDF.r20" if we don't have something similar already (we may, see what we use for our current Resource menu options). This will auto-push to display the specific attached document. 2 Hours 

  


[ ] Add 30 system switches (3 x 10) 1 hour

[ ] On the menu, for each of the 10 menu items: 1 hour

[ ] use #ResourceMenu01Label# for the label

[ ] Use visibility of NOT IsNA( ResourceMenu01Label)

[ ] Path is Standard\Std AutoPush Wiki Page Action.r20|vPageID="#ResourceMenu01WikiID#",vAction="#ResourceMenu01Action#"

  


Sagar Sagar 05/21/2025: CLS job ID - [[PC0178319]], [[PC0178862]]

  


Tim Reitz 05/21/2025: Note that we are changing the "View Attached PDF" option to "View Attached File", since this function can open other file types (not just PDFs).
