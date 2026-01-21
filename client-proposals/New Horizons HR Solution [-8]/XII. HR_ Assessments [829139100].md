12\. HR: Assessments

  


Requirements

We will have a way to define Assessments. We will have four possible directions:

  * Assessment by Self
  * Assessment by Peers (if there are at least 2 other peers)
  * Assessment by Manager
  * Assessment by Downlines (if there are at least 2 downlines)



  


We will be able to set up specific assessments which will define:

  * The schedule/frequency
  * How long the employee needs to be in their current role (i.e. 30 days)
  * The reminder schedule
    * # of days for assignment
    * # of days for completion
    * # of days for managerial review
  * For self, manager, and peer:
    * Wording (question and choices) for "engagement" question.
    * Wording (question and choices) for "performance" question
  * Wording for an arbitrary number of open-ended questions
  * Additional manager instructions (i.e. questions to ask during review)



  


The {FirstName} and {DisplayName} can be used in any of the questions.

 

At the scheduled time, we'll automatically set up the assessments for everyone, but not assign them.

  


We will send reminders to the managers to assign assessors. If they want to skip the assessment, they can leave the list of assessors blank and provide their approval. (We need to add a comment to this extent.)

  


This means that if the managers take a long time to assign assessments, the entire process will be delayed.

  


When assigning them, we will have sections for:

  * Choosing Peers (if relevant)
  * Choosing Managers
  * Choosing Direct Downlines (if relevant)
  * Choosing Others



  


We warn if they have 2 peers and/or direct downlines, but no evaluations from that direction.

  


Once the assessors are assigned, we will send emails (and reminders) to the assessors to complete the assessment. When the assessors pull up the review, we will indicate clearly the ROLE that the individual is being reviewed for.

  


Once all assessments have been completed, we will send an email to the manager. We will keep reminding them until they sign off.

  


Once the manager signs off, we will send an email to their upline with a link to generate the report.

  


Reporting

The scores will be combined on a scale of 1-10 (with 1 decimal place). They will all be combined into a single report.

  


The text answers will be randomized.

 

Once they provide an answer for the assessment, they will not be able to go back and change their answers.

  


The manager's comments will be included on the report.

  


Permissions

Individuals will not be able to see their own assessments results, under any circumstances.

  


Administrators will be able to see everyone ELSE's assessments.

  


Accountability

We will provide a report to allow people to see outstanding requirements (i.e. manager needs to assign, or X people need to complete it.)

  


We will create a manager summary report that summarizes the manager comments for each of their direct downline's reviews. These reports will always include the manager comments. The manager summary report can be for:

  * For people reporting to _______
  * Include direct reports or entire part of org chart



  


We will have a report that allows anyone to view all assessments for their downlines. (Presumably, this will be hidden for individuals who are not managers.)

  


Development Specification

If the RoleID is a list, we can use this to link assessments to the role?

  


I'm proposing we have an AssessmentDefinition with:

  * Name
  * Dates (such as Month + Day)
  * Don't Assess Before ____ Days
  * ReminderDays
  * Engagement Question
  * Engagement Answers
  * Performance Question
  * Performance Answers



  


I think we'll create an assessment record, which will assign all assessors. It will also include the manager signoff.

  


We will have a record with:

  * Assess
  * AssessmentDefinition
  *   * We will then have an RG of:
    * Assessor
    * Engagement Score
    * Performance Score
    * Engagement Text
    * Performance Text



  


We will restrict the name column (but somehow still allow creating new rows). We will restrict other people's rows, as well.

  


We will use detail variables with a hidden child screen to allow inputing results. We will hide the controls if it's already been supplied.

  


We will assign random numbers to determine the sort order for each of the full-text fields.

  


Hidden

For the hidden child detail screen:

  * Have an expression
  * Have an editable detail variable
  * Have a PushButton called "Next".
  * Stomp this into the array of answers
  * When it's done, hide the "Next" button and give instructions to save.



  


We will show the assessee and the role.

  


Longterm_

We can provide a graph of employee engagement/performance.

  


  


Matthias Miller 11/01/2017: 

  * Have a link to Google setup for non-Gmail accounts??


