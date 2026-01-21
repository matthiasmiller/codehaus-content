3.3. Applications Page

  


Requirements

Jonathan Bergen 03/11/2024: This page will display the following: (prefilled in green)

  * General:
    * Application Year: droplist of all years in which the school has created an application through the portal.
      * "Submitted" (this text will be displayed beside the application year for applications that have been submitted and are now read-only.)
      * "Submit by [date]" (this text will display the associated date from the Silverloom Settings page in XFB system, depending on the school's selection for Option 3) (on and after this date, the application will only show the "Submit" option at the bottom, and will be read-only after the first save.
    * School is OSTC approved: checkbox.
    * Target EITC funds: number.
    * Tuition Schedule explanation: text field, optional if document is uploaded.



Jonathan Bergen 10/30/2024: This document is likely not sensitive, so we could send it to document archive? Would we gain anything this way?

  * Tuition Schedule attachment: upload box, optional if text is entered.


  * Family Eligibility Paperwork:
    * Option 1-A: checkbox, toggles with Option 1-B.
    * Option 1-B: checkbox, toggles with Option 1-A.
  * Discretionary Funds:
    * Option 2-A: checkbox, toggles with Option 2-B.
    * Option 2-B: checkbox, toggles with Option 2-A.
  * Distribution Timing:
    * Option 3-A: checkbox, toggles with Option 3-B.
    * Option 3-B: checkbox, toggles with Option 3-A.
  * Custom Family Income Threshold:
    * Option 4-A: checkbox, optional.
  * Footer:
    * Name of authorized person: text field, required.
    * Date: date field, required.
    * Save: button, saves the form.
    * Submit: launches a "confirm?" popup before saving and locking the form.



  


Sub-pages:

  * Addendum: Displays the Addendum PDF in a overlay.
  * Family Documents: Displays a overlay with the following fields:
    * Amount requested for tuition assistance: number field, required.
    * Amount requested for discretionary user: number field, required.
    * Total scholarship disbursement requested: number field, required.
    * Program: required; Three options: selected any option clears the others.
      * EITC K-12, OSTC K-12, PRE-K
    * Income verification source: text field



  


Development Specification

Jonathan Bergen 05/07/2024: How should the link to the Addendum be stored? Maybe a Silverloom Settings field? [https://www.fbep.org/wp-content/uploads/FBSS-School-Application-Addendum.pdf](https://www.fbep.org/wp-content/uploads/FBSS-School-Application-Addendum.pdf)
