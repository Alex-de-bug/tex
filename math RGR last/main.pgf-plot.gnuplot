set table "main.pgf-plot.table"; set format "%.5f"
set format "%.7e";; set samples 25; set dummy x; plot [x=-5:5] pi/2 + sum [n=1:3] 2/(pi * n**2) * ((-1)**n-1) * cos(n*x);
