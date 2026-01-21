7.2. Contact Record

  


Requirements

Overview: The Solution will use the standard AppHosting Contacts module, with some customizations.

  


The Solution can track the individual and their organization/business separately, and has the ability to link an individual contact to an organization contact. 

  


Accessed via: 

  * View Contacts report
  * Member Directory report
  * Various record screens and/or reports that include links to Contact records 



  


Data Access: See Data Access Controls section of the proposal for details. 

  


Special Considerations:

  * Copy Record: Clear Contact ID
  * Delete Record: Disallow for Member-type contacts (error message: "Contacts of 'Member' type cannot be deleted.")
  * Merge Record: N/A



  


Other Notes:

  * Note that when a membership ends, the membership will be marked as inactive but the Contact record itself will not be deactivated. Tis is to make reporting cleaner and reinstating returning members
  * The Solution will not directly report on historical membership details, for example if a member ends their membership for a time and later rejoins, or if a member changes groups. However, this information can be found by viewing Modification History on the Contact record or by pulling a report of Growth Ring Meetings or Goals that the member is associated with.
  * The Contact ID will be automatically added to the end of each contact's name. This will allow for handling contacts with the same name. The Contact ID will be removed/hidden in various places, such as the Member Directory Report and printout.
  * Note that only Super Admins can create new Contact records. This can be changed in the future if desired.
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockups:

  * Main Contact Record:  [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=873949625](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=873949625)
  * Child Screens Mockup:  [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1581977838](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1581977838)



  


As noted in the System Switches section, we need to turn on the Allow Multiple Organizations system switch for Symbiz.
