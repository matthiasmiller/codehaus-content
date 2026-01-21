8\. Shed drawings (batch uploads)

  


Requirements

There is a drafter who develops the drawings and blueprints for various buildings. He maintains many files that should be accessible from the software. The software should make these files available via fax, including automatically updating them when necessary.

  


USER SPECIFICATION

To facilitate storage of these shed drawings, the drafter will need to convert them to PDF and send them to the administrator. The software will include a program to run on the administrator's computer to store the files in the software, so that they are available via fax.

  


The files may be arranged in folders to better organize the drawings. In order to facilitate a stable number access while allowing the drafter to rename the files, the files should be named like "NNN_content.pdf", where NNN is the access #.

  


The upload program will automatically detect which files have been modified, and upload only the files that have changed. It will also automatically create the menu structure implied by the drawing files' folder structure supplied by the drafter. It will do this by comparing the list of documents stored on the server with the files stored on the client, and compare the difference between the two. Any files that show up on the administrator's computer not on the server will be uploaded, and any files on the server not on the administrator's computer will be marked as deleted.

  


The upload program will not run on a schedule, but must be run manually. When run, it will display a list of changes to be made, and allow the user to confirm before continuing.

  


Development Specification

We need to think this one through a bit more. Will the drafter really be willing to organize his files to facilitate the menu structure?? If not, then the administrator will need to reorganize them upon receipt.

  


The files may be organized by folders. Again, can't mix folders and files.

  


The filename is "NNN_content.pdf", where NNN is the access #.

  


If a file is deleted, the file is marked as deleted in the DB. If it comes back, it's un-marked as deleted (we match on access # (+ name?).

  


The root folder will have a config.ini that contains the username/password, as well as the parent folder ID.

  


What about an updater mechanism?

  


25 hours?
