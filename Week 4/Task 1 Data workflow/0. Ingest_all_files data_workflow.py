# Databricks notebook source
v_result = dbutils.notebook.run("1. Ingest_circuits_file data_workflow", 0, {"p_data_source": "Ergast API"})

# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("2. Ingest_Races_file data_workflow", 0, {"p_data_source": "Ergast API"})

# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("3. Ingest_Constructors_file data_workflow", 0, {"p_data_source": "Ergast API"})

# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("4. ingest_drivers_file data_workflow", 0, {"p_data_source": "Ergast API"})

# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("5. Assignment_ingest_result_file data_workflow", 0, {"p_data_source": "Ergast API"})

# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("6. Ingest_pit_stops_file_json data_workflow", 0, {"p_data_source": "Ergast API"})

# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("7. Ingest_lap_times_multiple_file data_workflow", 0, {"p_data_source": "Ergast API"})

# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("8. Ingest_qualifying_multiple_file data_workflow", 0, {"p_data_source": "Ergast API"})

# COMMAND ----------

v_result