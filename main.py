import zipfile
import perf_tests_boxplot_set
import perf_tests_boxplot_read_set
import perf_tests_mean_read_set
import stress_test_boxplot_labnet
import latencies_chart

# unzip the data
with zipfile.ZipFile("data.zip", 'r') as zip_ref:
    zip_ref.extractall("data")

# use template.tex to create the boxplot latex file for the set test
perf_tests_boxplot_set.create_tex_file()

# use template.tex to create the boxplot latex file for the "set and read" test
perf_tests_boxplot_read_set.create_tex_file()

# use template.tex to create the bar plot latex file for the "set and read" test
perf_tests_mean_read_set.create_tex_file()

# create the box plot for the "stress test"
stress_test_boxplot_labnet.create_tex_file()

# use template.tex to create the bar plot latex file with latencies
latencies_chart.create_tex_file()