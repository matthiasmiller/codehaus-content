4\. Approving participant's work site choices

  


Requirements

While the participants specify their preferred work sites, CHLDC staff is ultimately responsible to match participants with work sites. This may include approving the participant's first, second, or third choice; or it may involve manually specifying a work site for a participant. The software will enable this matching, along with tools to better understand participant engagement. CHLDC staff will be notified about participant choices requiring approval.

  


USER SPECIFICATION

Algorithm for proposing approvals

Because multiple students can request the same work site, the possibility of a participant not getting their first choice exists. For this reason, and because the student may pick a site that they are not eligible for, participants should pick three choices. The software will proposal match approval on a first come, first served basis, while displaying necessary information to CHDLC staff to approve or disapprove the participant's choice.

  


Approve Participant Choice

When participants make their choices on the website, those participants will show up in this report. The report will show students who have made choices, but who have not had their choices approved.

  


This is the primary interface for approving participant choices. It will have checkboxes or buttons to approve the first, second, or third choices. It will include a link to the participant, where manual or uncommon operations can be done.

  


Note that CHLDC staff is responsible to ensure that potential participants meet the work site's criteria.

  


Participants Without Choice

This report will show all participants who have not made a choice, along with their contact information. This allows CHLDC staff to reach out to them and encourage participation.

  


Matching Results

This will show all participants who have been matched to a work site, and whether they got their first, second, or third choice.

  


Participation Rate Graph

This will show the # of participants who made choices over the past sixty days. This may be useful for better understanding overall engagement.

  


Development Specification

We'll want a nightly email export that shows the participant choices that have not been approved.

  


The overall flow of matching:

  * At the start of the season, a list of participating work sites is imported into the software.
  * A batch of 100-200 users is selected by NYDOE lottery. They are emailed by the DOE.
  * These students are exported out of YEPS and imported into the software.


  * During the night after they have been imported, the software emails them a link to make their choices.


  * During Wednesday - Friday, the participants make their choices.
  * After they have made their choices (during the same time period), CHLDC staff approve the choices, verifying criteria.


