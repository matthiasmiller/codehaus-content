2.1. Changes for Policy #

  


Requirements

*Documentation N/A

  


Policy #:

  * The existing hard-coded approach for Policy # (one number for the whole Plan) is being replaced by the ability to set the method on a Plan-by-Plan basis via a the special "Policy Number" System Switch. This is an expression that can be set for a Plan's specific situation, with the intention of being set in one of the two following ways by the development team as part of the initial configuration:
    * Option 1: One policy number for the whole Plan. The number is provided to CCI and set in the System Switch to apply across the whole system. It may contain the prefix "SI" (for "Self-Insured").
    * Option 2: One policy number for each member/client. The details are configured in the System Switch by CCI, and an individual # is assigned to each client. It also may contain the prefix "SI".



  


Development Specification

Ellis Miller 04/24/2025: Policy # is only used on printouts. Driven by system switches (see later spec).
