# Initializing dbt
from dbt.cli.main import dbtRunner, dbtRunnerResult
dbt_runner = dbtRunner()

# Helper function to run dbt inside a notebook
def dbt(dbt_args: [str], exception_on_fail: bool = True,
        return_result: bool = False) -> dbtRunnerResult:
    res: dbtRunnerResult = dbt_runner.invoke(dbt_args)
    if exception_on_fail and not res.success:
        print(f'Exception: {res.exception}')
        raise Exception(f"dbt {' '.join(dbt_args)} failed")
    if return_result:
        return res