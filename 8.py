import jdatetime


def show_jalali_age(birth):
    thisyear = int(jdatetime.datetime.now().strftime("%Y"))  # strftime.org
    age = thisyear - birth
    print(f"You are {age} years old")


show_jalali_age(1394)
