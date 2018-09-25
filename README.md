# OpenFlow

OpenFlow is a Python library which lets you handle data flows into your application. It uses pandas.DataFrame as its primary tool.

You can find a basic introduction to OpenFlow [here](https://blog.lapw.at/serverless-data-fetching-stack-openfaas-openflow/).

## DataSource

DataSource objects are used to extract data from data feeders such as Databases, JSON or CSV files. You can find examples on how to build your own DataSource [here](examples/datasources.py). It has to inherits from DataSource and implement the `run(self, data)` function.

