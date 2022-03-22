from importlib import import_module
from socket import create_connection
import db
from datetime import datetime

def GetParking(): 
    try:
        cnt = db.create_connection()
        cursor = cnt.cursor()
        parking = '''select * from car WHERE is_checkin = 1 '''
        cursor.execute(parking)
        rs = cursor.fetchall()
        cnt.close()
        return rs
    except Exception as e:
        print(e)

def getCarByLicensePlate(licensePlate):
    try: 
        cnt = db.create_connection()
        cursor = cnt.cursor()
        get =  f''' select * from car where  license_plate = '{licensePlate}' and is_checkin = 1 '''
        cursor.execute(get)
        rs = cursor.fetchone()
        cnt.close()
        return rs
    except Exception as e:
        print(e)

def create(carName, licensePlate):
    try:
        cnt = db.create_connection()
        cursor = cnt.cursor()
        create = f'''insert into car(car_name, license_plate, time_in, is_checkin) values('{carName}','{licensePlate}', '{datetime.now()}', 1)'''
        cursor.execute(create)
        cnt.commit()
        cnt.close()
        print(f"{carName} - {licensePlate} - {datetime.now()}")
    except Exception as e:
        print(e)   

def updateBylicensePlate(plate, deposit, timeOut):
    try:
        cnt = db.create_connection()
        cursos = cnt.cursor()
        update = f'''update car set time_out = '{timeOut}' , deposits = '{deposit}', is_checkin = 0 where license_plate = '{plate}' ''' 
        cursos.execute(update)
        cnt.commit()
        cnt.close()
    except Exception as e:
        print(e)



def payment(plate):
    results = getCarByLicensePlate(plate)
    time_out = datetime.now()            
    time_in = results[5]
    real_time = time_out - time_in

    day = real_time.total_seconds() / 86400

    money = 0
    if day <= 1:
            money = 5000
    else:
            money = int(day) * 20000
    print("--> Số tiền phải trả: ", money)
    #lưu giờ ra và tiền gửi vào db
    updateBylicensePlate(plate,money,time_out)
