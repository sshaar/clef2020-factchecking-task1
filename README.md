# CLEF2020-CheckThat! Task 1 on Check-Worthiness for Tweets

This repository contains the _dataset_, _format checker, scorer and baselines_ for the [CLEF2020-CheckThat! task 1](https://sites.google.com/view/clef2020-checkthat/tasks/tasks-1-5-check-worthiness?authuser=0). 
The task consists in ranking a stream of tweets according to their check-worthiness. 

````
FCPD corpus for the CLEF-2020 LAB on "Automatic Identification and Verification of Claims"
Version 5.0: Jun 8th, 2020 (Data, Baseline, Test data Release)
````

This file contains the basic information regarding the CLEF2020-CheckThat! Task 1
on check-worthiness on tweets provided for the CLEF2020-CheckThat! Lab
on "Automatic Identification and Verification of Claims".
The current version (5.0, Jun 8th, 2020) corresponds to the release of the first batch of the training data set. 
The test set is released with the current version.

__Table of contents:__

- [CLEF2020-CheckThat! Task 1](#clef2020-checkthat-task-1)
  - [Evaluation Results](#evaluation-results)
  - [List of Versions](#list-of-versions)
  - [Contents of the Repository](#contents-of-the-repository)
  - [Data Format](#data-format)
    - [Input Dataset](#input-dataset)
    - [Results File](#results-file)
  - [Data Annotation Process](#data-annotation-process)
  - [Format checkers](#format-checkers)
  - [Scorers](#scorers)
    - [Evaluation metrics](#evaluation-metrics)
  - [Baseline](#baseline)
  - [Licensing](#licensing)
  - [Credits](#credits)

## Evaluation Results

You can find the results in this spreadsheet, https://tinyurl.com/y9sjooxo.

## List of Versions

* __v1.0 [2020/03/22]__ - Training/Dev data. The training data for task 1 contains 488 annotated tweets and the dev data contains 150 annotated tweets.

* __v2.0 [2020/05/17]__ - Training/dev data with updated labels. The training dataset has been extended to 672 annotated tweets, whereas the dev dataset contains 150 tweets.

* __3.0 [2020/05/26]__ - Input test data released

* __4.0 [2020/06/03]__ - Fixed test data tweet JSON object's formatting

* __5.0 [2020/06/08]__ - Test Data with gold labels released

## Contents of the Repository

We provide the following files:

* Main folder: [data](data)
  * Subfolder: [v1](data/v1)
    * [training.tsv](data/v1/training.tsv) <br/>
    Contains the training tweets with claim worthiness labels from the first (outdated) version of the data
    * [dev.tsv](data/v1/dev.tsv) <br/>
    Contains the dev tweets with claim worthiness labels from the first (outdated) version of the data
  * Subfolder: [v2](data/v2)
    * [training_v2.tsv](data/v2/training_v2.tsv) <br/>
    Contains the training tweets with claim worthiness labels from the second (and latest) version of the data
    * [dev_v2.tsv](data/v2/dev_v2.tsv) <br/>
    Contains the dev tweets with claim worthiness labels from the second (and latest) version of the data
    * [training_v2.json](data/v2/training_v2.json) <br/>
    Contains the [twitter object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object) for the tweets included in the v2 training dataset
    * [dev_v2.json](data/v2/dev_v2.json) <br/>
    Contains the twitter object for the tweets included in the dev dataset
    Note: Not all tweets which are included in the training and dev sets have a corresponding twitter object
  * Subfolder: [test](data/test)
    * [test-gold.tsv](data/test.zip) <br/>
    Contains the test tweets with gold labels
    * [test-input.json](data/test/test.zip) <br/>
    Contains the twitter object for the tweets included in the test set
* [README.md](README.md) <br/>
  this file
  
* Main folder: [test-input](test-input)
  * [test-input.zip](test-input/test-input.zip) <br/>
    File containing tweets used for testing

## Data Format

### Input Dataset

The datasets are TAB separated text files. The text encoding is UTF-8. 
A row of the file has the following format:

> topic_id <TAB> tweet_id <TAB> tweet_url <TAB> tweet_text <TAB> claim <TAB> check_worthiness

Where: <br>
* topic_id: unique ID for the topic the tweet is about <br/>
* tweet_id: Tweet ID for a given tweets given by Twitter <br/>
* tweet_url: URL to the given tweet <br/>
* tweet_text: content of the tweet <br/>
* claim: 1 if the tweet is a claim; 0 otherwise <br/>
* check_worthiness: 1 if the tweet is worth fact checking; 0 otherwise <br/>

Example:
> covid-19	1235648554338791427	https://twitter.com/A6Asap/status/1235648554338791427	COVID-19 health advice⚠️ https://t.co/XsSAo52Smu	0	0 <br/>
> covid-19	1235287380292235264	https://twitter.com/ItsCeliaAu/status/1235287380292235264	There's not a single confirmed case of an Asian infected in NYC. Stop discriminating cause the virus definitely doesn't. #racist #coronavirus https://t.co/Wt1NPOuQdy	1	0 <br/>
> covid-19	1236020820947931136	https://twitter.com/ddale8/status/1236020820947931136	Epidemiologist Marc Lipsitch, director of Harvard's Center for Communicable Disease Dynamics: “In the US it is the opposite of contained.' https://t.co/IPAPagz4Vs	1	1 <br/>
> ... <br/>

Note that the gold labels for the task are the ones in the *check_worthiness* column 

### Results File

For this task, the expected results file is a list of tweets with the estimated score for check-worthiness. Each row contains four tab-separated fields:

> topic_id <TAB> tweet_id <TAB> score <TAB> run_id 

Where: <br>
* topic_id: unique ID for the topic the tweet is about given in the test dataset file <br/>
* tweet_id: Tweet ID for a given tweets given by Twitter given in the test dataset file<br/>
* score: score given by the participant's model about whether a claim is worth fact checking or not <br/>
* run_id: string identifier used by participants. <br/>

Example:
> covid-19	1235648554338791427	0.39  Model_1<br/>
> covid-19	1235287380292235264	0.61  Model_1<br/>
> covid-19	1236020820947931136	0.76  Model_1<br/>
> ... <br/>

## Data Annotation Process

The annotation of the tweets were done according to the following guidelines. 

We define a factuale claim as a claim that can be verified using factual, verifiable information such as statistics, specific examples, or personal testimony. For each tweet, we would label it as a claim or not based on that definition.
Some positive examples include: stating a definition, mentioning quantity in the present or the past, etc.
Some negative examples include: spersonal opinions and preferences.

If a tweet contains a factual claim, we determine if it is worth fact checking we try to answer 3 questions and based on their answer we determine of the tweet is worth fact checking. The questions we tried to answer were:

* *To what extent does the tweet appear to contain false information?* <br/>
False information is news, stories or hoaxes created to deliberately misinform or deceive readers. To answer this question most often it is important to open the link to the tweet and to see if the tweet contains a link to an article from an reputable information source (e.g., Reuters, Associated Press, France Press, Aljazeera English, BBC) then the answer could be “Contains no false info”.

* *Will the tweet's claim have an effect on or be of interest to the general public?* <br/>
In general, topics such as healthcare, political news and findings, and current events are of higher interest to the general public. If it has higher interest to the public then fact-checking such tweets is important.

* *To what extent does the tweet look weaponized, i.e., has the potential to do harm to the society or to person(s)/company(s)/product(s)?* <br/>
This can be measured as the extent to which the tweet aims to and has the capacity to negatively affect the society as a whole or specific person(s), company(s), or product(s) or to spread rumours about them. If a tweet is harmful then it is worth checking it's validity.


## Format checkers

The checker for the subtask is located in the [format_checker](format_checker) module of the project.
The format checker verifies that your generated results file complies with the expected format.
To launch it run: 
> python3 format_checker/main.py --pred_file_path=<path_to_your_results_file> <br/>

Note that the checker can not verify whether the prediction file you submit contain all lines / claims), because it does not have access to the corresponding gold file.

The script used is adapted from the one for the [CLEF2019 Check That! Lab Task 5 (check-worthiness for political debates)](https://github.com/apepa/clef2019-factchecking-task5).

## Scorers

Launch the scorer for the task as follows:
> python3 scorer/main.py --gold_file_path="<path_gold_file_1, path_to_gold_file_k>" --pred_file_path="<predictions_file_1, predictions_file_k>" <br/>

Both `--gold_file_path` and `--pred_file_path` take a single string that contains a comma separated list of file paths. The lists may be of arbitraty positive length (so even a single file path is OK) but their lengths must match.

__<path_to_gold_file_n>__ is the path to the file containing the gold annotations for topic/batch __n__ and __<predictions_file_n>__ is the path to the corresponding file with participants' predictions for topic/batch __n__, which must follow the format, described in the 'Results File Format' section.

The scorer invokes the format checker for the task to verify the output is properly shaped.
It also handles checking if the provided predictions file contains all lines / tweets from the gold one.

The script used is adapted from the one for the [CLEF2019 Check That! Lab Task 5 (check-worthiness for political debates)](https://github.com/apepa/clef2019-factchecking-task5).

### Evaluation metrics

The official evaluation measure is MAP, but we also report (P@5,10…,P@30). 

## Baseline

The [baselines](/baselines) module contains a random and a simple ngram baseline for the task.
To launch the baseline script you need to install packages dependencies found in [requirement.txt](requirement.txt) using the following:
> pip3 install -r requirements.txt <br/>

To launch the baseline script run the following:
> python3 baselines/baselines.py  <br/>

Both baselines will be trained on the training tweets from [training.tsv](data/training.tsv) and the performace of the model was was evaluated on the dev tweets from [dev.tsv](data/dev.tsv)
The performance of both baselines will be displayed:<br/>
Random Baseline AVGP: 0.34661954358047853<br/>
Ngram Baseline AVGP: 0.6926897425211712<br/>

The scripts used are adapted from the ones for the [CLEF2019 Check That! Lab Task 5 (check-worthiness for political debates)](https://github.com/apepa/clef2019-factchecking-task5).

## Licensing

  These datasets are free for general research use.

## Credits

Task 1 Organizers:

* Alex Nikolov, Sofia University <br/>

* Firoj Alam, Qatar Computing Research Institute, HBKU <br/>

* Shaden Shaar, Qatar Computing Research Institute, HBKU <br/>

* Giovanni Da San Martino, Qatar Computing Research Institute, HBKU <br/>

* Preslav Nakov, Qatar Computing Research Institute, HBKU <br/>

Task website: https://sites.google.com/view/clef2020-checkthat/tasks/tasks-1-5-check-worthiness?authuser=0

Contact:   clef-factcheck@googlegroups.com

