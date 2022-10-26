This repository contains data and analysis code for the manuscript:

LabNet hardware control software for the Raspberry Pi

data.zip contains latency measurements data for Autopilot, Bpod, pyControl and LabNet.

Call **main.py**. It will unzip the data.zip and creates all latex files.
Requirements are: numpy and pandas.

**perf_tests_boxplot_set.py**
generate [pgf-tikz](https://github.com/pgf-tikz/pgf) code for the boxplot chart of the "set test"

**perf_tests_boxplot_read_set.py**
generate [pgf-tikz](https://github.com/pgf-tikz/pgf) code for the boxplot chart of the "read and set test"

**perf_tests_mean_read_set.py**
generate [pgf-tikz](https://github.com/pgf-tikz/pgf) code for the bar chart of the "read and set test"

**stress_test_boxplot_labnet**
generate [pgf-tikz](https://github.com/pgf-tikz/pgf) code for the boxplot chart of the "stress test"

**latencies_chart.py**
generate [pgf-tikz](https://github.com/pgf-tikz/pgf) code for the bar chart for latencies

**read_set_timing.tex**
Timing diagram for latency measurements in "read and set" and "stress" test.

**systems.tex**
Figure 1 from paper.

**perf_images.tex**
Figure 2 from paper. It combines "perf_tests_boxplot_set", "perf_tests_boxplot_read_set", "perf_tests_mean_read_set" and "stress_test_boxplot_labnet" into one figure.

**software.tex**
Figure 3 from paper.

**latencies.tex**
Figure 3 from paper. It combines "latencies_chart" and "read_set_timing" into one figure.

**exp_system.tex**
Figure 4 from paper. Touchscreen system with sorter.