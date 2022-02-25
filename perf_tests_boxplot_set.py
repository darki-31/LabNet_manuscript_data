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


print("\\begin{document}")
print("\\begin{tikzpicture}")
print("  \\pgfplotsset{")
print("    /pgfplots/boxplot legend/.style={")
print("    legend image code/.code={")
print("      \draw [|-|,##1] (0,2mm) --")
print("        node[rectangle,minimum size=2.5mm,draw,fill,##1]{}")
print("        (0,7mm);")
print("      }")
print("    }")
print("  }")

print("  \\begin{axis} [")
print("    boxplot/draw direction = y,")
print("    ylabel={latency, ms},")
print("    ymajorgrids=true,")
print("    enlarge y limits,")
print("    enlarge x limits=0.05,")
print("    major x tick style = transparent,")
print("    major y tick style = transparent,")
print("    cycle list={{col1},{col2},{col3}},")
print("    ymin=0.21,")
print("    ymax=2.0,")
print("    width=14cm,")
print("    height=7cm,")
print("    ytick={0,0.5,1,1.5,2},")
print("    xtick={0,1,2,...,10},")
print("    x tick label as interval,")
print("    xticklabels={%")
print("      {Rv2},%")
print("      {Rv3},%")
print("      {Rv4},%")
print("      {Rv2\\\\{\\scriptsize optimized}},%")
print("      {Rv3\\\\{\\scriptsize optimized}},%")
print("      {Rv4\\\\{\\scriptsize optimized}},%")
print("    },")
print("    x tick label style={")
print("      text width=2.5cm,")
print("      align=center")
print("    },")
print("    boxplot={")
print("      box extend=0.2")
print("    },")
print("    legend style={at={(0.85,0.95)}, anchor=north,legend columns=-1,draw=none},")
print("    boxplot legend")
print("  ]")
print("  \\legend{C\\#,C++,Python}")

lg = ["C#", "C++", "Python"]
r2n = [cs2n, cp2n, p2n]
pos = 0.25
for q in zip(lg, r2n):
    print("  % Rv2 " + q[0])
    print("  \\addplot+ [fill, draw=black,")
    print("  boxplot prepared={")
    print("    median=" + ff(q[1]["SetTest"].median()) + ",")
    print("    lower quartile=" + ff(q[1]["SetTest"].quantile(0.25)) + ",")
    print("    upper quartile=" + ff(q[1]["SetTest"].quantile(0.75)) + ",")
    print("    lower whisker=" + ff(q[1]["SetTest"].quantile(0.025)) + ",")
    print("    upper whisker=" + ff(q[1]["SetTest"].quantile(0.975)) + ",")
    print("    draw position=" + str(pos))
    print("  },")
    print("  ] coordinates {};")
    print("")
    pos += 0.25

r3n = [cs3n, cp3n, p3n]
pos += 0.25
for q in zip(lg, r3n):
    print("  % Rv3 " + q[0])
    print("  \\addplot+ [fill, draw=black,")
    print("  boxplot prepared={")
    print("    median=" + ff(q[1]["SetTest"].median()) + ",")
    print("    lower quartile=" + ff(q[1]["SetTest"].quantile(0.25)) + ",")
    print("    upper quartile=" + ff(q[1]["SetTest"].quantile(0.75)) + ",")
    print("    lower whisker=" + ff(q[1]["SetTest"].quantile(0.025)) + ",")
    print("    upper whisker=" + ff(q[1]["SetTest"].quantile(0.975)) + ",")
    print("    draw position=" + str(pos))
    print("  },")
    print("  ] coordinates {};")
    print("")
    pos += 0.25

r4n = [cs4n, cp4n, p4n]
pos += 0.25
for q in zip(lg, r4n):
    print("  % Rv4 " + q[0])
    print("  \\addplot+ [fill, draw=black,")
    print("  boxplot prepared={")
    print("    median=" + ff(q[1]["SetTest"].median()) + ",")
    print("    lower quartile=" + ff(q[1]["SetTest"].quantile(0.25)) + ",")
    print("    upper quartile=" + ff(q[1]["SetTest"].quantile(0.75)) + ",")
    print("    lower whisker=" + ff(q[1]["SetTest"].quantile(0.025)) + ",")
    print("    upper whisker=" + ff(q[1]["SetTest"].quantile(0.975)) + ",")
    print("    draw position=" + str(pos))
    print("  },")
    print("  ] coordinates {};")
    print("")
    pos += 0.25


#opt
r2o = [cs2o, cp2o, p2o]
pos += 0.25
for q in zip(lg, r2o):
    print("  % Rv2 opt " + q[0])
    print("  \\addplot+ [fill, draw=black,")
    print("  boxplot prepared={")
    print("    median=" + ff(q[1]["SetTest"].median()) + ",")
    print("    lower quartile=" + ff(q[1]["SetTest"].quantile(0.25)) + ",")
    print("    upper quartile=" + ff(q[1]["SetTest"].quantile(0.75)) + ",")
    print("    lower whisker=" + ff(q[1]["SetTest"].quantile(0.025)) + ",")
    print("    upper whisker=" + ff(q[1]["SetTest"].quantile(0.975)) + ",")
    print("    draw position=" + str(pos))
    print("  },")
    print("  ] coordinates {};")
    print("")
    pos += 0.25

r3o = [cs3o, cp3o, p3o]
pos += 0.25
for q in zip(lg, r3o):
    print("  % Rv3 opt " + q[0])
    print("  \\addplot+ [fill, draw=black,")
    print("  boxplot prepared={")
    print("    median=" + ff(q[1]["SetTest"].median()) + ",")
    print("    lower quartile=" + ff(q[1]["SetTest"].quantile(0.25)) + ",")
    print("    upper quartile=" + ff(q[1]["SetTest"].quantile(0.75)) + ",")
    print("    lower whisker=" + ff(q[1]["SetTest"].quantile(0.025)) + ",")
    print("    upper whisker=" + ff(q[1]["SetTest"].quantile(0.975)) + ",")
    print("    draw position=" + str(pos))
    print("  },")
    print("  ] coordinates {};")
    print("")
    pos += 0.25

r4o = [cs4o, cp4o, p4o]
pos += 0.25
for q in zip(lg, r4o):
    print("  % Rv4 opt " + q[0])
    print("  \\addplot+ [fill, draw=black,")
    print("  boxplot prepared={")
    print("    median=" + ff(q[1]["SetTest"].median()) + ",")
    print("    lower quartile=" + ff(q[1]["SetTest"].quantile(0.25)) + ",")
    print("    upper quartile=" + ff(q[1]["SetTest"].quantile(0.75)) + ",")
    print("    lower whisker=" + ff(q[1]["SetTest"].quantile(0.025)) + ",")
    print("    upper whisker=" + ff(q[1]["SetTest"].quantile(0.975)) + ",")
    print("    draw position=" + str(pos))
    print("  },")
    print("  ] coordinates {};")
    print("")
    pos += 0.25


print("\\end{axis}")
print("\\end{tikzpicture}")
print("\\end{document}")