from Request import requester
from Daytimeconv import datemaker
from Console import UI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Database2 import Days



if __name__ == '__main__':

    time=datemaker.makedate() #today in unix
    koords = UI.TinkerUI() #Get Koordinates over UI
    lat = koords[0]
    lon = koords[1]
    lat = str(lat) #make strings for API call
    lon = str(lon)

    ## A SQLalchemny engine that interacts with our db
    engine = create_engine('sqlite:///movies_db', echo=False)
    ## SQLAlchemy ORM session bound to this engine
    Session = sessionmaker(bind=engine)
    session = Session()


    snow=(requester(time, lat, lon)) #Snow today

    ## Inserting records
    day_0 = Days("Day-0", snow[0], snow[1])
    #  persists data
    session.add(day_0)


    time=int(time)
    day_1_t=time-86400 #Yesterday in Unix
    day_2_t=time-(2*86400)
    day_3_t = time - (3 * 86400)
    day_4_t = time - (4 * 86400)
    day_1_t = str(day_1_t)
    day_2_t = str(day_2_t)
    day_3_t = str(day_3_t)
    day_4_t = str(day_4_t)


    snow=(requester(day_1_t, lat, lon)) #snow yesterday
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


    query1 = session.query(Days).all()

    for day in query1:
        print(f'On {day.day_number}')
        print(f'The amount of fresh snow was {day.snowheight} cm')
        print(f'And there were {day.melting_hours} hours with melting conditions')


    #For deleting commited tables
    #session.query(Days).delete()
    #session.commit()

