# Project 3: Understanding User Behavior

- I am a data scientist at a game development company  

- I set up data pipeline to track two events on a mobile game: `buy a
  sword` & `join guild`

- Each has metadata characterstic of two events (i.e., sword type, guild name)


## Content

- Instrument the game API server to log events to Kafka  (game_api.py)

- Assemble a data pipeline to catch these events: use Spark streaming to filter
  select event types from Kafka, land them into HDFS/parquet to make them
  available for analysis using Presto (all_stream_and_hive.py)

- Use Apache Bench to generate test data for the pipeline 

- Produce an analytics report where I provide a description of the data pipeline
  and some basic analysis of the events (project-3-FL.ipynb)


The events in this pipeline are _generated_ events which make
them hard to connect to _actual_ business decisions.  However, I tried my best to demonstrate my ability to plumb this pipeline end-to-end, which
includes initially generating test data as well as submitting a notebook-based
report of at least simple event analytics.


