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
