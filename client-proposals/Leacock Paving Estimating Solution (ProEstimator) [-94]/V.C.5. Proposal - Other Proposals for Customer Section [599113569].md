5.3.5. Proposal - Other Proposals for Customer Section

  


Requirements

  * Other Proposals for Customer section (visible if any Proposal records exist with the "Customer" = the currently-selected Contact in the current Proposal record; located to the right of the Customer & Job Information section)
    * Other Proposals for Customer (no label; read-only embedded spreadsheet with the following; displays any/all other Proposal records for the selected Customer: 
      * Columns:  
        * Status 
        * Proposal # 
        * Received Date 
        * Sales Rep 
        * Result Date (displays the "Proposal Result Date") 
        * Proposal Price $ 
        * View (link to open the corresponding Proposal record; displays as "Link")
      * Automatically sorted by: Proposal # (latest at the top) 
      * Buttons to insert/append/remove rows: N/A 
      * Show 6 rows without scrolling
      * Other Notes:
        * Note that the user can click-sort by any column by clicking on the column heading)
    * View All (link; opens the "Proposals by Customer" report for the selected Customer -- see corresponding spec)



  


Development Specification

Ellis Miller 06/18/2025:

[ ] Virtual RG:

[ ] Create a ProposalsForClient( vContact, vExcludeID) macro that does a ProposalsByClientAndIDNdxConcat( BinString( vContact) + "...", String(ProposalID)) skipping vExcludeID. Call ReversePipeList to have most recent on top.

[ ] Create a ProposalFieldFromIDStr( vIDStr, vField) that does ProposalField( BinString( Value( vIDStr), 4), vField). Columns can then just call ProposalFieldFromIDStr(RepeatListItem, ProposalReceivedDate), etc.

  


BID: 4 HOURS
