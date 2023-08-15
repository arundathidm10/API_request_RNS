from faker import Faker
def generateEmail():
    faker = Faker()
    return faker.email()

emailgen = generateEmail()