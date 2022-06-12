import pandas as pd
import numpy as np
import math

cable_name = ["CVV", "CVVS", "PVC", "XLPE"]
pipe_name = ["EMT", "PVC", "RSG", "SUS304"]
print("cable name:", cable_name)
print("pipe name:", pipe_name)
pi = 3.14159265359
choose_cable = input("choose cable: ")
choose_pipe = input("choose pipe: ")
base_dir = "C:\\Users\\gcsi\\Desktop\\pipe_data\\"

if choose_cable in cable_name:
    pass
else:
    print("no match cable")

if choose_pipe in pipe_name:
    pass
else:
    print("no match pipe")

for item in cable_name:
    if choose_cable == item:
        Cable_item = item
        cable_choosed = pd.read_csv(base_dir + "Cable_" + item + ".csv")
        if item in ["CVV", "CVVS"]:
            cores = list(cable_choosed.columns)[1:-1]
            sectional_area = list(cable_choosed.iloc[:, 0])
            cable_choosed.set_index("公稱(mm^2)-芯數(C)", inplace=True)
            break
        else:
            cores = list(cable_choosed.iloc[:, 0])[0:-1]
            sectional_area = list(cable_choosed.columns)[1:]
            cable_choosed.set_index("芯數(C)-公稱(mm^2)", inplace=True)

    else:
        pass

for item in pipe_name:
    if choose_pipe == item:
        Pipe_item = item
        pipe_choosed = pd.read_csv(base_dir + "Pipe_" + item + ".csv")
        break
    else:
        pass

print("{} cores list: {}".format(Cable_item, cores))
print("{} 公稱截面積 list: {}".format(Cable_item, sectional_area))

choose_cores = input("choose Cable cores: ")
choose_sectional_area = input("choose Cable 公稱截面積: ")
choose_colines = int(input("How many cables together?"))
remainder = float(input("choose remainder: "))

cores_item = 0
sectional_area_item = 0
while cores_item <= len(cores):
    if choose_cores == cores[cores_item]:
        break
    elif cores_item == len(cores):
        print("out of range")
    cores_item += 1

for i, item in enumerate(sectional_area):
    if str(item) == choose_sectional_area:
        sectionalarea_item = i
# print(cable_choosed.iloc[sectionalarea_item, cores_item])
try:
    choosed_place = cable_choosed.iloc[sectionalarea_item, cores_item]
    TOTAL_AREA = (((choosed_place / 2) * (choosed_place / 2) * pi)*choose_colines)/remainder
    print("TOTAL AREA", TOTAL_AREA)

    delimeter_cal = math.sqrt((TOTAL_AREA/pi)) * 2
    for i, num in enumerate(pipe_choosed["管內徑"]):
        if num > delimeter_cal:
            delimeter_choosed = num
            delimeter_choosed_index = i
            break
    print("Calulated delimeter: ", delimeter_cal)
    print("Pipe {} delimeter choose: {}".format(Pipe_item, delimeter_choosed))
    print("Pipe {} 公稱 choose: {}".format(Pipe_item, pipe_choosed.iloc[delimeter_choosed_index,0]))
except:
    print("OUT OF RANGE")