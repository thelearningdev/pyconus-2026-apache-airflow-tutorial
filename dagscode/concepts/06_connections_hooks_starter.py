from datetime import datetime
from airflow.sdk import dag, task


@dag(dag_id="06_connections_hooks_starter", start_date=datetime(2026, 1, 1), schedule=None, catchup=False, tags=["concepts", "starter"])
def connections_demo():

    @task
    def check_database():
        # Before running: go to Admin > Connections and create the bookops_postgres connection.
        # Conn ID: bookops_postgres | Type: Postgres | Host: postgres
        # Database: bookops | Login: airflow | Password: airflow | Port: 5432
        # TODO: Import PostgresHook from airflow.providers.postgres.hooks.postgres.
        #       Create hook = PostgresHook(postgres_conn_id="bookops_postgres").
        #       Run hook.get_first("SELECT version()") and print the result.
        pass

    check_database()


connections_demo()
