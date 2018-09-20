## OpenFlow

OpenFlow is a Python library that lets you automate data flows into your application.

### DataSource

DataSource objects are used to extract data from data feeders such as Databases or json Requests. You can find examples on how to build your own DataSource [here](examples/datasources.py). It has to inherits from DataSource and implement the `run(self, data)` function.

### Openflow

Openflow objects are used to extract data from DataSources and train Artificial Intelligence models. You can define several inputs such as `x` or `y` to train / predict over the model.
