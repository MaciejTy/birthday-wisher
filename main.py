##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import smtplib
import random

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
today = dt.datetime.now()
today_tuple = (today.month, today.day)
letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
random_letter = random.choice(letters)
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(random_letter, "r") as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", birthday_person["name"])
    my_email = "myemail@gmail.com"
    password = "qkrc gnou zdan tgtp"
    with smtplib.SMTP("smtp.gmail") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["name"],
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}")



