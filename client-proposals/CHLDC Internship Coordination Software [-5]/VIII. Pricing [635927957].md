8\. Pricing

  


Requirements

The initial cost for this system is $3000. This includes development, setup, and training on the use of the software. Bilingual (English + Spanish) support for the participant-facing website is available for an additional $500. One on-site training visit is included. If accepted by April 15, we will credit half of the initial proposal toward development, bringing the cost down to $2500. 50% payment is required at the start of development, and the balance upon completion.

  


Hosting

The software will be hosted on AppHosting.zone's cloud hosting infrastructure. This includes AppHosting.zone's comprehensive backups, monitoring, and security protection.

  


The normal rate for this hosting is $50/month. Due to the seasonal nature of CHLDC's programs, and thus the sporadic nature of access, we will discount this rate to $25/month. This includes 5 administrative users and an unlimited number of participants.

  


Ongoing changes

This proposal covers the initial development, setup, and training for the 2018 SYEP program. Future identical programs are supported in the software, but if additional changes are required to accommodate those programs, those changes will require additional proposals and cost.

  


Development Specification

  * Add fields - see “Administrative interface overview” section. (1 hour)
    * For choices, be sure to make choices read only once they have been approved.
    * Add OnChange button to clear choices.
    * Add link to re-send welcome email.
  * Indices:
    * Student secret key
    * Work site programs
  * Build imports, as soon as we get sample files. (2 hours)
    * Add a couple fake obsolete programs with students and work sites attached to test filtering.
  * Build basic reports - be sure to consider programs (1 hour)
  * Build import to mock up students making choices. (0.5 hours)
  * Build matching report. (2 hours)
  * Front-end site:
    * Build report to get list of work sites. (0.5 hours)
      * Use student secret ID as key.
      * Add column for exclusive site.
      * Don’t include over-booked sites.
      * Include GPS coords.
      * Include multiple rows for multiple job titles.
    * Build report to get participant’s info (name, email, GPS coords, etc). Or use QueryRecords? (0.5 hours)
    * Build import to set choices. (0.5 hours)
    * Tie together wsgi site:
      * Basic layout (2 hours)
      * Show list of sites using JS. Make them first pick their first choice, then their second choice, then third. (2 hours)
      * Handle exclusive sites! They should get a message saying that a work site has specially picked them, and they have to decline it to see other sites. (1 hour)
  * Build remaining reports. (2 hours)
  * On-site training and setup (2 hours)



  


  


Hide ContactOrganization
