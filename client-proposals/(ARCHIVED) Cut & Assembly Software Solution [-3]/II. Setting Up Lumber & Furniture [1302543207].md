2\. Setting Up Lumber & Furniture

  


Requirements

Instructions

Within the software, we will provide instructions on how to make different changes, such as:

  * Adding additional colors
  * Adding new styles of furniture
  * Changing cuts on an existing style of furniture
  * How to update the cut date or assembly date for a piece of furniture



  


Lumber

We will be able to set up the available sizes of lumber (i.e. 2x4x12). We will assume that all lumber is available in all colors.

  


Furniture

You will be able to view and edit furniture information.

  


Editing furniture information will update all cut lists, including ones from the past. For example, if you change the cuts of a piece of furniture, then print out a saved cut list, it will show that list of furniture with the new cuts.

  


Each piece of furniture will specify:

  * A code
  * A description
  * Active? (which can be used to remove old styles)
  * Cut type (90-degree, Mirrored 45-degree)



  


It will also specify a list of cuts, each one including:

  * Quantity
  * Length (for example, 36 1/4)
  * Size (from the list of lumber--for example, 1x6x12, 2x4x12)
  * Primary/Secondary Color designation
  * Part description



  


Development Specification

We will internally store a Numerator + Denominator, allowing us to sort via decimal length.

  


We will need to parse out "36-1/4" etc -- basically we can replace '-' or ' ' with '|' and do pipelistelement, and repeat.
