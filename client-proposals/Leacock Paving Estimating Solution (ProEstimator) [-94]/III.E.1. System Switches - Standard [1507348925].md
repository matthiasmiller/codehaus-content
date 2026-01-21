3.5.1. System Switches - Standard

  


Requirements

The Solution includes the following standard System Switches:

  


  * SMTP Settings for outbound email 



  


  * Label: "From" email address for notifications" 
    * Code: EmailNotificationsSendingAddress
    * Field Type: Plain text 
    * Description: Specifies the 'From' email address to be used whenever the application sends notification emails.
    * Value / set to: __ (TBD / initially set at deployment) 
    * Other Notes: 
      * Editable



  


  * Label: "Sales Item Require Description"   
    * Code: Config_SalesItemDescrRequired
    * Field Type: Checkbox
    * Description: "Specifies whether Description is required on Sales Item records"
    * Value / set to: Checked (customized)
    * Other Notes: 
      * Not editable in the Solution (must be set/changed by CodeCrafters) 



  


  * Label: "Sales Item Show Cost & Markup"   
    * Code: "Config_SalesItemShowCostAndMarkup"
    * Field Type: Checkbox
    * Description: "Specifies whether the Unit Cost $ and Markup % fields are visible on Sales Item records and report"
    * Value / set to: Checked (customized)
    * Other Notes: 
      * Not editable in the Solution (must be set/changed by CodeCrafters) 



  


  * Label: "Sales Item Show UOM"   
    * Code: "Config_SalesItemUOMVisible"
    * Field Type: Checkbox
    * Description: "Specifies whether the Unit of Measure field is visible on Sales Item records and report"
    * Value / set to: Checked (customized)
    * Other Notes: 
      * Not editable in the Solution (must be set/changed by CodeCrafters) 



  


  * Label: "Show multiple contact types"
    * Code: ConfigContacts_ShowMultipleTypes
    * Field Type: Checkbox
    * Description: "Specifies whether a contact can be multiple types."
    * Value / set to: Checked (customized)
    * Other Notes:
      * Editable



  


Development Specification

Tim Reitz 12/02/2025: 

[ ] Email SMTP password

[ ] Email SMTP port

[ ] Email SMTP security

[ ] Email SMTP server 

[ ] Email SMTP timeout

[ ] Email SMTP user name
