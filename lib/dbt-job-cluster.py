# Databricks notebook source
# MAGIC %md
# MAGIC Install and configure requirements for a dbt job cluster.
# MAGIC
# MAGIC #### Required environment variables:
# MAGIC - `DBT_PROJECT_NAME` - fairly self-explanatory, the name of your dbt project.
# MAGIC - `DBT_PROJECT_DIR` - the path where the dbt project to be deployed is to be saved locally.
# MAGIC - `DBT_PROJECT_GIT_REPOSITORY` - the git repository containing the dbt project to be cloned.
# MAGIC
# MAGIC #### Optional environment variables:
# MAGIC - `DBT_REPOSITORY_REF` - the git reference to be cloned. If not set, `prod` is taken as the production branch name.
# MAGIC - `DBT_GITHUB_SSH_PRIVATE_KEY` - the raw code of a SSH key. If set, the SSH key will be placed at `~/.ssh/github_id` and the ssh config will be created for the host github.com.
# MAGIC - `DBT_CORE_VERSION` - the package version of `dbt-core` to be installed when not already installed (e.g. via dependencies in a workflow task). If not set, 1.8.9 is taken.
# MAGIC - `DBT_SPARK_VERSION` - the package version of `dbt-databricks` to be installed when not already installed (e.g. via dependencies in a workflow task). If not set, 1.8.0 is taken.

# COMMAND ----------

# MAGIC %run ./dbt

# COMMAND ----------

# MAGIC %sh
# MAGIC if [ -z "${DBT_PROJECT_NAME}" ]
# MAGIC then
# MAGIC   echo 'You must provide environment variable DBT_PROJECT_NAME in your cluster configuration when using this lib.'
# MAGIC   exit 1
# MAGIC fi
# MAGIC mkdir -p /root/.dbt
# MAGIC echo "$DBT_PROJECT_NAME:
# MAGIC   target: default
# MAGIC   outputs:
# MAGIC     default:
# MAGIC       type: spark
# MAGIC       method: session
# MAGIC       schema: dbt
# MAGIC       host: NA
# MAGIC       threads: 14
# MAGIC
# MAGIC elementary:
# MAGIC   target: default
# MAGIC   outputs:
# MAGIC     default:
# MAGIC       type: spark
# MAGIC       method: session
# MAGIC       schema: dbt_elementary
# MAGIC       host: NA
# MAGIC       threads: 14" > /root/.dbt/profiles.yml