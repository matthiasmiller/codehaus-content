4.3. Ad Details Section

  


Requirements

The Ad Details section of the Customer/Ads Page will have the following fields and options.

  


Note that the ad can be saved with "required" fields that are empty, so they should warn on save if they are empty, rather than give an error. Fields of this type are marked "warn on Save if blank" here rather than "required".

  


General Features and Buttons:

  * Arrow buttons to cycle through the Ad Details for the customer  
  * Button to open the Ads List Child Screen (see details in the corresponding section of this proposal)
  * New Ad button (creates a new ad, adding it to the Ads List)



  


Ad Detail: 

Each Ad Detail will track the following:

  


  * Ad Title (required; does not affect export file name; required because it is used to link to Tasks; if the Ad does not yet have a title, the user can enter "New ad" or something similar)
  * Ad Size (warn on Save if blank; list of Ad Sizes from Configure Publication; determines the amount of square inches for the Square Inch report; if changed, the ad retains the new selection for future runnings of the ad)
  * Ad Color (warn on Save if blank if Ad Size is blank, required if Ad Size is filled; list of of available color options from Configure Publication for the selected Ad Size; if only one is available, defaults to that one; if both are available, defaults to blank)
  * Main Ad Price (auto-filled and read-only; based on the Ad Size & Ad Color selections; pull from the Ad Size Sales Item)
    * When a running of an ad is scheduled, the Ad Price field on the Publication Schedule list is filled from here, and is editable there until it is invoiced
    * The Ad Price on the Publication Schedule will default to this current main Ad Price as defined on the Sales Item, and it will update when the Sales Items is updated unless it is locked. See notes about locking ads on the Pay with Credit checkbox and Ad Price requirements in the Publication Schedule below. 



  


  * Ad Image Upload/Preview (warn on Save if blank; memo field; to upload an ad image, drag it onto this field)
    * The preview will appear soon - typically a couple seconds of dropping it into the memo - but will not be instantaneous
    * If the image is larger than the preview field, it will scale down to fill the field
  * Ad File Name (read-only; auto-fill with the file name of the uploaded ad)
  * Actual Ad Dimensions (read-only; auto-fill from the uploaded ad; display as <height>" x <width>", to 2 decimal places)
    * The system automatically calculates this from the image that was uploaded
    * This is basically just a reference - nothing else is tied to this (not even square inch calculations)
  * Download Ad (link to download the original ad file to the user's device)
  * Print Ad (link to open the original ad file in another tab for printing)
  * Fax Proof and Email Proof (links; visible if Fax/Email are available for the Customer; each opens a new email draft with the Customer's fax or email, subject, and email body pre-filled; ad file gets manually downloaded separately via the Download Ad link, then dragged and dropped into the email draft)
    * "Proof Subject" would be set in AppHosting.zone settings (text box)
    * "Proof Email Body" would be set in AppHosting.zone settings (multi-line text box)
    * The links might require a browser extension or initial other setup by the user (like the links in the Email Section of the Customer/Ads Page)



  


  * Index Name (required; auto-fill from Customer; editable; does not automatically change back to the Customer after it has been edited)
  * Index Page # (included in the Publication Schedule embedded spreadsheets rather than the main Ad Detail)
  * Special Placement Page Number (optional if Special Placement Location is blank, warn on Save if blank if Special Placement Location is filled; text field; validate against duplicates for same Location and Page Number within the same publication date; edits apply to all runnings of the ad, including past runnings)
  * Special Placement Page Location (optional if Special Placement Page Number is blank, warn on Save if blank if Special Placement Page Number is filled; drop list from Configure Publication; validate against duplicates for same Location and Page Number within the same publication date; edits apply to all runnings of the ad, including past)
  * Charge for Special Placement (checkbox; defaults to unchecked; note that the Special Placement Charge does not get discounted by any of the Sales Items discounts - Multi-Run, Special, or Prepay - but it does get discounted by the invoice discounts - like the 2% prompt-pay discount)
  * Create Invoice (link; creates an individual invoice for the current running of this Ad; visible if no invoice exists for this Ad for the current Publication Date)
  * Pay with Credit (checkbox; defaults to cleared; filling this box applies to all current and future runnings of the Ad until it is unchecked; clearing this box applies to all current and future runnings of the Ad; any runnings for which this box is filled will have their price locked from updating in the event that the main Ad Price changes)
  * Create Task (button; creates a new Task, auto-filling Customer, Publication Date)
  * Run Until Further Notice (checkbox; defaults to cleared; filling this schedules all current and future runnings of this ad and continues to schedule it until this box is cleared; clearing this box would un-schedule any current and future scheduled runnings; the user still would be able to fill/clear an individual running) 



  


  * Publication Schedule
    * This would be an embedded spreadsheet with the following columns (most of which are initially filled from the fields on the main Ad Detail):
      * Publication Date (read-only; list based off of Configure Publication; start with the current publication date at the top and go 1.5 years in the future; at least 12 rows should be visible)
      * Run (optional; checkboxes; determines whether the ad will be run for that Publication Date)
      * Ad Size (editable; default to what is selected on the Ad Detail)
      * Ad Color (editable if ; default to what is selected on the Ad Detail)
      * Ad Price (editable; auto-filled from the main Ad Price on the Ad Detail, but can be edited here to override that price; entering a price that is different from the main price will lock in the new price for that publication date, and changing it back to the main price will unlock it; locked prices will be displayed in a different color, probably green)
      * Discount % (editable; auto-fill with the Discount % from the Customer Information section; but can be edited here to override that percentage; whatever value entered here is overridden when the main Discount % is changed and the Apply Discount button is clicked)
      * Pay with Credit? (editable; auto-fills from the main Ad Detail but can be overridden here; if checked, the 5% Prepay Discount and credit from the customer's Available Credit should be applied to the ad at invoicing; if filled, the price should be locked)
      * Index Page # (optional; editable text field; default to blank; normally filled from the Review Ads Report)
      * Invoice Number (read-only; displays the number for the invoice for this Ad; links to the invoice)
      * Invoice Status: (read-only; auto-filled from the Ad's invoice status)
      * (the following items may be on the far right-hand side and visible by scrolling to the right)
      * Charge for Special Placement? (read-only)
      * Special Placement Page Number (read-only)
      * Special Placement Page Location (read-only)
    * The text for the lines that aren't checked to "Run" would be silver and the ones that are selected to run would be black and bold, to increase visibility for the selected dates.
    * There would be a nightly process that moves Publication Dates from this list to the Past Schedule when they go to the past and updates the Publication Schedule list to include 1.5 years of dates into the future



Example: 

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAo0AAABzCAYAAAD9qjgNAAAgAElEQVR4nO3df1DTd54/8Ofnvlr2EwkqiYqESkrFcHYVJlqPEhlnbFWu47UVbwr+4Oxt25Pz3Dp2Fj2vQq2pdSldOTqch2tt18XU4q3s2PEcKCvdLgQZi5xo7SXSYqQELXwSlYR8pO1tvn+wn3fzIQkhAoL6esxkRj755PN5vz+f9+f9eb1f708iB8ALQgghhBBCBvFXY10AQgghhBAy/k2Q/uH1UsKREEIIIYTIcRwHgDKNhBBCCCFkCChoJIQQQgghIVHQSAghhBBCQqKgkRBCCCGEhERBIyGEEEIICYmCRkIIIYQQEhIFjYQQQgghJCQKGgkhhBBCSEhhBY2iKCI3Nxccx7FXRkYGHA5H0M+YzWaYTCa/5SaTCWazGQ6HA0ajEaIohlXw8+fPw2q1QhRFGI3GQcswFGazWVavQGWW3GmZh/LZkaoPIYQQQshICjvTqNFoIAgCvF4vvF4vcnJyUFVVdccFUKlUyM/PB8/zYX3u008/BQDwPI/8/HyoVKo7LoPD4UB5eTmrl8fjQUtLC6xW6x1vkxBCCCHkfjJi09MDM2jFxcUs6GppaUFKSkrADJ7v53yzfUajEQBgtVrZZzmOg9lshtlsxquvvootW7bAbrezzJzD4UBGRgY4jkNKSgrLRG7btg0rVqwImhlVKBSIioqCIAgA+gPRt99+GzqdDkB/VnRgBtLlcuFnP/sZOI5Dbm4uq3egdX0ztK+99hrbr5RtlepZXFzsd2yk+oTK6BJCCCGEjKawg0a73Q61Ws0Co7q6OmRmZg76mZ6eHpw5cwaCIKCuri5g8ON0OlFaWgqLxQKPxwOXy8WCvjNnzsDr9aK+vh61tbUwGAzYt28fSkpKEB0dzbaxf/9+5OTkwOv1oqKiAocOHYIoiujp6UFBQQG8Xi8MBgMsFots3zzP44033kBxcbFfwGe1WnHy5EkIgsDK73Q68c0332DXrl3weDyIiopCe3s7rFYrWlpa4PF44PV60dbWBrPZjMrKSqSnp7PMrN1uH9Kx3r9/P/Lz8+H1elFSUoLCwsI7mhInhBBCCBmuYU9Pl5WVhZxaTk9PB8/zUKlU0Ol0LKM30Ny5czFr1ixZpk+n02Hr1q3gOA6LFy8edD+RkZFYuHAhAECtVqOnpweiKEKj0SApKQkAkJCQEPCzPM+jrKyM1UsK+ABg0aJFUKlUUKlUKCsrQ3R0tKysM2fOBAAIgoCioiIoFApwHIeCggLYbDa0tbVBq9UCAJKSkqDRaAatBwDcvn0bdrsdixcvBsdxSEpKwoULF+DxeEJ+lhBCCCFkpI3ot6ftdjs8Hg9EUcS1a9fY8ra2NgD9061WqxVqtXrQzwOA0WiE2WxGWVkZtm7dyjKNg3G73WhqagLQH8BFRUUN6VlJq9WKbdu2ybJ4vsHltWvXIIoim+r+6quvAm5HrVYjLy+PZRq9Xi/WrVuHhIQE2Gw2Vi6Xy8U+47vc7Xaz5T/5yU+g0WhQX1/PtlVVVTWsZzcJIYQQQu7UiAWNKpUKGo0GarUaTzzxBNrb29l7ly5dAsdxUKvVyMnJCRj4REdHIycnh019A4DBYMD06dORlJQEjuNQXl4OoP8ZQbfbjaysLFy+fJltY9OmTSgvLwfHccjKysKLL744pKBRp9Ph2WefZRlCjuPQ1tYGg8EAnU6H5ORkKBQKKBQKJCcnY/bs2UG3I63r+wxmZmYm6urqwHEcXnnlFbb+woULUVRUBI7jsHv3bkRGRsq2t2nTJhiNRrYt32cnCSGEEELuJg6AFwC8Xu8YF4UQQgghhIw3UjKPftybEEIIIYSEREEjIYQQQggJiYJGQgghhBASEgWNhBBCCCEkJAoaCSGEEEJISBQ0EkIIIYSQkChoJIQQQgghIU0ItYL02zyEEEIIIeT+Ee5vdIcMGgHI/ts7cn9TKpV3/XyPxT7HwoNSz0AelLqPp3qOp7KMpgelz3pQzudAD0q9R72ezj+Au7hKtihyZfiboelpQgghhJD7WfRT8M77PcD9v2FthoJGQgghhJD7XfRT8P70d8MKHCloJIQQQgh5EEiB4x2ioJEQQggh5EEhTVXfgWEHjY2NjVAqlbJXRUVF0PVFUURhYSGcTqdsudPpRGFhIW7cuBHw/VCcTidqa2sBABUVFWhsbAy/Mj4KCwtldVq1alXIMvmW4X7T2tqKtLQ02THZsmULRFEcszI1NjYOWgapTQ18f2BdCgsLAQRvm2PtTusJ9F8LUj3T0tLQ2toacl+DXb93i9PpxD/+4z8OWt7S0lK/94faHw12zEaKKIrYsmVL0GtmuP2UdG6lbUr7893mUM/7cPm2m4HX13Dak3SMfM+Xbz8b6Pi1traitLQ07H0MJIoiPvjgA4iiiP/+7/8Ouy2GK5z9BRNu3YNtI1D/CAAXLlwYtFxS2UfTYOULJdA1Kd3bB+sTfOMB31gg3GvYt38aSkwxqqKfuqOPjUim8b333oPL5YLL5cLVq1fR0NBwxwfjJz/5CbZv347o6OiwPnf58mV0d3cDALKyspCamnpH+5dMmjQJzc3NrF7bt2/HG2+8MehNxrcM96O1a9ey4+FyuRAbG4uWlpYxKYsoijh58iSUSmVYZRBFEYcPH8bhw4dZPYD+i5nn+Ttqe6PpTusJ9HdoNpuN1fPw4cN46623xl1QHEhNTQ00Gg2qq6vD/uxQ+qPo6Ghs374dPM+PVJEDio2NxdWrV1l50tLS8O677wIYXj8liiJsNhuuXr2KxMREdHR0oKWlBbGxsbJtulwu7Nu3D5WVlSNSn2AcDgf0ej1aW1vx1ltv4eTJk3C5XOjq6kJDQ8OwB/G+50vqZ51OJ44ePTpCNfAniiI4jgPP8+ju7oZKpRq1fY3F/oKVIVj/CAB/+tOfBv18R0cHrly5MmblG4qB12R2djZqamqCrl9YWAitVhtWLBCI1F6lfWdnZ+PgwYNhbWM8GNXpad8ofOAI6I033ggYbd++fZtle5xOJ1atWuU3GpCWSaNYaYTw0ksvsRFvY2Oj36hCKktFRQVeeOEFv+WDSU5OhlKpREdHx5DKEKjs96uBGTrf7MCWLVvYqHAkM5MdHR2IiYnBhg0b0NTUJCuLdM7feOMNv8/xPA+lUgmHw8GWbd++HampqbJ6DMw0D2xPdyN7M5x6SkHFyy+/zJYlJibigw8+YEGxbxYy0Gg90PuNjY3s2hluIBCMVPZ//ud/Rm9vr+zakcq0atUqXL9+PaztStd9WloampqaWFbBd/Qv1XO0rt9ly5ahs7MTTqczaD8lZeYClSsYaXCRmZkZ8hgMzHQ0NjbK6r1lyxa/Y15RUcHKKV3Hvsu7uroQFxeH5uZmbNy4kbUxnudRUlKC1NRUWX8gXWeBjrFU77S0NFy8eJGVq7CwEJ2dnayfvXz5MkpKSkLWN1BfH2gfvgoLCxEfH4+f//znUCqV+PnPfz6kQCFYn1dYWCi7F+7cuVO2rTvdXzCiKGLnzp147rnnZMd34L59ywUM3j82NjZix44d2LZtm18fuWXLFty4cQOlpaXYsWMHa9tSW/bN4g0n2zaU/lu6lkbiupU+/8wzz7BlqampKCkpYQPOzz77zK99+bbtnTt3orS0FNHR0SgpKZElJbRa7bDKNxZGJGh86aWX2EGLj4/HmjVrBs3WdHZ2Ys2aNSGj/IMHDyI7O1u2ntPpxKFDh+ByudDc3IyLFy+yDNF7770nG2V//PHHiI2NZRmHo0ePskbw13/913C5XKipqcFnn30Wso48zyMmJgYAhlSGgwcPYvv27XC5XHj77bexb9++MZ3KHQkffvihLJACEDJT0tPTg8OHD6Orq4sF3SOhsrISCxcuRGJiIgCwAO7jjz9GWloaXC4X1qxZg87OTr/Pbt++XXahB7ohS+eupqYGO3fuRGpqqmzbJ0+eRGlp6agPBu60nlJbC5ZJa21tRVVVFRv1AvLR+mDvS9fOcLP5wUgZVY1GgyVLlrD+obW1FRcvXkRXVxcOHToEu90e8POD9Ud/+7d/i4aGBiQkJAAAbty4gQMHDqC5uRldXV1wuVxobW0dteuX53nExsbKlnV0dCAxMZFlMrKysuB0OgOWy3c7Wq0W8fHxaG1txblz5xATE4Nt27bJbl5S+3755ZchiiI7d9L5u3z5MubMmcMC2cuXLyM2NlbWf+v1ely8eJG19Z6eHjidTly8eBF6vR4dHR2YPn36kDNkJ0+exPbt2wMe487OTpaNOX36tN/v1k2dOjVgXz+YgX29b8Yn0D4AsH3U1NSgubkZe/fulQUKgwnU5y1ZsoTdZyorK7Fy5UrZtoazv2BcLhf+9V//VXau4+LiAPS3udbWVrhcLiQnJ/vVPVD/mJqair179+Ltt98GAKxevZplk5VKJQRBwObNm7F3715kZWUFLVdTUxObxfv9738f9szOYP33UGKLzs5OxMfHs883NDTIgkJfDocDkyZNCnkeBsYSvm173rx56O3tZetKgy8Agx6n8WrEp6eHcjOJjY3FnDlzAPR3SMGmdCdNmgS9Xg+g/+BmZWVh9uzZOHjwIJRKJfR6fcgfw1yyZAkA/xGKtFylUmHSpEkh6yiKIstshCqDKIro7OzEsmXL2DqXLl2654NGaXr66tWr+NnPfibLYgWTlJSEuLg4WdA9XFJ2RDq+O3bsQHNzMwDAZrMhPj4eADBnzhy/G7REuqBdLhe0Wm3A564aGxvx2WefYfv27WzbUkASHx+Pzz//XDbiHWnDqafUyQ1scxcuXGDLFixYwDpsrVaLq1evytYN9v5oj44/++wzvPnmm1AqlVi2bBkaGhogiiIcDgeUSiV4nkd0dDQWLFgQ8POD9UfSMfPl20bffPNNxMXFjdr1K/UNvhITE9Hb2+uXaRxYLmngIMnKyoLL5cLrr7+O8+fP45FHHkF2djaam5tZVtr3xszzPHieZ1mwN998E0D/1G9aWhrOnz8fMFspBRrnz59HYmIiFixYgPPnz7P3mpubWaA4bdo0v2vCbrezAD82NhY8zwftIzs7O9k5lso6XAP7et92FGwfUjZz2bJl0Ov12LFjx5BnSgL1eVJg9tVXX6Gzs5Pd/0Zif8H43mela5bneaxcuRLNzc1obm7GvHnzAgZEofrH6OhoCIIApVKJ6dOnh/Us/4oVK7Bhw4ZhZQODlW8oscXA6enBgnOVSoXe3l6/8+A7wB7YvqR1fcvhG2NIj5HciwEjcBe+PS3daBwOB4u2XS4X61iam5sxbdq0gJ/t7e1l60lTKBUVFViyZAnL8kkZr2CkyF8URbhcrjt+TqSlpQUulwtxcXEhyyBlE2pqaljDvJMR1XgVHR2NzZs3y7IvvufUZrON6v5rampYBnrgc2u+wY3D4fAL6ANNvwUKJAYGjEB/x+sbkDQ0NPjdyEfScOopZaJ8n5lpbW1FQUEBy/aeO3eOHQffIFQS6v3RIGU/pOya77OzKpUKLpeLfekj3OnpYDo7O2XTdVKnPhrXb01NjV8mD/jxJiid4xs3bviVK9jjADU1NUhLSwvZtzmdTlRWVrLs2s6dO9l7er0ev/3tbwH8GCRKeJ7HvHnz8F//9V+YNm0apk2bhi+++IIFHKIoym6QBw4cYO1GFEW8/fbbqK+v99tmoGOckJDAzjEwOn2JbzsKto9XXnkF7777Lrq6uvDRRx+hubl5WJk/6Xo8fvx4wPM/0vsbzJw5c3Dx4kU0NDSwpIxkqP1ja2srmpqa2LW6dOnSgPuSjq1vH5WYmIiGhoYhPU84UKjydXZ24vLlywAGjy2GSjpPH3/8MVsmxSLBgl3pnPmWwzfTmJqaKruv3GtGNWjU6/UoKSmBUqnEL3/5S1m0nZeXFzI1/PLLL7PnJqQplvj4eDY6feuttwD8mE156aWXZCOiZ555ho1chzJt7qu3txd6vZ6N/o8ePYpf/vKX4Hl+SGXwLftIP883HiQmJmLevHl499132U1FOl7/+7//O2r7FUWRTYtJpExJTU0NnnnmGTQ0NECpVCIvL8/v81LAu3LlStm59W2D0jf4pWyXlP3x3fZoP6s63HoC/ZkorVbLyrthwwYUFRUhMTERiYmJyMjIYNM0gPxRg1Dvj5ZA2Y/MzEycPHkScXFxmDdvHqZPn44nn3xyRB51mDp1KtasWeNXz5G6fgdOhdlsNr8bhu+3QePj45GWloZHH300YLkGkqbsn3nmGcyZMwcfffQR9Ho9Fi5c6Lcuz/Po7OzE9OnT2TalgUdcXBwmT54cNPMUHx+P48ePIz4+HvHx8Thx4gT0ej1r/1K/mpiYiH/7t39j19f06dORlpYWMKsS6BjzPC+rd7C+ZGBfH47o6OiQ++jo6GA3+i+++GJEvpSi1+tx5syZgM+djsb+gomOjoZSqURsbKzfoDdU/9jb24sNGzbg1q1bOH36NJRKJZ588kkAYEmDDz/8EIWFhZgzZw57ftG3j/I95x999BGWLVsWVtkHK19sbCyOHj0aMrYIx/bt22Gz2WTT4YcOHRo0lvBt2xcvXpTFPr7PEN+LOABeIPh/Ws1x3APx/z6Sfkol/Z+qo+VBqWcgD0rdx1M9wymLKIrYs2cPNmzYMKrZ89HwoPRZ46lt3U1Drbcoinj33Xfx8ssvj/msXmFhIZYsWYLU1FQ2uAk1HT1WbSpY7DcQx3EA6Me9CSHkgeZ0OrF27Voolcp7LmAkZDzKzMzEq6++ekfZ1PGOMo1EhkbQo+dBqWcgD0rdx1M9x1NZRtOD0mc9KOdzoAel3vdKpnFIQSMhhBBCCLm/hBs0ThjJjRJCCCGEkPC43e67vs9Qvz4TCD3TSAghhBBCQqKgkRBCCCGEhERBIyGEEEIICYmCRkIIIYQQEhIFjYQQQgghJCQKGgkhhBBCSEgUNBJCCCGEkJAoaCSEEEIIuQd1d3fj888/v2u/80hBIyGEEELIPejbb79FZGQkOjs778r+7ihoFEURubm54DgOHMchIyMDDodjpMs2pHL8+te/hiiKQcsmvUwm06DbMpvNYdXDbDaHvY9gZR6vgh1L6ZWSkgKr1Toq+zYajaOyn/Pnz9/xtnzLNNr1Hw2BzqfRaAz4fm5uLmujZrNZ1rZNJpOs7larFdu2bRtXbdpqtaK4uFj2d0pKit916nsdm83mgNuSzrtv/xDsWJEHl9kMcFz/y7cpBVtuNPYvy8gApNuOw9H/N8cBubnAYM3KbDaPeB8kteuh3MvuxnbI4Do6OvDnP/8Zjz76KG7fvn1Xso1hB40OhwOrVq2CRqOB1+uFx+OBVqvF/v37R6N8QYmiiK1bt+Lbb78Fz/Nsucfjgc1mw5EjR+D1euH1enHkyBGUl5cPGhDabDZotVooFIoh7d9ms2HFihUQBAFerxcWiwVFRUVBbzyDlXm82717NzuWvsd0tBiNRiQkJLB9/cd//AeysrJGpHP89NNP7/izkZGRsFgssnIdO3Zs2GW6mzQaDWuzHo8HLpeLHdfm5makp6fD6/VCp9Ohvb0dAKBWq9HS0gJRFCGKIlpaWrB8+XI0NTUBAARBgFKpHDdt2mQyISkpCYsWLQLQ32ft2rULFRUV8Hg8aGlpgdVqhdVqRWlpKQRBgCAIAfsI6abn9XqRn5/P+rl33nmHHav09HRUVlbe3UreA9xuN44cOYLf/OY37PXBBx+gurp6rIs24qxWoLQUEIT+V3l5fwAYbLkUS3m9QH4+IN0+9+/v/9vrBTQaoLk5+D5tNhtiYmKgVqtHrB48z6OsrAzr1q0b1nak+7BWqx2Zgo2hGzdu4JVXXkFubi57bdy4EWVlZWNdNMTFxWH+/Pl46KGHMH/+fERGRo76PsMOGquqqgAAmzZtAvBjI8vPz4fD4UBGRgbMZrPfSMNoNCI3NxcZGRnIyMjAjh07ZH+3trYiIyNDlsGRtjcwmycFXwcOHEBBQUHA0YzUWEVRRF1dHbRaLW7fvh20fG1tbbhy5QqeeOIJvwxMML5Bpk6nw+rVq1FbW8vqK5U5NzcXTqfTr8y+WY57JVtx9uxZxMbGIi8vb1S2b7Va4XK5kJmZyZYZDAbk5eWhqakJoijCaDSym7t0HAH/Yy6KIsxmM7Kzs8FxHMrKyvDqq69iy5YtcDgcsuMvnW+Hw4Hc3FykpKQMqQ1ITCZTwMy7tDwjIwM//PDDSB2mETN79mzMmjULAKDX61FXVweO4+B2u6HT6QAAs2bNglKphMfjgcfjgVKpxNq1a9HV1QUAqK2txdKlS8esDr6MRiPa2tqwb98+djOtqqrCypUrodPpwPM8Zs6cCQA4duwYNm/eDJVKBYVCAY1GI9uWw+FAXV0d6+vUajUiIyP92uj9cGMcDX19fZgxYwZeeOEF9srOzsbt27fHumh+zGYz6zOsVivWrFmDU6dO+S0Llng4dgzYvBlQqQCFoj/gC7bc6QTq6oC/NCuo1YB0r8/PBwyGoZW5ra2N3YMGzoJI5TYajbK+LSMjQ3ZPHtj/SRl5qU8NdI8aOGMhret7v167di28Xu+IBrRj5c9//jPmzZuHsrIy9vr3f/931o88aMIKGqUAzGAwQKVS+b1vsVhw/fp1qNVq2UhDFEXY7XY0NjaipKQEv//973Hjxg3Z37/61a9gMBjg9XqxevVqFBcXo6OjA9evX8eRI0fg8XiwceNGtLW1ged5bN26FcuXL4fFYpGNigRBwPXr17F48WJwHAeFQgGbzYY9e/bAZrMNWr5HHnkEZ86cgcViQX19/aCZrba2Nr9jY7fbAfRfPFlZWSwDeeXKFXR3d8vKvHDhQvzLv/wL6uvrIQgCbDbbuM9WiKKI999/H6tWrUJBQcGo7WfmzJl+WatQN2bfY+7xeBAVFcUyZY899hi8Xi9yc3Oxb98+lJSUAADKy8tZ1i0hIUE2+Dh9+jTy8/Nl+3C73UhKSpJ1tJs2bYIoimwfXq8XBoMBFosFVqsVLS0t8Hg8MJlM8Hq9I3B0hsdut0OtVrNro7KyEh6PBwBQWVmJK1euIDs7mwVKQP/AMCEhARaLBRaLBQDw8MMPw2q1oqOjAwCQlJR09ysTQH5+PjZt2gSr1cpuWF1dXVi4cCGA/jbsdrvZiFwqt3QMfGcaBEGATqdjfZ0gCJg+fToEQUBycjJro/dLRuVBZjAYkJOTg7KyMhQXF6O0tBRPP/2037JA9z1prC9dAn9pSuC4wMs9HkCn6w8kgf4M5PTpP25Pms5eujR4ACndb6SBjt1ux8aNG+HxeHDkyBHYbDZ4PB4kJCTAbrdDFEXs378fBoMB69atg9FohNlsZll2s9nM/gb6B0hWq9XvHtXc3Ix33nnnL/Xo35c0iN+/fz+0Wi08Hg/+4R/+Ad9++234J4KMeyP6RRibzYbU1FTMmjWL3Yx9A7S8vDzodLqgfxcUFIDjOBaQSKO6hQsXsnUSEhIAAE1NTeA4zm8kIzV632nEqqoqqFSqkOVLT08f0hSb7wUrrd/e3o7GxkaWcXnllVfAcRwLMtRqtazMgiCgpaUFixcvhlqtHtdTNq2trVi7di327t0Lp9OJgoICKJXKUdvftWvXws66qlQqdHd3s2Dok08+Ye9JbcaXIAhobGxkAdT69evZQECj0QR8TGHg9LTUrnieB8/z7Jk5qf36BhcqlQqcdBcZQ77T016vFzk5OaiqqoLVakVXVxeqq6uxa9cuFBYWYs2aNWzgpNVqYbPZWFZRpVJBo9Hg1KlTcLlcQ36s424QBAFRUVFQKBQsSJT6ifb2drhcLrauVG4pGPa9/qUgUVJbW8uOg+9MRktLy32RUXnQGQwGuN1u5OTksOAw0LKBpGBQugT+0pQgjREHLne75UFibS3gO+YwGORT2YH3+eP9cOD9yzcDKbXXTz75BGazmQ1y7Xa7X51sNptsyrupqQmpqanQ6/VQqVSoqqqCXq+H3W7HgQMHoFAosH79egCA0+mE2WxGTk4Ou4ZGeuqcjA9hBY08zyM9PR1ms1k2/ZaSkoKWlhbU1dWxQOrYsWN+Qd3A0fjAv+vr69nNrKysDBEREazhSRlE6TNtbW0BM57BnvOQsqSDlU8y2HsA/AJYURRRXFzMLjBpROf1erF79252AQ8ss+8zkV6vd9jPkYyWxMREfPjhh3j99ddx7NgxzJgxY9T2pdPpoFQqWdbVaDTCZDLhyy+/REZGBgDA5XKxwYEU6FmtVpw9e5ZlGpcvXz7oftRqNVJTU2XHf2BmcagcDgeOHTuGM2fOsHMu7UN6FtDhcIyLTGMg0jV19uxZOBwO6HQ6JCcnY+7cuWyKOikpCXV1dfjyyy9Zdm7p0qWora2VZd3GA99gned5REZGQhAEdp0+++yziI6OBtB/LTscDpSWluL555+XbUetVrMpeLPZDLvdDr1ez27EQH92VqlUsuNE7l0mkwkzZszAiRMn2GAp0LKBpKDQ4+kP8kpLgeefD75crQb+0qxgNgN2O6DX938xRnokXhCAqKgftxGM7z3Ud9ZMus+p1Wpcv34dzz33nF+QKPWdVVVVuH79OsvGB3q232QyISMjA06nEwBk3xmoqqpi15PNZpM9EjaeBpNkZISdaczMzIRWq2UZmvLycpw+fRrJyclIT09n2ULgx8bnm9UD4Pe3SqVCfn4+m1KWnl0c+OWUGTNmyAK5goICv+fOfEdZvqSAN1j5pk6dyp7nOn78OEpKSqBQKAJ+A0wKYNevX88yWwBQXFzMpvJ8s6a+GUmpzAaDAQaDgR3H8fxNXKkuEyZMYOdHGmGOhvz8fLS1tbHjt379evzTP/0TXnvtNQBAcnIyy+BeunQJAFi2luM4PPHEEwB+zDr7crvdyMrKgiAIyMnJYcd/qN9+D0ShUMBut0OhULC2ZbPZWPClUCiwbt26cZFp9J2e5jiODWR0Oh1WrlzJ3mtra0NCQgK7vqTM4uTJk1l7V6vVuHHjBrvZjBdSRlDy9NNPIysrC7KIpCcAABEtSURBVAqFAunp6TAYDOB5HkuXLoVarYZarcbmzZuh0+lk3xTX6XRwu93sUYQ9e/aA53nZs591dXX4xS9+MUY1Hf++/vpr/PGPf2Svuro63Lx5c6yL5cdkMqGurg45OTl48cUXsWvXLhw4cMBvWaBnGnm+fypZre5/bd7cP/0cbLlO159t5Lj+QHHPnv51N2368RvVWVnAiy/2Lw9EugdJ/x74/KCU0Jg1axZSU1OxceNG9gyu9HjX8ePHwXEcioqKUFFRAZ1Oh7a2Nna/ktZXKBQoKipCSUkJNBoNtm7diqKiItljOiqVCjk5OVi/fj0UCgUOHDggu+/d6/7nf/4HhYWF7PWrX/0K33zzzVgXa0xwALwAgmZBOI4btxkSQsYzq9WKQ4cO4Y033mDPWU6cOHGsi0UIIWScuVs/zu1LqVQOOb6Tkh4TRrNAhDzIpKl2KTM3Hr89TQgZntGeQKCcDRlPKNNICCGEEDKG7pVMI/03goQQQgghJCQKGgkhhBBCSEgUNBJCCCGEkJAoaCSEEEIIISFR0EgIIYQQQkKioJEQQgghhIREQSMhhBBCCAmJgkZCCCGEEBISBY2EEEIIISQkChoJIYQQQkhIFDQSQgghhJCQJoT7gb6+Ppw8eRIzZ85EWloaW97Q0ACLxYLly5cjLi4urG02NTUhJiYG06ZNQ3V1NfR6/ZC38Yc//AFJSUmy9Xt6elBfX48nn3wSERERYZWF/Kivrw+1tbX4q7/yH1v09vZi0aJFYZ9rQgghhNybwg4au7u78f3338Pj8bBlHR0dEAQBSUlJmDZtWljb6+vrQ1dXF+bMmYO+vj58//33iIqKGvJnv/vuO7/1e3p68NBDD1HAOAKmTZuGhQsX+i1vamoag9IQQgghZKyEHTS63W5MnDgR3333Hfr6+hAREYELFy5g8uTJ8Hg8iIiIgMViwZ/+9CcAgEqlwsqVK9Hd3Y1PPvkEP/zwg2z56dOn0dHRgfr6esyfPx+3bt3CRx99BACIi4vD008/Ldt/T08PTpw4AVEUkZCQAACyfU6YMAGPPvooFApF0Do0NDQgOjoaSUlJbN96vR7t7e146qmnWDY1ISEB165dYxnLU6dOYcqUKfB4PCy7abFYcOnSJaxcuZKCVEIIIYTct8IOGp1OJ9RqNXp7e9HX14crV64AACZOnIiJEyeio6MD58+fR3Z2NqKionDq1CnZOn//938PAKipqUFfXx8SEhIwZcoUpKWloaGhAZMnT2ZBpsVike27r68PNTU1ePzxx5GUlISGhgZ899136O7uZvuMiIjAyZMn8dhjjwWtQ3R0NJxOJwDgwoULSElJQUxMDL766itWJ57nMXfuXFy7dg19fX3o7u7GDz/8gAULFuDcuXNwu93o6+vD5cuX8Td/8zcUMBJCCCHkvhb2F2Fu3ryJGTNm4KGHHoIgCLh8+TKSkpIgCAJmzZqF9vZ2zJo1i00ZT5kyBUB/sPnoo48iKioKPT09mDhxIiIiIuB0OhEdHc22/dhjjyEiIgJut9svW9jd3Y2JEyfikUceYcumTJnit8+JEyciMjIyaB0iIyPh8XhYUJqUlMSCPkEQcOnSJSxevBgRERGsns3NzdDr9YiIiGBB57lz56BWq+m5PkIIIYTc98IKGvv6+gAAsbGxmDJlCpxOJ2JjY6FWqwM+i9jR0YH29nbExsbi5s2bLDh0u92YMKE/yXnz5k3Exsair68PP/zwAwv22tra2PqB9PT04Ouvv/Zb58qVK7h169agz0VGRUXB4/Hg0qVLmD9/PgCwAPHcuXOYOXMm+7xCoYDFYsGECRNYcBgZGQlBEHDt2jX89Kc/HfLxI4QQQgi5V4U1PS1N0UZERCAyMhKff/45nn32WVnmcMGCBTh58iR+/etfY8KECVi+fDkiIiJkAaHT6WQZSFEUUVNTgyVLlmDChAmYNm2aXwApiYuLw4ULF3D48GEAAM/ziI2NRWxsLE6cOIEvvviCrRcVFSV7dtFXREQEvv/+e8ycOVOWJVQoFLh16xYWLFjAlkVHR+Prr7/Gs88+y5ZFRUXh1q1bePzxx4f8pZ17VXd3N6qrq/2W9/b2IiYmZgxKRAghhJCxwAHwAoDX6w28AscFfW+86+7uBgC/b3QH+0meQD/fEyjw7OjogMViwVNPPTXKNSCEEELI/c7tdt/1fSqVyiHHdxzHAbiPf9y7p6cHn3/+uV8msKGhAb/73e8wf/58FjB2dHTg/fffh0KhYAFjT08PysvLcfPmTVnAeOrUKXz66adYtGjR3asMIYQQQsgYu68zjYQQQggh4x1lGgkhhBBCyH2DgkZCCCGEEBISBY2EEEIIISQkChoJIYQQQkhIFDQSQgghhJCQKGgkhBBCCCEhUdBICCGEEEJCoqCREEIIIYSEREEjIYQQQggJiYJGQgghhBASEgWNhBBCCCEkJAoaCSGEEEJISGEHjWazGRzHwWg0AgBMJhM4jkNubi5EURxWYU6cOAGr1Qqz2YyMjAw4HI4hf9ZoNLIyDSxvuNsi/URRRG5uLjiOC/hKSUmB1Wod8X0ajUbZ+bJardi2bduQ25fZbIbJZBqxMtXU1AzafgLtz2q1ori4WLbs//7v/0asTHci0Pn0vWZ83/e9ngfWz2Qyyc59uOfnbhh4/KV+a2C79V1uNpsDbstoNILjOFk/EuxYEULI/SzsoNFmsyErKwt2ux0OhwN1dXUjUhCTyYT//M//hFqths1mg1arhUKhGNJnRVGE3W5HQkJCwPKGsy3ib/fu3fB6vbLXkSNHxrpYQRkMBqxbt25EtiWKIhobG0dkW+OBRqOBIAjwer3weDxwuVwsgGpubkZ6ejq8Xi90Oh3a29sBAGq1Gi0tLRBFEaIooqWlBcuXL0dTUxMAQBAEKJVK8Dw/ZvXyZTKZkJSUhEWLFrFltbW1qK+vh9frxfnz56HT6WC1WlFaWgpBECAIAsrLy/0GB1Kw7PV6kZ+fj/379wMA3nnnHXas0tPTUVlZefcqeI9wu904cuQIfvOb37DXBx98gOrq6rEuGiFDRu1YLuygsaurC7NmzQIAfPPNN7h16xY2btwIjUbDbhpWqxUpKSl+o3opKym9pJG7yWTC+vXrUV1djddeew1WqxUHDhyAQqEIOpL3Hek/99xzaGxshFarle0nJSUFv/3tb2VlG8jhcCAjI4NlGaQsSlVVFVasWMHKbjQakZGRgQMHDrDySJ+VspxS1kaq/0hmu8aLs2fPIjY2Fnl5eWOyf+mYB2pb2dnZSElJwdGjR2EymWTr+ra3QNsQRRHbtm3DihUrZOtWVlaioKAAr732Gux2u2x798P5nT17Nrue9Xo96urqwHEc3G43dDodAGDWrFlQKpXweDzweDxQKpVYu3Yturq6APQHZEuXLh2zOvgyGo1oa2vDvn37oFarAfS3mS+//BK7d++Wnbdjx45h8+bNUKlUUCgU0Gg0sm1Jg+JNmzYB6A+eIyMjYbVa4XK5kJmZCQCs3yFyfX19mDFjBl544QX2ys7Oxu3bt8e6aIQMGbVjubCCRofDgbNnz2L27NkA+gOIuXPnQqPRsCyf1WpFVlYW8vLy4PV6kZeXh+LiYoiiiLa2NqxYsQKCIKC+vh7Xr1+HIAjIzMzExo0bceTIERQXF6OrqwsbN26Ex+PBkSNHYLPZ4PF4ZGWprKyEzWaDIAgoKChAS0sL239RURHq6+tx+vRpcBw3aJ0UCgW0Wi1sNhscDgfKy8uRl5eHxx9/HBzHQRAEWK1WHD9+HPn5+fjpT3/KylNVVQUA2LRpExISEmC32yGKIo4dO4bU1FR2U7lfiKKI999/H6tWrUJBQcGo7cdut0OtVrPgLCkpCT09PQCA/fv3IycnB16vFxUVFTh06BAbUPzd3/0dzp8/z4IglUqFqqoqeL1e7N69G/n5+VCpVEG30dPTg4KCAni9XhgMBlgsFmRmZmL37t3Ys2cPent7YTKZ4PV6YbFYWPYtmMOHD8sGSd9///2oHbOh8j22CoUClZWV7NqqrKzElStXkJ2dzQIlAOB5HgkJCbBYLLBYLACAhx9+GFarFR0dHQCApKSku1+ZAPLz87Fp0yZYrVYWNAqCgMmTJ+PQoUMQBAF1dXWw2+0Afiy3dAx8ZyQEQYBOp4NKpWJ/T58+HYIgIDk5mQ1EpdkMQgi534UVNAqCAAB47LHHcPPmTezfvx+pqamw2+2s0xQEATExMcjIyGCfs9lscDqdsNvtMBgMUKlUsNlsiImJgVqtRnt7O8sUejwe2Gw2pKeng+d5tLW1+U0vi6KIuro65OTksA49OTkZarUaTU1NSE1NhV6vZ+sHmraW8DzPMgxSEJiRkcGCSQAsCNTr9VCr1Zg6dSoLMKUySOtKAWZOTs64ma4brtbWVqxduxZ79+6F0+lEQUEBlErlqO3PdwpVCtCioqIAAJGRkVi4cCGA/sxPT08Pu+EHu3EbjUYsXboUBoMh6DZEUYRGo2FBRKA2M2fOHOzfv98vkA1mw4YNsin9iRMnhn8wRtjAY5uTk4OqqipYrVZ0dXWhuroau3btQmFhIdasWcMyudLASsoqqlQqaDQanDp1Ci6Xa1w9/iEIAqKioliZdDodysrKEBcXx9YZGCRKwbDvNSsFiZLa2lp2HKS2Jk3XSwEqIYTcz8IOGidPnoxJkybBYrEgJiYG8fHxsNlssvWkDKIUWBkMBkRHRwP48WbsGwxKgaZvtkKr1bJnFYNNL7e1tQHo78ylABQAywRaLBZUV1eHzAIkJCSgrq5OFgRKweSJEydkQaC0j/feew8AWHCsVqtx69YtlJWV+QWt97rExER8+OGHeP3113Hs2DHMmDFjzMridrtlz9L5BgeBDAwYg21jKAG+yWTC0qVL/QLZe510fZw9exYOhwM6nQ7JycmYO3cum6JOSkpCXV0dvvzyS3adLl26FLW1tbKs23jgmwmUHjuQgt+qqipoNBoWQHo8HjgcDpSWluL555+XbUetVrMpeLPZDLvdDr1ezwJHoD87q1Qq2XEihJD7WVhBo81mg0ajwcMPP4yYmBg2xef1elkwZTAYsHr1aiQlJUGtVsNgMCA/P59lEH0DON9gsLq6GuvWrcNXX30l2x7gn/XheR45OTkoKCgAx3EoKChgAahvELd48WKWgRz47KIvrVaLAwcOQKvVyqaUExISUFRUhNWrV7OgQ6FQYPLkySgqKmLTndL+bty4gcbGRmzdunVc3USHSzrOEyZMYFOt69evH5OybNq0CeXl5eA4DllZWXjxxReDHmuz2YyCggIsXrxY9vxiONsA+qd0161bh6lTp7Jt7dq1CwD8HpsY7wZO/be1tcFgMECn02HlypXsvba2NiQkJLDndKXM4uTJk1mQLrV5KWs7XkgZQaC/r3jxxReRlZUFjuNQV1eHX/ziF+B5HkuXLoVarYZarcbmzZuh0+lk3xTX6XRwu93sW+Z79uwBz/OyZz+l7ZHAvv76a/zxj39kr7q6Oty8eXOsi0VIWKgd/4gD4AX6vx0YcAWOC/revebgwYPIzMxkgZ5E+iJOfX29LCNlNBpx/PhxVFRUsEyCw+HAunXroNVqUVxcLPvyT1ZWFlavXo38/Py7VylCCCGE3NPcbvdd36dSqRxyfCd9P+SB+XFvk8kEhUIhCxilb2CvX78eu3fvZgGjlJUsKChAXl4eCxjNZjPUajWuX78uyyZKP/ERExMj+wIBIYQQQsj94oHKNBJCCCGEjDeUaSSEEEIIIfcNChoJIYQQQkhIFDQSQgghhJCQKGgkhBBCCCEhUdBICCGEEEJCoqCREEIIIYSEREEjIYQQQggJif1OIyGEEEIIIcFQppEQQgghhIT0/wFW8EsKSi/lAQAAAABJRU5ErkJggg==)

  


  * Past Schedule (read-only)
    * This would be a read-only embedded spreadsheet with the same columns as the Publication Schedule embedded spreadsheet (data and formatting moved down from Publication Schedule via the nightly process mentioned above)
    * The most recent past Publication Date would be at the top and the list would go down from there



  


General Notes: 

An ad is considered to be "inactive" or "in the past" when it no longer is actively running or scheduled to run in the future, and it will continue to show in the list for the customer. Ads cannot be deleted.

  


If the main Ad Price for an ad has changed during the time that a customer has pre-paid for that ad to be run, PNP wants to honor the price that the customer paid for it. Also, if a price has been manually changed on an individual running, it should remain the same. However, if a customer has scheduled multiple ads but has not prepaid for them, and the ad price changes during that time period, the customer would pay the new price when that goes into effect. This is handled by locking the prices on the Publication Schedule as mentioned above. Note that prices on the Past Schedule will always be locked.

  


Development Specification

Notes: 

  * Note that there is a difference between Ads Details and individual runnings of ads. I think there could be confusion about this. Were not having separate records for the ads, but I might still be referring to them as "Ad Records" or "Ad Details" because of this. There can be (and normally will be) multiple runnings/occurrences/publications of each Ad ("Ad Detail"). 



  


Ads Upload/Preview: 

  * Have an upload memo to upload items.
  * Have a database trigger (or something similar) to send it to S3. Store the S3 (with the preview) on a separate record to avoid collisions. Scrub the uploads memo on a nightly basis. If we don't like having seeing the files in the upload memos, then we could copy it from the visible Upload memo to a hidden memo on save, then scrub the hidden memo at night to avoid collisions.



  


Actual Ad Dimensions:

  * For JPEG or PNG files, this is calculated by converting pixels to inches, using 96 PPI. 
    * Tim Reitz 01/06/2021: Here is a converter that uses 96 PPI, and it looks like others do too: [http://www.unitconversion.org/typography/pixels-x-to-inchs-conversion.html](http://www.unitconversion.org/typography/pixels-x-to-inchs-conversion.html)



  


Schedule RGs:

  * The Schedule RG will be a linked RG. Work with Ellis to set this up. For reference, see the Client Proposals Detail Screen. 
  * The current date should remain in the Publication Schedule RG until it is in the past.
  * Have a nightly process that moves all past dates from the Publication Schedule RG to the Past Schedule RG (as needed) and updates the Publication Schedule RG to include 1.5 years of dates.



  


Ad Prices: We are thinking of using a hidden "Override Price" checkbox to lock/unlock prices.

  


Run Until Further Notice: This can be implemented using an OnInit on the RG's Run field.
