6.17. Raw Material Record*

  


Requirements

The Raw Material defines the raw materials (lumber, fasteners, etc) and is used to score assembly of items, calculate the cost, as well as specify the cut list.

Lumber uses board feet and linear feet for pricing. All others use per-item pricing.

Standard Dimensions are used to round up.

Sections and Fields:

•     Raw Material section:

–     Name (string)

–     Type (drop list of Raw Material Types; required)

–     Active (checkbox)

–     Sort Order (number; 0 decimals)

–     Expected Keyword (drop list of Raw Material Keywords)

•     Dimensions section:

–     Lumber Thickness (In) (number; 4 decimals; required)

–     Lumber Width (In) (number; 4 decimals; required)

–     Lumber Length (In) (number; 4 decimals; required)

•     Cost section:

–     Cost Unit of Measure (drop list of Units Of Measure)

–     Setup Cost (number; 2 decimals)

–     Unit Cost (number; 4 decimals)

–     Standard Dimensions; embedded spreadsheet of:

•     Dimension (drop list of Item Dimensions; required)

•     Amount (rounds up for pricing) (number; 2 decimals; required)

•     Fasteners section:

–     Fastener Category (drop list of Fastener Category Names)

–     Fastener Score (number; 0 decimals; sometimes required)

  


Development Specification

DO_NOT_REMOVE_ZMM_ISD_ID=967

  


  

