import random
import requests
from faker import Faker
from datetime import timedelta
from time import time
from logger import Logger



def generateEmail():
    faker = Faker()
    return faker.email()

emailgen = generateEmail()

#satya
def CustomerIDGen():
    fake =Faker()
    return fake.customerid()
customerid = CustomerIDGen()
print("customerid: ",customerid)

def OrderNameGen():
    fake =Faker()
    return fake.ordername()
ordername = OrderNameGen()
print("ordername: ",ordername)

def AgentGen():
    fake =Faker()
    return fake.agent()
agent = AgentGen()
print("agent: ",agent)

#rakesh
def PassWordGen():
    fake =Faker()
    return fake.password()
passwordgen = PassWordGen()
print("Password: ",passwordgen)

def AddressGen():
    fake = Faker()
    return fake.address()
addressgen = AddressGen()
print("Address: ",addressgen)

def MobileNumGen():
    fake = Faker()
    return fake.phone_number()
mobilenumgen= MobileNumGen()
print("Mobile Number: ",mobilenumgen)

def PostCodeGen():
    fake = Faker()
    return fake.postalcode()
postcode = PostCodeGen()
print("Post Code", postcode)


def PassWordGen():
    fake =Faker()
    return fake.password()
passwordgen = PassWordGen()
print("Password: ",passwordgen)

def AddressGen():
    fake = Faker()
    return fake.address()
addressgen = AddressGen()
print("Address: ",addressgen)

def MobileNumGen():
    fake = Faker()
    return fake.phone_number()
mobilenumgen= MobileNumGen()
print("Mobile Number: ",mobilenumgen)

def PostCodeGen():
    fake = Faker()
    return fake.postalcode()
postcode = PostCodeGen()
print("Post Code", postcode)


def randomDigits(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return str(random.randint(lower, upper))

def CustomerIDGen():
    fake =Faker()
    return fake.customerid()
customerid = CustomerIDGen()
print("customerid: ",customerid)

def OrderNameGen():
    fake =Faker()
    return fake.ordername()
ordername = OrderNameGen()
print("ordername: ",ordername)

def AgentGen():
    fake =Faker()
    return fake.agent()
agent = AgentGen()
print("agent: ",agent)


def decorate_test(test_function):
    def wrapper():
        Logger.log_test_start(test_function)
        time_delta, _ = measure_time(test_function)
        Logger.log_test_finish(test_function, timedelta(seconds=time_delta))

    return wrapper


def measure_time(function):
    start = time()
    result = function()
    end = time()
    return end - start, result

def CountryGen():
  fake=Faker()
  return fake.country()
countrygen=CountryGen()
print("Country:",countrygen)

def CityGen():
  fake=Faker()
  return fake.city()
citygen =CityGen()
print("City:",citygen)

def UserNameGen():
  fake=Faker()
  return fake.username()
usernamegen=UserNameGen()
print("Username:",usernamegen)


