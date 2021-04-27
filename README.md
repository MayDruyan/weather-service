# Tomorrow.io Weather Service

### URL to working service
https://weather-service-tomorrowio.herokuapp.com/

### How to use the service
Using Postman:
1.	For /weather/data, send GET request with body as json:  
{  
    "lon": "-178",  
    "lat": "-90"  
}
2.	For /weather/summarize, send GET request with body as json:  
{  
    "lon": "-178",   
    "lat": "-90"  
}


### Future Developments
- Implement a listener to new data such that a user can enter csv files and keep querying the DB for results
- Support more conversions (for example from Kelvin to Celsius)
- Implement a logging system such that the server will be able to show logs and document its actions
- Add another service that does the pre-processing of the csv files, such that the server will be independent
