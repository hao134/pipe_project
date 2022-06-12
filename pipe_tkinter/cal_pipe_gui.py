import tkinter as tk
import math
import pandas as pd
import numpy as np

pi = 3.14159265359

window = tk.Tk()
window.title('Pipe App')
window.geometry('800x300')
window.configure(background='#F5FFE8')

## ============================== Load Data ======================================
CVV_Cable_pd = pd.DataFrame(
    np.array([[0.5, 7.8, 8.2, 8.9, 9.7, 10.4, 10.4, 11.2, 12.9, 13.3, 14.7, 16.2, 18, 19.1, 20.5], \
              [0.75, 8.2, 8.7, 9.4, 10.2, 11, 11, 11.9, 13.7, 14.2, 15.6, 17.3, 19.2, 20.4, 22.1], \
              [1.25, 8.8, 9.3, 10.1, 10.9, 11.8, 11.8, 12.7, 14.7, 15.2, 16.8, 18.7, 20.7, 22.2, 23.9], \
              [2, 9.7, 10.3, 11.2, 12.1, 13.1, 13.1, 14.2, 16.5, 17.1, 19, 21.1, 23.6, 25.3, 27.4]]), \
    columns=["ITEM", "2", "3", "4", "5", "6", "7", "8", "10", "12", "16", "20", "24", "30", "36"])
CVV_Cable_pd.set_index("ITEM", inplace=True)

CVVS_Cable_pd = pd.DataFrame(
    np.array([[0.5, 8.4, 8.8, 9.5, 10.2, 10.9, 10.9, 11.7, 13.4, 13.8, 15.2, 16.7, 18.5, 19.6, 21.0], \
              [0.75, 8.8, 9.3, 10, 10.7, 11.5, 11.5, 12.4, 14.2, 14.7, 16.1, 17.8, 19.7, 20.9, 22.6], \
              [1.25, 9.3, 9.8, 10.6, 11.4, 12.3, 12.3, 13.2, 15.2, 15.7, 17.3, 19.2, 21.2, 22.7, 24.6], \
              [2.0, 10.2, 10.8, 11.7, 12.6, 13.6, 13.6, 14.7, 17, 17.6, 19.5, 21.6, 24.1, 25.8, 27.9]]), \
    columns=["ITEM", "2", "3", "4", "5", "6", "7", "8", "10", "12", "16", "20", "24", "30", "36"])
CVVS_Cable_pd.set_index("ITEM", inplace=True)

PVC_Cable_pd = pd.DataFrame(np.array([[2, 11.5, 13.5, 15.5, 19, 22, 24, 27, 28, 31, 34, 37, 41, 44], \
                                      [3, 12.5, 14.5, 16.5, 20, 24, 26, 29, 30, 33, 37, 40, 44, 47], \
                                      [4, 13.5, 16, 18, 22, 27, 28, 32, 34, 36, 41, 44, 49, 52]]), \
                            columns=["ITEM", "3.5", "5.5", "8", "14", "22", "30", "38", "50", "60", "80", "100", "125", "150"])
PVC_Cable_pd.set_index("ITEM", inplace=True)
PVC_Cable_pd = PVC_Cable_pd.T

XLPE_Cable_pd = pd.DataFrame(np.array([[2, 11, 12.2, 16, 17.2, 19.5, 22, 24.7, 26.9, 28.7, 31.5, 34.3, 37.9, 40.9], \
                                       [3, 11.6, 12.9, 17, 18.5, 22, 23.4, 27, 29, 31, 34, 37, 41, 46], \
                                       [4, 12.7, 14.9, 18.5, 21, 24, 25.7, 29, 32, 34, 38, 43, 47, 51]]), \
                             columns=["ITEM", "3.5", "5.5", "8", "14", "22", "30", "38", "50", "60", "80", "100", "125", "150"])
XLPE_Cable_pd.set_index("ITEM", inplace=True)
XLPE_Cable_pd = XLPE_Cable_pd.T

EMT = {"公稱": ["E19", "E25", "E31", "E39", "E51", "E63", "E75"],
       "管內徑": ["16.7", "23.0", "29.0", "35.3", "48.0", "60.3", "72.6"]}
EMT_Pipe_pd = pd.DataFrame(EMT)

PVC = {"公稱": ["13", "16", "20", "28", "35", "41", "52", "65", "80", "100", "125", "150", "200"], \
       "管內徑": ["14", "18", "22", "28", "35", "41", "52", "67", "75", "100", "125", "148", "194"]}
PVC_Pipe_pd = pd.DataFrame(PVC)

RSG = {"公稱": ["G16", "G22", "G28", "G36", "G42", "G54", "G70", "G82", "G104"], \
       "管內徑": ["16.4", "21.9", "28.3", "36.9", "42.8", "54.0", "69.6", "82.3", "106.4"]}
RSG_Pipe_pd = pd.DataFrame(RSG)

SUS304 = {"公稱": ["10", "15", "20", "25", "32", "40", "50", "65", "80", "90", "100", "125", "150", "200"], \
          "管內徑": ["13.3", "16.7", "22.2", "28.0", "36.7", "42.6", "53.5", "69.3", "81.1", "93.6", "106.3", "129.8", "155.2", "203.2"]}
SUS304_Pipe_pd = pd.DataFrame(SUS304)
### ============================================= Load Data =======================


    #CableCores_label.configure(text = str(cores))
def set_options(*args):
    """
    Function to configure options for second drop down
    """
    global CVV_variable, Cablecores_variable, opt_cores
    a = ['2', '3','4','5','6','7','8','10','12','16','20','24','30','36']
    b = ['2', '3', '4']

    # check something has been selected
    if CVV_variable.get() == '(select)':
        return None

    # refresh option menu
    Cablecores_variable.set('(select)')
    opt_cores['menu'].delete(0, 'end')

    # pick new set of options
    if CVV_variable.get() in ["CVV","CVVS"]:
        new_options = a
    else:
        new_options = b

    # add new options in
    for item in new_options:
        opt_cores['menu'].add_command(label=item, command=tk._setit(Cablecores_variable, item))

def set_options2(*args):
    """
    Function to configure options for second drop down
    """
    global CVV_variable, CableSArea_variable, opt_sarea
    a = ['0.5', '0.75', '1.25', '2']
    b = ['3.5', '5.5', '8', '14', '22', '30', '38', '50', '60', '80', '100', '125', '150']

    # check something has been selected
    if CVV_variable.get() == '(select)':
        return None

    # refresh option menu
    CableSArea_variable.set('(select)')
    opt_sarea['menu'].delete(0, 'end')

    # pick new set of options
    if CVV_variable.get() in ["CVV","CVVS"]:
        new_options = a
    else:
        new_options = b

    # add new options in
    for item in new_options:
        opt_sarea['menu'].add_command(label=item, command=tk._setit(CableSArea_variable, item))

def calculate_pipe():
    Cable = str(CVV_variable.get())
    Pipe = str(PIPE_variable.get())
    Choosed_cores = str(Cablecores_variable.get())
    Choosed_sectional_area = str(CableSArea_variable.get())
    Choosed_num_colinear = int(CableNumber_label_entry.get())
    Choosed_remainder = float(Remainder_label_entry.get())
    if not 0.0 < float(Choosed_remainder) <= 1.0:
        return result_label.configure(text="餘裕不在範圍內")

    Cable_name = ["CVV", "CVVS", "PVC", "XLPE"]
    cable_map = [CVV_Cable_pd, CVVS_Cable_pd, PVC_Cable_pd, XLPE_Cable_pd]
    Pipe_name = ["EMT", "PVC", "RSG", "SUS304"]
    pipe_map = [EMT_Pipe_pd, PVC_Pipe_pd, RSG_Pipe_pd, SUS304_Pipe_pd]
    cable_index = [i for i, x in enumerate(Cable_name) if x == Cable]
    cable_choosed = cable_map[cable_index[0]]
    pipe_index = [i for i, x in enumerate(Pipe_name) if x == Pipe]
    pipe_choosed = pipe_map[pipe_index[0]]
    cores = list(cable_choosed.columns.astype(int).astype(str))
    Sectional_area = list(cable_choosed.index)

    cores_item = 0
    sectional_area_item = 0
    while cores_item <= len(cores):
        if Choosed_cores == cores[cores_item]:
            break
        elif cores_item == len(cores):
            print("out of range")
        cores_item += 1

    for i, item in enumerate(Sectional_area):
        if str(item) == Choosed_sectional_area:
            sectional_area_item = i
    try:
        choosed_place = cable_choosed.iloc[sectional_area_item, cores_item]
        TOTAL_AREA = (((choosed_place / 2) * (choosed_place / 2) * pi) * Choosed_num_colinear) / Choosed_remainder
        # print("TOTAL AREA", TOTAL_AREA)

        delimeter_cal = math.sqrt((TOTAL_AREA / pi)) * 2
        for i, num in enumerate(pipe_choosed["管內徑"]):
            if float(num) > delimeter_cal:
                delimeter_choosed = num
                delimeter_choosed_index = i
                break
        # print("Calulated delimeter: ", delimeter_cal)
        # print("Pipe {} delimeter choose: {}".format(Pipe_item, delimeter_choosed))
        # print("Pipe {} 公稱 choose: {}".format(Pipe_item, pipe_choosed.iloc[delimeter_choosed_index, 0]))
        Choosed_nomiater = pipe_choosed.iloc[delimeter_choosed_index, 0]
        return result_label.configure(text=Pipe + "-" + str(Choosed_nomiater))
    except:
        #print("OUT OF RANGE")
        return result_label.configure(text="Out of range")

title_label = tk.Label(window, text = "Pipe Select Form", font = ("Times New Roman", 24), bg = "#F5FFE8")
title_label.grid(column = 0, row = 0, sticky = "WN", columnspan = 2)

header_label = tk.Label(window, text='1. 填入Cable資料',font = ("標楷體", 14, "bold"), bg = "#F5FFE8")
header_label.grid(column = 0, row = 1, sticky = "WN")


CVV_variable = tk.StringVar(window)
CVV_variable.set("(select)") # devault VALUE
CableChoose_label = tk.Label(window, text = "Cable 種類",font = ("標楷體", 14),bg = "#F5FFE8", width = 15)
CableChoose_label.grid(column = 0, row = 2)
opt_cvv = tk.OptionMenu(window, CVV_variable, 'CVV', 'CVVS','PVC','XLPE')
opt_cvv.grid(column = 1, row = 2)

CVV_variable.trace('w', set_options)
Cablecores_variable = tk.StringVar(window)
Cablecores_variable.set("(select)") # devault VALUE
Cablecores_label = tk.Label(window, text = "芯數",font = ("標楷體", 14),bg = "#F5FFE8", width = 15)
Cablecores_label.grid(column = 2, row = 2)
#c_cores = list(calculate_pipe().get_Cable(source = str(CVV_variable.get())))
opt_cores = tk.OptionMenu(window, Cablecores_variable,"(select)")
opt_cores.grid(column = 3, row = 2)
# initialise
set_options()

CVV_variable.trace('w', set_options2)
CableSArea_variable = tk.StringVar(window)
CableSArea_variable.set("(select)") # devault VALUE
CableSArea_label = tk.Label(window, text = "公稱截面積",font = ("標楷體", 14),bg = "#F5FFE8", width = 15)
CableSArea_label.grid(column = 4, row = 2)
opt_sarea = tk.OptionMenu(window, CableSArea_variable,"(select)")
opt_sarea.grid(column = 5, row =2)
# initialise
set_options2()

header2_label = tk.Label(window, text='2. 選擇Pipe',font = ("標楷體", 14, "bold"), bg = "#F5FFE8")
header2_label.grid(column = 0, row = 3, sticky = "WN")

PIPE_list = ["EMT","PVC","RSG","SUS304"]
PIPE_variable = tk.StringVar(window)
PIPE_variable.set("(select)") # devault VALUE
PIPEChoose_label = tk.Label(window, text = "Pipe 種類",font = ("標楷體", 14),bg = "#F5FFE8", width = 15)
PIPEChoose_label.grid(column = 0, row =4)
opt_pipe = tk.OptionMenu(window, PIPE_variable, *PIPE_list)
opt_pipe.grid(column = 1, row = 4)
#
header3_label = tk.Label(window, text='3. 輸入數值',font = ("標楷體", 14, "bold"), bg = "#F5FFE8")
header3_label.grid(column = 0, row = 5, sticky = "WN")
#
CableNumber_frame = tk.Frame(window)
CableNumber_frame.grid(column = 0, row = 6)
CableNumber_label = tk.Label(CableNumber_frame, text='Cable共線數選擇',font = ("標楷體", 14),bg = "#F5FFE8")
CableNumber_label.grid(column = 0, row = 6)
CableNumber_label_entry = tk.Entry(window, width = 6)
CableNumber_label_entry.grid(column= 1, row =6)
#
Remainder_frame = tk.Frame(window)
v = tk.StringVar(window, value=0.6)
Remainder_frame.grid(column = 2, row = 6)
Remainder_label = tk.Label(Remainder_frame, text='餘裕(0<num<=1)',font = ("標楷體", 14),bg = "#F5FFE8")
Remainder_label.grid(column = 2, row = 6)
Remainder_label_entry = tk.Entry(window, width = 6,textvariable=v)
Remainder_label_entry.grid(column = 3, row = 6)
#
result_label = tk.Label(window,font = ("Times New Roman", 20),bg = "#F5FFE8", fg = "red")
result_label.grid(column = 0, row = 7)
#
calculate_btn = tk.Button(window, text='Submit', font = ("Times New Roman", 12),command=calculate_pipe)
calculate_btn.grid(column = 0, row = 8)

#window.wm_attributes("-transparentcolor", "white")
window.mainloop()