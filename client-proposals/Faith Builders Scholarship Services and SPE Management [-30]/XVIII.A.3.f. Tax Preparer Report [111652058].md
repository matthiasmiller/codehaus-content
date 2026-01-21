18.0.3.6. Tax Preparer Report

  


Requirements

This is a report of admitted SPE Member Applications.

  


Accessed from: Faith Builders SPE | Financial Reports | Tax Preparer Report

  


Title: Tax Preparer Report

  


Columns:

  * Member
  * Business Name
  * First Name
  * Last Name
  * Address
  * City
  * State
  * Zip
  * SSN/EIN
  * Entity Type
  * Owner SSN
  * PA Revenue ID
  * Total Contribution (total type = sum)
  * Membership % (4 decimals; calculates Total Contribution / Total Admitted Amount; total row shows sum)
  * Tax Credit



  


Filters:

  * SPE (required; drop-list of SPEs)
  * Tax Year (required)



  


Sorted by: Member

  


Additional notes:

  * The membership percentage is calculated using each member's individual contribution as a percentage of the total of all contributions for the SPE for that tax year. This includes all members, regardless of whether they are Year 1 of 2 or Year 2 of 2.
  * The tax credit is calculated as 90% of the total contribution.
  * All reports can be exported to Excel. This report can be used to submit information to the accountant.



  


Development Specification

Change Requests:

  * Ben Reitz 01/06/2026: [[[IN11092](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11094&)]] - XFB - SPE - Tax Preparer Report - Update columns



  


Add a hidden, unchangeable system switch for the 90% for the tax credit calculation.

  


Ellis Miller 02/08/2021: 

[ ] Note: This is a report based on the Member Applications, filtered by SPE and other fields. 

[ ] All the columns through PA Revenue ID are actually from the Member Application's Contact record.

[ ] Total Contribution is from the Member Application

[ ] Membership % is Member Total / SPE Total (from the SPE record, not from the rpt)

[ ] Tax Credit is Round(TotalContrib * Config_TaxCreditRate, 2) (set at 0.9)

Target: 2 Days
