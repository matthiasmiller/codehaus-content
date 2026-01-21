13.3.7. Note Record

  


Requirements

This replaces the Notes memos on all the standard records. It should show up on each detail screen as a read-only Notes memo (concatenated by Note ID), with a link to a New Record that takes a Type and a Record Number.

  


  * Overview Section
    * Record Type (list of Database levels that support notes; read-only)
    * Needs Followup (checkbox)
    * Linked Record (hidden fields)
      * ID (hidden number field for custom DB level)
      * Contact, etc for all lookup types (required to handle merging)
    * Record (read-only description generated based on Type + Record ID)
    * View Record link
    * Assignees (default to blank; multi-select list of any active user profiles; store as list name; display as display names; visible and required if Needs Followup)
    * Created By ("Created By Duane Burkholder on 04/16/2018")
      * hidden fields:
        * Created By (read-only; linked to User Profile, stored as list item; displayed as display name)
        * Created On (read-only; Today)
    * Due Date (visible if Needs Followup)
    * Note Type (list of Note Types; required; uneditable if type was set to "System Note"; editable if Template is blank; otherwise the Note Type from the template; )
    * Email Note (link to an email merge with SendingEmail as From, ReplyTo as current user name/email, To as defaulted ask prompt, subject as ask prompt, body as Note Contents)  \- requires save before run
      * Multi-select prompt for the person who gets it (list of active contacts; show email in the drop list so people can make sure it's the right one); ask prompt for subject line
      * Default the ask prompt based on levels:
        * Contact- default to that contact
        * Contract- default to the current primary/secondary customers
        * Product - Manufacturer
        * Payment- customer
    * Print Note (PDF) (generates a PDF, 1" margins with the Contents embedded)



  


Contents Section:

  * Note Template (drop list of note template records)
    * When a user selects a template:
      * If the Contents memo is not blank, a warning appears stating that selecting the template will replace the current note contents. Contents are immediately replaced and Requires Followup is set to the template value.
      * If the Contents memo is not blank, the warning prompts the user to confirm via a button. Once confirmed, contents are replaced and Requires Followup is set to the template value, allowing the user to then edit the note as needed.
    * Confirm (button; visible if Contents memo is not blank and Template is changed; sets Contents and Requires Followup to template values)
  * Contents (memo; defaults to User Name + Current Date)
  * Search Text (hidden string field with a text version of the note for searching; no audit trail)
  * Completed (checkbox that sets read-only fields to log the user who completed it and the date; always editable; visible if Needs Followup is checked)



  


Record Restriction:

  * Only visible for Admins if Note Type is "Confidential"



Seth Miller 10/13/2025: TODO_Permissions

  


Linked Record Types:

  * Contact (manufacturer, customer, rental company)
  * Contracts
  * Contract Definitions
  * Payments
  * Product
  * User



Notes Section on above records:

  * "This record must be saved before creating a linked note." (label, visible for new unsaved records)
  * New Note (opens a new note record; populates the Type + Linked Record, visible if the record has been saved)
  * View Notes (report link; opens the My Notes report)
  * Notes (read-only memo that concats based on record Type + record ID, sorted in order of Note ID; newest first; including up the number of notes specified in the "Number of notes to display" system switch)



Promised Payment Note Created on 05/01/2025 by Matthias Miller

[Note Contents]

  


Scary Collections Letter Note Created on 04/21/2025 by Seth Miller

Contents omitted.

  


19 Additional Notes Omitted.

  


  * User Profile Record
    * Validate against Duplicate Full Names for active user profiles (standard)



  


  * Reports
    * New Note (ties it to the current user's user profile record)
    * My Notes (all notes needing followup)
    * Search Notes (easy way to search all notes. Full spec in the reports section)



  


  * Can Delete Record: can be deleted unless the note type is "System Note"



  


Development Specification

  * Dev Spec
    * Macros for list of Active User Display Names + mapping to User Profile


