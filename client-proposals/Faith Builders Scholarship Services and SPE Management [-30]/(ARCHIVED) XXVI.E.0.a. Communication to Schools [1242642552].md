26.5.0.1. Communication to Schools

  


Requirements

Accessed from: SPE Application detail screen

  


Name: Communication to Schools

  


Level: SPE Approval

  


Subject: Notification of EITC Contributors

  


Send to: School contacts

  


Body:

Faith Builders

Special Purpose Entity

  


#ContactField( EmailContact, ContactPrimaryContactGreeting)#,

On #ContactField( EmailContact, ContactOrganizationName )#’s most recent contribution update from Faith Builders Scholarship Services, you received $#CommaString(SPEAppTotalDesigSchoolAmount(EmailSPEApp, EmailContact), 0, 2)# of EITC funds from #SPEField( SPEApplicationField( EmailSPEApp, SPEAppSPE), SPELegalName)#. Please contact Justin Kauffman at [secretary@FBScholarship.org](mailto:secretary@FBScholarship.org) or 814-789-4518 ext. 244 with any questions about the distribution of funds.

 

Below are the SPE members contributing to that amount:

  


#SPEAppMemberContributions(EmailSPEApp, EmailContact)#

  


Blessed to be partnering with you,

 

#CurrentEmailSenderName#

#CurrentEmailSenderCommunicationTitle#

 

Faith Builders Educational Programs, Inc.

28527 Guys Mills Road

Guys Mills, PA 16327

(814) 789-4518 ext. 245

Fax: (814) 789-3396

  


Development Specification

Target: 1 day

  


I believe this is a RepeatRG on Disbursement RG for any that haven't been notified.
