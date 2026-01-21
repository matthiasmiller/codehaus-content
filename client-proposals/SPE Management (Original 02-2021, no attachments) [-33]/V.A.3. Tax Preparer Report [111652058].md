5.1.3. Tax Preparer Report

  


Requirements

This report will show all admitted SPE members.

  


It will prompt for:

  * SPE (required; list of SPEs)
  * Tax Year (required; number field)



  


Its columns will include:

  * Member (name of individual or business)
  * Address
  * County
  * City
  * State
  * Zip
  * SSN/EIN 
  * Entity Type
  * Owner SSN
  * PA Revenue #
  * Total Contribution ($ amount)
  * Membership % (4 decimals)
  * Tax Credit ($ amount)



  


The report should be sorted by Member.

  


The membership percentage is calculated using each member's individual contribution as a percentage of the total of all contributions for the SPE for that tax year. This includes all members, regardless of whether they are Year 1 of 2 or Year 2 of 2.

  


The tax credit is calculated as 90% of the total contribution.

  


NOTE: All reports can be exported to Excel. This report can be used to submit information to the accountant.

  


Development Specification

Add a hidden, unchangeable system switch for the 90% for the tax credit calculation.

  


Ellis Miller 02/08/2021: 

[ ] Note: This is a report based on the Member Applications, filtered by SPE and other fields. 

[ ] All the columns through PA Revenue ID are actually from the Member Application's Contact record.

[ ] Total Contribution is from the Member Application

[ ] Membership % is Member Total / SPE Total (from the SPE record, not from the rpt)

[ ] Tax Credit is Round(TotalContrib * Config_TaxCreditRate, 2) (set at 0.9)

Target: 2 Days
