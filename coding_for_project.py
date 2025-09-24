import requests
import re
import matplotlib.pyplot as plt


def get_words_from_gutenberg(url):
    # Fetching the content of the file from the Gutenberg project
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the content.")
        return []

    # Extracting text from the response
    text = response.text

    # Tokenizing the text into words and filtering out non-ASCII words
    words = re.findall(r'\b[a-zA-Z]+\b', text)

    return words

def dictOfLengths(url):
    words = get_words_from_gutenberg(url)
    
    length_dict = {}
    for word in words:
        if len(word) in length_dict:
            length_dict[len(word)] += 1
        else:
            length_dict[len(word)] = 1
            
    sumOfResultDict = sum(length_dict.values())
    for key in length_dict: 
        length_dict[key] = length_dict[key]/sumOfResultDict
        
    return length_dict

def dictOfLengthsMultiple(url_list):
    result_dict = {}
    for url in url_list:
        curr_dict = dictOfLengths(url)
        for key in curr_dict:
            if key in result_dict:
                result_dict[key] += curr_dict[key]
            else:
                result_dict[key] = curr_dict[key]
    sumOfResultDict = sum(result_dict.values())
    for key in result_dict: 
        result_dict[key] = result_dict[key]/sumOfResultDict
    return result_dict

def draw_histogram(data):
    keys = list(data.keys())
    values = list(data.values())

    plt.bar(keys, values)
    plt.xlabel('Length', fontsize = 15)
    plt.ylabel('Relative Frequency', fontsize = 15)
    plt.xlim(0, 12)
    plt.ylim(0,0.25)
    plt.show()
    
def getDictDistance(dict1,dict2):
    distance = 0
    for key in dict1:
        if key < 13:
            distance += (dict1[key] + dict2[key])**2
    distance = distance ** 0.5
    return distance

def orderDictByFrequency(powerFrequencyLength):
    ls = []
    
    for length in powerFrequencyLength:
        ls.append(powerFrequencyLength[length])
    ls.sort(reverse=True)  
    return ls

import math
import matplotlib.pyplot as plt

def drawLogGraph(orderedList,start = 1,end = 7):
    rank = []
    freq = []
    for i in range(start,end+1):
        rank.append(math.log(i))
        freq.append(math.log(orderedList[i-1]))
    plt.scatter(rank,freq)
    
    plt.xlabel("Logarithm of rank", fontsize = 15)
    plt.ylabel("Logarithm of relative frequency", fontsize = 15)
    
    plt.show()
    
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def drawLogGraphWithTrendLine(orderedList,start = 4,end = 7):
    rank = []
    freq = []
    for i in range(start,end+1):
        rank.append(math.log(i))
        freq.append(math.log(orderedList[i-1]))
    plt.scatter(rank, freq)
    
    slope, intercept, _, _, _ = stats.linregress(rank, freq)
    plt.plot(np.array(rank), slope*np.array(rank) + intercept, color='red', label='Trend Line')
    
    plt.xlabel("Logarithm of rank", fontsize = 15)
    plt.ylabel("Logarithm of relative frequency", fontsize = 15)
    
    plt.legend()
    plt.show()
    
    return slope

def getGradientOfTrendLine(orderedList,start = 4,end = 7):
    rank = []
    freq = []
    for i in range(start,end+1):
        rank.append(math.log(i))
        freq.append(math.log(orderedList[i-1]))
    
    slope, intercept, _, _, _ = stats.linregress(rank, freq)
    
    return slope

