19.1. Pavement Conditions List

  


Requirements

_VA: Tim Reitz 03/19/2025: This list no longer needed. Update here and on the Proposal screen spec. 

  


  


List of:

  * None
  * Some Cracks
  * Many Cracks
  * Some Potholes
  * Many Potholes
  * Both



  


DO_: Tim Reitz 01/03/2025: look at the recording for more info here. 

  


_VA - Consider switching to None/Some/Many on two fields. Consider how to migrate "Both". (You could have a hidden option called "Both" for each of these that's only used for migrated records.) 

Tim Reitz 12/31/2024: Looks like we need to dig into the design for the main record more before we settle on this.

_EM: Tim Reitz 01/16/2025: Thoughts on this?

_VA: Tim Reitz 01/20/2025: Migration: We'd probably just pick something, like "Many" \+ "Both"

Tim Reitz 01/21/2025: Noted in the Data Migration section of this proposal.

_VA: Tim Reitz 01/20/2025: Ellis likes the idea of two fields: 

  * None/Some/Many
  * Cracks/Potholes/Both



_AF: Tim Reitz 01/20/2025: Are you good with two fields (seems cleaner)? Or do you prefer the list you currently have?

_VA: Tim Reitz 03/19/2025: Client thinks they might not need the current list. Looking at changing the Pavement Condition field here. 

Option 1: Maybe instead a list of actual conditions:  

  * Bad 
  * Poor 
  * Fair 
  * Good 
  * Excellent 



Option 2: Maybe just a plain text field

Client opted to remove the Cracks/Potholes list and replace with a plain text field where the user can type in a description from the customer's words. 

  


  


\-------------

Initial specs: 

  


This is a custom non-editable simple list used to track the condition of existing pavement for Proposals. It is used in conjunction with a selection from the "None / Some / Many" list, and includes the following items: 

  


  * Cracks 
  * Potholes 
  * Both



  


This list is universal for all users.

  


Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

  


This list will be set up by CCI as part of the main development. If changes need to be made to this list, it will require some coding work.

  


  


New "None / Some / Many" list: 

This is a non-editable simple list used to track the condition of existing pavement for Proposals. It is used in conjunction with the "Pavement Conditions" list and includes the following items: 

  


  * None
  * Some 
  * Many



  


This list is universal for all users.

  


Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

  


This list will be set up by CCI as part of the main development. If changes need to be made to this list, it will require some coding work.

  


Development Specification

Mockup: N/A
