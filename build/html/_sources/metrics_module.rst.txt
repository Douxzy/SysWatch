Metrics Module
==============

This module provides functionality to monitor system metrics (CPU, memory, and disk usage) 
and expose them via an HTTP server for Prometheus.

Contents
--------

Metrics
-------

The following Prometheus metrics are defined in this module:

- **CPU Usage**: A gauge metric labeled by individual CPU cores that tracks CPU usage percentage.
- **Memory Usage**: A gauge metric tracking the overall memory usage percentage.
- **Disk Usage**: A gauge metric labeled by mount points, tracking disk usage percentage.

Functions
---------

The module defines the following functions:

.. autofunction:: record_metrics
.. autofunction:: expose_metrics

Main Entry Point
----------------

The module exposes metrics through an HTTP server when executed directly. Metrics are periodically updated and exposed at the `/metrics` endpoint.

.. note::
   To run the module:
   
   .. code-block:: bash
   
      python3 metrics_module.py
