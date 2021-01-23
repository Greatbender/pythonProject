class listmaker:



    def makelist (pass_times):

        hourly_values = pass_times["hourly"]  # just get the hourly values

        templist = []
        snowlist = []
        meltinglist =[]

        for d in hourly_values:  # loop over all hours
            temp = d["temp"]  # get temp entry
            clouds = d["clouds"]
            if temp > 274 and clouds < 50: # Check if Temperature is above 0 and sun is shining (clouds under 50%)
                melting = 1 #Melting 1 is True, = means no snow melts
            else:
                melting = 0

            snow = d.get("snow", 0)  # get snow entry or 0 if no snow
            if type(snow) is dict:
                snowheight = (snow["1h"])  # get just the hight from snow entry
            else:
                snowheight = 0

            #print(temp)
            #print(snowheight)
            templist.append(temp)  # create List with all Temperatures of this day, not yet used
            snowlist.append(snowheight)  # create List with all snowheights of this day
            meltinglist.append(melting)

        sum_snowheight=round(sum(snowlist), 1) #Sum of Snowheights for requested day
        sum_meltinghours=sum(meltinglist) #Sum of Melting Hours for requested day




        return sum_snowheight, sum_meltinghours




