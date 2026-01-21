11\. HR: Onboarding/Exit Tasks

  


Requirements

We need a way to manage onboard/exit tasks. This will be associated with each role, and will be initiated when the user changes a role.

  


We will introduce accountability, requiring individuals to sign off on the task and providing a way for an administrator to ensure that these tasks are completed.

  


USER SPECIFICATION

When we create the system, we will define HR tasks. Each task will specify:

  * A name, which will be used for internal reference.
  * A type, which will be either "Onboarding Task" or "Exit Task"
  * Trigger role (which role causes this task to be initiated)
    * Single role
    * Multiple roles
    * All roles
    * All roles except... (used to help Matt/Nate with onboarding)
  * Assignee role
    * The individual themselves
    * An upline (list of uplines, defaulting to the direct upline) -- this is required since the TS manager may have a hierarchy of multiple depths
    * An unrelated role (includes everyone in the role, but the task is only completed for 1 individual).
  * Compensation Method (required to handle compensation agreement).
    * Any
    * Hourly
    * Salary
  * Trigger task:
    * ____ days before
    * ____ days after
  * Email subject
  * Email body
  * Attach target job description (checkbox to include a PDF attachment with the latest job description)
  * Remind ____ days
  * To complete:
    * Require Acknowledgment
    * Require Completed Form
      * This will be linked to a Survey
    * Require Signature?
      * If so, we will require a statement:  "I have read and understood the job description"
      * We will file a PDF of the statement to the personnel record and show them the form they agreed to.
  * Repeat task:
    * Every ______ months. This will repeat based on the last completion date. (This is necessary for DOC applications to work correctly.
    * Every Month/Day of the year. (This would be used for the W-4.)



  


Email Format

The email body will accept a few keywords:

  * {ToFirstName}
  * {ToDisplayName}
  * {FromFirstName}
  * {FromDisplayName}
  * {TaskCompleteLink}
  * {VacationDays}
  * {HourlyWage}
  * {AnnualWage}



  


The {TaskCompleteLink} keyword will become a “click here” link that allows the user to indicate the task is complete.  For example:

  * Once you’ve completed this training, please {TaskCompleteLink} to mark this training as complete.



This gets displayed as:

  * Once you’ve completed this training, please click here to mark this training as complete.



  


Reminder Emails

We will also have a “Remind Every ___ days”. The email will be based on the other email.

  


Subject: Reminder: {OriginalSubject}

Body:

{ToFirstName},

  


We recently sent you an email with the subject “_______”. If you have already completed it, please {TaskCompleteLink} to mark it as complete.

  


If you have trouble logging in, please contact the office at (719) 275-5242.

  


Thank you.

  


{FromFirstName}

  


These emails will be from their direct upline (the manager). They will also Bcc the direct upline (the manager).

  


Visibility and Permissions

Task definitions will only be visible and editable if:

  * An upline of the target role
  * Either the assignee or an upline of the assignee



  


As an example, for some of these forms, we will email Nate with links to PDFs (or instructions), and we will also email the new hire to see Nate to review these forms.

  


Completion

Each task will be confirmed with an electronic signature. Once the task is complete, we will file a PDF copy of the document. The user will be redirected to the signed PDF.

  


Email on Completion

If a task has multiple assignees (i.e. houseparents), the email will be sent to both of them. However, it will be tracked as completed if either of them complete it.

  


When the task gets completed, we will send out an email to all OTHER assignees, such as:

  


Subject: Completed: {OriginalSubject}

Body:

{ToFirstName},

  


We recently sent you an email with the subject “_______”. This has been completed by _______, so there's nothing more for you to do.

  


Thank you.

  


{FromFirstName}

  


Changes Affecting Existing Assignments

Changing any of the task's settings will update any pending assignments. This is important to ensure nothing gets dropped during a manager transition.

  


If a personnel has received an initial email, the reminder will continue using the new reminder schedule based on the last email sent.

  


Email Schedule

These emails will be sent out daily at 5 AM.

  


If we are scheduled to send an email 10 days before the start date, but the start date isn’t entered until 2 days before, we will simply send the email the following day.

  


Accountability

We will have a way to view all pending onboarding tasks. This will show:

  * Assignee
  * Personnel
  * Date
  * Subject



  


It will be sorted from oldest to newest, and it will be grouped in two sections: Waiting for Completion and Waiting to Send.

  


You will be able to see your own tasks, as well as the tasks of all your downlines.

  


Signed Forms

We will use a cursive font for electronic signatures on the I-9 and W-4

  


Skipped Tasks

Skipping a task will require a simple text box to be filled in with an explanation.

  


One-Time Tasks

We will allow tasks to be run arbitrarily. This will be required for things such as Direct Deposit.

  


Development Specification

We will need to track the date each email is sent for two reasons:

  * We might not always get to send the email on the scheduled date. If it's scheduled to be sent 10 days before and the role is added 2 days before, for example.
  * The user might change the schedule.



  


My proposal is to have a hidden RG that includes:

  * RoleID (associated with role)
  * HRTask
  * LastReminderDt
  * CompletedBy Contact (blank until complete)
  * CompletedBy Date
  * CompletionSignature
  * CompletionPDF



  


We could then have a virtual RG to show task assignments.

  


Question:

  * Restrictions/permissions for archived documents -- if it's a hidden memo, they CAN'T delete it. Ever.
  * How to handle the archived PDFs? The signature will be a memo on the hidden RG



  


I think what we'll do for these forms is:

  * Create a Survey to get all relevant information
  * Allow survey's to be tied to a PDF, which will include the template PDF, as well as a column for field names
  * You can generate a PDF from the survey results
  * We will have a special entrypoint for these tasks that will lead them through the survey. 
  * Thus the hidden RG will contain a reference to the survey
  * When the survey is complete, we will generate and archive the PDF.



  


Notes:

  * Since this is set on a personal basis (and we need to store hourly vs. salary), I think the exact form gets determined based on the contact themselves.
    * This can be done with a custom PDF and a survey


