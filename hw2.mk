resultados.pdf : resultados.tex PlotFourier1.pdf PlotTransFourier2.pdf PlotFourier3.pdf PlotFourier4.pdf specgram1.pdf specgram2.pdf specgramTemblor.pdf U_vs_freq.pdf w9.pdf w37.pdf w57.pdf w46.pdf
    pdflatex resultados.tex
PlotFourier1.pdf : signalSuma.dat signal.dat
    python Fourier.py
PlotTransFourier2.pdf : signalSuma.dat signal.dat
    python Fourier.py
PlotFourier3.pdf : temblor.txt
    python Fourier.py
PlotFourier4.pdf : temblor.txt
    python Fourier.py  
specgram1.pdf : signalSuma.dat signal.dat
    python Fourier.py
specgram2.pdf : signalSuma.dat signal.dat
    python Fourier.py
specgramTemblor.pdf : temblor.txt
U_vs_freq.pdf : edificio.txt
    python Plots_hw2.py
w9.pdf : edificio.txt
    python Plots_hw2.py
w37.pdf : edificio.txt
    python Plots_hw2.py 
w57.pdf : edificio.txt
    python Plots_hw2.py 
w46.pdf : edificio.txt
    python Plots_hw2.py 
edificio.txt : Edificio.cpp a.out
    ./a.out > edificio.txt
a.out : Edificio.cpp
    g++ Edificio.cpp