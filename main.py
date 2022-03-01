import zipfile
import perf_test_boxplot_id
import latex_table_stats
import perf_tests_boxplot_set
import perf_tests_boxplot_set_read
import perf_tests_mean_set_read
import latencies_chart

# unzip the data
with zipfile.ZipFile("data.zip", 'r') as zip_ref:
    zip_ref.extractall("data")

# create the data summary table
latex_table_stats.create_summary_table()

# use template.tex to create the boxplot latex file for the id test
perf_test_boxplot_id.create_tex_file()

# use template.tex to create the boxplot latex file for the set test
perf_tests_boxplot_set.create_tex_file()

# use template.tex to create the boxplot latex file for the "set and read" test
perf_tests_boxplot_set_read.create_tex_file()

# use template.tex to create the bar plot latex file for the "set and read" test
perf_tests_mean_set_read.create_tex_file()

# use template.tex to create the bar plot latex file with latencies
latencies_chart.create_tex_file()