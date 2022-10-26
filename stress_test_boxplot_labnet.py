import numpy as np
import pandas as pd
import shutil


def create_tex_file():
    # float numbers f.write format
    ff = "{:.2f}".format

    # read all files
    p4n    = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt.csv', delimiter=';')
    p4n_2  = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_2.csv', delimiter=';')
    p4n_3  = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_3.csv', delimiter=';')
    p4n_4  = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_4.csv', delimiter=';')
    p4n_5  = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_5.csv', delimiter=';')
    p4n_6  = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_6.csv', delimiter=';')
    p4n_7  = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_7.csv', delimiter=';')
    p4n_8  = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_8.csv', delimiter=';')
    p4n_9  = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_9.csv', delimiter=';')
    p4n_10 = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_10.csv', delimiter=';')
    p4n_11 = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_11.csv', delimiter=';')
    p4n_12 = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_12.csv', delimiter=';')
    p4n_13 = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_13.csv', delimiter=';')
    p4n_14 = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt_14.csv', delimiter=';')
    

    cs4n    = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt.csv', delimiter=';')
    cs4n_2  = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_2.csv', delimiter=';')
    cs4n_3  = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_3.csv', delimiter=';')
    cs4n_4  = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_4.csv', delimiter=';')
    cs4n_5  = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_5.csv', delimiter=';')
    cs4n_6  = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_6.csv', delimiter=';')
    cs4n_7  = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_7.csv', delimiter=';')
    cs4n_8  = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_8.csv', delimiter=';')
    cs4n_9  = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_9.csv', delimiter=';')
    cs4n_10 = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_10.csv', delimiter=';')
    cs4n_11 = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_11.csv', delimiter=';')
    cs4n_12 = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_12.csv', delimiter=';')
    cs4n_13 = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_13.csv', delimiter=';')
    cs4n_14 = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt_14.csv', delimiter=';')
    

    cp4n    = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt.csv', delimiter=';')
    cp4n_2  = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_2.csv', delimiter=';')
    cp4n_3  = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_3.csv', delimiter=';')
    cp4n_4  = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_4.csv', delimiter=';')
    cp4n_5  = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_5.csv', delimiter=';')
    cp4n_6  = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_6.csv', delimiter=';')
    cp4n_7  = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_7.csv', delimiter=';')
    cp4n_8  = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_8.csv', delimiter=';')
    cp4n_9  = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_9.csv', delimiter=';')
    cp4n_10 = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_10.csv', delimiter=';')
    cp4n_11 = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_11.csv', delimiter=';')
    cp4n_12 = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_12.csv', delimiter=';')
    cp4n_13 = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_13.csv', delimiter=';')
    cp4n_14 = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt_14.csv', delimiter=';')

    shutil.copyfile("template.tex", "stress_test_boxplot_labnet.tex")
    f = open("stress_test_boxplot_labnet.tex", "a")


    f.write("\\begin{document}\n")
    f.write("\\begin{tikzpicture}\n")
    f.write("  \\pgfplotsset{\n")
    f.write("    /pgfplots/boxplot legend/.style={\n")
    f.write("    legend image code/.code={\n")
    f.write("      \draw [|-|,##1] (0,2mm) --\n")
    f.write("        node[rectangle,minimum size=2.5mm,draw,fill,##1]{}\n")
    f.write("        (0,7mm);\n")
    f.write("      }\n")
    f.write("    }\n")
    f.write("  }\n")

    f.write("  \\begin{axis} [\n")
    f.write("    boxplot/draw direction = y,\n")
    f.write("    ylabel={latency, ms},\n")
    f.write("    ymajorgrids=true,\n")
    f.write("    enlarge y limits,\n")
    f.write("    enlarge x limits=0.05,\n")
    f.write("    major x tick style = transparent,\n")
    f.write("    major y tick style = transparent,\n")
    f.write("    cycle list={{col1},{col2},{col3}},\n")
    f.write("    ymin=0.21,\n")
    f.write("    ymax=2.0,\n")
    f.write("    width=16cm,\n")
    f.write("    height=7cm,\n")
    f.write("    ytick={0,0.5,1,1.5,2},\n")
    f.write("    xtick={0,1,2,...,14},\n")
    f.write("    x tick label as interval,\n")
    f.write("    xticklabels={%\n")
    f.write("      {1},%\n")
    f.write("      {2},%\n")
    f.write("      {4},%\n")
    f.write("      {6},%\n")
    f.write("      {8},%\n")
    f.write("      {10},%\n")
    f.write("      {12},%\n")
    f.write("      {14},%\n")
    f.write("    },\n")
    f.write("    x tick label style={\n")
    f.write("      text width=2.5cm,\n")
    f.write("      align=center\n")
    f.write("    },\n")
    f.write("    boxplot={\n")
    f.write("      box extend=0.2\n")
    f.write("    },\n")
    f.write("    legend style={at={(0.85,0.95)}, anchor=north,legend columns=-1,draw=none},\n")
    f.write("    boxplot legend\n")
    f.write("  ]\n")
    f.write("  \\legend{C\\#,C++,Python}\n")

    lg = ["C#", "C++", "Python"]
    r4n = [cs4n, cp4n, p4n]
    pos = 0.25
    for q in zip(lg, r4n):
        f.write("  % Rv4, 1 test " + q[0] + "\n")
        f.write("  \\addplot+ [fill, draw=black,\n")
        f.write("  boxplot prepared={\n")
        f.write("    median=" + ff(q[1]["SetAndRead"].median()) + ",\n")
        f.write("    lower quartile=" + ff(q[1]["SetAndRead"].quantile(0.25)) + ",\n")
        f.write("    upper quartile=" + ff(q[1]["SetAndRead"].quantile(0.75)) + ",\n")
        f.write("    lower whisker=" + ff(q[1]["SetAndRead"].quantile(0.025)) + ",\n")
        f.write("    upper whisker=" + ff(q[1]["SetAndRead"].quantile(0.975)) + ",\n")
        f.write("    draw position=" + str(pos) + "\n")
        f.write("  },\n")
        f.write("  ] coordinates {};\n")
        f.write("\n")
        pos += 0.25

    r4n_2 = [cs4n_2, cp4n_2, p4n_2]
    pos += 0.25
    for q in zip(lg, r4n_2):
        f.write("  % Rv4, 2 test " + q[0] + "\n")
        f.write("  \\addplot+ [fill, draw=black,\n")
        f.write("  boxplot prepared={\n")
        f.write("    median=" + ff(q[1]["SetAndRead"].median()) + ",\n")
        f.write("    lower quartile=" + ff(q[1]["SetAndRead"].quantile(0.25)) + ",\n")
        f.write("    upper quartile=" + ff(q[1]["SetAndRead"].quantile(0.75)) + ",\n")
        f.write("    lower whisker=" + ff(q[1]["SetAndRead"].quantile(0.025)) + ",\n")
        f.write("    upper whisker=" + ff(q[1]["SetAndRead"].quantile(0.975)) + ",\n")
        f.write("    draw position=" + str(pos) + "\n")
        f.write("  },\n")
        f.write("  ] coordinates {};\n")
        f.write("\n")
        pos += 0.25

    r4n_4 = [cs4n_4, cp4n_4, p4n_4]
    pos += 0.25
    for q in zip(lg, r4n_4):
        f.write("  % Rv4, 4 test " + q[0] + "\n")
        f.write("  \\addplot+ [fill, draw=black,\n")
        f.write("  boxplot prepared={\n")
        f.write("    median=" + ff(q[1]["SetAndRead"].median()) + ",\n")
        f.write("    lower quartile=" + ff(q[1]["SetAndRead"].quantile(0.25)) + ",\n")
        f.write("    upper quartile=" + ff(q[1]["SetAndRead"].quantile(0.75)) + ",\n")
        f.write("    lower whisker=" + ff(q[1]["SetAndRead"].quantile(0.025)) + ",\n")
        f.write("    upper whisker=" + ff(q[1]["SetAndRead"].quantile(0.975)) + ",\n")
        f.write("    draw position=" + str(pos) + "\n")
        f.write("  },\n")
        f.write("  ] coordinates {};\n")
        f.write("\n")
        pos += 0.25

    r4n_6 = [cs4n_6, cp4n_6, p4n_6]
    pos += 0.25
    for q in zip(lg, r4n_6):
        f.write("  % Rv4, 6 test " + q[0] + "\n")
        f.write("  \\addplot+ [fill, draw=black,\n")
        f.write("  boxplot prepared={\n")
        f.write("    median=" + ff(q[1]["SetAndRead"].median()) + ",\n")
        f.write("    lower quartile=" + ff(q[1]["SetAndRead"].quantile(0.25)) + ",\n")
        f.write("    upper quartile=" + ff(q[1]["SetAndRead"].quantile(0.75)) + ",\n")
        f.write("    lower whisker=" + ff(q[1]["SetAndRead"].quantile(0.025)) + ",\n")
        f.write("    upper whisker=" + ff(q[1]["SetAndRead"].quantile(0.975)) + ",\n")
        f.write("    draw position=" + str(pos) + "\n")
        f.write("  },\n")
        f.write("  ] coordinates {};\n")
        f.write("\n")
        pos += 0.25

    r4n_8 = [cs4n_8, cp4n_8, p4n_8]
    pos += 0.25
    for q in zip(lg, r4n_8):
        f.write("  % Rv4, 8 test " + q[0] + "\n")
        f.write("  \\addplot+ [fill, draw=black,\n")
        f.write("  boxplot prepared={\n")
        f.write("    median=" + ff(q[1]["SetAndRead"].median()) + ",\n")
        f.write("    lower quartile=" + ff(q[1]["SetAndRead"].quantile(0.25)) + ",\n")
        f.write("    upper quartile=" + ff(q[1]["SetAndRead"].quantile(0.75)) + ",\n")
        f.write("    lower whisker=" + ff(q[1]["SetAndRead"].quantile(0.025)) + ",\n")
        f.write("    upper whisker=" + ff(q[1]["SetAndRead"].quantile(0.975)) + ",\n")
        f.write("    draw position=" + str(pos) + "\n")
        f.write("  },\n")
        f.write("  ] coordinates {};\n")
        f.write("\n")
        pos += 0.25

    r4n_10 = [cs4n_10, cp4n_10, p4n_10]
    pos += 0.25
    for q in zip(lg, r4n_10):
        f.write("  % Rv4, 10 test " + q[0] + "\n")
        f.write("  \\addplot+ [fill, draw=black,\n")
        f.write("  boxplot prepared={\n")
        f.write("    median=" + ff(q[1]["SetAndRead"].median()) + ",\n")
        f.write("    lower quartile=" + ff(q[1]["SetAndRead"].quantile(0.25)) + ",\n")
        f.write("    upper quartile=" + ff(q[1]["SetAndRead"].quantile(0.75)) + ",\n")
        f.write("    lower whisker=" + ff(q[1]["SetAndRead"].quantile(0.025)) + ",\n")
        f.write("    upper whisker=" + ff(q[1]["SetAndRead"].quantile(0.975)) + ",\n")
        f.write("    draw position=" + str(pos) + "\n")
        f.write("  },\n")
        f.write("  ] coordinates {};\n")
        f.write("\n")
        pos += 0.25

    r4n_12 = [cs4n_12, cp4n_12, p4n_12]
    pos += 0.25
    for q in zip(lg, r4n_12):
        f.write("  % Rv4, 12 test " + q[0] + "\n")
        f.write("  \\addplot+ [fill, draw=black,\n")
        f.write("  boxplot prepared={\n")
        f.write("    median=" + ff(q[1]["SetAndRead"].median()) + ",\n")
        f.write("    lower quartile=" + ff(q[1]["SetAndRead"].quantile(0.25)) + ",\n")
        f.write("    upper quartile=" + ff(q[1]["SetAndRead"].quantile(0.75)) + ",\n")
        f.write("    lower whisker=" + ff(q[1]["SetAndRead"].quantile(0.025)) + ",\n")
        f.write("    upper whisker=" + ff(q[1]["SetAndRead"].quantile(0.975)) + ",\n")
        f.write("    draw position=" + str(pos) + "\n")
        f.write("  },\n")
        f.write("  ] coordinates {};\n")
        f.write("\n")
        pos += 0.25
    
    r4n_14 = [cs4n_14, cp4n_14, p4n_14]
    pos += 0.25
    for q in zip(lg, r4n_14):
        f.write("  % Rv4, 14 test " + q[0] + "\n")
        f.write("  \\addplot+ [fill, draw=black,\n")
        f.write("  boxplot prepared={\n")
        f.write("    median=" + ff(q[1]["SetAndRead"].median()) + ",\n")
        f.write("    lower quartile=" + ff(q[1]["SetAndRead"].quantile(0.25)) + ",\n")
        f.write("    upper quartile=" + ff(q[1]["SetAndRead"].quantile(0.75)) + ",\n")
        f.write("    lower whisker=" + ff(q[1]["SetAndRead"].quantile(0.025)) + ",\n")
        f.write("    upper whisker=" + ff(q[1]["SetAndRead"].quantile(0.975)) + ",\n")
        f.write("    draw position=" + str(pos) + "\n")
        f.write("  },\n")
        f.write("  ] coordinates {};\n")
        f.write("\n")
        pos += 0.25

    f.write("\\end{axis}\n")
    f.write("\\end{tikzpicture}\n")
    f.write("\\end{document}\n")

