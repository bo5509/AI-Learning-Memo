

import urllib
import urllib.request,urllib.response,urllib.error,urllib.parse

# If you are using Python 3+, import urllib instead of urllib2

import json


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"],
                    "Values": [ [ "0", "0", "audi", "gas", "std", "four", "sedan", "fwd", "front", "114.5", "189.7", "72.6", "56.4", "1640", "ohc", "four", "140", "mpfi", "3.18", "3.4", "8.5", "140", "5500", "18", "25", "0" ], [ "0", "0", "value", "value", "value", "value", "value", "value", "value", "0", "0", "0", "0", "0", "value", "value", "0", "value", "0", "0", "0", "0", "0", "0", "0", "0" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/58fbc8370a4046499459a962c9fb05ef/services/d4ddaa543f7c4060ae1484b0b3d1e1df/execute?api-version=2.0&details=true'
api_key = '51kAm7jbApICZycNt41x1/CP7zyekyJCF0qQpAnIRNFR0YKxhv0MCpnXvQeWCFV2Fg3pjyyeRhgD0cCi8vnsqQ==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers)
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(json.dumps(json.loads(result),indent=2))
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))

