# -*- coding: utf-8 -*-
'''
Created on 6 abr. 2017

@author: cruce
'''

from gui.mainwindow import *
# Manejo numerico de datos
import numpy as np
#Funcion para pasar datos como si fueran un archivo de texto
from io import StringIO

from instruments import MultimetrosAgilent
from workers.loopdaq import daq_worker
from ploter.QtMatplotLibPlot import canvas
from ploter.QtMatplotLibPlot import NavigationToolbar
        
class JMCAGILENTDAQ (QtGui.QMainWindow, Ui_jmc_agilent_daq) :
    def __init__(self):
        #Inicializamos interfaz graica---------------------------
        QtGui.QMainWindow.__init__( self )
        self.setupUi(self)
        self.init_plot_figure()
        #Cargar configuracion por defecto.
        #self.load_available_devices()
        #self.connect_thread()
    def init_plot_figure(self):  
        # Generamos los planos donde graficaremos los datos------------------------
        # Inicializando base de ploteo para mainplot-------------------------------
        self.vbl_main = QtGui.QVBoxLayout( self.gb_daq_mainplot )
        self.maincanvas = canvas( self.gb_daq_mainplot )
        self.mainbar=NavigationToolbar(self.maincanvas,self.gb_daq_mainplot)
        self.vbl_main.insertWidget( 0, self.maincanvas )
        self.vbl_main.insertWidget( 1, self.mainbar) 
        #--------------------------------------------------------------------------  
    def connect_thread(self):
        # Configurar subproceso encargado de la adquisicion de datos    
        self.emit(QtCore.SIGNAL ( "splashUpdate(QString, int)" ), 'Conecting worker thread. . .', 132)    
        self.daq = daq_worker()
        self.thread=QtCore.QThread()
        self.thread.started.connect(self.daq.adquire)
        self.connect( self.daq, QtCore.SIGNAL ( "finished()" ), self.thread.quit )
        self.daq.moveToThread(self.thread)
        
        # Conectamos seniales de los threads con funciones de manejo de datos---------------
        self.connect( self.daq, QtCore.SIGNAL ( "readsignal(PyQt_PyObject)" ), self.show_data )
        
    def load_available_devices(self):
        self.emit(QtCore.SIGNAL ( "splashUpdate(QString, int)" ), 'Loading conected devices . . .', 132)
        resources_list = MultimetrosAgilent.list_agilent_multimeters()
        i = self.cbx_input_device.count()
        while -1 < i:
            # Si hay algun item en el combobox removerlo
            self.cbx_input_device.removeItem(i)
            i -= 1 
        for inst in resources_list:
            self.cbx_input_device.addItem(inst[1],str (inst[0]))
            
        if len(resources_list) == 0:
            self.pb_start.setEnabled(False)
            self.statusbar.showMessage('ERROR: Please check the conection and power on the device',5000)
        else:
            self.pb_start.setEnabled(True)

            
    def init_device(self, multimeter):
        s=StringIO(self.pte_config_lines.toPlainText())
        for line in s.readlines():
            if line != '':
                
                if line[0]=='W':
                    time.sleep(float(line.replace('W','')))
                else:
                    multimeter.dev.write(line)
                time.sleep(0.1)
            
    @QtCore.pyqtSlot ()
    def show_data(self,data):
        if self.daq.mode=='monitor':
            self.lcd_current_value.display(str('{0:f}'.format(float(data[1]))))
        elif self.daq.mode=='datalog':
            
            self.lcd_current_value.display(str('{0:f}'.format(float(data[1]))))
            
            f = open( self.le_output_file.text() + '.txt' )
            s = StringIO( f.read() )
            f.close()
            s.seek( 0 )

            x,y = np.genfromtxt( s,
                                       usecols = ( 0, 1),
                                       deletechars = "\n",
                                       dtype = float,
#                                        comment='%',
                                       autostrip = True,
                                       unpack = True )
            
                        # Ploteando en los canvas ya definidos con las funciones heredadas de la clase canvas
            # Deformacion en funcion de temperatura
            self.maincanvas.axes.cla()
            self.maincanvas.axes.grid( True )
            self.statusbar.showMessage( 'Ploteando principal...' )
            #self.maincanvas.axes.set_xlim( self.sb_xmin.value(), self.sb_xmax.value() )
            #self.maincanvas.axes.set_ylim( self.sb_ymin.value(), self.sb_ymax.value() )
            self.maincanvas.axes.plot( x, y, 'og' )
            self.maincanvas.fig.canvas.draw()
    
    @QtCore.pyqtSlot ()
    def on_pb_start_pressed(self):
        
        if self.pb_start.text()=='Start':
            
            self.pb_start.setEnabled(False)
            self.disable_controls()
            
            multimeter= MultimetrosAgilent.AG344XXA(str(self.cbx_input_device.itemData(self.cbx_input_device.currentIndex()).toString()))
            
            self.init_device(multimeter)
            
            if self.le_output_file.text() == '':
                self.daq.adquire(multimeter,None, int (self.sb_data_per_second.value()), 'monitor' )
                
            else:
                self.daq.adquire(multimeter, str(self.le_output_file.text()), int(self.sb_data_per_second.value()), 'datalog' )
            
            if self.daq.isRunning():
                self.pb_start.setText('Stop')
                self.pb_start.setEnabled(True)
                
        elif self.pb_start.text() == 'Stop':
            self.pb_start.setEnabled(False)
            
            self.daq.exiting=True
            while not self.daq.isFinished():
                continue
            #time.sleep(1)
            #self.daq.terminate()
            self.connect_thread()
            self.pb_start.setText('Start')
            self.enable_controls()
            self.pb_start.setEnabled(True)
            
                
                
    @QtCore.pyqtSlot()
    def on_tlb_load_devices_pressed(self):
        self.load_available_devices()     
        
    @QtCore.pyqtSlot ()
    def on_pb_save_multimeter_config_pressed(self):
        cfg_filename=str (QtGui.QFileDialog.getSaveFileName( parent = None, 
                                                        caption= 'Select Config Multimeter File',
                                                        directory=os.path.expanduser('~') ))
         

        
        text = self.pte_config_lines.toPlainText() 
        f = open(cfg_filename, 'w')
        f.write(text)
        f.close()
        
    @QtCore.pyqtSlot ()
    def on_pb_load_multimeter_config_pressed(self):
        cfg_multimeter= (QtGui.QFileDialog.getOpenFileName(None, 'Load Config Multimeter File',
                                                            directory=os.path.expanduser('~')) )
        
        f = open( cfg_multimeter,'r' )
        s = StringIO( f.read() )
        f.close()
        s.seek( 0 )
        self.pte_config_lines.clear()
        for line in s.readlines():
            self.pte_config_lines.appendPlainText(line.replace('\n','')) 
            
        
        
    def on_tlb_output_file_pressed(self):
        ofile=os.path.splitext(str(QtGui.QFileDialog.getSaveFileName(self, caption='Seleccionar archivo de salida',
                                                                        directory=os.path.expanduser('~'))))[0]
        self.le_output_file.setText(ofile)

def SplashMouseEvent (event):
    pass      
    
def main():
    app = QtGui.QApplication( sys.argv )
    # Create a pixmap - not needed if you have your own.
    from gui.splash import SplashScreen
    pixmap = QtGui.QPixmap('./gui/images/splash.png')
    splash = SplashScreen(pixmap)
    splash.setTitle('Agilent DAQ')
    splash.show()
    app.processEvents()
    DAQ = JMCAGILENTDAQ()
    splash.connect(DAQ, QtCore.SIGNAL('splashUpdate(QString, int)'), splash.showMessage)
    DAQ.load_available_devices()
    DAQ.connect_thread()
    DAQ.show()
    splash.finish(DAQ)
    sys.exit( app.exec_() )
    
if __name__ == '__main__':
    main()