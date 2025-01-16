HTTP Request Module
===================

This module provides functionality for testing HTTP services by sending GET requests.

Functions
---------

.. autofunction:: check_http

Usage Example
-------------

Here is how to use the function `check_http` to check the availability of HTTP services:

.. code-block:: python

   from request_module import check_http

   urls = [
       "https://example.com/",
       "https://google.com/",
   ]

   for url in urls:
       check_http(url)
