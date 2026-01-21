7.5.0.3. "Set Email Announcement Status to Sent"

  


Requirements

*Done. 

  


  * Name: "Set Email Announcement Status to Sent"
    * Description: This automatic process sets the Announcement "Status" to "Sent" after the <Service Name> Announcement email merge runs. 
    * Prompts: 
      * Announcement "Internal ID" 
    * Initiated:
      * When the <Service Name> Announcement Email Merge runs 
    * Action(s): 
      * Takes the "Internal ID" and sets "Status" for that record from "Draft" to "Sent"



  


Development Specification

Tim Reitz 01/20/2026: This is the x30 import that runs from the "<Service Name> Announcement" email merge.
