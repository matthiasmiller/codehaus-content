17.7. (MM) Store asset value for validation?

Do we want to store the asset value on the asset, so that we can find out if a sync accidentally recreates a row for an asset via a PO/VI?

  


Matthias Miller 09/11/2023: Add it as a field, require it to be filled in, then have a report alert that appears when it doesn't match, on or after the in-service date.
