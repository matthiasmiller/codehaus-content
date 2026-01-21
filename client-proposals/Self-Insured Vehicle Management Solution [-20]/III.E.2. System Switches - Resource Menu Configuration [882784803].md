3.5.2. System Switches - Resource Menu Configuration

  


Requirements

*Done. 

  


Custom System Switches pertaining to the customizable Resource Menu Options: 

  


The "Resources" section on the Home menu supports one hard-coded menu option for printing the Vehicle Guidelines Sheet, plus up to 10 user-specified menu items that point to specific wiki pages. This allows providing easy access to specific resources for agents.

  


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
      * If "Page to PDF" is selected, it should respect the "Include Title in Export" checkbox on the Wiki page) 
      * If "View Attached File" is selected, the menu option opens the last uploaded file (based on alphabetical order) in the Wiki page memo (the Solution looks at the files as a list sorted alphabetically).
      * This is editable in the Solution.



  


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

  * Tim Reitz 08/18/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident
  * Tim Reitz 05/12/2025: [[[IN11459](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11461&)]] - ZWA - Multi-State Feature - System Switches - Add System Switch for Vehicle Guidelines Sheet Menu Option


