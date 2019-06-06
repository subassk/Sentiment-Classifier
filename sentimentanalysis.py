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

    
    
    
    
