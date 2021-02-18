File
====

The ``File`` object is needed to store the metadata about the files
used in a project.  The object indicates the IPFS link to the file,
besides other metadata such as uploader, uploaded time, file name, ...

``id`` : ``string``
   UUID unique to the upload.

``cid`` : ``string``
   Content identifier of the file in CID_ v1.

``name`` : ``string``
   Name of the file.

``size`` : ``integer``
   Size of the file, in bytes.

``time`` : ``datetime``
   The time when the file was uploaded.

``user`` : ``string``
   Username of the uploader.

.. _CID: https://github.com/multiformats/cid
