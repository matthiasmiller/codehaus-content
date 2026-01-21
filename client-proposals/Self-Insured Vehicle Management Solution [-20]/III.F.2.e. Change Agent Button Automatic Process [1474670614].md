3.6.2.5. Change Agent Button Automatic Process

  


Requirements

*Done

  


  * Name: "Change Agent Button" 
    * Description: This automatic process changes the "Client's Agent" from the current Agent to a new Agent, and sets an Effective Date. 
    * Prompts: 
      * From Agent (plain text; defaults to the "From Agent" selected in the "Change Agents" report - see corresponding spec) 
      * To Agent (drop list) 
      * Effective Date (date; defaults to the current date) 
    * Initiated: 
      * When the "Run Import" button is clicked on the "Change Agents" prompt screen on the "Change Agents" report - see corresponding spec. 
    * Action(s): 
      * Sets the "Client's Agent" field on the client's Contact record to the Agent selected in the "To Agent" prompt. 
      * Sets the "Prior Agent Change Date" field on the client's Contact record to the date entered in the "Effective Date" prompt



  


Development Specification

Tim Reitz 09/05/2025: Note that this is the "Std Change Agent Button" import ([https://testweaverland.silverloom.io/ImportSettings/Standard/Std_Change_Agent_Button?State=pa4IpoPlMj0&](https://testweaverland.silverloom.io/ImportSettings/Standard/Std_Change_Agent_Button?State=pa4IpoPlMj0&) in the test system).
