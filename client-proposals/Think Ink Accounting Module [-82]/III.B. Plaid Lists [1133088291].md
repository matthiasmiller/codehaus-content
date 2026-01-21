3.2. Plaid Lists

  


Requirements

The Solution will have the following user-configurable lists:

  * Plaid Categories
  * Plaid Accounts



  


Development Specification

  * For Plaid ID, consider using a 37-byte string and tricking the index into thinking it's a binary string so we get case-sensitive matching, OR have a compare function that double-checks case. Probably not an issue in practice, but as a matter of principle.


