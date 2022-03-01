import numpy as np
import pandas as pd
import shutil

def create_tex_file():
    # float numbers f.write format
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

    shutil.copyfile("template.tex", "perf_tests_boxplot_set_read.tex")
    f = open("perf_tests_boxplot_set_read.tex", "a")


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
    #f.write("    ylabel={latency, ms},\n")
    f.write("    ymajorgrids=true,\n")
    f.write("    enlarge y limits,\n")
    f.write("    enlarge x limits=0.05,\n")
    f.write("    major x tick style = transparent,\n")
    f.write("    major y tick style = transparent,\n")
    f.write("    cycle list={{col1},{col2},{col3}},\n")
    f.write("    ymin=0.21,\n")
    f.write("    ymax=2.0,\n")
    f.write("    width=14cm,\n")
    f.write("    height=7cm,\n")
    f.write("    ytick={0,0.5,1,1.5,2},\n")
    f.write("    xtick={0,1,2,...,10},\n")
    f.write("    x tick label as interval,\n")
    f.write("    xticklabels={%\n")
    f.write("      {Rv2},%\n")
    f.write("      {Rv3},%\n")
    f.write("      {Rv4},%\n")
    f.write("      {Rv2\\\\{\\scriptsize optimized}},%\n")
    f.write("      {Rv3\\\\{\\scriptsize optimized}},%\n")
    f.write("      {Rv4\\\\{\\scriptsize optimized}},%\n")
    f.write("      {Rv4\\\\{\\scriptsize 1kHz}},%\n")
    f.write("      {Rv4\\\\{\\scriptsize max}},%\n")
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
    r2n = [cs2n, cp2n, p2n]
    pos = 0.25
    for q in zip(lg, r2n):
        f.write("  % Rv2 " + q[0] + "\n")
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

    r3n = [cs3n, cp3n, p3n]
    pos += 0.25
    for q in zip(lg, r3n):
        f.write("  % Rv3 " + q[0] + "\n")
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

    r4n = [cs4n, cp4n, p4n]
    pos += 0.25
    for q in zip(lg, r4n):
        f.write("  % Rv4 " + q[0] + "\n")
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


    #opt
    r2o = [cs2o, cp2o, p2o]
    pos += 0.25
    for q in zip(lg, r2o):
        f.write("  % Rv2 opt " + q[0] + "\n")
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

    r3o = [cs3o, cp3o, p3o]
    pos += 0.25
    for q in zip(lg, r3o):
        f.write("  % Rv3 opt " + q[0] + "\n")
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

    r4o = [cs4o, cp4o, p4o]
    pos += 0.25
    for q in zip(lg, r4o):
        f.write("  % Rv4 opt " + q[0] + "\n")
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

    #poll
    r2o = [cs4_1, cp4_1, p4_1]
    pos += 0.25
    for q in zip(lg, r2o):
        f.write("  % Rv4 1kHz " + q[0] + "\n")
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

    r2o = [cs4_max, cp4_max, p4_max]
    pos += 0.25
    for q in zip(lg, r2o):
        f.write("  % Rv4 max " + q[0] + "\n")
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