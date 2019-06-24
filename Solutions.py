STEP 1:

We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(strWord):
    for charPunc in punctuation_chars:
        strWord = strWord.replace(charPunc,"")
    return(strWord)
    
Result	Actual Value	Expected Value	Notes
Pass	'Amazing'	'Amazing'	Testing that the correct output is returned when #Amazing is provided as input.
Pass	'wow'	'wow'	Testing that the correct output is returned when wow! is provided as input.
Pass	'incredible'	'incredible'	Testing that the correct output is returned when #in.cred..ible! is provided as input.
Pass	'wonderful'	'wonderful'	Testing that the correct output is returned when wonderful is provided as input.
You passed: 100.0% of the tests

STEP 2:

Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents a one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurances there are of positive words in the text.

SOLUTION 1:
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(strWord):
    for charPunc in punctuation_chars:
        strWord = strWord.replace(charPunc,"")
    return(strWord)

def get_sentiment(strSentences, sentimentWords):
    strSentences = strip_punctuation(strSentences)
    print(strSentences)
    listStrSentences = strSentences.split()
    print(listStrSentences)

    count = 0
    for word in listStrSentences:
        for sentimentWord in sentimentWords:
            if word == sentimentWord:
                count += 1
    return count

def get_pos(strSentences):
    return get_sentiment(strSentences, positive_words)

SOLUTION 2:
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(strWord):
    for charPunc in punctuation_chars:
        strWord = strWord.replace(charPunc,"")
    return(strWord)

def get_pos(strSentences):
    strSentences = strip_punctuation(strSentences)
    print(strSentences)
    listStrSentences = strSentences.split()
    print(listStrSentences)

    count = 0
    for word in listStrSentences:
        for positiveWord in positive_words:
            if word == positiveWord:
                count += 1
    return count
    
OUTPUT:
what a truly wonderful day it is today incredible
['what', 'a', 'truly', 'wonderful', 'day', 'it', 'is', 'today', 'incredible']
what a truly wonderful day it is today
['what', 'a', 'truly', 'wonderful', 'day', 'it', 'is', 'today']
the weather is what it is
['the', 'weather', 'is', 'what', 'it', 'is']
The weather truely is abnormal - its october and already snowing
['The', 'weather', 'truely', 'is', 'abnormal', '-', 'its', 'october', 'and', 'already', 'snowing']


Result	Actual Value	Expected Value	Notes
Pass	2	2	Testing that the correct output is returned for get_pos.
Pass	1	1	Testing that the correct output is returned for get_pos.
Pass	0	0	Testing that the correct output is returned for get_pos.
Pass	0	0	Testing that the correct output is returned for get_pos.
You passed: 100.0% of the tests


STEP 3:

Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents a one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurances there are of negative words in the text.

SOLUTION 1:
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(strWord):
    for charPunc in punctuation_chars:
        strWord = strWord.replace(charPunc,"")
    return(strWord)

def get_sentiment(strSentences, sentimentWords):
    strSentences = strip_punctuation(strSentences)
    print(strSentences)
    listStrSentences = strSentences.split()
    print(listStrSentences)

    count = 0
    for word in listStrSentences:
        for sentimentWord in sentimentWords:
            if word == sentimentWord:
                count += 1
    return count

def get_neg(strSentences):
    return get_sentiment(strSentences, negative_words)
    
    
SOLUTION 2:

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(strWord):
    for charPunc in punctuation_chars:
        strWord = strWord.replace(charPunc,"")
    return(strWord)

def get_neg(strSentences):
    strSentences = strip_punctuation(strSentences)
    print(strSentences)
    listStrSentences = strSentences.split()
    print(listStrSentences)

    count = 0
    for word in listStrSentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count += 1
    return count

OUTPUT:

what a truly wonderful day it is today incredible
['what', 'a', 'truly', 'wonderful', 'day', 'it', 'is', 'today', 'incredible']
The weather truely is abnormal - its october and already snowing
['The', 'weather', 'truely', 'is', 'abnormal', '-', 'its', 'october', 'and', 'already', 'snowing']
their departure was rather abrupt However it was amusing how aloof they had been
['their', 'departure', 'was', 'rather', 'abrupt', 'However', 'it', 'was', 'amusing', 'how', 'aloof', 'they', 'had', 'been']
the weather is what it is
['the', 'weather', 'is', 'what', 'it', 'is']


Result	Actual Value	Expected Value	Notes
Pass	0	0	Testing that the correct output is returned for get_neg.
Pass	1	1	Testing that the correct output is returned for get_neg.
Pass	2	2	Testing that the correct output is returned for get_neg.
Pass	0	0	Testing that the correct output is returned for get_neg.
You passed: 100.0% of the tests


STEP 4:
Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.

SOLUTION :
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(strWord):
    for charPunc in punctuation_chars:
        strWord = strWord.replace(charPunc,"")
    return(strWord)

def get_sentiment(strSentences, sentimentWords):
    strSentences = strip_punctuation(strSentences)
    #print(strSentences)
    listStrSentences = strSentences.split()
    #print(listStrSentences)

    count = 0
    for word in listStrSentences:
        for sentimentWord in sentimentWords:
            if word == sentimentWord:
                count += 1
    return count

def get_pos(strSentences):
    return get_sentiment(strSentences, positive_words)

def get_neg(strSentences):
    return get_sentiment(strSentences, negative_words)

projectTwitterDataFile = open("project_twitter_data.csv", "r")
resultingDataFile = open("resulting_data.csv","w")
line = projectTwitterDataFile.readline()
count = 1
while line:
    if (count != 1):
        values = line.split(',')
        positive_score = get_pos(values[0])
        negative_score = get_neg(values[0])
        net_score = positive_score - negative_score
        #print("line {}: {} {} {} {}".format(count,values[1],values[2].strip(),positive_score,negative_score))
        #print("{},{},{},{},{}".format(values[1], values[2].strip(), positive_score, negative_score,net_score))
        resultingDataFile.write("{},{},{},{},{}".format(values[1], values[2].strip(), positive_score, negative_score,net_score))
        resultingDataFile.write("\n")
    else:
        resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
        resultingDataFile.write("\n")
    line = projectTwitterDataFile.readline()
    count += 1


OUTPUT:
Data file: resulting_data.csv
Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score
3,0,0,0,0
1,0,2,2,0
1,2,0,0,0
3,1,1,0,1
6,0,2,0,2
9,5,2,0,2
19,0,2,0,2
0,0,0,3,-3
0,0,0,2,-2
82,2,2,0,2
0,0,0,1,-1
0,0,1,0,1
47,0,2,0,2
2,1,1,0,1
0,2,1,0,1
0,0,2,1,1
4,6,3,0,3
19,0,2,1,1
0,0,1,0,1

Result	Actual Value	Expected Value	Notes
Pass	'Numbe...core\n'	'Numbe...core\n'	checking that the headers are set correctly.
Pass	'19'	'19'	checking that the value for a particular cell matches.
Pass	'-3'	'-3'	checking that the value of the net score is correct for a particular cell.
Pass	20	20	checking that the file has the correct number of rows.
Pass	5	5	checking that the file has the correct number of columns.
You passed: 100.0% of the tests
