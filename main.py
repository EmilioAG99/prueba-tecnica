from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Opening JSON file
f = open('cities.json')

# returns JSON object as a dictionary
cities = json.load(f)

def calculateScore(city, lat): 
    score = round (1- (abs(float(city['latitude'])-lat)/10),2)
    return score

def sortCities(cityList):
    for i in range(len(cityList)):
        for j in range(0,len(cityList)-1-i):
            if(float(cityList[j]['score'])< float(cityList[j+1]['score'])):
                aux = cityList[j]
                cityList[j] = cityList[j+1]
                cityList[j+1] = aux
    return cityList

@app.route("/search", methods=['GET'])
def search():
    #saving arguments from query 
    arguments = request.args
    
    #check if the query has all the elements to make a request
    hasLatitude = "latitude" in arguments
    hasLongitude = "longitude" in arguments
    hasCity = "q" in arguments
    if arguments:
        if hasCity:
            #Iterate to find all cities that contain the sent search term, this doesnt have a score since the parameters longitude and latitude are missing
            filteredData = [ {"latitude": city['lat'], "longitude": city['long'], "name": "{0}, {1}".format(city['name'],city['country'])} 
                            for city in cities if arguments['q'].lower() in city['name'].lower()]
            
            if hasLatitude and hasLongitude:
                lat = arguments['latitude']
                long = arguments['longitude']
                #check if latitude and longitude can be converted to float 
                try:
                    lat = float(lat)
                    long = float(long)
                    #The latitude and longitude values are used to filter the data and to find a score for the given cities
                    matchCoordinates = [ {"latitude": city['latitude'], "longitude": city['longitude'], "score": calculateScore(city,lat), "name":city['name']}
                                        for city in filteredData  if (float(city['latitude'])>=lat-5 and float(city['latitude'])<=lat+5) 
                                        and (float(city['longitude'])>=long-10 and float(city['longitude'])<=long+10)]
                    if(len(matchCoordinates)>0):
                        #once we found the matched cities, its time to sort the elements based on their score
                        return jsonify({"search": sortCities(matchCoordinates)})
                    else:
                        return jsonify({"search": []})
                except:
                    #If latitude or longitude cant be converted to float, it will send an error message
                    return "Invalid type value in latitude or longitude"
            elif (hasLatitude and not hasLongitude) or (not hasLatitude and hasLongitude):
                return "Missing latitude or longitude"
            else:
                if len(filteredData) > 0:
                    return jsonify({"search": filteredData})
                else:
                    return jsonify({"search": []})
        #If the query cant be run, a message will se sent to the user
        else:
            return "Missing one or more parameters",400
    else:
        return  "Missing one or more parameters",400
