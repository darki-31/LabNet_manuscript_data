import numpy as np
import pandas as pd

# float numbers print format
ff = "{:.2f}".format

# read all files
p2n = pd.read_csv('data/python_r2_no_opt.csv', delimiter=';')
p2o = pd.read_csv('data/python_r2_opt.csv', delimiter=';')
p3n = pd.read_csv('data/python_r3_no_opt.csv', delimiter=';')
p3o = pd.read_csv('data/python_r3_opt.csv', delimiter=';')
p4n = pd.read_csv('data/python_r4_no_opt.csv', delimiter=';')
p4o = pd.read_csv('data/python_r4_opt.csv', delimiter=';')
p4_1 = pd.read_csv('data/python_r4_1kHz.csv', delimiter=';')
p4_max = pd.read_csv('data/python_r4_max.csv', delimiter=';')

cs2n = pd.read_csv('data/c_sharp_r2_no_opt.csv', delimiter=';')
cs2o = pd.read_csv('data/c_sharp_r2_opt.csv', delimiter=';')
cs3n = pd.read_csv('data/c_sharp_r3_no_opt.csv', delimiter=';')
cs3o = pd.read_csv('data/c_sharp_r3_opt.csv', delimiter=';')
cs4n = pd.read_csv('data/c_sharp_r4_no_opt.csv', delimiter=';')
cs4o = pd.read_csv('data/c_sharp_r4_opt.csv', delimiter=';')
cs4_1 = pd.read_csv('data/c_sharp_r4_1kHz.csv', delimiter=';')
cs4_max = pd.read_csv('data/c_sharp_r4_max.csv', delimiter=';')

cp2n = pd.read_csv('data/cpp_r2_no_opt.csv', delimiter=';')
cp2o = pd.read_csv('data/cpp_r2_opt.csv', delimiter=';')
cp3n = pd.read_csv('data/cpp_r3_no_opt.csv', delimiter=';')
cp3o = pd.read_csv('data/cpp_r3_opt.csv', delimiter=';')
cp4n = pd.read_csv('data/cpp_r4_no_opt.csv', delimiter=';')
cp4o = pd.read_csv('data/cpp_r4_opt.csv', delimiter=';')
cp4_1 = pd.read_csv('data/cpp_r4_1kHz.csv', delimiter=';')
cp4_max = pd.read_csv('data/cpp_r4_max.csv', delimiter=';')

r2n =  str(ff(cs2n["SetAndRead"].mean())) + " " + str(ff(cp2n["SetAndRead"].mean())) + " " + str(ff(p2n["SetAndRead"].mean()))
r2n += " " + str(ff(cs2n["SetAndRead"].std())) + " " + str(ff(cp2n["SetAndRead"].std())) + " " + str(ff(p2n["SetAndRead"].std()))

r3n =  str(ff(cs3n["SetAndRead"].mean())) + " " + str(ff(cp3n["SetAndRead"].mean())) + " " + str(ff(p3n["SetAndRead"].mean()))
r3n += " " + str(ff(cs3n["SetAndRead"].std())) + " " + str(ff(cp3n["SetAndRead"].std())) + " " + str(ff(p3n["SetAndRead"].std()))

r4n =  str(ff(cs4n["SetAndRead"].mean())) + " " + str(ff(cp4n["SetAndRead"].mean())) + " " + str(ff(p4n["SetAndRead"].mean()))
r4n += " " + str(ff(cs4n["SetAndRead"].std())) + " " + str(ff(cp4n["SetAndRead"].std())) + " " + str(ff(p4n["SetAndRead"].std()))

r2o =  str(ff(cs2o["SetAndRead"].mean())) + " " + str(ff(cp2o["SetAndRead"].mean())) + " " + str(ff(p2o["SetAndRead"].mean()))
r2o += " " + str(ff(cs2o["SetAndRead"].std())) + " " + str(ff(cp2o["SetAndRead"].std())) + " " + str(ff(p2o["SetAndRead"].std()))

r3o =  str(ff(cs3o["SetAndRead"].mean())) + " " + str(ff(cp3o["SetAndRead"].mean())) + " " + str(ff(p3o["SetAndRead"].mean()))
r3o += " " + str(ff(cs3o["SetAndRead"].std())) + " " + str(ff(cp3o["SetAndRead"].std())) + " " + str(ff(p3o["SetAndRead"].std()))

r4o =  str(ff(cs4o["SetAndRead"].mean())) + " " + str(ff(cp4o["SetAndRead"].mean())) + " " + str(ff(p4o["SetAndRead"].mean()))
r4o += " " + str(ff(cs4o["SetAndRead"].std())) + " " + str(ff(cp4o["SetAndRead"].std())) + " " + str(ff(p4o["SetAndRead"].std()))

r41 =  str(ff(cs4_1["SetAndRead"].mean())) + " " + str(ff(cp4_1["SetAndRead"].mean())) + " " + str(ff(p4_1["SetAndRead"].mean()))
r41 += " " + str(ff(cs4_1["SetAndRead"].std())) + " " + str(ff(cp4_1["SetAndRead"].std())) + " " + str(ff(p4_1["SetAndRead"].std()))

r4m =  str(ff(cs4_max["SetAndRead"].mean())) + " " + str(ff(cp4_max["SetAndRead"].mean())) + " " + str(ff(p4_max["SetAndRead"].mean()))
r4m += " " + str(ff(cs4_max["SetAndRead"].std())) + " " + str(ff(cp4_max["SetAndRead"].std())) + " " + str(ff(p4_max["SetAndRead"].std()))

print("\pgfplotstableread{")
print("a   cs   cp   py   st1  st2  st3")
print("Rv2 " + r2n)
print("Rv3 " + r3n)
print("Rv4 " + r4n)
print("Rv2o " + r2o)
print("Rv3o " + r3o)
print("Rv4o " + r4o)
print("Rv41 " + r41)
print("Rv4m " + r4m)
print("}\mytable")