3.2.3.4. System Switches - Policy # Configuration

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Related to the Policy #: These System Switches can be set for a Plan's specific situation, with the intention of being set in one of the two following ways by the development team as part of the initial configuration:

  * Option 1: One policy number for the whole Plan. The number is provided to CCI and set in the System Switch to apply across the whole system. It may contain the prefix "SI" (for "Self-Insured").
  * Option 2: One policy number for each member/client. The details are configured in the System Switch by CCI, and an individual # is assigned to each client (normally based on the Contact ID). It also may contain the prefix "SI". 



  


  * Label: Contact Policy Number 
    * Code: Config_ContactDisplayPolicyNum 
    * Field Type: String expression 
    * Description: "This sets the Policy # (either per-Plan or per-Member), to be evaluated on the Contact record. 
    * Default Value: N/A
    * Set to: As described in the "Dev Configuration - System Switches (Plan-Specific)" section of the proposal. 
    * Other Notes: 
      * The set value for this System Switch is read-only in the Solution and hard-coded on a Plan-by-Plan basis (configured by CCI).
      * For Option 1 above (one Policy # for the whole Plan), the Policy # is hard-coded here. For Option 2 (one Policy # per member), the logic is hard-coded here, to set the Policy # as needed. 
      * Technical details: This is a string expression evaluated on the Contact.



  


Development Specification

Ellis Miller 09/04/2024: 

[ ] This is a readonly Contact-level string expression system switch. In the base catalog, it can be defined as a hardcoded string "99999". It will be overridden in derived catalogs.

_EM: Tim Reitz 04/30/2025: Is this still relevant? 

_VA: Tim Reitz 05/05/2025: Per Ellis, no, we won't default it at all since it's going to be defined in the outer catalogs only. 

  


Included with above.

  


Murshid Rahman 04/29/2025: CLS Job ID [[PC0178321]].
