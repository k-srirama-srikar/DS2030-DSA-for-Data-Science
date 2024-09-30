set title "Sort comparison"
set xlabel "n"
set ylabel "t(n)"
plot "merge_times.data" with lines, "insertion_times.data" with lines
