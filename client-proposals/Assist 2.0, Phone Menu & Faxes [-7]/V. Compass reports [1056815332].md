5\. Compass reports

  


Requirements

The system can be used to access reports from Compass. These reports will be run on demand, and thus will have the most recent data available. 

  


Availability of reports will depend on development in the Compass system.

  


USER SPECIFICATION

Compass reports will be accessible from both the phone menu and via fax cover sheet. Reports may have no parameters, or may have several:

  * A single date
  * A date range. This consists of a start and end date. The user will be able to select a custom date range, or choose from the following predefined options:
    * Yesterday
    * Last week (the Monday - Saturday of the prior week)
    * Last month (the 1st through the end of the month of the prior month)
    * Last quarter (the 1st of the first month through the end of the last month of the prior quarter)
    * Last year (Jan 1 - Dec 31 of the prior year)
    * Week # (1 - 53)
    * Week range (start and end week #)



  


If the report accepts a date, the report definition will specify a default set of date(s). To use the default dates, the user can fill in the appropriate box on the cover sheet, or press 0 in the date prompt above.

  


Reports will be defined in the software in such a way that Jason will be able to add new reports that he has built without involving AppHosting.zone. Reports that take a new kind of parameter will require additional programming.

  


When the report is accessed via the phone menu or fax cover sheet, the software will automatically recognize the user based on Caller ID and select the corresponding builder or company.

  


Interface for Jason

For Jason, the online interface for the software will have a Compass tab. Jason will not have access to the normal Administration tab.

  


Reports   View all Compass reports  
| Activity   Recent report requests|   
  
  
---|---|---  
  
  


Diagnostic console

Sometimes, particularly when adding new reports, the interaction between the system and Compass will fail. The system will provide a diagnostic console for Jason that includes each request to Compass with details about the request and what response Compass provided.

  


Available Reports

  * Aged Report
  * Delivered Sort Old Report
  * Salable Inventory Report
  * Sales Report



  


Development Specification

Need to talk about parameters. What parameters can he set up?

  


Report record

  * URL base
  * Query parms
    * Name
    * Type (String, Date)
    * Value (hardcoded, or ask (only for dates))



  


  


The structure of parameters also affects batch jobs.
