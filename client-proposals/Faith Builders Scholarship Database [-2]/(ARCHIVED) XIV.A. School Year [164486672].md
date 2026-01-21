14.1. School Year

  


Requirements

TODO_NM

  


We will track information for each school by school year.

  


We will have an annual process that creates new applications for all active schools (excluding schools with no prior applications). We will default the information from their latest application. However, we will flag these applications drafts until we receive a confirmation from the school.

  


Fields

  * Year - This is based on the start of the school year.
  * All for Tuition? - This information indicates whether the school wants discretionary funds or not. When creating a distribution for this school, it will default the discretionary funds to 0% if "All for Tuition?" is checked. Otherwise, it will default to 13%.
  * "Paperwork" is an option between "FBSS Managed" or "School Managed"
  * "School Type" is a choice between:
    * "September School" (using funds from prior year)
    * "November School" (using funds from current year)
  * Custom Income Limits:
    * Custom Base Salary
    * Custom Per Dependent Amount
  * Received Confirmation from School (date) - The application will appear as a draft until this date is filled in.



  


Development Specification

Matthias Miller 04/06/2018: 

  * This can be keyed off "SchoolID-Year" as the name.


