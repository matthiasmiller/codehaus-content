5.2. Repeating Tasks

  


Requirements

Repeating Tasks will always be for specific Ads and should match the schedule for their connected Ads. Therefore, it will be required that there be an Ad Title selected for a Task to be marked as Repeating. The repetitions must match the schedule of that Ad. 

  


To schedule repeating Tasks, enter the desired number of repetitions in the "Repeat # of Times" field, then check the "Repeat Task" checkbox. This will create duplicates of the current Task to complete that number of repetitions, including the original one (for example, if "12" is entered, 11 more repetitions should be created to make a total of 12). 

  


If there are more repetitions than scheduled runnings of the selected Ad Title, there will be an error on the "Repeat # of Times" field. To fix this error, the Number of Times must be reduced or more runnings of the ad must be scheduled. 

  


If any additional runnings of the ad are scheduled after the repeating Task has been set up, either between existing runnings or after the end of the repetitions, the user would need to create additional repetitions of the Task prior to the new running(s) to cover those. 

  


All details from the original Task will be duplicated except Reminders. A few specific details on this:

  * Publication Date:
    * This will be updated to with a corresponding selected future publication dates for each repetition of the Task
  * Comments:
    * Any comments that are in Prior Comments when the "Repeat Task" is checked will be copied to the new repetitions.
    * Any comments in the New Comment field of the original Task would be copied to the New Comments fields of the new repetitions, then added to the Prior Comments on Save
    * Future comments added to the original Task or other repetitions will not be added to subsequent repetitions



  


Repeating Tasks can only be created for current or future Tasks (not past/completed).

  


Development Specification

Clicking the Repeat Task checkbox will clear the "Repeat # of Times" field.
