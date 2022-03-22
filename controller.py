import curd
import db
import pandas as pd
import export


def validate(plate):
    check = False
    text = {"D", "L", "C", "U", "Z"}
    hyphen = {"-"}
    rplate = str(plate).replace(" ","")
    if len(rplate) <= 11 and len(rplate) >= 8:
        first = rplate[0:2]
        second = rplate[2:3]
        third  = rplate[3:4]
        fourth = rplate[4:]
        
        if first.isdigit() and fourth.isdigit() and int(first) >= 50 and int(first) <= 59 and len(fourth) <= 5  and second in text and third in hyphen:
                check = True
    return check    



while True:
    db.create_table()
    print('''\n
        0.Thoát chương trình
        1.Gởi Xe
        2.Hiển thị Xe Gởi
        3.Lấy Xe
        4.Export
    ''')

    select = input("Mời nhập lựa chọn: ")

    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break
        if select == 1:
            carName = input("nhập tên xe: ")
            licensePlate = str(input("nhập biển số xe: "))
            if (validate(licensePlate)):
                if(curd.getCarByLicensePlate(licensePlate)): 
                    print("xe đã tồn tại")
                else:   
                    curd.create(carName, licensePlate)
            else:
                print('biển số xe không hơp lệ yêu cầu nhập lại biển số xe')
                licensePlate2 = str(input("nhập biển số xe: "))
                if (validate(licensePlate2)):
                    if(curd.getCarByLicensePlate(licensePlate2)): 
                        print("xe đã tồn tại")
                        break
                    else:
                        curd.create(carName, licensePlate2)

        if select == 2:
            a = pd.DataFrame(curd.GetParking(), columns=['stt','car_name','plate','is_checkin','deposits','time_in','time_out'])
            print(a)
        if select == 3:
            lp = str(input("nhập biển số xe: "))
            b = curd.getCarByLicensePlate(lp)
            if b:
                curd.payment(lp)  
            else :
                print("xe không tồn tại hoặc đã thanh toán.")   
                break
        if select == 4:
            export.export_data()    
            break





