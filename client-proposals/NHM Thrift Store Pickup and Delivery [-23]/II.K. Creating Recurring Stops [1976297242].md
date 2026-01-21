2.11. Creating Recurring Stops

  


Requirements

We will have a nightly process that auto-creates new repeating stops. The process will look for any recurring stops without a requested stop in the future.

  


Development Specification

[ ] Create a helper report that runs on all Routes with a RepeatRG on repeating stops. It should calculate the RouteNextAvailableDate, passing in the schedule from the RG.

  


[ ] The x30 should auto-populate the stop, skipping it if if a stop exists for that RouteStopRecurringStopID and date.

[ ] Add this to the daily maintenance x30list. Note that it's VERY IMPORTANT for the other x30 to run first so we don't duplicate recurring stops if they are missed. Matthias Miller 09/23/2020: Tim, this would be a good thing to test.
