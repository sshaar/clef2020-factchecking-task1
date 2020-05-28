This folder contains a zip file [test-input.zip](test-input.zip) with the test files without the gold labels. 
There are 140 tweets that will be used to test your models. 
<br>
The ZIP file contains two files a json file containing the Twitter object of the test tweets and a TSV file that has an identical format to that in the training/dev set, except that the fifth and the sixth columns are missing.  

For instance, test-input.tsv looks like this:

> topic_id	tweet_id	tweet_url	tweet_text <br>
> covid-19	1237160250513522688	https://twitter.com/user/status/1237160250513522688	POTUS wanted everyone to know he was in close contact with Gaetz and Collins today, both of whom were supposedly exposed to Corona. Did he look worried at the presser? No. It’s a message. <br>
> covid-19	1237125962871037953	https://twitter.com/user/status/1237125962871037953	Who would you prefer to lead our nation’s response to the growing #coronavirus threat? <br>
> [...]

The folder [test-input](./) contains also a [submission_instance.tsv](submission_instance.tsv) file that is an example of what we 
expect the participants to submit.

As mentioned in the main page in the [Results File Format subsection](https://github.com/sshaar/clef2020-factchecking-task1#results-file) the submission files should have the same format as the files used during training: tab-separated topic_id, tweet_id, score and run_id one instance per line, where the score is the judgment given by the participants about whether a claim is worth fact-checking.
From the example:

> [...] <br>
> covid-19	1237178597024108552	0.25891675029296335	random <br>
> covid-19	1237049051058561024	0.5112747213686085	random <br> 
> covid-19	1237185090079383553	0.4049341374504143	random <br>
> covid-19	1237050222485868544	0.7837985890347726	random <br>
> [...]

The scores in the example submission were computed using the random baseline given in [baseline script](../baselines/baselines.py).

We have implemented some [checkers](../format_checker/main.py), but it is still the responsibility of the participants to double-check that their submissions are correct. <br>

You should submit the output TSV file via the [submission link](https://docs.google.com/forms/d/e/1FAIpQLSfsBfruzsYLg9mngQmLkKjBeyazxeAD-uknonXqJhVoozsKDg/viewform). 
<br>
You have to submit **ONE** primary submission, and optionally you could submit up to **TWO** contrastive runns. 
<br>
If you make multiple primary/contrastive 1/contrastive 2 submissions, only the latest ones will be considered.
<br>
The official ranking will be based on the primary submission.

As a reminder, the participants can submit predictions more than once, but only the last one before the deadline 
**(5 June 2020)** will be evaluated and considered as official. 
