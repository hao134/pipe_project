import pandas as pd
from flask import Flask, request, render_template
import math

pi = 3.14159265359
base_dir = "C:\\Users\\gcsi\\Desktop\\pipe_data\\"

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

    if request.method == "POST" and "cable" in request.form and "pipe" in request.form:
        Cable = str(request.form.get("cable"))
        Pipe = str(request.form.get("pipe"))
        try:
            cable_choosed = pd.read_csv(base_dir + "Cable_" + Cable + ".csv")
            pipe_choosed = pd.read_csv(base_dir + "Pipe_" + Pipe + ".csv")
            if Cable in ["CVV", "CVVS"]:
                cores = list(cable_choosed.columns)[1:-1]
                Sectional_area = list(cable_choosed.iloc[:, 0])
                cable_choosed.set_index("公稱(mm^2)-芯數(C)", inplace=True)
            else:
                cores = list(cable_choosed.iloc[:, 0])[0:-1]
                Sectional_area = list(cable_choosed.columns)[1:]
                cable_choosed.set_index("芯數(C)-公稱(mm^2)", inplace=True)
        except:
            no_file_sign = 1
            Choosed_nomiater = "沒選擇資料，無法算"
            return render_template("test2.html", no_file_sign=no_file_sign, Choosed_nomiater= Choosed_nomiater)
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
                if Choosed_cores == cores[cores_item]:
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
                if num > delimeter_cal:
                    delimeter_choosed = num
                    delimeter_choosed_index = i
                    break
        # print("Calulated delimeter: ", delimeter_cal)
        # print("Pipe {} delimeter choose: {}".format(Pipe_item, delimeter_choosed))
        # print("Pipe {} 公稱 choose: {}".format(Pipe_item, pipe_choosed.iloc[delimeter_choosed_index, 0]))
            Choosed_nomiater = pipe_choosed.iloc[delimeter_choosed_index, 0]
        except:
            #print("OUT OF RANGE")
            Choosed_nomiater = "cannot be found"
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