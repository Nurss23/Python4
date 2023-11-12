def make_car( name, model,**kwargs):
    dct_car = {
        "name": name,
        "model": model
    }
    dct_car.update(kwargs)
    return dct_car

car = make_car("Subaru", "Outback", color = "blue", engine = 'V8', max_speed = "200 k/h" , suspension_typ = "front", tire_rim_Size = 225)
print(car)

#
# def make_car(dct_car = {"subaru": "outback"},**kwargs):
#     dct_car.update(kwargs)
#     return dct_car
# car = make_car(color = "blue", engine = 'V8', max_speed = "200 k/h")
# print(car)

# def make_car(dct_car = {"name" : "subaru","model": "outback",},**kwargs):
#     dct_car.update(kwargs)
#     return dct_car
# car = make_car(color = "blue", engine = 'V8', max_speed = "200 k/h")
# print(car)