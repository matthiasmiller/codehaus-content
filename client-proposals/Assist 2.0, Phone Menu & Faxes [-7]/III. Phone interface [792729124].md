3\. Phone interface

  


Requirements

The menu interface described above will be accessible via a phone interface. This interface will allow access in two ways:

  * Moving through the menu tree interactively for ease of use or for unfamiliar parts of the menu. In this mode, the user would listen to the menu choices, then press the desired number, followed by #. This would move them to the next part of the menu. At any point, the user could press the # key to return to the home menu.
  * Direct access by immediate dial of a series of numbers to a specific item for efficient selection. Menu item numbers can be separated with an asterisk. For example: 3*2*50#.



  


USER SPECIFICATION

In addition to the normal menu content, inside each folder will be a special menu, accessible via the 0 key, with the following actions:

  * Print menu items listing
  * Print menu tree
  * Add new document
  * Delete document
  * Search
  * List most commonly used menu items (via fax)
  * List recent transmissions (via fax)
  * Get cover sheets (see fax interface)



  


Numbers 6 - 8 will be available only from the home menu.

  


If a user selects a PIN-protected document either interactively or with immediate dial, the system will prompt the user to enter their PIN before producing the document.

  


Menu items description

#1: sends via fax a listing of all folders or files in that directory (but only immediate children.) This could be useful in the following situation: a user wants to get a specific drawing, but the list of drawings may have been updated. Rather than listening to the entire menu by phone, they can request a listing to be faxed to them so they can make a rapid selection.

#2: like #1, but includes all descendants of that menu location. This is more comprehensive, but may result in large faxes.

#3: this allows the user to prepare to upload a document. (See below.)

#4: delete a document. The user will be prompted for the access # of the item. Once they make a selection, the document title will be read to them and they will be asked to confirm. (In the case of a mistake, a deleted document may be recovered by the administrator.)

#5: Search (see below)

#6: Users may find themselves mostly using only a few menu items, and want to have a quick way to get those menu items so they can remember which numbers to request via immediate dial or fax cover sheet.

#7: This would include the most recent faxes that have been sent or received to/from the system. This would include date+time, fax #, number of pages, and the document title (if applicable.)

#8: Some users may prefer to make requests via a fax cover sheet instead of using the phone menu. If so, they can use this item to have the fax cover sheets faxed to them. If the user selects this item, the system will allow them to enter their PIN to get a list of cover sheets with their PIN included.

  


Searching

A user can look for documents or menu items in two ways:

  * By viewing recent transmissions (most recent 50 faxes, for example)
  * By searching for text in the menu. Text can be entered with the phone number pad ("22" = b, for example, with * as a delimiter.) This will search the menu item name, but not the content.



  


Adding a new document

A user can add a new document by selecting the the "Add new document" and entering access number as well as the document title with the phone number pad (just like searching.) The system will then accept the next fax from that number as the document content. This will time out after 20 minutes. The new access number may be left blank, in which case the system will automatically assign them.

Users will only be able to upload documents into certain folders (in the example menu, these folders are marked "input via fax") Permissions can be configured for these folders by an administrator; initially, these folders will be marked as being limited to a specific company and only users from that company will be able to store documents in their folder.

  


Development Specification

The phone interface needs to be driven from an Invest report, so that we can respect permissions and visibility, PIN-protection, etc. How do we keep this fast enough? I think that we need to cache listing. Do we do that when the user calls in? Can we make the report fast enough?

  


Whenever the user makes a selection, we add a transmission record with the menu item chosen, then poke the transmission daemon to start processing the queue.
