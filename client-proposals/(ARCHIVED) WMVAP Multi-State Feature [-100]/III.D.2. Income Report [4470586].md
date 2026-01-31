3.4.2. Income Report

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Overview: This is a custom report of income, based on Invoices, with various filtering options. 

  


Accessed from: Admin | Admin Reports | Income Report. 

  


Title: Income Report 

 

Columns: 

  * Agent (no heading label; link to open the Agent's contact record) 
  * Liability Units
  * Liability $
  * <Alternate text for Collision - Short label> Units 
  * <Alternate text for Collision - Short label> $
  * <Alternate text for Collision - Short label> Entry Fee Units (visible if Solution uses <Collision> Entry Fee) 
  * <Alternate text for Collision - Short label> Entry $ (visible if Solution uses <Collision> Entry Fee) 
  * Cargo Units
  * Cargo $
  * High Risk Units
  * High Risk $
  * Credit $
  * Other $
  * Total $



  


Grouped by: Fund

  


Sorted by: N/A

  


Filters: 

  * Filter Dates (drop-list of Date Range, Period Year)
  * Invoice Date Start (blank = all) (date; visible if Filter Dates is set to "Date Range"; looks at the Invoiced Date)
  * Invoice Date End (blank = all) (date; visible if Filter Dates is set to "Date Range"; looks at the Invoiced Date; defaults to the current year)
  * Period Year (blank = all) (multi-select list; visible if Filter Dates is set to "Period Year"; looks at the Invoiced Date)
  * Invoice Status (required; drop list of Invoiced, Paid, and Invoiced & Paid; defaults to Invoiced & Paid)



  


Menu Visibility: Admin 

  


Other Notes: 

  * N/A



  


Development Specification

Ellis Miller 09/05/2024: 

  


1 Hour to hide column conditionally
