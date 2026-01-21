3.2.3.5. Incorporating Existing Incidents

  


Requirements

Since Think Ink has been using the core system for a while prior to design and development of the main customization work, there already are incidents in the database. These incidents will all need to have a Type set by the time the customizations are live in the Solution. 

  


Existing Incident Types will need to be removed, and some or all of them could be replaced with corresponding Workflows. 

  


Think Ink will migrate existing incident types prior to deployment using a custom user report provided to them by CCI/CH.

  


Development Specification

This section is included to alert the client and us that there will be some time invested in planning and executing this work.

  


We need to include a few hours of support time from Tim for deployment. We're planning to help them set up workflows, then clone [https://think.apphosting.zone/Reports/Standard/Std_Incidents_(helper)?&](https://think.apphosting.zone/Reports/Standard/Std_Incidents_\(helper\)?&) and make Type, Workflow, and Stage be editable.
