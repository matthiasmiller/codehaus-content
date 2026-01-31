5\. Renumbering Households

  


Requirements

The menu will include an option to Renumber Households. This will assign new Household #'s in proper order, starting with 1 and continuing with whole numbers (2, 3, 4, etc). This option will only be available to administrators.

  


Sort by last name, first name, middle name, and age (oldest first).

  


When assigning Household #'s, all previous marriages will be grouped together in order of latest to earliest. For example, given a situation where a couple have both been married previously:

  * Jim and Joanna (current marriage)
  * Jim and Ruth (Jim's 2nd marriage)
  * Jim and Sue (Jim's 1st marriage)
  * Joe and Joanna (Joanna's 2nd marriage)
  * Jerry and Joanna (Joanna's 1st marriage)



  


These previous marriages can be sorted by anniversary

  


Development Specification

TODO_CCI: I think I need more understanding how previous marriages work. Is this only used for men or also women? If Sally was married to Bob Brown who died and then married to Joe Smith, how are those represented? Matthias Miller 04/21/2021: Clarified

  


TODO_CCI: I think we can group previous marriages by simply adding Anniversary to the end of our sort order in newest first order? There could be a possibility that two "Bob B. Brown" born on the same day each had multiple marriages that would get interleaved. If we are worried about that, we could first sort by Parent Household # or birth place to make sure they are unique.

Matthias Miller 04/21/2021: The safest approach is to find the latest household #, use that household's sort as the base, then use the prior household to add an A or B to order the husband's marriages first, followed by the prior household's anniversary.

  


  


Ellis Miller 04/21/2021: TODO_CCI: Shouldn't we simply use a list-tied record (maybe just a lookup record) and have the household # be the list field? I think that would let us more easily create records. I don't know how a detail screen save could create a numeric-ID record. For reordering the numbers, we would have an x30list do a single pass through the household records renaming everything to "1-New", "2-New", etc and then a second pass going through and removing the "-New" suffixes.

Matthias Miller 04/21/2021: Correct. That's what I was thinking. Feel free to rename Household ID to something that makes more sense.

  


2.5 Days
