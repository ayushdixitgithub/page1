from faker import Faker
import pandas as pd
import re
import random

fake = Faker()

def full_name():
    names=[]
    for i in range(50):
        names.append(fake.name())

    df = pd.DataFrame(names)
    #print(df)
    df.to_clipboard(index=False,header=False)

def address_US():
    AddressListRaw=[]
    for i in range(50):
        AddressListRaw.append(fake.address())

    res = []
    for sub in AddressListRaw:
        res.append(re.sub('\n', ' ', sub))
    
    #print(res)
    df = pd.DataFrame(res)
    #print(df)
    df.to_clipboard(index=False,header=False)

def email():
    email=[]
    for i in range(50):
        email.append(fake.ascii_email())

    df = pd.DataFrame(email)

    #print(df)
    df.to_clipboard(index=False,header=False)

def phone_US():
    phone=[]
    for i in range(50):
        phone.append(fake.phone_number())

    df = pd.DataFrame(phone)

    #print(df)
    df.to_clipboard(index=False,header=False)

def work_description():
    bs=[]
    for i in range(50):
        bs.append(fake.bs())

    df = pd.DataFrame(bs)

    #print(df)
    df.to_clipboard(index=False,header=False)

def company_name():
    company=[]

    for i in range(50):
        company.append(fake.company())

    df = pd.DataFrame(company)

    #print(df)
    df.to_clipboard(index=False,header=False)   

def building_type():
    lst=[]
    a=['Residential Building', 'Educational Building', 'Institutional Building', 'Assembly Building', 'Business Building',
    'Mercantile Building', 'Industrial Building', 'Storage Building', 'Wholesale Establishment', 'Mixed Land Use Building', 'Detached Buildings']
    for i in range(50):
        lst.append(random.choice(a))

    df = pd.DataFrame(lst)
    #print(df)
    df.to_clipboard(index=False,header=False)

def board_trustee_director():
    import random
    import pandas as pd

    lst=[]
    a=['Board of Governors', 'Trustees', 'Directors']

    for i in range(50):
        lst.append(random.choice(a))

    df = pd.DataFrame(lst)
    #print(df)
    df.to_clipboard(index=False,header=False) 
        
choice=1
menu = """
1 - Full Name
2 - Address
3 - Company Name
4 - Work Description
5 - Phone Number
6 - Email
7 - Building Type
8 - Board/Trustee/Director
"""
print(menu)
while choice != 0:
    choice = int(input("Enter choice : "))
    if choice == 1 :
        full_name()

    elif choice == 2 :
        address_US()

    elif choice == 3:
        company_name()

    elif choice == 4:
        work_description()

    elif choice == 5:
        phone_US()

    elif choice == 6:
        email()

    elif choice == 7:
        building_type()

    elif choice == 8:
        board_trustee_director()

    else:
        print('Choose a valid option from the menu please')


    
