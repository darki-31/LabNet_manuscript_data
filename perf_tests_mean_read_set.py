import numpy as np
import pandas as pd
import shutil


def create_tex_file():
    # float numbers f.write format
    ff = "{:.2f}".format

    # read all files
    p2n    = pd.read_csv('data/read_and_set_test/LabNet/python_r2_no_opt.csv', delimiter=';')
    p2o    = pd.read_csv('data/read_and_set_test/LabNet/python_r2_opt.csv', delimiter=';')
    p3n    = pd.read_csv('data/read_and_set_test/LabNet/python_r3_no_opt.csv', delimiter=';')
    p3o    = pd.read_csv('data/read_and_set_test/LabNet/python_r3_opt.csv', delimiter=';')
    p4n    = pd.read_csv('data/read_and_set_test/LabNet/python_r4_no_opt.csv', delimiter=';')
    p4o    = pd.read_csv('data/read_and_set_test/LabNet/python_r4_opt.csv', delimiter=';')
    p4_1   = pd.read_csv('data/read_and_set_test/LabNet/python_r4_1kHz.csv', delimiter=';')
    p4_max = pd.read_csv('data/read_and_set_test/LabNet/python_r4_max.csv', delimiter=';')

    cs2n    = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r2_no_opt.csv', delimiter=';')
    cs2o    = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r2_opt.csv', delimiter=';')
    cs3n    = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r3_no_opt.csv', delimiter=';')
    cs3o    = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r3_opt.csv', delimiter=';')
    cs4n    = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_no_opt.csv', delimiter=';')
    cs4o    = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_opt.csv', delimiter=';')
    cs4_1   = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_1kHz.csv', delimiter=';')
    cs4_max = pd.read_csv('data/read_and_set_test/LabNet/c_sharp_r4_max.csv', delimiter=';')

    cp2n    = pd.read_csv('data/read_and_set_test/LabNet/cpp_r2_no_opt.csv', delimiter=';')
    cp2o    = pd.read_csv('data/read_and_set_test/LabNet/cpp_r2_opt.csv', delimiter=';')
    cp3n    = pd.read_csv('data/read_and_set_test/LabNet/cpp_r3_no_opt.csv', delimiter=';')
    cp3o    = pd.read_csv('data/read_and_set_test/LabNet/cpp_r3_opt.csv', delimiter=';')
    cp4n    = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_no_opt.csv', delimiter=';')
    cp4o    = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_opt.csv', delimiter=';')
    cp4_1   = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_1kHz.csv', delimiter=';')
    cp4_max = pd.read_csv('data/read_and_set_test/LabNet/cpp_r4_max.csv', delimiter=';')

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

    shutil.copyfile("template.tex", "perf_tests_mean_read_set.tex")
    f = open("perf_tests_mean_read_set.tex", "a")

    f.write("\pgfplotstableread{\n")
    f.write("a   cs   cp   py   st1  st2  st3\n")
    f.write("Rv2 " + r2n + "\n")
    f.write("Rv3 " + r3n + "\n")
    f.write("Rv4 " + r4n + "\n")
    f.write("Rv2o " + r2o + "\n")
    f.write("Rv3o " + r3o + "\n")
    f.write("Rv4o " + r4o + "\n")
    f.write("Rv41 " + r41 + "\n")
    f.write("Rv4m " + r4m + "\n")
    f.write("}\mytable\n")

    f.write("\\begin{document}\n")
    f.write("    \\begin{tikzpicture}\n")
    f.write("        \pgfplotsset{compat=1.11,\n")
    f.write("            /pgfplots/ybar legend/.style={\n")
    f.write("            /pgfplots/legend image code/.code={\n")
    f.write("            \draw[##1,/tikz/.cd,yshift=-0.25em]\n")
    f.write("                    (0cm,0cm) rectangle (3pt,0.8em);},\n")
    f.write("            %\draw[##1,/tikz/.cd,bar width=5pt,yshift=-0.2em,bar shift=0pt]\n")
    f.write("                    %plot coordinates {(0cm,0.8em)};},\n")
    f.write("            },\n")
    f.write("        }\n")
    f.write("\n")
    f.write("        \\begin{axis}[\n")
    f.write("            %scale only axis,\n")
    f.write("            %nodes near coords={\pgfmathprintnumber\pgfplotspointmeta},\n")
    f.write("            %every node near coord/.append style={xshift=0pt,yshift=0pt, red, font=\scriptsize},\n")
    f.write("            ybar,\n")
    f.write("            %title=set and read gpio (mean with std dev),\n")
    f.write("            enlarge x limits=0.1,\n")
    f.write("            %ylabel={latency, ms},\n")
    f.write("            ymajorgrids=true,\n")
    f.write("            %compat=newest,\n")
    f.write("            major x tick style = transparent,\n")
    f.write("            major y tick style = transparent,\n")
    f.write("            %axis on top,\n")
    f.write("            xtick align=inside,\n")
    f.write("            ytick align=inside,\n")
    f.write("            ytick={0.5,1,1.5,2},\n")
    f.write("            symbolic x coords={Rv2,Rv3,Rv4,Rv2o,Rv3o,Rv4o,Rv41,Rv4m},\n")
    f.write("            xtick = data,\n")
    f.write("            xticklabels={%\n")
    f.write("                {Rv2},%\n")
    f.write("                {Rv3},%\n")
    f.write("                {Rv4},%\n")
    f.write("                {Rv2\\\\{\scriptsize optimized}},%\n")
    f.write("                {Rv3\\\\{\scriptsize optimized}},%\n")
    f.write("                {Rv4\\\\{\scriptsize optimized}},%\n")
    f.write("                {Rv4\\\\{\scriptsize 1kHz}},%\n")
    f.write("                {Rv4\\\\{\scriptsize max}},%\n")
    f.write("            },\n")
    f.write("            x tick label style={\n")
    f.write("                text width=2.5cm,\n")
    f.write("                align=center\n")
    f.write("            },\n")
    f.write("            %x=2cm,\n")
    f.write("            %y=2.5cm,\n")
    f.write("            ymin=0,\n")
    f.write("            ymax=2.19,\n")
    f.write("            width=16cm,\n")
    f.write("            height=7cm,\n")
    f.write("            %enlarge x limits,\n")
    f.write("            %enlarge y limits,\n")
    f.write("            legend style={at={(0.867,0.95)}, anchor=north,legend columns=-1,draw=none},\n")
    f.write("            ]\n")
    f.write("            \legend{C\#,C++,Python}\n")
    f.write("\n")
    f.write("            \\addplot[draw = blue,\n")
    f.write("                fill = col1,\n")
    f.write("                draw=black,\n")
    f.write("                error bars/.cd,\n")
    f.write("                y dir=both, \n")
    f.write("                y explicit,\n")
    f.write("                error bar style={color=black}] table[x=a,y=cs,y error=st1] {\mytable};\n")
    f.write("\n")
    f.write("            \\addplot[draw = red,\n")
    f.write("                fill = col2, \n")
    f.write("                draw=black,\n")
    f.write("                error bars/.cd, \n")
    f.write("                y dir=both, \n")
    f.write("                y explicit,\n")
    f.write("                error bar style={color=black}] table[x=a,y=cp,y error=st2] {\mytable};\n")
    f.write("\n")
    f.write("            \\addplot[draw = brown,\n")
    f.write("                fill = col3, \n")
    f.write("                draw=black,\n")
    f.write("                error bars/.cd, \n")
    f.write("                y dir=both, \n")
    f.write("                y explicit,\n")
    f.write("                error bar style={color=black}] table[x=a,y=py,y error=st3] {\mytable};\n")
    f.write("\n")
    f.write("        \\end{axis}\n")
    f.write("    \\end{tikzpicture}\n")
    f.write("\\end{document}\n")
