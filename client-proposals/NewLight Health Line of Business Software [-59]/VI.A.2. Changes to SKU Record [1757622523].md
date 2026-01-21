6.1.2. Changes to SKU Record

  


Requirements

Add the following fields to the SKUs in a new custom Catalog section (only for Primary SKUs):

  * Catalog Sections (multi-select list)
  * Catalog Sort Order (number)
  * New Item (checkbox)
  * Taxable (checkbox)
  * Top Seller (checkbox)
  * Pregnancy Safe (checkbox)
  * Catalog Description (plain-text, supporting <b>bold</b>, <i>italic</i>, etc.)
  * Catalog Preview (formatted version of Catalog Description)
  * Image (S3 file upload)
  * Image Preview
  * Image Scale % (1-100)



  


The catalog description will be formatted the same as Pagination's import format, as described here [https://pagination.com/api-usage-guide/](https://pagination.com/api-usage-guide/). It will support bold and italic. For example:

  


This <b>bold, <i>both</b>, and just italic</i>, with a |.

  


This would be formatted as:

  


This bold, both, and just italic, with a |.

  


NOTE: Pagination supports <sub>subscript</sub> and <sup>superscript</sup>. We could support that for the export, but we don't have a a good way of previewing it without simply reducing font size in the preview.

  


Development Specification

TODO_IDD: Do they need sub/sup?

TODO_IDD: My proposal is to have a Preview memo with an HTML parser:

  


Assign vHTML = 'This <b>bold, <i>both</b>, and just italic</i>, with a |.';

  


Assign vPipePlaceholder = '`PIPE`';

Assign vHTML = Replace( vHTML, '|', vPipePlaceholder);

Assign vHTML = Replace( vHTML, '<b>', '|<b>|');

Assign vHTML = Replace( vHTML, '<i>', '|<i>|');

Assign vHTML = Replace( vHTML, '</b>', '|</b>|');

Assign vHTML = Replace( vHTML, '</i>', '|</i>|');

  


Assign vBold = False;

Assign vItalic = False;

ListSubstitute( vHTML

              , Ifs( ListSubstituteItem = '<b>'

                   , Assign vBold = True;

                     ''

  


                   , ListSubstituteItem = '<i>'

                   , Assign vItalic = True;

                     ''

  


                   , ListSubstituteItem = '</b>'

                   , Assign vBold = False;

                     ''

  


                   , ListSubstituteItem = '</i>'

                   , Assign vItalic = False;

                     ''

  


                   , True

                   , FormattedText( Replace( ListSubstituteItem, vPipePlaceholder, "|")

                                  , ""

                                  , NA

                                  , Ifs( vBold AND vItalic

                                       , "Bold Italic"

                                       , vBold

                                       , "Bold"

                                       , vItalic

                                       , "Italic"

                                       , True

                                       , ""

                                       )

                                  , ""

                                  , ""

                                  )

                   )

              , ""

              )

  


.
