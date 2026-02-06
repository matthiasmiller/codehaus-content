10.1. Invoicing

  


Requirements

The AppHosting Invoices Module would be included with various customizations so invoices can be printed in the database for ads. Individual invoices would also be used for adding, storing, and using credit (see the corresponding sections in this proposal).

  


AppHosting will show the logo provided by John/PNP on the invoice. 

  


Ads are non-taxable, so no tax information is needed on the invoices. 

  


Reporting on Aging Invoices and sales is described in the Reports section of this proposal.

  


Invoices should automatically be addressed to the customer's Billing address type. If there is no Billing address, it should be addressed it to their next available address.

  


Development Specification

Data Restrictions:

  * Full Admins: Full access
  * Publication Admins: Full access for assigned publication, but some items are Full Admin only
  * Standard Users: Full access for assigned publication, but some items are Full Admin only



  


Tim Reitz 11/25/2020: Get logo for the invoice

  


Invoicing individual vs. batch: We'll need to assign ID's to the Ad Details, then have the x30 take an optional Ad ID and only update that Ad if updating for an individual Ad.

  


Cache Publication on Invoices.
