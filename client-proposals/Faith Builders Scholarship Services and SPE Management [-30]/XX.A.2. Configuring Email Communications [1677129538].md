20.1.2. Configuring Email Communications

  


Requirements

A template system is used to send email communications for both FBSS and FBSPE, using the "FB Email Template" records.

  


The number and names of the templates are unchangeable. Adding a new template requires a coding change and system update. The file attachments are only changeable by a coding change.

  


The email subject and email body for the template can be configured by system users.

  


All communications are previewed before being sent.

  


Each record tracks the history of past communications. This avoids sending duplicate communications. 

  


The Contact record and the Member Application record contain an embedded spreadsheet (RG) of Communications have a link to a report of email communications.

  


Development Specification

Ellis Miller 02/14/2021:

  


  


[ ] Simplified FB Email Template Lookup record

[ ] Investortools-owned list of lookup items (one per template)

  


[ ] Editable FBEmailLevel drop list with options for:

Contact

Member Applications

SPE Approval

Editable so that we don't have to ship lookup records.

  


[ ] Add Subject and Body expression fields for each of the levels (visible based on Level):

FBEmailSubjectExpr_Contact

FBEmailSubjectExpr_MemberApp

FBEmailSubjectExpr_SpeApp

FBEmailBodyExpr_Contact

FBEmailBodyExpr_MemberApp

FBEmailBodyExpr_SpeApp

  


[ ] Add expression requirements for each of these for the right level.

[ ] One report alert that gives warnings if any of these fields are invalid.

Target: 1.5 days

  


[ ] Basic Report to show the email templates

Target: 2 hours

  


[ ] Add editable in import SentCommunications RG to Contacts and Member Applications.

[ ] The Type field is of type FBEmailTemplate

[ ] Sent On is a date

[ ] Reverse sorted by Date

Target: 1 day

  


[ ] Adding needed links to various screens as specified.

Matthias Miller 08/10/2021: This will simply be running the preview report with the appropriate ask prompt filled in.

Target: 4 hours

  


[ ] Each of the template exports will use a ModifyRecordsAfterExport template export to set the Communication Type RG row:

ContactSentCommunications: NewRG|

ContactSentCommType = "Notice of This Email Type"|

ContactSentCommDate = Today

Target: 4 hours for first one, others should be cloned

  


Matthias Miller 08/10/2021: Addition

[ ] Add a checkbox called "Evaluate template from email record"

[ ] Add an "FBEmailSubjectExpr_Email" and an "FBEmailBodyExpr_Email". Show these if the checkbox is checked. Otherwise, show the level-specific fields.
