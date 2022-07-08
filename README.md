This repository contains data and analysis code for the manuscript:

LabNet: hardware control software for the Raspberry Pi

Data also contains the testing scripts for Autopilot, Bpod and pyControl.

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