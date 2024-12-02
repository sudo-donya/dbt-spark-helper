# Databricks dbt helper

This repository holds helper Databricks notebooks to deploy dbt projects on a Databricks job cluster.

&nbsp;

## But, why?

All-purpose clusters are quite expensive in comparison to job clusters.

## Running dbt on a job cluster

*Note:* Does not work with Python models, see [databricks/dbt-databricks#586](https://github.com/databricks/dbt-databricks/issues/586)

*Follow these steps to run dbt on a job cluster:*

1. Clone this repository into your Databricks workspace

2. Create a dedicated job cluster and add the environment variables specified in the lib notebooks when configuring it.

3. Create a new workflow. As its first "step", add a notebook task which executes ```lib/dbt-job-cluster``` from the repo you cloned.

4. Create a new python notebook and add it as second task dependent on the ```lib/dbt-job-cluster``` task.
Add the python code contained in ```run-dbt.py``` as the first task of this new notebook.

Now you can call all your favourite dbt commands inside the notebook as additional tasks like so:
```
dbt(['deps'])

dbt(['run', '-s', 'tag:hourly'])
```
## Why so convoluted?

The ```dbt-databricks``` package is essentially useless when you want to run something on a job cluster since it requires a Databricks API token and the Databricks API can’t be used inside a job cluster, no matter what. I’ve tried using a developer token, creating the token on runtime, passing it via environment variables and connecting to the spark cluster from the python notebook — nothing worked. The only thing that seems to work on a job cluster is to run a notebook inside Databricks with SQL or python commands against the current Spark session.

And here is where I figured out that one can “ingest” dbt commands: the ```dbt-spark``` package offers a config option to use the current spark session. In combination with the programmatic invocation feature, it is possible to run dbt inside a python notebook:

## Limitations of this approach:

* No way to take advantage of ```dbt-databricks```-specific features such as Unity Catalog support, liquid clustering etc.

* No way to execute models in an environment that contains different catalogs (i.e. databases)