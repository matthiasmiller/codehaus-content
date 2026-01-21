6.4. Accouting Class

Coded in [[PC0077937]] - E00 - Accounting: Define Transactions detail and Accounting Class detail

  


Heading Title:

[X] Accounting Class

  


Fields:

[X] Class Name (string)

\- In XLP system the label is changed to Class ID.

[X] Active (checkbox) - By default True.

[X] Notes (memo)

  


Client system fields:

[X] Class Label in XLP. Added in [[PC0079163]]

  


Links:

[X] Modification History

  


Validations:

[X] Cannot delete class if referenced. Coded in [[PC0113155]]

  


Report link:

[X] Accounting | Accounting Configuration | Classes

See "Accounting Configuration | Classes" on the left pane for full report documentation.

  


Referenced:

[X] In Financial Account record we can define default class.

\- Added in [[PC0086409]]. Also see Financial Accounts on the left pane.

[X] In Accounting Transactions record, we can select class in Transaction RG.

\- See Accounting Transactions on the left pane.
