import random 
import datetime

# Home Class
class Home():
    def __init__(self): 
      
        print("\t\t\t\t\t\t WELCOME TO HOTEL PENNSYLVANIA\n") 
        print("\t\t\t\t\t\t  1 Booking\n") 
        print("\t\t\t\t\t\t  2 Rooms Info\n") 
        print("\t\t\t\t\t\t  3 Room Service(Menu Card)\n") 
        print("\t\t\t\t\t\t  4 Payment\n") 
        print("\t\t\t\t\t\t  5 Current Entries Record\n") 
        print("\t\t\t\t\t\t  0 Exit\n") 
        try:
            cha=int(input("\n-> ")) 
      
            if cha == 1: 
                print(" ") 
                b=Booking() 
      
            elif cha == 2: 
                print(" ") 
                r=Rooms_Info() 
      
            elif cha == 3: 
                print(" ") 
                re=Restaurant() 
      
            elif cha == 4: 
                print(" ") 
                p=Payment() 
      
            elif cha == 5: 
                print(" ") 
                rc=Records()
      
            else:
                print('Logging off from HOTEL PENNSYLVANIA')
                input('Hit any key...')
                exit()
        except ValueError:
            print('Wrong key pressed')
            print('Loading again...\n')
            h=Home()


# class for filing the data of costumer
class Savingdata:
        def __init__(self,a):
            self.a=a
            f=open('Records.txt','a+')
            f.write(str(self.a)+',')
            f.close

# class for details of rooms available in the hotel
class Rooms_Info:
    def __init__(self):
        try:    
            n = int(input("\n0-BACK\n1-Display\n\n-> ")) 
            if n == 0: 
                h=Home()
            if n == 1:
                self.displayroomsinfo()
                print('\n')
                print('Ready for Booking...')
                input('Hit any key if ready!!')
                h=Home()
        except ValueError:
            print('Wrong key pressed')
            h=Home()
    def displayroomsinfo(self):
        print("\t------ HOTEL ROOMS INFO ------") 
        print("") 
        print("**STANDARD NON-AC") 
        print("---------------------------------------------------------------") 
        print("Room amenities include: 1 Double Bed, Television, Telephone,\nDouble-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and\nan attached washroom with hot/cold water.\n") 
        print("**STANDARD AC") 
        print("---------------------------------------------------------------") 
        print("Room amenities include: 1 Double Bed, Television, Telephone,\nDouble-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and\nan attached washroom with hot/cold water + Window/Split AC.\n") 
        print("**3-Bed NON-AC") 
        print("---------------------------------------------------------------") 
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,\nTelephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa,\n1 Side table, Balcony with an Accent table with 2 Chair and an\n attached washroom with hot/cold water.\n") 
        print("**3-Bed AC") 
        print("---------------------------------------------------------------") 
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,\nTelephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa,\n1 Side table, Balcony with an Accent table with 2 Chair and an\n attached washroom with hot/cold water + Window/Split AC.\n\n") 
        


# class for booking a room in the hotel
class Booking(Rooms_Info,Savingdata):
        i=0
        name=[]
        add=[]
        day=[]
        checkin=[]
        checkout=[]
        room=[]
        price=[]
        phno=[]
        roomno=[]
        custid=[]
        p=[]
        rc=[]
        def __init__(self): 
                print("\t********BOOKING ROOM********\n\n")  
            
                while 1:
                    try:
                      n = input("Name: ") 
                      p1 = int(input("Phone No.: ")) 
                      a = input("Address: ")
                      # checks if desired input is entered
                      if n.isalpha():
                          pass
                      else:
                          raise ValueError
                      if a.isalnum():
                          pass
                      else:
                          raise ValueError
                      if isinstance(p1,int):
                          pass
                      # checks if any field is not empty 
                      if n!="" and p1!="" and a!="": 
                        Booking.name.append(n)
                        Savingdata(n)
                        Booking.add.append(a)
                        Savingdata(a)
                        break

                    except ValueError: 
                         print("Please enter correct information...!!")
               
                cii=input("Check-In seperated by /:") 
                Booking.checkin.append(cii) 
                cii=cii.split('/') 
                ci=cii 
                ci[0]=int(ci[0]) 
                ci[1]=int(ci[1]) 
                ci[2]=int(ci[2])
                # calling to check if date enter is valid or not
                self.datecheckin(ci)
                
                coo=input("Check-Out seperated by /:") 
                Booking.checkout.append(coo) 
                coo=coo.split('/') 
                co=coo 
                co[0]=int(co[0]) 
                co[1]=int(co[1]) 
                co[2]=int(co[2]) 
          
                # checks if check-out date falls after check-in date 
                if co[1]<ci[1] and co[2]<ci[2]: 
              
                    print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In")
                    print('\tLoading again...\n\n')
                    Booking.name.pop(Booking.i) 
                    Booking.add.pop(Booking.i) 
                    Booking.checkin.pop(Booking.i) 
                    Booking.checkout.pop(Booking.i) 
                    self.__init__() 
                elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]: 
                      
                    print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In")
                    print('\tLoading again...\n\n')
                    Booking.name.pop(Booking.i) 
                    Booking.add.pop(Booking.i) 
                    Booking.checkin.pop(Booking.i) 
                    Booking.checkout.pop(Booking.i) 
                    self.__init__()
                else:
                    Savingdata(cii)
                    Savingdata(coo)
                    pass
                # calling to check if date enter is valid or not  
                self.datecheckout(co)
                # calculating total number of days to stay
                d1 = datetime.datetime(ci[2],ci[1],ci[0]) 
                d2 = datetime.datetime(co[2],co[1],co[0]) 
                d = (d2-d1).days 
                Booking.day.append(d)
                # calling to select room 
                self.roomchoice()
           
  
                # randomly generating room no. and customer id for customer 
                rn = random.randrange(40)+300
                cid = random.randrange(40)+10
          
          
                # checks if alloted room no. & customer id already not alloted 
                while rn in Booking.roomno or cid in Booking.custid: 
                    rn = random.randrange(60)+300
                    cid = random.randrange(60)+10
              
                Booking.rc.append(0) 
                Booking.p.append(0)
                
                # checks if contact number already exists and if payment is made or not       
                if p1 not in Booking.phno: 
                    Booking.phno.append(str(p1))
                    Savingdata(p1)
                elif p1 in Booking.phno: 
                    for n in range(0,Booking.i): 
                        if p1== Booking.phno[n]: 
                            if Booking.p[n]==1: 
                                Booking.phno.append(str(p1))
                                Savingdata(p1)
                elif p1 in Booking.phno: 
                    for n in range(0,Booking.i): 
                        if p1== Booking.phno[n]: 
                            if Booking.p[n]==0: 
                                print("\tPhone no. already exists and payment yet not done..!!") 
                                Booking.name.pop(Booking.i) 
                                Booking.add.pop(Booking.i) 
                                Booking.checkin.pop(Booking.i) 
                                Booking.checkout.pop(Booking.i) 
                                self.__init__(self)
                print("") 
                print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n") 
                print("Room No. - ",rn) 
                print("Customer Id - ",cid) 
                Booking.roomno.append(rn)
                Savingdata(rn)
                Booking.custid.append(cid) 
                Booking.i=Booking.i+1
                
                try:    
                    n = int(input("\n0-BACK\n -> ")) 
                    if n == 0: 
                        h=Home() 
          
                except ValueError:
                    print('Wrong key pressed')
                    h=Home()
            
        def datecheckin(self,c): 
         # if year is current and month, date is within range
         if  c[2] == 2020 and c[2]>0: 
          
            if c[1] != 0 and c[1] <= 12 and c[1]>0: 
              
                if c[1] == 2 and c[0] != 0 and c[0] <= 31 and c[0]>0: 
                  
                    if c[2]%4 == 0 and c[0] <= 29 and c[0]>0: 
                        pass
                  
                    elif c[0]<29 and c[0]>0: 
                        pass
                  
                    else: 
                        print("\n\tInvalid date\n")
                        print('\tLoading again...\n\n')
                        Booking.name.pop(Booking.i)  
                        Booking.add.pop(Booking.i) 
                        Booking.checkin.pop(Booking.i) 
                        self.__init__()
              
              
            # if month is odd & less than equal to 7th  month  
                elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31 and c[1]>0 and c[0]>0: 
                    pass
              
            # if month is even & less than equal to 7th month and not 2nd month 
                elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2 and c[1]>0 and c[0]>0: 
                    pass
              
            # if month is even & greater than equal to 8th  month 
                elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31 and c[1]>0 and c[0]>0: 
                    pass
              
            # if month is odd & greater than equal to 8th  month 
                elif c[1]>=8 and c[1]%2!=0 and c[0]<=30 and c[1]>0 and c[0]>0:   
                    pass
              
                else:  
                    print("\n\tInvalid date\n")
                    print('\tLoading again...\n\n')
                    Booking.name.pop(Booking.i) 
                    Booking.add.pop(Booking.i) 
                    Booking.checkin.pop(Booking.i)  
                    self.__init__()
                  
            else: 
                print("\n\tInvalid date\n")
                print('\tLoading again...\n\n')
                Booking.name.pop(Booking.i)  
                Booking.add.pop(Booking.i) 
                Booking.checkin.pop(Booking.i)  
                self.__init__() 
              
         else: 
            print("\n\tInvalid date\n")
            print('\tLoading again...\n\n')
            Booking.name.pop(Booking.i)  
            Booking.add.pop(Booking.i) 
            Booking.checkin.pop(Booking.i)  
            self.__init__()

        def datecheckout(self,c): 
         # if year is current and month, date is within range
         if c[2] == 2020 and c[2]>0: 
          
            if c[1] != 0 and c[1] <= 12 and c[1]>0: 
              
                if c[1] == 2 and c[0] != 0 and c[0] <= 31 and c[0]>0: 
                  
                    if c[2]%4 == 0 and c[0] <= 29 and c[0]>0: 
                        pass
                  
                    elif c[0]<29 and c[0]>0: 
                        pass
                  
                    else: 
                        print("\n\tInvalid date\n")
                        print('\tLoading again...\n\n')
                        Booking.name.pop(Booking.i)  
                        Booking.add.pop(Booking.i) 
                        Booking.checkin.pop(Booking.i) 
                        Booking.checkout.pop(Booking.i) 
                        self.__init__()
              
              
            # if month is odd & less than equal to 7th  month  
                elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31 and c[1]>0 and c[0]>0: 
                    pass
              
            # if month is even & less than equal to 7th month and not 2nd month 
                elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2 and c[1]>0 and c[0]>0: 
                    pass
              
            # if month is even & greater than equal to 8th  month 
                elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31 and c[1]>0 and c[0]>0: 
                    pass
              
            # if month is odd & greater than equal to 8th  month 
                elif c[1]>=8 and c[1]%2!=0 and c[0]<=30 and c[1]>0 and c[0]>0:   
                    pass
              
                else:  
                    print("\n\tInvalid date\n")
                    print('\tLoading again...\n\n')
                    Booking.name.pop(Booking.i) 
                    Booking.add.pop(Booking.i) 
                    Booking.checkin.pop(Booking.i) 
                    Booking.checkout.pop(Booking.i) 
                    self.__init__()
                  
            else: 
                print("\n\tInvalid date\n")
                print('\tLoading again...\n\n')
                Booking.name.pop(Booking.i)  
                Booking.add.pop(Booking.i) 
                Booking.checkin.pop(Booking.i) 
                Booking.checkout.pop(Booking.i) 
                self.__init__() 
              
         else: 
            print("\n\tInvalid date\n")
            print('\tLoading again...\n\n')
            Booking.name.pop(Booking.i)  
            Booking.add.pop(Booking.i) 
            Booking.checkin.pop(Booking.i) 
            Booking.checkout.pop(Booking.i) 
            self.__init__()

        def roomchoice(self):
            print("----SELECT ROOM TYPE----") 
            print(" 1. Standard Non-AC") 
            print(" 2. Standard AC") 
            print(" 3. 3-Bed Non-AC") 
            print(" 4. 3-Bed AC") 
            print(("\t\tPress 0 for Room Prices and Details"))
            while True:   
                try:
                  ch=int(input("\n-> ")) 
          
                  # if-conditions to display alloted room type and it's price 
                  if ch==0:
                    Rooms_Info.displayroomsinfo(self)
                    print("*Standard Non-AC Price: Rs. 3500") 
                    print("*Standard AC Price: Rs. 4000") 
                    print("*3-Bed Non-AC Price: Rs. 4500") 
                    print("*3-Bed AC Price: Rs. 5000") 
                    ch=int(input("\n-> ")) 
                  if ch==1: 
                    Booking.room.append('Standard Non-AC') 
                    print("\nRoom Type- Standard Non-AC")   
                    Booking.price.append(3500) 
                    print("Price- 3500\n")
                    break
                  elif ch==2: 
                    Booking.room.append('Standard AC') 
                    print("\nRoom Type- Standard AC") 
                    Booking.price.append(4000) 
                    print("Price- 4000\n")
                    break
                  elif ch==3: 
                    Booking.room.append('3-Bed Non-AC') 
                    print("\nRoom Type- 3-Bed Non-AC") 
                    Booking.price.append(4500) 
                    print("Price- 4500\n")
                    break
                  elif ch==4: 
                    Booking.room.append('3-Bed AC') 
                    print("\nRoom Type- 3-Bed AC") 
                    Booking.price.append(5000) 
                    print("Price- 5000\n")
                    break
                  elif ch<0 or ch>=5:
                    raise ValueError
                except ValueError: 
                    print(" Wrong choice..!!")
                    print('Enter again...\n\n')

# class for the room services
class Restaurant(Booking):
    rate=0
    def __init__(self): 
        ph=int(input("Customer Id: ")) 
        f=0
        for n in range(0,Booking.i): 
            if Booking.custid[n]==ph and Booking.p[n]==0: 
                f=1
                print("-------------------------------------------------------------------------") 
                print("                           HOTEL PENNYSLYVANIA") 
                print("-------------------------------------------------------------------------") 
                print("                               Menu Card") 
                print("-------------------------------------------------------------------------") 
                print("\n BEVARAGES                              26 Dal Fry................ 140.00") 
                print("----------------------------------      27 Dal Makhani............ 150.00") 
                print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00") 
                print(" 2  Black Tea............... 25.00") 
                print(" 3  Coffee.................. 25.00      ROTI") 
                print(" 4  Cold Drink.............. 25.00     ----------------------------------") 
                print(" 5  Butter.................. 30.00      29 Plain Roti.............. 15.00") 
                print(" 6  Jam..................... 30.00      30 Butter Roti............. 15.00") 
                print(" 7  Chicken Sandwich........ 50.00      31 Tandoori Roti........... 20.00") 
                print(" 8  Veg.Toast Sandwich...... 50.00      32 Butter Naan............. 20.00") 
                print(" 9  Cheese Toast Sandwich... 70.00") 
                print(" 10 Grilled Sandwich........ 70.00      RICE")  
                print("                                       ----------------------------------") 
                print(" SOUPS                                  33 Plain Rice.............. 90.00") 
                print("----------------------------------      34 Zeera Rice.............. 90.00") 
                print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00") 
                print(" 12 Hot & Sour............. 110.00      36 Matar Pulao............ 110.00") 
                print(" 13 Veg. Noodle Soup....... 110.00") 
                print(" 14 Sweet Corn............. 110.00      PASTAS") 
                print(" 15 Chicken Soup........... 110.00     ----------------------------------") 
                print("                                        37 Chicken Pasta.......... 100.00") 
                print(" MAIN COURSE                            38 Chicken Alfredo........ 110.00") 
                print("----------------------------------      39 Spicy Pasta............ 130.00") 
                print(" 16 Shahi Mutton........... 110.00      40 Green Pasta............ 130.00") 
                print(" 17 Chicken Karahi......... 110.00      41 Mushroom Past.......... 130.00") 
                print(" 18 Handi Paneer........... 120.00      42 Ravioli Pasta.......... 140.00") 
                print(" 19 Palak Aloo............. 120.00") 
                print(" 20 Chilli Chicken......... 140.00      ICE CREAM") 
                print(" 21 Matar Mushroom......... 140.00     ----------------------------------") 
                print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00") 
                print(" 23 Zeera Aloo............. 140.00      44 Strawberry.............. 60.00") 
                print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00") 
                print(" 25 Aloo Matar............. 140.00      46 Chocolate............... 60.00") 
                print("\nPress 0 to end\n") 
                ch=1
                while(ch!=0):
                  try:
                    ch=int(input("\n-> "))
                    # if-elif-conditions to assign item prices listed in menu card 
                    if ch==1 or ch==31 or ch==32: 
                        rs=20
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch<=4 and ch>=2: 
                        rs=25
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch<=6 and ch>=5: 
                        rs=30
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch<=8 and ch>=7: 
                        rs=50
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch<=10 and ch>=9: 
                        rs=70
                        Restaurant.rate=Restaurant.rate+rs 
                    elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38: 
                        rs=110
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch<=19 and ch>=18: 
                        rs=120
                        Restaurant.rate=Restaurant.rate+rs 
                    elif (ch<=26 and ch>=20) or ch==42: 
                        rs=140
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch<=28 and ch>=27: 
                        rs=150
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch<=30 and ch>=29: 
                        rs=15
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch==33 or ch==34: 
                        rs=90
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch==37: 
                        rs=100
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch<=41 and ch>=39: 
                        rs=130
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch<=46 and ch>=43: 
                        rs=60
                        Restaurant.rate=Restaurant.rate+rs 
                    elif ch==0: 
                        pass
                    else: 
                        print("Item not found..!!")
                  except ValueError:
                      print('Enter valid choice...!')
                      
                print("Total Bill: ",Restaurant.rate) 
              
                # updates restaurant charges and then appends in 'rc' list 
                Restaurant.rate=Restaurant.rate+Booking.rc.pop(n) 
                Booking.rc.append(Restaurant.rate)     
            else: 
                pass
        if f == 0: 
            print("Invalid Customer Id")
            print("Loading again...\n\n")
            h=Home()
        try:    
            n = int(input("\n0-BACK\n -> ")) 
            if n == 0: 
                h=Home() 
          
        except ValueError:
            print('Wrong key pressed')
            h=Home()


# class for checkingout of hotel and doing payment
class Payment(Booking):
   def __init__(self): 
      
    ph=str(input("Phone Number: "))  
    f=0
      
    for n in range(0,Booking.i): 
        if ph==Booking.phno[n] : 
              
            # checks if payment is not already done 
             if Booking.p[n]==0: 
                f=1 
                print(" --------------------------------") 
                print("  MODES OF PAYMENT") 
                   
                print("  1- Credit/Debit Card") 
                print("  2- Cash") 
                print("  3- PayPal") 
                print("  4- Western Union")
                try:
                    x=int(input("\n-> "))
                    if x==1 or x==2 or x==3 or x==4:
                        print("\n***********Paying For HOTEL PENNSLYVANIA***********")
                        print("-----------------------------------------------")  
                        print("-----------------------------------------------") 
                        print("\n*********************Bill*********************") 
                        print("----------------------------------------------") 
                        print(" Name: ",Booking.name[n],"\t\n Phone No.: ",Booking.phno[n],"\t\n Address: ",Booking.add[n],"\t") 
                        print("\n Check-In: ",Booking.checkin[n],"\t\n Check-Out: ",Booking.checkout[n],"\t") 
                        print("\n Room Type: ",Booking.room[n],"\t\n Room Charges: ",Booking.price[n]*Booking.day[n],"\t") 
                        print(" Restaurant Charges: \t",Booking.rc[n]) 
                        print(" --------------------------------") 
                        print("\n Total Amount: ",(Booking.price[n]*Booking.day[n])+Booking.rc[n],"\t") 
                        print(" --------------------------------") 
                        print("************Thank You for choosing HOTEL PENNSLYVANIA************") 
                        print("\t************Visit Again:)************") 
                        print(" --------------------------------\n") 
                        Booking.p.pop(n) 
                        Booking.p.insert(n,1) 
                          
                        # pops room no. and customer id from list and later assigns zero at same position 
                        Booking.roomno.pop(n) 
                        Booking.custid.pop(n) 
                        Booking.roomno.insert(n,0) 
                        Booking.custid.insert(n,0)
                except ValueError:
                        print('Select carefully')
                        p=Payment()
                      
             else: 
                  
                for j in range(n+1,Booking.i): 
                    if ph==Booking.phno[j] : 
                        if Booking.p[j]==0: 
                            pass
                          
                        else: 
                            f=1
                            print("\n\tPayment has been Made :)\n\n")  
    if f==0:     
        print("\n\tPhone Number not found")
        print("\tLoading again...\n\n")
        h=Home()

    input('Hit any key to exit!!')
    exit()

# class for seeing the current records of hotel
class Records(Booking):
    
  def __init__(self): 
      
    # checks if any record exists or not 
    if Booking.phno!=[]: 
        print("\t\t\t\t*** HOTEL RECORD ***\n") 
        print("|Name\t\t|PhoneNo.\t|Address\t|Check-In\t|Check-Out\t|\tRoom No.|") 
        print("-------------------------------------------------------------------------------------------------") 
          
        for n in range(0,Booking.i): 
            print(f'|{Booking.name[n]:15}|{Booking.phno[n]:15}|{Booking.add[n]:15}|{Booking.checkin[n]:15}|{Booking.checkout[n]:15}|{Booking.roomno[n]:15}|')
          
        print("-------------------------------------------------------------------------------------------------") 
      
    else: 
        print("\n\tNo Current Entries\n")
        print('\tLoading again...\n\n')
        h=Home()

    try:    
        n = int(input("\n0-BACK\n -> ")) 
        if n == 0: 
            h=Home() 
          
    except ValueError:
        print('Wrong key pressed')
        h=Home()




