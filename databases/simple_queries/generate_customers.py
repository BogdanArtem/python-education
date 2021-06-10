"""This module generates SQL inserts for a customer table"""

from faker import Faker
import random

fake = Faker()
num_of_entries = int(input("Enter number of records to generate?: "))
template = "INSERT INTO potential_customers(id, email, name, surname, second_name, city) VALUES ({}, '{}', '{}','{}', '{}', '{}');\n"

with open("fake_customer.sql", "w") as file:
    for num in range(num_of_entries):
        # Generate randomly 1 or 0
        is_male = random.randint(0, 1)
        if is_male:
            name = fake.first_name_male()
            surname = fake.first_name_male()
            second_name = fake.last_name_male()
        else:
            name = fake.first_name_female()
            surname = fake.first_name_female()
            second_name = fake.last_name_female()
        email = fake.email()
        # Used numbered cities to match the first task
        city = f"city {num}" #fake.city()

        entry = template.format(num, email, name, surname, second_name, city)
        file.write(entry)
