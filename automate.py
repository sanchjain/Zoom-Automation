import schedule
import pandas as pd

def join_class():
    print("In class")

if __name__ == '__main__':
    timeTable = pd.read_csv('schedule.csv')
    timeTable.columns = ["Day", "Code", "Start Time"]
    schedule.every(1).minutes.do(join_class) 
    schedule.every().saturday.do(join_class)

    for i in timeTable.index:
        day  = timeTable['Day'][i]
        classCode = timeTable['Code'][i]
        start_time = str(timeTable['Start Time'][i])
        end_time = str(timeTable['End Time'][i])

        if day.lower()=="monday":
            schedule.every().monday.at(start_time).do(join_class, classCode,start_time,end_time)
            print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
        if day.lower()=="tuesday":
            schedule.every().tuesday.at(start_time).do(join_class,classCode,start_time,end_time)
            print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
        if day.lower()=="wednesday":
            schedule.every().wednesday.at(start_time).do(join_class,classCode,start_time,end_time)
            print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
        if day.lower()=="thursday":
            schedule.every().thursday.at(start_time).do(join_class,classCode,start_time,end_time)
            print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
        if day.lower()=="friday":
            schedule.every().friday.at(start_time).do(join_class,classCode,start_time,end_time)
            print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
        if day.lower()=="saturday":
            schedule.every().saturday.at(start_time).do(join_class,classCode,start_time,end_time)
            print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
        if day.lower()=="sunday":
            schedule.every().sunday.at(start_time).do(join_class,classCode,start_time,end_time)
            print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")