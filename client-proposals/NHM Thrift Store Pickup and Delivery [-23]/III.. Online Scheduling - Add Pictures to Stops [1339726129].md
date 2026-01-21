3.30. Online Scheduling - Add Pictures to Stops

  


Requirements

We will add a new field to the stop detail for Pictures.

  


These can be copied and pasted from the SMS screen into the appropriate stop. When selecting a guest in the SMS screen, we will show their scheduled stops in a subpane.

  


Development Specification

Matthias Miller 09/14/2020: Josh will fix pictures sent to SMS for $500 (already discounted/subsidized) -- and we will embed the attachments in the report...

  


  


ArchivedDocumentImage( 'SMS Conversation'

                     , Assign vPath = PipeListItem( ArchivedDocumentFilePaths( 'SMS Conversation'), 1);

                       Assign vPathSegments = Replace( vPath, '\', '|');

                       PipeListItem( vPathSegments, PipeListCount( vPathSegments))

                     , 100

                     , 100

                     , 100

                     )
