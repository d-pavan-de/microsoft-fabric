# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "b4912435-e602-48e4-bae5-da2b9feedf77",
# META       "default_lakehouse_name": "LH_demo",
# META       "default_lakehouse_workspace_id": "564203eb-7d67-4112-95f3-e61a02eaa88f",
# META       "known_lakehouses": [
# META         {
# META           "id": "b4912435-e602-48e4-bae5-da2b9feedf77"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/shortcuts/csvfiles/departments.csv")
# df now is a Spark DataFrame containing CSV data from "Files/shortcuts/csvfiles/departments.csv".
df.createOrReplaceTempView("df_tempview")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC select * from df_tempview

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
