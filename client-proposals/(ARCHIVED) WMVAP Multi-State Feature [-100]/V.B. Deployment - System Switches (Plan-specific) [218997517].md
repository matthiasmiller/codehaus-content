5.2. Deployment - System Switches (Plan-specific)

*Documented. Tim Reitz 08/26/2025

  


Standard System Switches with custom settings for the PA (WMVAP) Group-specific Solution: 

  


  * Label: Max contact ID num:
    * Code: MaxContactIDNum
    * Field Type: Number
    * Description: Specifies the maximum ID number for contacts.
      * Note that this should be set to 1 less than the desired first number. 
    * Set to: N/A (does not need to be set for the existing PA system)
    * Other Notes:
      * Note that if a custom Contact ID and/or custom per-member Policy # is desired, this system switch should be set prior to any contacts being added to the Solution.



  


Related to Menu options (specifically the Home | Resources menu section):

  


  * Label: Resource Menu Vehicle Guidelines Sheet
    * Code: ResourceMenuGuidelinesWikiID  
    * Field Type: Plain text field
    * Description: "This is used to configure the linked Wiki page for the "Vehicle Guidelines Sheet" menu item in the Resources section of the menu."
    * Default Value: N/A (may be left blank)
    * Set to: "W0005"
    * Other Notes: 
      * Note that if this System Switch is configured, the menu option is visible; if this is blank, the menu option is hidden.
      * This is editable in the Solution.



  


User-Specified Item 1: "View Handbook" 

  * Label: Resource Menu item 1 Label 
    * Code: ResourceMenu01Label 
    * Field Type: Plain text field
    * Description: "This is used to configure the name for the 1st menu item in the Resources section of the menu."
    * Default Value: N/A
    * Set to: "View Handbook"
    * Other Notes: 
      * Note that if this is configured, the menu option is visible; if blank, the menu option is hidden.
      * This is editable in the Solution.



  


  * Label: Resource Menu item 1 Wiki action 
    * Code: ResourceMenu01Action 
    * Field Type: Drop list of "View Page" / "Page to PDF" / "View Attached File" 
    * Description: "This is used to configure the action that is taken when the 1st menu item in the Resources section of the menu is clicked."
    * Default Value: N/A 
    * Set to: "View Attached File"
      * Deployment note: Will need to move the PDF to a new Wiki page, as the existing Handbook record is being removed.
    * Other Notes: 
      * Note that if "Page to PDF" is selected, it should respect the "Include Title in Export" checkbox on the Wiki page) 
      * Note that if "View Attached File" is selected, the menu option opens the last uploaded file (based on alphabetical order) in the Wiki page memo (the Solution looks at the files as a list sorted alphabetically). 
      * This is editable in the Solution.



  


  * Label: Resource Menu item 1 Wiki page 
    * Code: ResourceMenu01Page 
    * Field Type: Plain text field
    * Description: "This is used to configure the linked Wiki page for the 1st menu item in the Resources section of the menu."
    * Default Value: N/A
    * Set to: TBD
    * Other Notes: 
      * This is editable in the Solution.



  


User-Specified Item 2: "View Allowed Vehicles"

  * Label: Resource Menu item 2 Label 
    * Code: ResourceMenu02Label 
    * Field Type: Plain text field
    * Description: "This is used to configure the name for the 1st menu item in the Resources section of the menu."
    * Default Value: N/A
    * Set to: "View Allowed Vehicles"
    * Other Notes: 
      * Note that if this is configured, the menu option is visible; if blank, the menu option is hidden.
      * This is editable in the Solution.



  


  * Label: Resource Menu item 2 Wiki action 
    * Code: ResourceMenu02Action 
    * Field Type: Drop list of "View Page" / "Page to PDF" / "View Attached File" 
    * Description: "This is used to configure the action that is taken when the 1st menu item in the Resources section of the menu is clicked."
    * Default Value: N/A 
    * Set to: "View Attached File"
    * Other Notes: 
      * Note that if "Page to PDF" is selected, it should respect the "Include Title in Export" checkbox on the Wiki page) 
      * Note that if "View Attached File" is selected, the menu option opens the last uploaded file (based on alphabetical order) in the Wiki page memo (the Solution looks at the files as a list sorted alphabetically).
      * This is editable in the Solution.



  


  * Label: Resource Menu item 2 Wiki page 
    * Code: ResourceMenu02Page 
    * Field Type: Plain text field
    * Description: "This is used to configure the linked Wiki page for the 1st menu item in the Resources section of the menu."
    * Default Value: N/A
    * Set to: "W0003"
    * Other Notes: 
      * This is editable in the Solution.



  


  


User-Specified Item 3: "View Truck Weight Chart"

  * Label: Resource Menu item 3 Label 
    * Code: ResourceMenu03Label 
    * Field Type: Plain text field
    * Description: "This is used to configure the name for the 1st menu item in the Resources section of the menu."
    * Default Value: N/A
    * Set to: "View Truck Weight Chart"
    * Other Notes: 
      * Note that if this is configured, the menu option is visible; if blank, the menu option is hidden.
      * This is editable in the Solution.



  


  * Label: Resource Menu item 3 Wiki action 
    * Code: ResourceMenu03Action 
    * Field Type: Drop list of "View Page" / "Page to PDF" / "View Attached File" 
    * Description: "This is used to configure the action that is taken when the 1st menu item in the Resources section of the menu is clicked."
    * Default Value: N/A
    * Set to: "View Attached File"
    * Other Notes: 
      * Note that if "Page to PDF" is selected, it should respect the "Include Title in Export" checkbox on the Wiki page) 
      * Note that if "View Attached File" is selected, the menu option opens the last uploaded file (based on alphabetical order) in the Wiki page memo (the Solution looks at the files as a list sorted alphabetically).
      * This is editable in the Solution.



  


  * Label: Resource Menu item 3 Wiki page 
    * Code: ResourceMenu03Page 
    * Field Type: Plain text field
    * Description: "This is used to configure the linked Wiki page for the 1st menu item in the Resources section of the menu."
    * Default Value: N/A
    * Set to: "W0004"
    * Other Notes: 
      * This is editable in the Solution.



  


User-Specified Item 5: TBD

  


User-Specified Item 6: TBD

  


User-Specified Item 7: TBD

  


User-Specified Item 8: TBD

  


User-Specified Item 9: TBD

  


User-Specified Item 10: TBD
