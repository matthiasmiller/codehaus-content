2.1. Glossary

Overview: The purpose of this glossary is to provide a description of key terms, roles, and other things referred to in this proposal. These are listed below: 

  


  * Proposal: The estimate that the ProEstimator Solution creates and Leacock Paving sends to the Customer. Also the name of the record type within ProEstimator that is used to track job & estimate details throughout the entire ProEstimator process.
    * Section: A portion of a Proposal that corresponds to a part of the job, such as a category of work or a certain portion of the jobsite. A Proposal may have one or multiple Sections (but must have at least one). A Section may contain one or more Groups (see explanation below), or may be standalone with no Groups (a line without a price -- can be used for custom text in the proposal). Residential Proposals usually have just one Section; Commercial Proposals average 3-4 Sections, but may have up to 10 or more.
      * Group: A section may have zero or more groups. A Group correlates to a single line on the Proposal printout. It is a portion of a Proposal that is linked to a Section and corresponds to a specific portion of the work being done under that Section. A Group may contain one or more Items (see explanation below). One or more Groups can be included under a Section. Residential Proposals usually have 2-3 Groups per Section; Commercial Proposals also average 2-3 Groups per Section, but may have up to 6 or more. 
        * Item: A group may have zero or more items. Items do not appear on the Proposal printout, but instead are used for internal calculations, Work Orders, supply quantities, etc. Items include all of the materials, labor hours, services, etc., that are required to do the work of a project. (Examples include grading, surface prep, stone, asphalt, paving labor, truck use, etc.) These may be specific Sales Items tracked in the Solution, or they may be manually-added on a per-Group basis. 
    * Types of Proposals: Proposals are categorized as being one of the following (tracked by a "Proposal Types" list): 
      * "Original" Proposal: A Proposal that meets one of the following criteria: 
        * Has no "parent" (Source Proposal), not created as a copy of another Proposal.
        * Was created as a "Duplicate" copy of another Proposal, normally for the purpose of preparing an estimate of the same work/job for a different Customer (i.e. multiple contractors bidding on the same project and asking Leacock to provide them with quotes). Duplicates do not replace their source Proposal and are treated as / labeled as "Original" Proposals. 
      * "Revised" Proposal: A Proposal created as a copy of an "Original", other "Revised", or "Duplicate" Proposal, as an updated version of the same Proposal, normally replacing the one from which it was copied. 
      * "Change Order" Proposal: A Proposal created from an "Original", other "Revised", or "Duplicate" Proposal, adding additional work to the job. 
    * Section Inclusion Types: Sections in Proposals are categorized as being one of the following (tracked by a "Section Inclusion Types" list): 
      * "Standard" Sections: 
        * These are the main or "base bid" Sections, with any included Groups, that are included as part of the main Proposal, with the assumption that the Customer will accept them to be included in the job work. 
        * A Proposal may have one, none, or multiple Standard Sections. 
        * Pricing for Standard Sections and their included Groups is included in the Proposal printout price prior to the Proposal being marked as "Awarded". 
      * "Option" and "Alternate" Sections: 
        * In Leacock Paving's workflow, there are two different ways these are used: 
          * 1\. Multiple ways to do the same job (i.e., the same driveway or parking lot job priced at multiple different thicknesses for price consideration; these could be listed as "Option #1", "Option #2", etc.) 
          * 2\. Optional add-ons for a job  
            * In this scenario, one or more Standard Sections would be included (but the software does not have any validations to require it) 
            * Items in this scenario can be viewed somewhat like a Change Order, but they are included as possibilities in the original Proposal, rather than written up later. 
        * Both Options and Alternates are handled exactly the same way by the Solution, even though they have different names. 
          * Options are generally used for Residential jobs. 
          * Alternates are generally used for Commercial/Sports/Agriculture jobs. 
        * In the Solution, Options and Alternates are assigned at the Section level.
        * A Proposal may have one, none, or multiple Options and/or Alternates. 
        * A single Option/Alternate may include multiple Sections linked with it. 
        * Pricing for Option and Alternate Sections and their included Groups is excluded from the Proposal printout price prior to the Proposal being marked as "Awarded". 
          * If an Option or Alternate is accepted (awarded) by the Customer, the Sales Rep would check the "Group Awarded" checkbox, just like for Standard Groups, to add it into the main calculations & pricing. 
    * Automated Proposal Group: A pre-configured Group that can be added to a Proposal with all of its Items and calculations, reducing the amount of work needed for things that are commonly done for jobs. 
    * Proposal Date: The effective date of the Proposal; the date that it was finalized to be printed or emailed to the customer. 
    * Work Order: A PDF printout document that lists Sections, Groups, and individual Items for a Proposal. This is used internally by Leacock Paving to list out the materials needed to complete the job. 
  * Oil Index: An index used by the different states to track the current liquid ton price for oil (the dollar amount per liquid ton). This index varies from state to state. For Phase 1, the ProEstimator Solution tracks the Oil Index for the state of Pennsylvania, but it can be overridden on a per-Proposal basis for jobs in other states. Within the Solution, this is used only as an indicator / reference point, and not used for any calculations internally. Pricing is affected indirectly by the Oil Index, based on updated prices from Leacock Paving's vendors that are impacted directly by the Index. 
  * Sales Rep: A member of the Leacock Paving team who handles estimating and sales for jobs. Within the Solution, a Sales Rep is defined as an Employee-type Contact with the "Is Sales Rep" checkbox checked on their Contact record. 
  * "Awarded": Leacock Paving's terminology for a Proposal that is accepted and signed by the customer.


