# pythonProject
#main.py starts the Program, 
	#gets the current unit time via datemaker.py, 
	#gets the user input cia Console.py
	#creates engine an session for the DB
	#requests via request.py the wheater data form opneweather for the last 5 days
	#inserts the Data for every Day in a Table: ID, Day_Number, cumalative snow height, hours with melting condition
	#queries the table for the data to show it to the user
	#(commit of tables not in use right now)
	
#request.py gets waeather Data from API and gives it to GetListsfromRequest.py, 
#GetListsfromRequest.py evaluates wheaterdata and returns the sums of snowheight and the hours with melting conditions
