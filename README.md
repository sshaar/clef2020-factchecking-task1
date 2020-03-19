# CLEF2020-CheckThat! Task 1

This repository contains the _dataset_ for the [CLEF2020-CheckThat! task 1](https://sites.google.com/view/clef2020-checkthat/tasks/tasks-1-5-check-worthiness?authuser=0).

It also contains the _format checker, scorer and baselines_ for the task.

````
FCPD corpus for the CLEF-2020 LAB on "Automatic Identification and Verification of Claims"
Version 1.0: March ?, 2020 (Data and Baseline Release)
````

This file contains the basic information regarding the CLEF2020-CheckThat! Task 1
on evidence retrieval estimation dataset provided for the CLEF2020-CheckThat! Lab
on "Automatic Identification and Verification of Claims".
The current version (1.0, March ?, 2020) corresponds to the release of a
part of the training data set.
The test set will be provided in future versions.
All changes and updates on these data sets and tools are reported in Section 1 of this document.

__Table of contents:__

- [CLEF2020-CheckThat! Task 1](#clef2020-checkthat-task-1)
  - [Evaluation Results](#evaluation-results)
  - [List of Versions](#list-of-versions)
  - [Contents of the Distribution v1.0](#contents-of-the-distribution-v10)
  - [Data](#data)
    - [Data Format](#data-format)
  - [Results File Format](#results-file-format)
  - [Format checkers](#format-checkers)
  - [Scorers](#scorers)
    - [Evaluation metrics](#evaluation-metrics)
  - [Baseline](#baseline)
  - [Licensing](#licensing)
  - [Credits](#credits)

## Evaluation Results

TBA

## List of Versions

* __v1.0 [2020/03/?]__ - Training data. The training data for task 1 contains (?) Tweets.

## Contents of the Distribution v1.0

We provide the following files:

* Main folder: [data](data)
  * [training.tsv](data/training.tsv) <br/>
  Contains all the tweets with claim worthiness labels.
  * [README.md](README.md) <br/>
    this file


## Data

The annotation of the tweets were done according to the following guidline. 

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


### Data Format

The datasets are text files with the information TAB separated. The text encoding is UTF-8. You will get:

> topic_id <TAB> tweet_id <TAB> tweet_url <TAB> tweet_text <TAB> claim <TAB> claim_worthiness

Where: <br>
* topic_id: unique ID for the topic the tweet is about <br/>
* tweet_id: Tweet ID for a given tweets given by Twitter <br/>
* tweet_url: URL to the given tweet <br/>
* tweet_text: Text of the tweet <br/>
* claim: 1 if the tweet is a claim; 0 otherwise <br/>
* claim_worthiness: 1 if the tweet is worth fact checking; 0 otherwise <br/>

Example:
> covid-19	1235648554338791427	https://twitter.com/A6Asap/status/1235648554338791427	COVID-19 health advice⚠️ https://t.co/XsSAo52Smu	0	0 <br/>
> covid-19	1235287380292235264	https://twitter.com/ItsCeliaAu/status/1235287380292235264	There's not a single confirmed case of an Asian infected in NYC. Stop discriminating cause the virus definitely doesn't. #racist #coronavirus https://t.co/Wt1NPOuQdy	1	0 <br/>
> covid-19	1236020820947931136	https://twitter.com/ddale8/status/1236020820947931136	Epidemiologist Marc Lipsitch, director of Harvard's Center for Communicable Disease Dynamics: “In the US it is the opposite of contained.' https://t.co/IPAPagz4Vs	1	1 <br/>
> ... <br/>

## Results File Format

For this task, the expected results file is a list of tweets with the estimated score for check-worthiness. Each row contains two tab-separated fields:

> topic_id <TAB> tweet_id <TAB> score <TAB> run_id 

Where: <br>
* topic_id: unique ID for the topic the tweet is about given in the test dataset file <br/>
* tweet_id: Tweet ID for a given tweets given by Twitter given in the test dataset file<br/>
* score: score given by the participant's model about whether a claim is worth fact checking or not <br/>
* run_id: string identifier used by participants. <br/>

Example:
> covid-19	1235648554338791427	0.39 <TAB> Model_1<br/>
> covid-19	1235287380292235264	0.61 <TAB> Model_1<br/>
> covid-19	1236020820947931136	0.76 <TAB> Model_1<br/>
> ... <br/>

## Format checkers

TBA

## Scorers

TBA

### Evaluation metrics

#TODO

## Baseline

TBA

## Licensing

  These datasets are free for general research use.

## Credits

Task 1 Organizers:

* Alex <br/>

* Firoj Alam, Qatar Computing Research Institute, HBKU <br/>

* Shaden Shaar, Qatar Computing Research Institute, HBKU <br/>

* Giovanni Da San Martino, Qatar Computing Research Institute, HBKU <br/>

* Preslav Nakov, Qatar Computing Research Institute, HBKU <br/>

Task website: https://sites.google.com/view/clef2020-checkthat/tasks/tasks-1-5-check-worthiness?authuser=0

Contact:   clef-factcheck@googlegroups.com

