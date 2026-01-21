15.2.2. General Release

  


Requirements

Niccolas Miller 02/16/2023: The current design is simply a word template. De-activating section.

  


As mentioned in the claims, we would like to have templates for General Release forms. It should have two fields:

  * Title
  * Template



  


These should only be editable by Admin.

  


Development Specification

Ellis Miller 08/18/2020: 

  


General Release (2 days)

This is a simple lookup record. GeneralReleaseTemplate is a memo with Expression Field Requirements that is evaluated on a claim (see Mag Entry Type Template in Gemiende catalog for an example).

  


The template export is quite simple. It has a header and a #Evaluate(....)#
