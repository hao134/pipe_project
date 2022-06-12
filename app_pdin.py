import pandas as pd
from flask import Flask, request, render_template
import numpy as np
import math

pi = 3.14159265359

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])

def calculate():
    cores = ""
    Cable = ""
    Pipe = ""
    Sectional_area = ""
    Choosed_nomiater = ""
    Choosed_cores=""
    Choosed_remainder=""
    Choosed_sectional_area=""
    Choosed_num_colinear = ""
    TOTAL_AREA = ""
    delimeter_cal = ""
    delimeter_choosed = ""
    pipe_delimeter = ""
    pipe_nomiater = ""
    no_value_sign = ""
    no_file_sign = ""
    out_range_sign = ""
    no_match_sign = ""
    MAX_PIPE_AREA = ""

    """ LOAD DATA """
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
                                columns=["ITEM", "3.5", "5.5", "8", "14", "22", "30", "38", "50", "60", "80", "100",
                                         "125", "150"])
    PVC_Cable_pd.set_index("ITEM", inplace=True)
    PVC_Cable_pd = PVC_Cable_pd.T

    XLPE_Cable_pd = pd.DataFrame(np.array([[2, 11, 12.2, 16, 17.2, 19.5, 22, 24.7, 26.9, 28.7, 31.5, 34.3, 37.9, 40.9], \
                                           [3, 11.6, 12.9, 17, 18.5, 22, 23.4, 27, 29, 31, 34, 37, 41, 46], \
                                           [4, 12.7, 14.9, 18.5, 21, 24, 25.7, 29, 32, 34, 38, 43, 47, 51]]), \
                                 columns=["ITEM", "3.5", "5.5", "8", "14", "22", "30", "38", "50", "60", "80", "100",
                                          "125", "150"])
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
              "管內徑": ["13.3", "16.7", "22.2", "28.0", "36.7", "42.6", "53.5", "69.3", "81.1", "93.6", "106.3", "129.8",
                      "155.2", "203.2"]}
    SUS304_Pipe_pd = pd.DataFrame(SUS304)

    if request.method == "POST" and "cable" in request.form and "pipe" in request.form:
        Cable = str(request.form.get("cable"))
        Pipe = str(request.form.get("pipe"))
        if Cable in ["CVV", "CVVS", "PVC", "XLPE"]:
            pass
        else:
            no_file_sign = 1
            Choosed_nomiater = "沒選擇資料，無法算"
            return render_template("test2.html", no_file_sign=no_file_sign, Choosed_nomiater=Choosed_nomiater)

        Cable_name = ["CVV","CVVS","PVC","XLPE"]
        cable_map = [CVV_Cable_pd, CVVS_Cable_pd, PVC_Cable_pd, XLPE_Cable_pd]
        Pipe_name = ["EMT", "PVC", "RSG", "SUS304"]
        pipe_map = [EMT_Pipe_pd, PVC_Pipe_pd, RSG_Pipe_pd, SUS304_Pipe_pd]
        cable_index = [i for i, x in enumerate(Cable_name) if x == Cable]
        cable_choosed = cable_map[cable_index[0]]
        pipe_index = [i for i, x in enumerate(Pipe_name) if x == Pipe]
        pipe_choosed = pipe_map[pipe_index[0]]
        cores = list(cable_choosed.columns.astype(int).astype(str))
        Sectional_area = list(cable_choosed.index)

        try:
            Choosed_cores = str(request.form.get("choosed_cores"))
            Choosed_sectional_area = str(request.form.get("choosed_sectional_area"))
            Choosed_num_colinear = int(request.form.get("choosed_num_colinear"))
            Choosed_remainder = float(request.form.get("choosed_remainder"))
            if not 0.0 < float(Choosed_remainder) <= 1.0:
                out_range_sign = 1
                Choosed_nomiater = "餘裕超出數值，無法算"
                return render_template("test2.html", out_range_sign=out_range_sign, Choosed_nomiater=Choosed_nomiater)
            else:
                pass
        except:
            no_value_sign = 1
            Choosed_nomiater = "沒輸入數值，無法算"
            return render_template("test2.html", no_value_sign=no_value_sign, Choosed_nomiater=Choosed_nomiater)
        cores_item = 0
        sectional_area_item = 0
        try:
            while cores_item <= len(cores):
                if Choosed_cores == str(cores[cores_item]):
                    break
                elif cores_item == len(cores):
                    print("out of range")
                cores_item += 1
        except:
            cores_item = 100

        for i, item in enumerate(Sectional_area):
            if str(item) == Choosed_sectional_area:
                sectionalarea_item = i
        pipe_delimeter = list(pipe_choosed["管內徑"])
        pipe_nomiater = list(pipe_choosed.iloc[:, 0])

        try:
            choosed_place = cable_choosed.iloc[sectionalarea_item, cores_item]
            TOTAL_AREA = round((((choosed_place / 2) * (choosed_place / 2) * pi) * Choosed_num_colinear) / Choosed_remainder, 2)
            #print("TOTAL AREA", TOTAL_AREA)

            delimeter_cal = round(math.sqrt((TOTAL_AREA / pi)) * 2,2)
            for i, num in enumerate(pipe_choosed["管內徑"]):
                if float(num) > delimeter_cal:
                    delimeter_choosed = num
                    delimeter_choosed_index = i
                    break
                # no_match_sign = 1
                # Choosed_nomiater = "cannot be found"
                # return render_template("test2.html", TOTAL_AREA=TOTAL_AREA, Choosed_nomiater=Choosed_nomiater)
        # print("Calulated delimeter: ", delimeter_cal)
        # print("Pipe {} delimeter choose: {}".format(Pipe_item, delimeter_choosed))
        # print("Pipe {} 公稱 choose: {}".format(Pipe_item, pipe_choosed.iloc[delimeter_choosed_index, 0]))
            Choosed_nomiater = pipe_choosed.iloc[delimeter_choosed_index, 0]
        except:
            no_match_sign = 1
            choosed_place = cable_choosed.iloc[sectionalarea_item, cores_item]
            TOTAL_AREA = round((((choosed_place / 2) * (choosed_place / 2) * pi) * Choosed_num_colinear) / Choosed_remainder, 2)
            Choosed_nomiater = "無法推薦pipe"
            length = len(pipe_choosed["管內徑"])
            MAX_PIPE_AREA = round((float(pipe_choosed["管內徑"][length-1]) * float(pipe_choosed["管內徑"][length-1]))* (1/4) * pi,2)
            return render_template("test2.html", no_match_sign=no_match_sign,TOTAL_AREA=TOTAL_AREA,MAX_PIPE_AREA=MAX_PIPE_AREA,Choosed_nomiater = Choosed_nomiater)


    return render_template("test2.html", cores=cores, Pipe=Pipe, Cable=Cable, Sectional_area=Sectional_area,\
                           Choosed_nomiater = Choosed_nomiater,Choosed_cores = Choosed_cores,Choosed_remainder=Choosed_remainder,\
                           Choosed_sectional_area = Choosed_sectional_area, Choosed_num_colinear=Choosed_num_colinear,\
                           TOTAL_AREA=TOTAL_AREA, delimeter_cal=delimeter_cal, delimeter_choosed=delimeter_choosed, pipe_delimeter=pipe_delimeter, pipe_nomiater=pipe_nomiater)
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)


#pipe_delimeter = list(pipe_choosed["管內徑"])
#pipe_nomiater = list(pipe_choosed.iloc[:, 0])
# @app.route("/result",methods = ["POST","GET"])
# def calculate2():
#     Choosed_cores = ""
#     Choosed_sectional_Area = ""
#     Choosed_remainder=""
#     choosed_nomiater=""
#     if request.method == "POST" and "choosed_cores" in request.form and "choosed_sectional_area" in request.form:
#         Choosed_cores = float(request.form.get("choosed_cores"))
#         Choosed_sectional_Area = float(request.form.get("choosed_sectional_area"))
#         Choosed_remainder = float(request.form.get("choosed_remainder"))
#         cores_item = 0
#         sectional_area_item = 0
#         while cores_item <= len(cores):
#             if Choosed_cores == cores[cores_item]:
#                 break
#             elif cores_item == len(cores):
#                 print("out of range")
#             cores_item += 1
#
#         for i, item in enumerate(Sectional_area):
#             if str(item) == Choosed_sectional_Area:
#                 sectionalarea_item = i
#     try:
#         choosed_place = cable_choosed.iloc[sectionalarea_item, cores_item]
#         TOTAL_AREA = ((choosed_place / 2) * (choosed_place / 2) * pi) / Choosed_remainder
#         print("TOTAL AREA", TOTAL_AREA)
#
#         delimeter_cal = math.sqrt((TOTAL_AREA / pi)) * 2
#         for i, num in enumerate(pipe_choosed["管內徑"]):
#             if num > delimeter_cal:
#                 delimeter_choosed = num
#                 delimeter_choosed_index = i
#                 break
#         # print("Calulated delimeter: ", delimeter_cal)
#         # print("Pipe {} delimeter choose: {}".format(Pipe_item, delimeter_choosed))
#         # print("Pipe {} 公稱 choose: {}".format(Pipe_item, pipe_choosed.iloc[delimeter_choosed_index, 0]))
#         choosed_nomiater = pipe_choosed.iloc[delimeter_choosed_index, 0]
#     except:
#         print("OUT OF RANGE")
#
#     return render_template("simple.html", choosed_nomiater = choosed_nomiater)





# from flask import session
#
# @app.route('/')
# def home():
#    store = index_generator()
#    session['store'] = store
#    return render_template('home.html')
#
#  @app.route('/home_city',methods = ['POST'])
#  def home_city():
#    CITY=request.form['city']
#    store = session.get('store')
#    request_yelp(DEFAULT_LOCATION=CITY,data_store=store)
#    return render_template('bank.html')