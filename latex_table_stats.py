# create latex table with all statistical parameters

import numpy as np
import pandas as pd
import shutil

def create_summary_table():
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

    f = open("summary_table.tex", "a")

    # create tabel header
    f.write("\\begin{tabular}{lrrrcrrrcrrrrrcrrrcrrrcrrr}\n")

    f.write("\\toprule\n")
    f.write("\\multicolumn{26}{c}{LabNet latencies}\\\\\n")
    f.write("\\toprule\n")
    f.write("\\multicolumn{14}{c}{non optimized} & & \\multicolumn{11}{c}{optimized} \\\\\n")
    f.write("\\cmidrule{1-14} \\cmidrule{16-26}\n")
    f.write("& \\multicolumn{3}{c}{id test} & & \\multicolumn{3}{c}{set test} & & \\multicolumn{5}{c}{set and read gpio} & & \\multicolumn{3}{c}{id test} & & \\multicolumn{3}{c}{set test} & & \\multicolumn{3}{c}{set and read gpio} \\\\\n")
    f.write("\\cmidrule{2-4} \\cmidrule{6-8} \\cmidrule{10-14} \\cmidrule{16-18} \\cmidrule{20-22} \\cmidrule{24-26}\n")
    f.write("& Rv2  & Rv3 & Rv4  &  & Rv2  & Rv3  & Rv4  &  & Rv2  & Rv3  & Rv4  & 1kHz & max  & & Rv2  & Rv3  & Rv4  &  & Rv2  & Rv3  & Rv4  &  & Rv2  & Rv3  & Rv4  \\\\\n")

    # print C# parameters
    f.write("\\cmidrule{1-14} \\cmidrule{16-26}\n")
    f.write("\\multicolumn{14}{c}{C\\#} & \\multicolumn{12}{c}{C\\#} \\\\\n")
    f.write("\\cmidrule{1-14} \\cmidrule{16-26}\n")

    mean = "mean & " + ff(cs2n["IdTest"].mean()) + " & " + ff(cs3n["IdTest"].mean()) + " & " + ff(cs4n["IdTest"].mean())
    mean +=  " & & " + ff(cs2n["SetTest"].mean()) + " & " + ff(cs3n["SetTest"].mean()) + " & " + ff(cs4n["SetTest"].mean())
    mean +=  " & & " + ff(cs2n["SetAndRead"].mean()) + " & " + ff(cs3n["SetAndRead"].mean()) + " & " + ff(cs4n["SetAndRead"].mean())
    mean +=  " &   " + ff(cs4_1["SetAndRead"].mean()) + " & " + ff(cs4_max["SetAndRead"].mean())
    mean +=  " & & " + ff(cs2o["IdTest"].mean()) + " & " + ff(cs3o["IdTest"].mean()) + " & " + ff(cs4o["IdTest"].mean())
    mean +=  " & & " + ff(cs2o["SetTest"].mean()) + " & " + ff(cs3o["SetTest"].mean()) + " & " + ff(cs4o["SetTest"].mean())
    mean +=  " & & " + ff(cs2o["SetAndRead"].mean()) + " & " + ff(cs3o["SetAndRead"].mean()) + " & " + ff(cs4o["SetAndRead"].mean()) + "\\\\"
    f.write(mean)
    f.write("\n")

    std = "STD & " + ff(cs2n["IdTest"].std()) + " & " + ff(cs3n["IdTest"].std()) + " & " + ff(cs4n["IdTest"].std())
    std +=  " & & " + ff(cs2n["SetTest"].std()) + " & " + ff(cs3n["SetTest"].std()) + " & " + ff(cs4n["SetTest"].std())
    std +=  " & & " + ff(cs2n["SetAndRead"].std()) + " & " + ff(cs3n["SetAndRead"].std()) + " & " + ff(cs4n["SetAndRead"].std())
    std +=  " &   " + ff(cs4_1["SetAndRead"].std()) + " & " + ff(cs4_max["SetAndRead"].std())
    std +=  " & & " + ff(cs2o["IdTest"].std()) + " & " + ff(cs3o["IdTest"].std()) + " & " + ff(cs4o["IdTest"].std())
    std +=  " & & " + ff(cs2o["SetTest"].std()) + " & " + ff(cs3o["SetTest"].std()) + " & " + ff(cs4o["SetTest"].std())
    std +=  " & & " + ff(cs2o["SetAndRead"].std()) + " & " + ff(cs3o["SetAndRead"].std()) + " & " + ff(cs4o["SetAndRead"].std()) + "\\\\"
    f.write(std)
    f.write("\n")

    q_s = ["median", "$p=25$", "$p=75$", "$p=2.5$", "$p=97.5$"]
    q_v = [0.5, 0.25, 0.75, 0.025, 0.975]
    for q in zip(q_s, q_v):
        st = q[0] + " & " + ff(cs2n["IdTest"].quantile(q[1])) + " & " + ff(cs3n["IdTest"].quantile(q[1])) + " & " + ff(cs4n["IdTest"].quantile(q[1]))
        st +=  " & & " + ff(cs2n["SetTest"].quantile(q[1])) + " & " + ff(cs3n["SetTest"].quantile(q[1])) + " & " + ff(cs4n["SetTest"].quantile(q[1]))
        st +=  " & & " + ff(cs2n["SetAndRead"].quantile(q[1])) + " & " + ff(cs3n["SetAndRead"].quantile(q[1])) + " & " + ff(cs4n["SetAndRead"].quantile(q[1]))
        st +=  " &   " + ff(cs4_1["SetAndRead"].quantile(q[1])) + " & " + ff(cs4_max["SetAndRead"].quantile(q[1]))
        st +=  " & & " + ff(cs2o["IdTest"].quantile(q[1])) + " & " + ff(cs3o["IdTest"].quantile(q[1])) + " & " + ff(cs4o["IdTest"].quantile(q[1]))
        st +=  " & & " + ff(cs2o["SetTest"].quantile(q[1])) + " & " + ff(cs3o["SetTest"].quantile(q[1])) + " & " + ff(cs4o["SetTest"].quantile(q[1]))
        st +=  " & & " + ff(cs2o["SetAndRead"].quantile(q[1])) + " & " + ff(cs3o["SetAndRead"].quantile(q[1])) + " & " + ff(cs4o["SetAndRead"].quantile(q[1])) + "\\\\"
        f.write(st)
        f.write("\n")


    # print C++ parameters
    f.write("\\cmidrule{1-14} \\cmidrule{16-26}\n")
    f.write("\\multicolumn{14}{c}{C++} & \\multicolumn{12}{c}{C++} \\\\\n")
    f.write("\\cmidrule{1-14} \\cmidrule{16-26}\n")

    mean = "mean & " + ff(cp2n["IdTest"].mean()) + " & " + ff(cp3n["IdTest"].mean()) + " & " + ff(cp4n["IdTest"].mean())
    mean +=  " & & " + ff(cp2n["SetTest"].mean()) + " & " + ff(cp3n["SetTest"].mean()) + " & " + ff(cp4n["SetTest"].mean())
    mean +=  " & & " + ff(cp2n["SetAndRead"].mean()) + " & " + ff(cp3n["SetAndRead"].mean()) + " & " + ff(cp4n["SetAndRead"].mean())
    mean +=  " &   " + ff(cp4_1["SetAndRead"].mean()) + " & " + ff(cp4_max["SetAndRead"].mean())
    mean +=  " & & " + ff(cp2o["IdTest"].mean()) + " & " + ff(cp3o["IdTest"].mean()) + " & " + ff(cp4o["IdTest"].mean())
    mean +=  " & & " + ff(cp2o["SetTest"].mean()) + " & " + ff(cp3o["SetTest"].mean()) + " & " + ff(cp4o["SetTest"].mean())
    mean +=  " & & " + ff(cp2o["SetAndRead"].mean()) + " & " + ff(cp3o["SetAndRead"].mean()) + " & " + ff(cp4o["SetAndRead"].mean()) + "\\\\"
    f.write(mean)
    f.write("\n")

    std = "STD & " + ff(cp2n["IdTest"].std()) + " & " + ff(cp3n["IdTest"].std()) + " & " + ff(cp4n["IdTest"].std())
    std +=  " & & " + ff(cp2n["SetTest"].std()) + " & " + ff(cp3n["SetTest"].std()) + " & " + ff(cp4n["SetTest"].std())
    std +=  " & & " + ff(cp2n["SetAndRead"].std()) + " & " + ff(cp3n["SetAndRead"].std()) + " & " + ff(cp4n["SetAndRead"].std())
    std +=  " &   " + ff(cp4_1["SetAndRead"].std()) + " & " + ff(cp4_max["SetAndRead"].std())
    std +=  " & & " + ff(cp2o["IdTest"].std()) + " & " + ff(cp3o["IdTest"].std()) + " & " + ff(cp4o["IdTest"].std())
    std +=  " & & " + ff(cp2o["SetTest"].std()) + " & " + ff(cp3o["SetTest"].std()) + " & " + ff(cp4o["SetTest"].std())
    std +=  " & & " + ff(cp2o["SetAndRead"].std()) + " & " + ff(cp3o["SetAndRead"].std()) + " & " + ff(cp4o["SetAndRead"].std()) + "\\\\"
    f.write(std)
    f.write("\n")

    q_s = ["median", "$p=25$", "$p=75$", "$p=2.5$", "$p=97.5$"]
    q_v = [0.5, 0.25, 0.75, 0.025, 0.975]
    for q in zip(q_s, q_v):
        st = q[0] + " & " + ff(cp2n["IdTest"].quantile(q[1])) + " & " + ff(cp3n["IdTest"].quantile(q[1])) + " & " + ff(cp4n["IdTest"].quantile(q[1]))
        st +=  " & & " + ff(cp2n["SetTest"].quantile(q[1])) + " & " + ff(cp3n["SetTest"].quantile(q[1])) + " & " + ff(cp4n["SetTest"].quantile(q[1]))
        st +=  " & & " + ff(cp2n["SetAndRead"].quantile(q[1])) + " & " + ff(cp3n["SetAndRead"].quantile(q[1])) + " & " + ff(cp4n["SetAndRead"].quantile(q[1]))
        st +=  " &   " + ff(cp4_1["SetAndRead"].quantile(q[1])) + " & " + ff(cp4_max["SetAndRead"].quantile(q[1]))
        st +=  " & & " + ff(cp2o["IdTest"].quantile(q[1])) + " & " + ff(cp3o["IdTest"].quantile(q[1])) + " & " + ff(cp4o["IdTest"].quantile(q[1]))
        st +=  " & & " + ff(cp2o["SetTest"].quantile(q[1])) + " & " + ff(cp3o["SetTest"].quantile(q[1])) + " & " + ff(cp4o["SetTest"].quantile(q[1]))
        st +=  " & & " + ff(cp2o["SetAndRead"].quantile(q[1])) + " & " + ff(cp3o["SetAndRead"].quantile(q[1])) + " & " + ff(cp4o["SetAndRead"].quantile(q[1])) + "\\\\"
        f.write(st)
        f.write("\n")

    # print Python parameters
    f.write("\\cmidrule{1-14} \\cmidrule{16-26}\n")
    f.write("\\multicolumn{14}{c}{Python} & \\multicolumn{12}{c}{Python} \\\\\n")
    f.write("\\cmidrule{1-14} \\cmidrule{16-26}\n")

    mean = "mean & " + ff(p2n["IdTest"].mean()) + " & " + ff(p3n["IdTest"].mean()) + " & " + ff(p4n["IdTest"].mean())
    mean +=  " & & " + ff(p2n["SetTest"].mean()) + " & " + ff(p3n["SetTest"].mean()) + " & " + ff(p4n["SetTest"].mean())
    mean +=  " & & " + ff(p2n["SetAndRead"].mean()) + " & " + ff(p3n["SetAndRead"].mean()) + " & " + ff(p4n["SetAndRead"].mean())
    mean +=  " &   " + ff(p4_1["SetAndRead"].mean()) + " & " + ff(p4_max["SetAndRead"].mean())
    mean +=  " & & " + ff(p2o["IdTest"].mean()) + " & " + ff(p3o["IdTest"].mean()) + " & " + ff(p4o["IdTest"].mean())
    mean +=  " & & " + ff(p2o["SetTest"].mean()) + " & " + ff(p3o["SetTest"].mean()) + " & " + ff(p4o["SetTest"].mean())
    mean +=  " & & " + ff(p2o["SetAndRead"].mean()) + " & " + ff(p3o["SetAndRead"].mean()) + " & " + ff(p4o["SetAndRead"].mean()) + "\\\\"
    f.write(mean)
    f.write("\n")

    std = "STD & " + ff(p2n["IdTest"].std()) + " & " + ff(p3n["IdTest"].std()) + " & " + ff(p4n["IdTest"].std())
    std +=  " & & " + ff(p2n["SetTest"].std()) + " & " + ff(p3n["SetTest"].std()) + " & " + ff(p4n["SetTest"].std())
    std +=  " & & " + ff(p2n["SetAndRead"].std()) + " & " + ff(p3n["SetAndRead"].std()) + " & " + ff(p4n["SetAndRead"].std())
    std +=  " &   " + ff(p4_1["SetAndRead"].std()) + " & " + ff(p4_max["SetAndRead"].std())
    std +=  " & & " + ff(p2o["IdTest"].std()) + " & " + ff(p3o["IdTest"].std()) + " & " + ff(p4o["IdTest"].std())
    std +=  " & & " + ff(p2o["SetTest"].std()) + " & " + ff(p3o["SetTest"].std()) + " & " + ff(p4o["SetTest"].std())
    std +=  " & & " + ff(p2o["SetAndRead"].std()) + " & " + ff(p3o["SetAndRead"].std()) + " & " + ff(p4o["SetAndRead"].std()) + "\\\\"
    f.write(std)
    f.write("\n")

    q_s = ["median", "$p=25$", "$p=75$", "$p=2.5$", "$p=97.5$"]
    q_v = [0.5, 0.25, 0.75, 0.025, 0.975]
    for q in zip(q_s, q_v):
        st = q[0] + " & " + ff(p2n["IdTest"].quantile(q[1])) + " & " + ff(p3n["IdTest"].quantile(q[1])) + " & " + ff(p4n["IdTest"].quantile(q[1]))
        st +=  " & & " + ff(p2n["SetTest"].quantile(q[1])) + " & " + ff(p3n["SetTest"].quantile(q[1])) + " & " + ff(p4n["SetTest"].quantile(q[1]))
        st +=  " & & " + ff(p2n["SetAndRead"].quantile(q[1])) + " & " + ff(p3n["SetAndRead"].quantile(q[1])) + " & " + ff(p4n["SetAndRead"].quantile(q[1]))
        st +=  " &   " + ff(p4_1["SetAndRead"].quantile(q[1])) + " & " + ff(p4_max["SetAndRead"].quantile(q[1]))
        st +=  " & & " + ff(p2o["IdTest"].quantile(q[1])) + " & " + ff(p3o["IdTest"].quantile(q[1])) + " & " + ff(p4o["IdTest"].quantile(q[1]))
        st +=  " & & " + ff(p2o["SetTest"].quantile(q[1])) + " & " + ff(p3o["SetTest"].quantile(q[1])) + " & " + ff(p4o["SetTest"].quantile(q[1]))
        st +=  " & & " + ff(p2o["SetAndRead"].quantile(q[1])) + " & " + ff(p3o["SetAndRead"].quantile(q[1])) + " & " + ff(p4o["SetAndRead"].quantile(q[1])) + "\\\\"
        f.write(st)
        f.write("\n")

    # end of the table
    f.write("\\bottomrule\n")
    f.write("\\end{tabular}\n")
