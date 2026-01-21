11.12.14. SPE Online Submission - Online Submission Status Section

  


Requirements

Online Submission:

  * Closed (checkbox and editable date; when the checkbox is checked the date is set to the current date)
  * Note (visible if there are no SPE Member Applications linked to the current record)



  


Validation:

  * Error on save if 'Note' is blank, there is no linked SPE Member Application, and 'Closed' is checked: "There is no linked Member Application. 'Note' is a required field to mark this Online Submission as Closed."



  


Development Specification

TODO_NM: 

Required and visibility expressions on the SPESubmissionClosedReason field are duplicate and slow. Optimize and make a macro.

  


There should be a section break in between created by and modified by strings and Modification History link. Top positioning should also be adjusted.
