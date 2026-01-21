2.3. Setup - Stop Types

  


Requirements

We will have three Stop Types:

  * Break
  * Delivery
  * Pickup



  


It should have the following fields:

  * Name
  * Color in schedule (list of colors; allow blank)
  * Default Stop Length



  


The available colors will be:

  * Aqua
  * Blue
  * Fuchsia
  * Gray
  * Green
  * Lime
  * Maroon
  * Navy
  * Olive
  * Orange
  * Purple
  * Red
  * Silver
  * Teal
  * Yellow



  


Development Specification

[ ] Rename the Subroutes to "Stop Types"

[ ] Make it Investortools-owned with the above 3 stop types

[ ] Remove the highlight checkbox

[ ] Rename the Color label

[ ] Change the Color label to be a Colors list field

[ ] Use the following Helper List (StopTypeColors macro):

ListSubstitute( ListToPipeList( colors)

              , If( IsNA( Find( ' ', ListSubstituteItem)) AND

                    ListSubstituteItem <>

                    ValidatedListString( Colors, 'White') AND

                    ListSubstituteItem <>

                    ValidatedListString( Colors, 'Black')

                  , MixCase( ListSubstituteItem)

                  , ''

                  )

              , NewLine

              )

[ ] Add a background item that shows the selected color just below the droplist.

[ ] Add a macro called StopTypeColorRGB that uses a Lookup(Colors, StopTypeColor) to return the RGB for the integration.

  


[ ] Add a required Default Stop Length field (number; 0 decimals; required; >0)

  


[ ] This should be restricted if not ConfigRoutes_IsRoutesUser

[ ] This should be read-only if not ConfigRoutes_IsAdminUser
