# Data Exploration With Matplotlib and D3.js

This is a small library built with Tornado, Matplotlib and Pandas to summarize and visualize any datasource in the browser.

Installation
------------

To install, simply: ::

    $ pip install data-explorer

Usage
-----

Starting Data Explorer:

    from data-explorer import DataExplorer

    dte = DataExplorer()
    dte.read_csv('example.csv')  #  connect csv data source
    dte.start()  #  starts a new server on port 9011 by default;

Basically this is how it works;

1. Data is loaded using the `Pandas` library
2. The server start with websocket support to the browser
3. Descriptive summary (Descriptive Statistics) of columns is generated and sent through the socket and rendered in the browser.
4. Distribution of values (`Boxplot` and `Barplot`) in each columns is then generated using `Matplotlib` and sent to the browser as `json`.
5. `D3.js` is then used to render the `json` plot in the browser


Documentation
-----------------

Documentation can be found [here]()


Running the Tests
-----------------

To run tests

    python -m tornado.testing tests/functests.py
