resultados.pdf : Resultados_hw2.tex PlotFourier1.pdf PlotTransFourier2.pdf PlotFourier3.pdf PlotFourier4.pdf specgram1.pdf specgram2.pdf specgramTemblor.pdf UF.pdf w9.pdf w37.pdf w57.pdf w46.pdf BONO.pdf
	pdflatex Resultados_hw2.tex
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
	python Fourier.py
UF.pdf : edificio.txt
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
BONO.pdf : BONO.txt
	python PlotsBONO_hw2.py 
BONO.txt : EdificioBONO.cpp b.out
	./b.out > BONO.txt
b.out : EdificioBONO.cpp
	g++ -o b.out EdificioBONO.cpp