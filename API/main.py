from External_API.Request import requester
from API.Daytimeconv import datemaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from API.Database2 import Days

from flask import Flask, request

app = Flask(__name__, static_folder="./static", static_url_path="")
app.debug = True




@app.route('/snow', methods=['GET']) # Main API, gets lat lon and gives back the amount of snow over the last 5 days
def snow():
    lat = request.args.get('lat')
    lon = request.args.get('lon')


    time=datemaker.makedate() #today in unix, necessary for API Call of external API


    ## A SQLalchemny engine that interacts with our db
    engine = create_engine('sqlite:///Days_db', echo=False)
    ## SQLAlchemy ORM session bound to this engine
    Session = sessionmaker(bind=engine)
    session = Session()


    snow=(requester(time, lat, lon)) #Snow today from external API

    ## Inserting records
    day_0 = Days("Day-0", snow[0], snow[1])
    #  persists data
    session.add(day_0)


    time=int(time)
    day_1_t=time-86400 #Yesterday in Unix
    day_2_t=time-(2*86400)
    day_3_t = time - (3 * 86400)
    day_4_t = time - (4 * 86400)
    day_1_t = str(day_1_t) #make string so its usable for API call
    day_2_t = str(day_2_t)
    day_3_t = str(day_3_t)
    day_4_t = str(day_4_t)


    snow=(requester(day_1_t, lat, lon)) #snowdata yesterday
    ## Inserting records
    day_1 = Days("Day-1", snow[0], snow[1])
    #  persists data
    session.add(day_1)




    snow=(requester(day_2_t, lat, lon)) #snow day before yesterday
    ## Inserting records
    day_2 = Days("Day-2", snow[0], snow[1])
    #  persists data
    session.add(day_2)

    snow=(requester(day_3_t, lat, lon))
    ## Inserting records
    day_3 = Days("Day-3", snow[0], snow[1])
    #  persists data
    session.add(day_3)

    snow=(requester(day_4_t, lat, lon))
    ## Inserting records
    day_4 = Days("Day-4", snow[0], snow[1])
    #  persists data
    session.add(day_4)

    #session.commit() #commit not necessary?


    query1 = session.query(Days).all() #query of the table to give the user relevant snow Data

    snowheight=0 #init snowheight
    for day in query1:
        print(f'On {day.day_number}')
        print(f'The amount of fresh snow was {day.snowheight} cm')
        diff_snowheight=float(day.snowheight)
        snowheight=snowheight+diff_snowheight #sum of the snowheight
        print(f'And there were {day.melting_hours} hours with melting conditions')


    # deleting commited tables:
    session.query(Days).delete()
    session.commit()
    return {'dataString': 'The amount of fresh snow at your current location over the last 5 days is {snow} cm.'.format(snow=snowheight)}

if __name__ == "__main__":
    app.run()
