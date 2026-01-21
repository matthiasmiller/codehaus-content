4\. Inventory

  


Requirements

Item

Each SKU would have an option to use inventory tracking. This would be enabled by default, but could be turned off for services charges or untracked items.

  


Inventory Adjustments

We will provide a way of adjusting the inventory on specific items. The inventory adjustments would have:

  * Inventory Adjustment ID
  * Date
  * Production Location
  * Spreadsheet of:
    * SKU
    * Description (read-only; autofilled)
    * Quantity



  


All SKUs should be displayed when entering the inventory adjustment. For convenience, it would be nice to be able to enter absolute values, even if the adjustment is stored as a delta.

  


Orders

All orders would automatically adjust inventory as soon as the materials are pulled for production. It doesn't specifically matter whether the adjustment is considered a beginning-of-day or end-of-day adjustment, since inventory will only be off a maximum of one day.

  


Inventory Reporting

For inventory management, we would provide a report that prompts for production location and date. This can be a past, present, or future date. It would show inventory totals as of that date:

  * SKU
  * Description
  * Quantity



  


Odd pieces would automatically be assigned their own SKU when they come into the system. These would be accounted for manually when inputting inventory adjustments.

  


Development Specification

Matthias Miller 02/14/2020: Josh is comfortable with an end-of-May timeline for his inventory tracking pieces.

  


His documents:

  * [Inventory Management Design - Shared with ABC](https://docs.google.com/document/d/1ZUopiU6LvTKjxrolawvN6cVXghSFYoyXBy7UTlXwDnU/edit?usp=sharing_eip&ts=5e46ba37 "https://docs.google.com/document/d/1ZUopiU6LvTKjxrolawvN6cVXghSFYoyXBy7UTlXwDnU/edit?usp=sharing_eip&ts=5e46ba37")
  * [Inventory Management Design](https://docs.google.com/document/d/1BbrZJVmI7AUWl6furs_YH145GMve8aQrNGUNOz26HyA/edit?usp=sharing_eip&ts=5e46ba2e "https://docs.google.com/document/d/1BbrZJVmI7AUWl6furs_YH145GMve8aQrNGUNOz26HyA/edit?usp=sharing_eip&ts=5e46ba2e")



  


Matthias Miller 02/17/2020:

  * [[File:MaterialSummary.pdf]]



[[File:MaterialSummary.xls]]
