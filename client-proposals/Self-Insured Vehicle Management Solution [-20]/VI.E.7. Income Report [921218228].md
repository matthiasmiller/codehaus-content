6.5.7. Income Report

  


Requirements

TODO_: Tim Reitz 07/19/2025: Wait to make any updates to this spec until after the Multi-State feature items have been documented. Then let's build out the spec more here.

  


Overview: This is a custom report of income, based on Invoices, with various filtering options. 

  


Accessed from: Admin | Admin Reports | Income Report. 

  


Title: Income Report 

 

Columns: 

  * Current Agent (no heading label; link to open the Agent's contact record) 
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

Change Requests: 

  * Tim Reitz 06/18/2024: [[[IN9141](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9143&)]] - ZWA - Changes to Liability & Collision Income Report (prev. "Add columns to...")
  * Tim Reitz 06/18/2024: [[[IN9648](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9650&)]] - ZWA - Income Report & Deposit Breakdown Reports - Clarify Date Labels
  * Tim Reitz 08/19/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident


