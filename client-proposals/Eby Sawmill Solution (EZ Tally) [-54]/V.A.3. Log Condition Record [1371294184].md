5.1.3. Log Condition Record

  


Requirements

Overview: The Log Condition record is used to configure options that can be used to quickly flag issues with a log when scaling.

  


Accessed via: Configure Log Conditions Report

  


Sections and Fields: 

  * Active (checkbox; defaults to filled)
  * Condition (auto-set and read-only; displays the log condition as it is displayed on lists, etc., elsewhere in the Solution, in the following format: "<Description> (<Hotkey>)") 
  * Description (required; plain text; validate against active Log Condition records with duplicate Descriptions - validation message: "The Description is used for another active Log Condition record. Please enter a different description.")
  * Hotkey (required; number; single digit; allow numbers 1-8 - validation message: "Only the numbers 1-8 are allowed. 0 is used to indicate that there are no conditions to report."; validate against active Log Condition records with duplicate Hotkeys - validation message: "The Hotkey is used for another active Log Condition record. Please enter a different hotkey.") 



  


Data Access:

  * View record: All users (specifically to allow users to view Description, Abbreviation, Hotkey in lists, records, etc. throughout the system)
  * Edit and delete full record: Administrators



  


Other Notes:

  * The following conditions will be included in the development of the system and cannot be edited by users (any changes require coding work): 
    * Condition with Hotkey of "0" \- used to indicate that there are no log conditions to report for the selected log. 
    * Condition with Hotkey of  "9" and Description of "Other" \- used to indicate an "other" condition for the selected log. 
  * Eby's will take care of setting up the other Log Condition records (with Hot Keys 1-8) at deployment or as needed.
  * As mentioned above, the Log Conditions will be displayed in lists in the following format: "<Description> (<Hotkey>)". For example, "Other (9)" if the Description is "Other" and the Hotkey is 9.



  


Development Specification

Mockup:

  * Google Sheets: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=57007202](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=57007202)



  


  * Designer: [https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D12&SinglePane=true&State=Tr1GcI4u7tA](https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D12&SinglePane=true&State=Tr1GcI4u7tA)



  


Ellis Miller 12/15/2022: 

BID 4 HOURS: 

[ ] Simple screen

[ ] Validation as described above.

[ ] Automatically construct list field from two other fields.
