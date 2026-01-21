6.1. Data Structure Summary

  


Requirements

Shared Records

  * Contacts (both School and Business type)



  


FBSS

  * EITC Businesses - business type contact records with EITC checked. These are businesses that make direct applications to the state.
  * Direct EITC Application - a business application directly to the state (not an application to an SPE). Every SPE Business will have one or more direct applications to the state.
  * Direct Contributions - a contribution from a business to FBSS. The contribution will designate which schools the money is for. For an SPE, the school amounts are the rolled up totals from all approved member applications.
  * School Applications - an application from a school applying for funds that will be channeled through FBSS.
  * School Distributions - documentation of a distribution of funds to a school.
  * Family - a record representing a family that applies for scholarships via a school.
  * Family Applications - an application for a family for one year. The attending school can be specified for each student in the family.
  * Students - a record storing basic information for each student.



  


SPE

  * SPE Member Business - a business type contact record with Eligible for SPE checked (can also be a direct EITC business).
  * SPE Member Individual - individual type contact records with Eligible for SPE checked. 
  * SPE - a record representing a single Special Purpose Entity. The SPE (e.g. 'SPE X') will need to specify a linked EITC business (e.g. 'Faith Builders Special Entity X LLC') that will have direct EITC applications and that will make direct contributions. There is a 1-to-1 correspondence with direct businesses that are named 'Faith Builders Special Entity X'. The SPE record could become a "Faith Builders SPE Organization" checkbox on the linked EITC business record, eliminating the need for this separate record.
  * SPE Application - an application from the SPE to the state. This is linked to the corresponding business contact's business application for the SPE's Direct Application. This has a one-to-one correspondence with direct applications from SPE's direct business records. This SPE application could potentially be merged into a "SPE" section on the Direct Application record that would only be visible for "Faith Builders SPE Organization" businesses.
  * Membership Application - an application from an SPE business or individual to apply to be an SPE donor (can either be a paper application or an online submission).
  * Online Submission - a record of an SPE application submission from the online portal. Once the contact information is confirmed, the 'Create Application' button will create a linked SPE Membership Application.



  


SPE Look-through

With the merged system, the software for FBSS can look through the SPE's direct contribution to the SPE Members who represent that contribution. This is used to report SPE members' contributions to schools as well as provide thank you postcards addressed to SPE members. 

  * If a direct contribution is from an SPE-linked business
  * We find the Direct EITC Application for this Direct Contribution
  * From the Direct Application, we find the linked SPE Application
  * We then find all Member Applications that were approved as part of the SPE Application
  * From the member application, we can retrieve the postcard address information and the school designations



  


Development Specification

TODO_NM: Our terminology for businesses applying directly to the state (not through an SPE) should perhaps change. They are currently somewhat ambiguously referred to throughout the system as EITC businesses. SPE donations can be for either EITC or OSTC, as can direct donations. We could either refer to them as Direct Application Businesses, or Non-SPE businesses. Revisit terminology with Justin.

  


This would require extensive renaming of macros, labels, menu items, etc.
