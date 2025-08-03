# Databricks notebook source
# MAGIC %md
# MAGIC # Kapitel 1

# COMMAND ----------

print("Hello CAS Data Engineering from Python")

# COMMAND ----------

# MAGIC %sql  
# MAGIC SELECT "Hello world from SQL!"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Titel 1

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Titel 2

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Titel 3

# COMMAND ----------

# MAGIC %run "./oreilly-databricks-dea/Chapter 1 - Getting Started with Databricks/Setup"

# COMMAND ----------

print(book_publisher)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()          # Übersicht aller Module  

# COMMAND ----------

dbutils.fs.help()       # Hilfe speziell zu Dateioperationen

# COMMAND ----------

files = dbutils.fs.ls("/databricks-datasets/")   # Listet Dateien & speichert Ergebnis
display(files)                                   # Zeigt Ausgabe als Tabelle mit Download/Visualisierung

# COMMAND ----------

