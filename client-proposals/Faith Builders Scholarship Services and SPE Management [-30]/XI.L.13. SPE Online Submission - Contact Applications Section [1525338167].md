11.12.13. SPE Online Submission - Contact Applications Section

  


Requirements

TODO_VA: standard format for the RG

  


Contact Applications:

Embedded spreadsheet (RG) of all SPE Member Applications for the Linked Member Contact in the year of the Application Date:

Columns:

  * Application Status
  * Application Date
  * Application Amount
  * Link to View
  * (unlabeled column; displays a "*" if the SPE Member Application was created from the current record)



  


  * Create Application (button; visible if the record has been saved, Linked Member Contact is not blank, and there is not a row in the Online Submission School Designation RG with either SPE School Name or SPE School County blank)
    * When clicked, the button prompts for the record to be saved, then opens a new SPE Member Application with available information auto-filled.
  * Save the record to create a new application. (label; visible if the record has not been saved; green text)
  * * Application linked to this online submission. (label; visible if there is an application that is linked to the submission)



  


Development Specification

TODO_NM:

On Remote Button labeled "Create Application" (line 105), highlighted code is redundant:

Visible: NOT NewRecord AND

NOT IsNA( SPESubmissionLinkedMember) AND

NOT IsNA( SPESubmissionDesigSPESchoolName) AND

NOT HasRG( SPESubmissionDesigSPESchoolName

         , IsNA( SPESubmissionDesigSPESchoolName) OR IsNA( SubmissionDesigSPESchoolCounty)

         )

  


TODO_NM:

The expression to display the star in the RG and to display the label explaining the star are redundant.
