# Tomorrow.io Weather Service
In this assignment I have created a weather service using Flask, Python and SQLAlchemy that processes csv files into PostgreSQL DB, such that the user can query
for data points concerning specific location. It returns temperature by celsius and precipitation by mm/hr. If needed, it converts the data from the csv file to this measurement.
The user can also get a summary of weather for a specific location.
The service is given as API and is deployed on Heroku.

### URL to working service
https://weather-service-tomorrowio.herokuapp.com/

### How to use the service
Using Postman:
1.	In order to get data points of specific location, using the route /weather/data, send GET request with body as json:  
{  
    "lon": "-178",  
    "lat": "-90"  
}
2.	In order to get a summary of the data points of specific location, using the route /weather/summarize, send GET request with body as json:  
{  
    "lon": "-178",   
    "lat": "-90"  
}


### Future Developments
- Implement a listener to new data such that a user can enter csv files and keep querying the DB for results
- Support more conversions (for example from Kelvin to Celsius)
- Implement a logging system such that the server will be able to show logs and document its actions
- Add another service that does the pre-processing of the csv files, such that the server will be independent

