4.7.2. Driver Assignment

Do they want to be able to reassign haulers?

Do they want to be able to predict multi-shed hauls? -- total length of buildings they can place on it?

Scenrio:

  * Guy A with pickup has 1 shed out west (single capacity)
  * Guy B with semi has 1 shed back east (3-shed capacity
  * Customer buys shed out west -- should we swap shed 1 and 2?



The basic process is:

  * Give a set of buildings and a set of drivers, can we deliver them effectively on that date?
  * What are the parameters for maximum distance? Maximum drive time? Etc



If we have that, we can simply look at days with open slots, and see if we can add this building to that date. We continue until we find the first date that works.

  


  


Matthias Miller 09/25/2020: Some ideas:

  * Could calculate proximity by distance from hauler -> shop -> customer -> hauler (round-trip??



Do )

  


  


We will need to keep the same margin for expedited deliveries as we do for builds, right? And then we can just fill it in with lot hauls, as soon as the drop below the minimum expedited lead time.
