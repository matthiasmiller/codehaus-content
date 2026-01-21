5.3.8.1. Proposal Details - Section Header

  


Requirements

  * Proposal # (auto-set and read-only; alphanumeric ID; unique identifier for the record; with the following details / behaviors:
    * displayed in section header; 
    * auto-set on the first Save for a new Proposal record (including for copied Proposals); 
    * can be set via import if blank; note that for Proposals imported from the existing Power App solution, this will be set to the "Power App Quote ID" from the imported data; 
    * generated in the following format: "<Numeric ID><Revision Suffix><-Change Order Suffix>" (see examples below, with the following details for each portion:
      * the "Numeric ID": 
        * always included;
        * for "Original" Proposals and "Duplicate" Proposals (based on checkboxes): starts with the higher of the following, and advances sequentially from there:
          * the highest existing "Numeric ID" out of all "Proposal #"'s in the Solution or
          * the current value of the "Minimum Proposal numeric ID" System Switch + 1; 
        * for "Revised" and "Change Order" Proposals (based on checkboxes): sets to the "Numeric ID" of the Source Proposal;
      * the "Revision Suffix": 
        * conditionally included if one of the following conditions is met:
          * if "Proposal Type" = "Revised" (i.e. a standard Revised Proposal): increments sequentially from the highest revision letter for all other "Revised" proposals with the same "Numeric ID" portion;
          * if the "Proposal Type" = "Change Order" and the Source Proposal's "Proposal Type" = "Revised" (i.e. a Change Order created from a Revised Proposal): retains the Source Proposal's "Revision Suffix" but does not increment; 
        * upper-case letter, with no hyphen or period, starting at "A" for the first "Revised" Proposal for a Numeric ID, and advances sequentially from there; 
        * note that this is not included for revisions made to Change Orders that were not created from "Revised"-Type Proposals; 
      * the "Change Order Suffix": 
        * conditionally included if "Proposal Type" = "Change Order";
        * hyphen and number;
        * starts at "1" for the first Change Order for a Numeric ID + Revision Suffix combination, and advances sequentially from there; 
    * examples: 
      * "Original" Proposals: "15001", "15002", etc.; 
      * "Revised" Proposals: "15001A", "15001B", "15001C", etc.; 
      * "Change Order" Proposals: "15001A-1", "15001A-2", etc.; 
      * Revised "Change Order" Proposals: same format as standard Change Orders ; 
      * "Duplicate" Proposal: same as Original Proposals)



  


Development Specification

Tim Reitz 09/22/2025: Overview of logic (TI for the original testing job): 

  * Proposal # is set on the first record save as follows:
    * If not created via copy: <Numeric ID> (e.g. "15001")
    * If created via copy as a duplicate proposal: <Numeric ID> (e.g. "15001")
    * If created via copy as a revised proposal: <Numeric ID><Revision Suffix> (e.g. "15001A").
    * If created via copy as a change order:
      * If source proposal is a revised proposal: <Numeric ID><Revision Suffix for the Source Proposal>-<Change Order Suffix> (e.g. "15001A-1"
      * If source proposal is not a revised proposal: <Numeric ID>-<Change Order Suffix> (e.g. "15001-1").



  


  


Ellis Miller 06/19/2025:

  


CODE BY NIC

[ ] Code this and supporting macros

[ ] System Switch for the Minimum Value

[ ] Lets have a ProposalsByNumAndSuffix.ndx - BinString(NumericPortion, 4) + PadOrTruncate(UpCase(SuffixPortion), 6)

[ ] Add wrapper macros to make it easier:

[ ] CalcNextProposalNum_New -no parameter

[ ] CalcNextProposalNum_Revised( vProposalNumberWithSuffix)

[ ] CalcNextProposalNum_ChgOrd( vProposalNumberWithSuffix)

  


[ ] Add ProposalFamilyGroup( vProposalNumber) -- none-level macro returns "1234" from "1234B-2"

[ ] Add ProposalFamilyAwardedNumber( vProposalNumber) -- none-level macro to return an Awarded proposal (excluding change orders) for this proposal family (e.g. if you pass in "1234B-2" it might return "1234C").

  


[ ] ProposalNumberSubset( vProposalNumber) - calls ProposalsByProposalNumberNdxFindPart, handles if family number or more full number. Returns all if blank.

[ ] FromSourceProposalSubset( vSourceProposal) - For SourceProposal searching, do a:

ProposalsByProposalNumberNdxFindPart( If ( IsNA( vSourceProposal, NdxSkip, BinString(ProposalFamilyGroup(vSourceProposal)))

to quickly get all of the proposals in the family group then:

(IsNA( vSourceProposal) OR ProposalSourceProposal = vSourceProposal)

  


  


Earlier Notes:

[ ] CalcNextRevision( vProposalNumberStr) - evaluates the next revision number (strip off the - change request, if any, check to see if there is a number at the end of the number. If so, increment it one letter (UpCase the letter for safety, Switch to number using Asc, add one, switch to letter using Chr).

  


[ ] ProposalType macro - 

[ ] Source - ProposalSourceProposalNumber

Niccolas Miller 08/21/2025: Just a list field: ProposalCopiedFromProposalNum.

[ ] Replaced By - ProposalReplacedByProposalNumber

  


[ ] Niccolas will code the Revision /Suffix/ChangeOrder as part of the "Copy Feature"

BID: 1.5 DAYS
