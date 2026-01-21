25.0.3. Delivery Ticket: Optional: Auto-fill most recent "$/BF"

Option for auto-setting Load Itemization "$/BF":

  


Tim Reitz 11/27/2024: Client isn't sure about this. He thinks this could get them in trouble. So we're not doing this for now. 

  


  


$/BF: 

_EM: Tim Reitz 10/28/2024: How hard would it be to auto-enter the most recent $/BF for the Species + Thickness + Grade for the Buyer + Member? Maybe something like a read-only RG on the Buyer or Member record? This is not something that we want right now, but could be something to add in the future, once things are ironed out more.

_DD: Tim Reitz 11/07/2024: Per Ellis this is doable. Probably in the $400-600 range. 

Questions: 

  * How far back into the past would you want to go to bring in the $ value? 



Dev Spec: 

  * Index of Buyer + Date 
  * Find matching keys and reverse sort in date order 
  * Go through Delivery Tickets in reverse date order, looking for a match, up to n days ago


