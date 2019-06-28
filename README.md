Falsk REST apis

How To Run :-

Python version = 3
Operating System = Ubuntu 16.04

install all requiremnts : $pip3 install requiremnts.text

Create database with Name : grexter

Go to project directory : $cd grexter -> $python3 app.py

Request guideline:

To add new record :

request url - http://localhost:PORT/addBuilding

parameters - {
	"name" : "karma",
	"address" : "17th main btm layput",
	"landmarks" : "btm taverkare madibala",
	"rooms": [
		{"flat_number":101, "name":"moon", "square_feet_area":200.16, "type":"1BHK", "no_of_bathrooms":2, "maintenance":"yes", "electricity_account_number": 1265008 },
		{"flat_number":102, "name":"sun", "square_feet_area":200.16, "type":"2BHK", "no_of_bathrooms":1, "maintenance":"yes", "electricity_account_number": 1265798 },
		{"flat_number":103, "name":"earth", "square_feet_area":200.16, "type":"2BHK", "no_of_bathrooms":3, "maintenance":"no", "electricity_account_number": 120000798 }
		]
}

headers = {
    'content-type': "application/json",
    }

Server Reponses :

Record Created success (code-200) -

{
    "message": "success",
    "building": Object                
}

Already exits (code-409):

{
    "message": "Building already exits",
    "building": Object
}

invalid parameters (422)-

{
    "message": "invalid parameters",
    "building": Object

}
