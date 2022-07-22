import pandas
import operator
dataset = pandas.read_csv(r"C:\Users\avyuk\OneDrive\Desktop\COVID Algorithm\Medical Records.csv")
record={}
a = dataset.iloc[::,4]
b= str(a)
c=b.replace("Name: PEC?, dtype: object", '')
cuff=c.replace("Yes",'')
cuff=cuff.replace("No",'')
cuff=cuff[-11:]
cuff=cuff.replace(" ",'')
cuff=cuff[1:-1]
last=int(cuff)
last=last+1
i=0
while i < last:
    number = 1
    k=i+1
    
    #name
    a = dataset.iloc[i:k:,0]
    b= str(a)
    c=b.replace("Name: Name, dtype: object", '')
    d=c.replace(" ", '')
    d=c[5:len(c)-1]
    x=d.replace(" ",'')

    #contact
    a = dataset.iloc[i:k:,6]
    b= str(a)
    c=b.replace("Name: Contact, dtype: object", '')
    d=c[5:len(c)-1]
    contact=d.replace(" ",'')

    #city
    a = dataset.iloc[i:k:,3]
    b= str(a)
    c=b.replace("Name: City, dtype: object", '')
    d=c[5:len(c)-1]
    place=d.replace(" ",'')

    #age
    a = dataset.iloc[i:k:,1]
    b= str(a)
    c=b[:len(b)-24]
    d=c[5:len(c)]
    d=d.replace(" ",'')
    age=int(d)

    #state
    a = dataset.iloc[i:k:,2]
    b= str(a)
    c=b.replace("Name: State, dtype: object", '')
    d=c.replace(" ", '')
    d=c[5:len(c)-1]
    state=d.replace(" ",'')

    #PEC
    a = dataset.iloc[i:k:,4]
    b= str(a)
    c=b.replace("Name: PEC?, dtype: object", '')
    d=c.replace(" ", '')
    d=c[5:len(c)-1]
    Do_you_have_any_pre_existing_conditions=d.replace(" ",'')

    #what is your PEC
    a = dataset.iloc[i:k:,5]
    b= str(a)
    c=b.replace("Name: Name PEC, dtype: object", '')
    d=c.replace(" ", '')
    d=c[5:len(c)-1]
    PEC=d.replace(" ",'')

    #Multiplying based on age
    if age <=10:
        number = number*6
    elif age in range(80,100):
        number = number*5
    elif age in range(60,80):
        number = number*4
    elif age in range(40,60):
        number = number*3
    elif age in range(15,40):
        number = number
    elif age in range(11,15):
        number = number*2
    elif age >=100:
        number = number*6

    #multiplying based on whether they have PECs
    if Do_you_have_any_pre_existing_conditions == ('Yes'):
        number = number*5
    elif Do_you_have_any_pre_existing_conditions == ('No'):
        number = number
    else:
        print("Answer to Name PEC is wrong by ",x)

    #We multiply by 2 for if they are form a Covid-19 hotspot

    if state == ("Delhi"):
        number = number*2
    elif state == ("Chandigarh"):
        number = number*2
    elif state == ("Jammu and Kashmir"):
        if place == ("Jammu"):
            number = number*2
        elif place == ("Srinagar"):
            number = number*2
        elif place == ("Udhampur"):
            number = number*2
        elif place == ("Bandipora"):
            number = number*2
        elif place == ("Baramulla"):
            number = number*2
        elif place == ("Kupwara"):
            number = number*2
        else:
            number=number
    elif state == ("Maharashtra"):
        if place == ("Mumbai"):
            number = number*2
        elif place == ("Pune"):
            number = number*2
        elif place == ("Thane"):
            number = number*2
        elif place == ("Nashik"):
            number = number*2
        elif place == ("Palghar"):
            number = number*2
        elif place == ("Nagpur"):
            number = number*2
        elif place == ("Solapur"):
            number = number*2
        elif place == ("Yavatmal"):
            number = number*2
        elif place == ("Aurangabad"):
            number = number*2
        elif place == ("Satara"):
            number = number*2
        elif place == ("Dhule"):
            number = number*2
        elif place == ("Akola"):
            number = number*2
        else:
            number=number*1.25
    elif state == ("Kerala"):
        if place == ("Jalgaon"):
            number = number*2
        elif place == ("Kasaragod"):
            number = number*2
        elif place == ("Kannur"):
            number = number*2
        elif place == ("Mallapuram"):
            number = number*2
        elif place == ("Ernakulam"):
            number = number*2
        elif place == ("Pathanamthitta"):
            number = number*2
        elif place == ("Thiruvananthapuram"):
            number = number*2
        else:
            number=number*1.5
    elif state == ("Uttar Pradesh"):
        if place == ("Moradabad"):
            number = number*2
        elif place == ("Ghaziabad"):
            number = number*2
        elif place == ("Saharanpur"):
            number = number*2
        elif place == ("Firozabad"):
            number = number*2
        elif place == ("Shamli"):
            number = number*2
        elif place == ("Lucknow"):
            number = number*2
        elif place == ("Agra"):
            number = number*2
        elif place == ("Gautam Budhh Nagar"):
            number = number*2
        elif place == ("Meerut"):
            number = number*2
        elif place == ("Noida"):
            number = number*2
        else:
            number=number*1.25
    elif state == ("Bihar"):
        if place == ("Siwan"):
            number = number*2
        else:
            number=number*1.25
    elif state == ("Haryana"):
        if place == ("Gurugram"):
            number = number*2
        elif place == ("Palwal"):
            number = number*2
        elif place == ("Faridabad"):
            number = number*2
        elif place == ("Nuh"):
            number = number*2
        else:
            number=number
    elif state ==("Chattisgarh"):
        if place == ("Korba"):
            number = number*2
        else:
            number=number
    elif state ==("Odisha"):
        if place == ("Khordha"):
            number = number*2
        else:
            number=number
    elif state ==("Uttarakhand"):
        if place == ("Dehradun"):
            number = number*2
        else:
            number=number
    elif state ==("Punjab"):
        if place == ("Jalandhar"):
            number = number*2
        elif place == ("Pathankot"):
            number = number*2
        elif place == ("SAS Nagar"):
            number = number*2
        elif place == ("Shaheed Bhagat Singh Nagar"):
            number = number*2
        else:
            number=number
    elif state ==("West Bengal"):
        if place == ("Kolkatta"):
            number = number*2
        elif place == ("Howrah"):
            number = number*2
        elif place == ("Medinipur East"):
            number = number*2
        elif place == ("24 Parganas North"):
            number = number*2
        else:
            number=number
    elif state ==("Karnataka"):
        if place == ("Bengaluru Urban"):
            number = number*2
        elif place == ("Mysore"):
            number = number*2
        elif place == ("Belagavi"):
            number = number*2
        else:
            number=number
    elif state == ("Gujrat"):
        if place == ("Ahmedabad"):
            number = number*2
        elif place == ("Surat"):
            number = number*2
        elif place == ("Rajkot"):
            number = number*2
        elif place == ("Vadodara"):
            number = number*2
        elif place == ("Bhavnagar"):
            number = number*2
        else:
            number=number
    elif state == ("Madhya Pradesh"):
        if place == ("Bhopal"):
            number = number*2
        elif place == ("Indore"):
            number = number*2
        elif place == ("Ujjain"):
            number = number*2
        elif place == ("Khargone"):
            number = number*2
        elif place == ("Hoshangabad"):
            number = number*2
        else:
            number=number*1.25
    elif state == ("Telangana"):
        if place == ("Hyderabad"):
            number = number*2
        elif place == ("Warangal Urban"):
            number = number*2
        elif place == ("Nizamabad"):
            number = number*2
        elif place == ("Ranga Reddy"):
            number = number*2
        elif place == ("Jogulamba Gadwal"):
            number = number*2
        elif place == ("Karimnagar"):
            number = number*2
        elif place == ("Medhchal Malkagiri"):
            number = number*2
        elif place == ("Nirmal"):
            number = number*2
        else:
            number=number*1.25
    elif state ==("Rajasthan"):
        if place == ("Jhunjhunu"):
            number = number*2
        elif place == ("Jhalawar"):
            number = number*2
        elif place == ("Banswara"):
            number = number*2
        elif place == ("Bharatpur"):
            number = number*2
        elif place == ("Bikaner"):
            number = number*2
        elif place == ("Kota"):
            number = number*2
        elif place == ("Tonk"):
            number = number*2
        elif place == ("Jaisalmer"):
            number = number*2
        elif place == ("Jodhpur"):
            number = number*2
        elif place == ("Jaipur"):
            number = number*2
        elif place == ("Bhilwara"):
            number = number*2
        else:
            number=number
    elif state ==("Arunachal Pradesh"):
        if place == ("Anantapur"):
            number = number*2
        elif place == ("Chittoor"):
            number = number*2
        elif place == ("East Godavari"):
            number = number*2
        elif place == ("West Godavari"):
            number = number*2
        elif place == ("YSR"):
            number = number*2
        elif place == ("Krishna"):
            number = number*2
        elif place == ("Vishakhapatnam"):
            number = number*2
        elif place == ("Prakasam"):
            number = number*2
        elif place == ("Guntur"):
            number = number*2
        elif place == ("Nellore"):
            number = number*2
        elif place == ("Kurnool"):
            number = number*2
        else:
            number=number
    elif state == ("Kerala"):
        if place == ("Kanyakumari"):
            number = number*2
        elif place == ("Viruhnagar"):
            number = number*2
        elif place == ("Karur"):
            number = number*2
        elif place == ("Chengalpattu"):
            number = number*2
        elif place == ("Nagapattinam"):
            number = number*2
        elif place == ("Namakkal"):
            number = number*2
        elif place == ("Villupuram"):
            number = number*2
        elif place == ("Thiruvarur"):
            number = number*2
        elif place == ("Theni"):
            number = number*2
        elif place == ("Tirupur"):
            number = number*2
        elif place == ("Tirunelveli"):
            number = number*2
        elif place == ("Cuddalore"):
            number = number*2
        elif place == ("Salem"):
            number = number*2
        elif place == ("Tiruchirapalli"):
            number = number*2
        elif place == ("Madurai"):
            number = number*2
        elif place == ("Tuticorin"):
            number = number*2
        elif place == ("Vellore"):
            number = number*2
        elif place == ("Erode"):
            number = number*2
        elif place == ("Dindigul"):
            number = number*2
        elif place == ("Coimbature"):
            number = number*2
        elif place == ("Chennai"):
            number = number*2
        else:
            number=number
    else:
        number = number

    if PEC=="-":
        number=number
    else:
        f=PEC.count(",")
        number=number*(f+1)
    
    #multiplying based on whether they have come in contact
    if contact == ('Yes'):
        number = number*2
    elif contact == ('No'):
        number = number
    else:
        print("Answer to Contact is wrong by ",x)
    i=i+1
    record[x,age,state]=number

    #delete from here
orders = sorted(record.items(), key=operator.itemgetter(1))
order=orders.reverse()
for x in range(len(orders)): 
    print (orders[x])
print("How many patients need help ")
help=int(input())
m=1
if help<last:
    help=help+1
    while m<help:
        m=m+1
        print("What is your name")
        ask_name=input()
        ask_name=ask_name.replace(" ", '')
        print("What is your state")
        ask_state=input()
        ask_state=ask_state.replace(" ", '')
        print("What is your age")
        ask_age=int(input())
        filler=record[ask_name,ask_age,ask_state]
        if filler < 11:
            print("Stay at home if you can")
            print("Wear a mask when you leave the house")
        elif filler in range(11,100):
            print("Stay at home")
            print("Wear a mask when you leave the house, only leave the house when absolutly necessary if necessary")
        elif filler >100:
            print("DO NOT LEAVE YOUR HOUSE")