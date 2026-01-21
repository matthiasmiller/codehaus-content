6.2.11. Change Agents

  


Requirements

*Done. 

  


Overview: This is a custom Admin-only report of clients for an Agent, used to facilitate changing the Agent for a batch of clients at one time. The report includes one row for each client Contact of the selected Agent. 

  


Accessed from: Admin | Exception Reports | Change Agents (opens a "Change Agents Helper Report" prompt screen with a "From Agent" filter (drop-list of active "In-State Agent"-type Contacts with a Fund, in the following format: "<Agent Name> \- <Agent Code>")) 

  


Title: "Change Agents"

  


Preface: N/A

  


Columns: 

  * Name (displays the name of the client Contact; link to open the record) 
  * Prior Agent
  * Current Agent
  * Contact Type
  * Phone
  * Phone Type
  * Email
  * City
  * Congregation



  


Row-Specific Buttons: N/A

  


Grouped by: N/A

  


Sorted by: Name (alphabetically) 

  


Filters: 

  * From Agent (hidden; drop-list of active "In-State Agent"-type Contacts with a Fund, in the following format: "<Agent Name> \- <Agent Code>"; sets based on the selection in the "Change Agents Helper Report" prompt screen, mentioned above) 
  * Session ID (hidden; plain text) 



  


Buttons: 

  * Change Agent (visible if the "Change Agent Button" automatic process has not been run; opens a child screen with the following: 
    * To Agent (required; drop-list of active "In-State Agent"-type Contacts with a Fund, in the following format: "<Agent Name>") 
    * Effective Date (required; date; defaults to the current date)  
    * "Clicking Continue will transfer all the clients to this agent." 
    * Run Import (button; runs the "Change Agent Button" automatic process to change all clients in the report from the current Agent to the "To Agent" - see corresponding automatic process spec) 
  * Print Agent Change Notices (visible if the "Change Agent Button" automatic process has been run; opens the "Agent Change Notice" printout PDF (see corresponding spec) for the affected clients)



  


Menu Visibility: Admin (by virtue of being on the Admin menu) 

  


Other Notes: 

  * N/A



  


Development Specification

TODO_CCI: Tim Reitz 08/28/2025: What is the specific condition for making the "Change Agents" button and "Print Agent Change Notices" button visible? 

Sagar Sagar 12/16/2025: I believe this is based on session ID. If the provided session ID matches with Session ID stored for any contact then "Print Agent Change Notices" button is visible. If not matches found then "Change Agent" button is visible.

  


TODO_CR: Tim Reitz 08/28/2025: Consider hiding the "Current Agent" from the drop list on the "To Agent" prompt (currently you can transfer the clients to the same agent). 

  


TODO_CR: Tim Reitz 08/28/2025: Change the "Run Import" button to something more user-friendly, like "Confirm" or __. 

  


  


Change Agents (1/2 day)

Simple x30

 

Print Agent Change Notices (1 day)
