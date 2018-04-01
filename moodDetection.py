"""This code is using DecisionTree classifier for predicting the 
genre of the songs based on 5 features.
This code can be extented to any number of features.
Written by - Rohit Bajaj """

import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from sklearn import tree
from urlparse import urlparse
import random
import numpy

def some_function():
    print "some_function got called"

#Output
genres = ["rock", "pop", "classical", "jazz"]
dTree = None

#Features
gender = ["male","female"]
ageGroup = ["10-20","21-30","31-40","41+"]
location = ["home","work","travel","exercise","none"]
time = ["morning","afternoon","evening","night","none"]
heartRate = ["low","medium","high","none"]

genderG = {'male' : 1 , 'female' : 2}
ageGroupG = {'10-20' : 1, '21-30' : 2 , '31-40' : 3 , '41+' : 4}
locationG = {'home' : 1 , 'work' : 2 , 'travel' : 3 , 'exercise' : 4 , 'none' : 5}
timeG = {'morning' : 1 , 'afternoon' : 2 , 'evening' : 3 , 'night' : 4 , 'none' : 5}
heartRateG = { 'low' : 1 , 'medium' : 2 , 'high' :3 , 'none' :4}


class test:
    def show(self):
        return "aaaa"

class http_server:
    def __init__(self, t1):
        myHandler.t1 = t1
        server = HTTPServer(('', 8000), myHandler)
        server.serve_forever()

def trainModel():
    global dTree # Accessing the global variable

    trainingX = numpy.loadtxt("/Users/rba/Desktop/EmojiHackathon/trainingX.txt", delimiter=',') 
    trainingY = numpy.loadtxt("/Users/rba/Desktop/EmojiHackathon/trainingY.txt", delimiter=',')

    """For testing purpose"""
    """testTrainingX = [[1,2,4,3,3],[1,2,3,1,1],[1,3,2,2,2],[1,2,2,2,2],[1,2,1,4,1]]
    testTrainingY = [1,2,3,1,3]
    dTree = tree.DecisionTreeClassifier()
    dTree = dTree.fit(testTrainingX,testTrainingY)"""

    dTree = tree.DecisionTreeClassifier() 
    dTree = dTree.fit(trainingX,trainingY) # fitting the classifier with X and Y
    """dTree.predict([[1,2,2,2,2]])"""


def detectMoodOfUser(heartRate,gender,time,ageGroup,location):
    global dTree
    print(heartRate, gender, time, ageGroup, location)
    print("Model prediction staring")
    """Checking the values are passed to the server correctly or not """
    if not heartRateG[heartRate] > 0  and heartRateG[heartRate] < 5:
        print "Wrong heart-rate information"
    if not genderG[gender] > 0  and genderG[gender] < 2:
        print "Wrong gender information"
    if not timeG[time] > 0  and timeG[time] < 6:
        print "Wrong time information"
    if not locationG[location] > 0  and locationG[location] < 6:
        print "Wrong location information"
    if not ageGroupG[ageGroup] > 0 and ageGroupG[ageGroup] < 5:
        print "Wrong age-group information"

    print "All correct"
    """Forming the input array to the model for prediction"""
    inputArray = [[genderG[gender], ageGroupG[ageGroup], locationG[location], timeG[time], heartRateG[heartRate]]]
    print inputArray
    resultArray = dTree.predict(inputArray)
    print resultArray
    result = genres[int(resultArray[0])-1]
    print result
    return result

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
    	"""Respond to a GET request."""
    	self.send_response(200)
    	self.send_header("Content-type", "text/json")
    	self.end_headers()
    	#self.wfile.write("<html><head><title>Title goes here.</title></head>")
        query = urlparse(self.path).query
        path = urlparse(self.path).path
        self.result = ""
        if urlparse(self.path).path == '/detectMood':
            query_components = dict(qc.split("=") for qc in query.split("&"))
            heartRate = query_components["heartRate"]
            gender = query_components["gender"]
            time = query_components["time"]
            ageGroup = query_components["age"]
            location = query_components["location"]
            print location
            self.result = "{Genre:\""+ detectMoodOfUser(heartRate,gender,time,ageGroup,location) + "\"}"
            print self.result
        self.wfile.write(self.result)
        return

class main:
    def __init__(self):
        self.t1 = test()
        trainModel()

        self.server = http_server(self.t1)

if __name__ == '__main__':
    m = main()
