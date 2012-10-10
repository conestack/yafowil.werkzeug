Introduction
============

This is the Werkzeug integration for YAFOWIL.

This package registers a global preprocessor for yafowil. 
It wraps a Werkzeug derived request instance.


Special behaviors
-----------------

Werkzeug params are returned in MultiDicts ``mixed`` flavor. This is how
YAFOWIL expects them. 
IOW: If a query-key exists several times the values are aggregated in a list.
If a query-key exists one time, the value is returned as string.  
     
File Uploads provided by Werkzeug (stream, filename, mimetype, headers) as
are turned into Dicts with the keys:

**file**
    file-like object to read data from

**filename**
    submitted name of the upload

**mimetype**
    type of the upload

**headers**
    all headers 

**original**
    keeps the original stream object


Detailed Documentation
======================

If you're interested to dig deeper: The
`detailed YAFOWIL documentation <http://yafowil.info>`_ is available.
Read it and learn how to create your example application with YAFOWIL.


Source Code
===========

The sources are in a GIT DVCS with its main branches at
`github <http://github.com/bluedynamics/yafowil.werkzeug`_.

We'd be happy to see many forks and pull-requests to make YAFOWIL even better.


Contributors
============

- Jens W. Klein <jens@bluedynamics.com>

- Robert Niederrreiter <rnix@squarewave.at>

- Dorian Santner <dorian.santner@gmx.net>
