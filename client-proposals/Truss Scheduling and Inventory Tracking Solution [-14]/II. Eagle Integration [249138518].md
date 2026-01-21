2\. Eagle Integration

  


Requirements

Syncing with Eagle

Eagle's software is the source of truth on all things related to jobs. We will need to pull in all information from there.  

  


Eagle has committed to providing us XML feeds that connect directly our software, allowing data to get sent to our system in real-time. (This is especially important because of the EWP have dedicated runs on Tuesdays and Thursdays, with a noon cutoff the day before.)

  


Eagle will also provide data for the initial import. We only plan to pull in orders from the past year and a half. This will also allow us to do "ad hoc" syncs if something misfires with their integration.

  


Eagle will also provide a way for importing all SKUs. This will be handled for the initial conversion, and can optionally be run if changes are made to SKUs in the management software.

  


The management software will have materials for each possible length of wood. You will need to enter any missing lengths for all types of wood, and all materials will need to be assigned a SKU. These SKUs will automatically be pushed across into the new system, and inventory will handle them as expected. Adjustments to inventory based on short pieces will be handled outside the new system. If you want to discontinue using certain lengths, you would need to update it in Eagle. This would prevent it from being sent across. If you want to start using new lengths or types of wood, you would need to run the one-time migration to update the new system.

  


Once the system is live, we are planning to pull across all jobs, even if they are simply quotes or are incomplete. They will need to be manually flagged as ready for production.

  


Integrating with AppHosting.zone

This system will be integrated with an inventory tracking system. For that reason, each job will be considered as a "Finished Good" internally. However, most of the menu options will still reflect the Job terminology.

  


We will be pulling the following information from Eagle. For customers:

  * Customer ID
  * Customer Name



  


For jobs:

  * Job ID
  * Customer (drop list to allow reporting)
  * Customer PO Number
  * Description
  * Delivery Address (this is the Ship Address from Eagle)
  * Additional Material Notes
  * Materials
    * SKU
    * Description (read-only)
    * Qty
    * Board Feet



  


For materials:

  * SKU
  * Description
  * Length



  


The job will automatically update with any material changes from Eagle. If materials change after a job has pulled for production, this will cause inventory totals to shift. This will be corrected the next time inventory adjustments are completed.

  


Development Specification

Matthias Miller 02/13/2020: The sync would simply use the web services framework with an x30 (or x30list if needed) import.

  


Here is a sample XML file: [[File:cussewagoexport-1.xml]]. I'm thinking we could probably auto-create sales items as needed from the XML import.

  


Matthias Miller 03/03/2020: Assign a price, then do that length.
