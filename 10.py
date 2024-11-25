def func(**kwargs):
    if "alireza" in kwargs["students"]:
        print("Record exists")
    else:
        print("Record doesnt exists")


func(name="adv-403-241", teacher="sadeghi", students=["ali", "fateme", "amir"])
