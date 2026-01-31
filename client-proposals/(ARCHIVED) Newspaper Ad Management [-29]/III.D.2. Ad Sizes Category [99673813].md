3.4.2. Ad Sizes Category

  


Requirements

Each Ad Size would have a separate Sales Item detail page where its specific details would be configured. This will allow for linking to invoices and for sales reporting.

  


The "Run By" setting on the Configure Publication detail will determine which type of ads the publication will use (Ad Size or Column Inch).

  


The Ad Size detail screen will have the following sections and fields:

  


Sales Items Section:

  


  * Code (required; text field; validate that the Publication Code is included at the end; validate against using the same base Code+suffix more than once in the system)
  * Is Active (checkbox, default to filled; when deactivating, validate that the Sales Item is not being used)
  * Description (required; text field; validate against using the same description more than once in the same publication)
  * Category (required; list of Ad Sizes, Discounts, Other)
  * Show in Sales Report (optional; checkbox; default to filled)
  * Default Quantity (optional; default to blank)



  


Sales Items codes for ads for the Gemeinde Brief publication could be something like this: 

  


Name| Code  
---|---  
Business Card| BCADGB  
Quarter Page| QPADGB  
Horizontal Half Page| HHPADGB  
Vertical Half Page| VHPADGB  
Full Page| FLPADGB  
Front Page| FRPADGB  
Back Page| BKPADGB  
  
  


  


Publication Details Section:

  * Publication (required; for Publication Admin, default to assigned publication and read-only; for Full Admin, list of publications, defaulting to blank, with validation against changing if the item is being used)
  * Publication Code (read-only; auto-filled based on Publication; display after the Code)



  


  


Ad Size Details Section: (visible if "Run By" = Ad Size in Configure Publication)

  


There would be the following fields and options to configure the Ad Sizes: 

  


  * Run By (auto-fill from Configure Publication for the selected
  * Ad Size (required; text field; auto-fill from Sales Item Description; editable)  
  * Ad Height (required if a value is entered in Ad Width; number to 2 decimals)
  * Ad Width (required if a value is entered in Ad Height; number to 2 decimals) 
  * Square Inches (auto-calculated from Ad Height and Ad Width; read-only; used for reference and for the Square Inch Report)
  * B&W? (required; list of Yes/No)
  * B&W Price (visible and required if "B&W?" = Yes; number to 2 decimals)
  * Color? (required; list of Yes/No)
  * Color Price (visible and required if "Color?" = Yes; number to 2 decimals) 
  * Uses Special Placements? (required; list of Yes/No)
  * Special Placement Item (visible and required if "Uses Special Placements?" = Yes; list of the Sales Items in the "Other" category; used to select which Special Placement Charge is used for the Ad Size, allowing linking for invoices and allowing for multiple Special Placement Charges)



  


If both B&W and Color are available for an Ad Size/Sales Item, both would show up as options on the Ad Details when the Ad Size is selected, If only one is available, only that option will show on the Ad Detail when that Ad Size is selected.

  


  


Special Placement Section: (visible if "Uses Special Placements?" = Yes)

This section would configure the Special Placement options for the Ad Size, to allow for special placement requests. This would allow us to configure multiple distinct locations for each Ad Size. It would contain the following:

  


  * Layout Grid (read-only) 
    * This field would have a visual layout grid that would look something like this:



![](data:image/png;base64,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)

  * Special Placement Options (optional; embedded spreadsheet with the below options and features)
    * Ad Size (auto-filled and read-only)
    * Placement Name (required; text field; allow for duplicates for different Ad Sizes)
    * Layout Grid #'s (required; a comma list of numbers; auto-sort this field numerically; remove duplicate numbers from this field; validate against duplicate Ad Size/Placement Name combinations)



  


Example of the embedded spreadsheet for the Quarter Page Ad Size: 

Ad Size| Placement Name| Layout Grid #'s  
---|---|---  
Quarter Page| Top Left| 1, 3  
Quarter Page| Top Right| 2, 4  
Quarter Page| Bottom Left| 5, 7  
Quarter Page| Bottom Right| 6, 8  
etc.|   
|   
  
  
  


New placement options could be added by clicking the "+" button beside the embedded spreadsheet. 

Options can be deleted by clicking the "-" button beside the embedded spreadsheet (but validate that the option is not being used).

  


  


General Notes:

Ad Sizes/Sales Items could be deleted  but do not allow deleting Ad Sizes that have been used (selected in one or more ads). Show an error message such as, "This Ad Size has been used for one or more ads."

  


Development Specification

Price Fields: Tim Reitz 02/02/2021: Our proposal is to use two custom fields on the Sales Item for the prices and not allow a standard price. If invoicing manually, price will be blank (enter manually). 

  


Layout Grid Memo: We should have a memo AppHosting.zone Settings where we can save an image to display here.

  


Special Placement Options Validation: Validate that no Grid Numbers are being used twice on a given page. For example, if a Quarter Page ad is placed at the Top Left (1, 3), do not allow a Horizontal Half Page ad to be placed at the Top (1, 2, 3, 4).

  


Ellis Miller 04/20/2021: 

  


TODO_CH: Should we ask John whether he would prefer using -GB instead of GB. I think it would improve readability greatly:

Business Card| BCAD-GB  
---|---  
Quarter Page| QPAD-GB  
Horizontal Half Page| HHPAD-GB  
Vertical Half Page| VHPAD-GB  
Full Page| FLPAD-GB  
Front Page| FRPAD-GB  
Back Page| BKPAD-GB  
  
  


This lets your eyes ignore the suffix and read the meaningful code easily.
