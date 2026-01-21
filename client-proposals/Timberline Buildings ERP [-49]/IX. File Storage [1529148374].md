9\. File Storage

  


Requirements

Files will be stored in Amazon S3 storage. TOS will have an Upload link that will open a new tab, allowing drag-and-drop of the file to automatically upload.

  


Some of these, such as Contracts, maybe linked to a special field. Others may be stored as a simple, uncategorized collection of files.

  


Development Specification

I propose that on the File record, we have some kind of categorization, such as "Customer Contract", etc.

  


This will then be interfaced as;

  


Contract: File Name.pdf   [...]   Upload

  


Where the ellipsis pulls up prior versions and perhaps date

The File record would be included as part of the S3 integration, I think, but we might need to check with Josh.

  


TODO_IDD: We should probably take a look at file sizes to make sure transfers aren't going to be an immense issue. I'd like to avoid Dropbox if possible, just because it's more cumbersome to implement.
