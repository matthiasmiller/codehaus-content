26.0.0.2. FGI Cost Estimates (ARCHIVED)

  


Requirements

Cost estimates will be defined first as a % by FGI Cost Categories. The FGI Cost Items will be broken down as a % of their respective category.

  


Add a new FGI Cost Estimate record:

  * Summary section
    * District (required; list of districts)
    * As-Of Date (required)
    * Name (automatic and read-only; "IN-2022-10-22")
  * Cost Categories section
    * Labor % (number; 0-2 decimals)
    * Material % (number; 0-2 decimals)
    * Overhead % (number; 0-2 decimals)
  * Cost Items section, embedded spreadsheet of:
    * FGI Cost Category (read-only; automatic)
    * FGI Cost Item (required; list of FGI Cost Items)
    * FGI Cost % (required; 0-2 decimals)



  


Migration:

  * This will place the Inventory % settings on the company record, as well as the Inventory Material % on the district record. To migrate, keep the old settings in place, create the new settings, then have someone manually migrate these settings in the live system before removing the old settings.



  


NOTE:

  * Automatically populate the Cost Items section when creating a new record, OR have a way to automatically add missing cost items.
  * Validate that all the sub-items of each category add up to 100%.
  * We would not want to adjust these percentages for any historical dates.
  * The Wholesale % on districts is NOT related to FGI numbers.



  


Future Enhancements: If we ever want to start tracking costs on a per-builder basis, we will need to:

  * Be able to create FGI Cost Estimates on a per-company level
  * Be able to filter buildings by builder when allocating financial costs



  


Development Specification

TODO_CCI: Keep the BuildingInventoryAmt macro and update it appropriately.
