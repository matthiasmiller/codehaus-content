9\. Scheduled faxes and emails

  


Requirements

The software will be able to send certain documents on a recurring schedule. This could include checklists, for example. The documents can be sent to a fax number or an email address.

  


USER SPECIFICATION

The batch send jobs can be configured only via the online administrator interface. The documents can be sent to any recipient, not just users of the system.

  


Batch jobs can include either a list of documents or a single document.

  


For a list of documents: any document accessible via the phone menu will be able to be sent, except other batch jobs. The batch send job will specify the user who the job is supposed to run as, list the documents/reports to be sent, and a destination number/address. For Compass reports, the batch job will specify the parameters for the report. For Compass reports and Quickbooks reports, the context user will determine the company/builder for the reports. The destination can be a fax number or an email address (this can also be used for IByFax's color faxes.)

  


For a single document: the batch job will hold the document itself. This will reduce the setup and maintenance burden of many recurring checklists.

  


The most recent results of a batch job run can be downloaded from the online administrative dashboard. These could be placed on a flash drive and mailed or emailed to recipients. This facilitates the periodic distribution of a large set of reports which can be printed by the recipient.

  


On demand runs

Batch jobs can be accessed via the phone menu. Each user will only see the batch jobs that are configured to run as that user. (Administrators can see all batch jobs if desired.)

  


Reporting

Users can be configured as a "batch job monitor". These users will be notified by fax whenever a batch job fails to run, and will receive a report at 4:00AM of all batch jobs that completed successfully or failed within the last 24 hours. This report would include for each document:

  * The document name
  * The time sent
  * The recipient



  


Additionally, users with administrative access will be able to retrieve a report listing all of the enabled scheduled jobs. This report will include the user(s), the document name, and the schedule.

  


Schedules

The following schedules will be supported:

  * Monthly, on the Nth date of the month
  * Monthly, on the Nth weekday of the month
  * Weekly, on a certain weekday
  * Daily
  * On demand



  


Supporting additional schedule options will require involvement by AppHosting.zone at additional cost.

  


Development Specification

Batch template

  * Have a batch template record.
    * Schedule
    * RG of documents to send. (What about compass parameters?)
      * Compass parameters:
        * District-vs-builder
        * Date
    * Who to run as
    * Where to send the results (only one recipient?)
  * "Running" the batch template actually just creates a bunch of "queue" transmission records.
    * With a "run" record that holds all the results
    * Record shows the status of all resulting transmission records.
  * Have wsgi entrypoint to download a .zip of all files in the batch job run.



  


The batch job record itself should never end up in the transmission queue.
