# Principles_0f_big_data
## Team Details
    Sireesha Keesara
    Ahamed Raziuddin
    Bhavaz Akula

# Phase 1
Firstly we generated Twitter Access keys from the developers.twitters.com using our twitter accounts.

Using tweepy package in python we downloaded data on topic Pulwama Attack and Love.

Writing python code again we extracted url and hashtags for downladed tweets and the output is our translated input.

We loaded traslated input to hdfs directory using "HDFS DFS -copyFromLocal source path HDFS destination path" command in the terminal.

We used the example word count program which is part of haddop installation and produced word count for the large data.

simillarly we executed spark word count job for the same input data to process the data. and the out put is in the folder
