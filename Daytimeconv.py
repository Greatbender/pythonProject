from datetime import datetime

class datemaker:



    def makedate ():

        # current date and time
        now = datetime.now()

        timestamp = datetime.timestamp(now)
        #int(timestamp)
        timestamp = round(timestamp, 0)
        #print("timestamp =", timestamp)
        #timestamp=str(1610023799)
        timestamp = timestamp-100 #prevent setting timestamp in the future
        timestamp = str(timestamp) # make to string

        split_string = timestamp.split(".", 1) #split string at .


        substring = split_string[0]

        #print(substring)

        return substring

    #makedate()