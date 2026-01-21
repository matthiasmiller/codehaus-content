12.2. Data Migration

  


Requirements

The following data is to be migrated into the Solution with the deployment of Phase 1: 

  * Customers (note that these will be imported as Contact records in ProEstimator) 
    * Note that the current addresses need to be parsed into fields (they currently are stored in multi-line text fields, for both Customers and Quotes)
  * Base Items (note that these will be imported as Sales Item records in ProEstimator)



  


The following data might be migrated into the Solution with the deployment of Phase 1:

  * Proposals
    * This would include the following data from the Power App:
      * Quotes (note that these will be imported as Proposal records)
      * Quote Sections (note that these will be added to Proposals)
      * Quote Groups (note that these will be added to Proposals)
      * Group Items (note that these will be added to Proposals)
    * There are various approaches for importing Proposals:
      * Option 1: Historical Data Import: historical data from the Power App could be migrated to the new Solution. 
        * This would be priced separately (no estimate included in the initial Phase 1 proposal).
      * Option 2: Linking: If migrating Proposals is difficult, or if it seems unnecessary, a read-only field could be added to Contact records to display a list of links to that customer's Quotes in the Power App, since the Power App would remain available for at least the near future. 
        * This can be included as part of the Contacts Import.
    * Details to consider if Quotes are imported (Option 1 above):
      * For importing call notes, 
        * Lead source items should be added to the "Lead Sources" list InImport (via the "Lead Source" field). 
        * Decision process items: 
          * The plan is to replace all references to "Speed" item with "Availability" ("Speed" is being merged into "Availability", with only the latter being included in the Silverloom solution).
          * The Power App solution has an option for "ALL", which will need to be considered and handled in a helpful way. One option is to replace all references to "ALL" with "Other" and set the corresponding "Decision Process Note" to "Quality, Speed, and Availability". 
        * Cracks/Potholes data should be imported into the "Pavement Condition" text field. 
      * Job Contacts from Quotes ideally will be added automatically to the corresponding Customer's Contact record. 
      * The existing "Printout Price" (if included on Quotes) should be imported into the "Total Proposal Price $". 



  


For all data migration that is done, CodeCrafters will provide the input format for migrating data from SharePoint (Power App) lists into the SIlverloom ProEstimator Solution, and probably will also provide the work of cleaning up the data and performing the actual migration. 

  


This work is to be done on a "Time & Materials" basis. This proposal includes an estimate for migration of Customers/Contact and Based Items/Sales Items. The cost and time spent on data migration will vary based on how much data is imported and how "clean" the data is. As mentioned above, an additional estimate can be provided for importing Proposals, if desired. 

  


Other Notes: 

  * N/A



  


Development Specification

Tim Reitz 07/26/2025: Here is an incident and linked PC for this: 

  * [[[IN11854](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11856&)]] - ZLP - Data Migration
  * [[PC0181483]] - ZLP - Phase 1 - Data Migration


