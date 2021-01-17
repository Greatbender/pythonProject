# pythonProject
    #run main.py (server)
    #run client.py (client) to make a request 

#client.py
    #gets latitude and longitude (the user input) cia Console.py
    #interacts with the main App via API (sends lat and lon and gets the snowheight as return)

#main.py starts the App 
	#creats Flask APP
	#gets the current unit time via datemaker.py, 
	#creates engine an session for the DB
	#requests via request.py the wheater data form opneweather for the last 5 days
	(request.py gets waeather Data from external API and gives it to GetListsfromRequest.py), 
	(GetListsfromRequest.py evaluates wheaterdata and returns the sums of snowheight and the hours with melting conditions)
	#inserts the Data for every Day in a Table: ID, Day_Number, cumalative snow height, hours with melting condition
	#queries the table for the data to extrakt the snowheights and returns it to the client 
	
	


