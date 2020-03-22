import argparse
import re
import logging


"""
This script checks whether the results format for Task 5 is correct. 
It also provides some warnings about possible errors.

The correct format of the Task 5 results file is the following:
<line_number> <TAB> <score>

where <line_number> is the number of the claim in the debate 
and <score> indicates the degree of 'check-worthiness' of the given line.
"""

_LINE_PATTERN_A = re.compile('^[1-9][0-9]{16,22}\t([-+]?\d*\.\d+|\d+)$')
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)


def check_format(file_path):
    with open(file_path, encoding='UTF-8') as out:
        file_content = out.read().strip()
        for i, line in enumerate(file_content.split('\n')):
            topic_id, tweet_id, score, run_id = line.strip().split('\t')

            if not _LINE_PATTERN_A.match("%s\t%s"%(tweet_id, score)):
                # 1. Check line format.
                logging.error("Wrong line format: {}".format(line))
                return False
            tweet_id = int(tweet_id)
            score = float(score.strip())

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred_file_path", "-p", required=True, help="The absolute path to the file you want to check.", type=str)
    args = parser.parse_args()
    logging.info("Task 5: Checking file: {}".format(args.pred_file_path))
    check_format(args.pred_file_path)