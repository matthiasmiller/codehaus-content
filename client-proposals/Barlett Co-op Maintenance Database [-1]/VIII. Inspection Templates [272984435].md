8\. Inspection Templates

  


Requirements

The choice of questions for an inspection inspections is configurable by the user by going to the Advanced menu and selecting Configuration | Inspection Templates. This will displays a list of inspection templates (these are called Questionnaire Templates within the software). 

  


Users with the "Edit Questionnaire Templates" permission will be able to create, modify, and delete Questionnaire Templates. 

  


Questionnaire Template Record

The template record will contain:

  * Template name -- required (e.g. "Anhydrous Tank Inspection")
  * Equipment type -- Selected from a list of equipment types. Can be blank if it is not equipment-specific.
  * Schedule -- Frequency of inspection. If no schedule is specified, the inspection can be done on an ad-hoc basis, but is not scheduled. Options include: 
    * Every _1 Month(s) -- where the # of months is specified. Allows blank or 1 - 120 months.
    * Starting Date -- visible and required if # Months specified. If the day of month is 29, 30, or 31, it will automatically be adjusted down for months with fewer days. 
    * Accept ___ Days before Due Date -- defaults to 30. Visible and required if # Months specified. 
  * List of questions. Each question will specify:
    * Question Type - required, options include Blank Row, Label Row, Yes/No, Date, Number, Text, List
    * Question Label - Text displayed to user. Required for all but Blank Rows.
    * List Values - required for list types, pipe-delimited list of options (e.g. "Square|Round|Triangular")
    * Answer Required? - if checked, then the user must specify the answer for this question
    * Explanation - optional text that is displayed below the question in a smaller font to clarify the question.



  


Development Specification

Scheduling is tricky with determining if needed. 

  


Permission: "Edit Questionnaire Templates"

  


OnChange when List Values are entered, if no pipes are specified, then replace commas and semicolons with pipes, always trim all entries.

  


Question ID - Hidden, unique numeric identifier for this question. This is auto-populated. In the future we can allow the user to add a text ID if desired. To avoid confusion, start numbering this at 1001 for the first one.
