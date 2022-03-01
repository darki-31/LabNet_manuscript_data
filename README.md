This repository contains data and analysis code for the manuscript:

LabNet: hardware control software for the Raspberry Pi

Call **main.py**. It will unzip the data.zip and creates all latex files.
Requirements are: numpy and pandas.

**latex_table_stats.py**
creates the latex summary table

**perf_test_boxplot_id.py**
generate [pgf-tikz](https://github.com/pgf-tikz/pgf) code for the boxplot chart of the "id test"

**perf_tests_boxplot_set.py**
generate [pgf-tikz](https://github.com/pgf-tikz/pgf) code for the boxplot chart of the "set test"

**perf_tests_boxplot_set_read.py**
generate [pgf-tikz](https://github.com/pgf-tikz/pgf) code for the boxplot chart of the "set and read test"

**perf_tests_mean_set_read.py**
generate [pgf-tikz](https://github.com/pgf-tikz/pgf) code for the bar chart of the "set and read test"