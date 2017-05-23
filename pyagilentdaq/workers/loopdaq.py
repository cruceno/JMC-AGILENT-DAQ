'''
Created on 13 abr. 2017

@author: javit
'''
from PyQt4.QtCore import QThread
from time import time, sleep

class daq_worker(QThread):
    def __init__(self):
        super(daq_worker,self).__init__()
        self.exiting=False
        self.mode=None
        
    def adquire(self,
                multimeter, 
                output_file, 
                data_per_second,
                mode):
        
        if not self.isRunning():
            self.mode=mode
            self.multimeter=multimeter

            if self.mode=='datalog':
                if data_per_second>0:
                    self.delay=1/data_per_second
                else:
                    self.delay=0
                self.output=output_file+'.txt'
                self.start()
                
            if self.mode=='monitor':
                if data_per_second>0:
                    self.delay=1/data_per_second
                else:
                    self.delay=0
                self.start()
            
    def run (self):
        if self.mode=='datalog':
            
            fsock=open(self.output, 'w')
            fsock.close()
            x_zero= time()
        
            while not self.exiting:

                y_value = self.multimeter.dev.query('READ?')
                x_value = time()-x_zero
                data=[x_value, y_value]
                
                fsock=open(self.output, 'a')
                line = str(x_value)+'\t'+str (y_value)+'\n'
                fsock.write(line)
                fsock.close()
                
                self.emit( QtCore.SIGNAL ( "readsignal(PyQt_PyObject)" ), data )
                sleep(self.delay)
                
            self.exit()
            
        elif self.mode=='monitor':
            
            while not self.exiting:
                
                y_value = self.multimeter.dev.query('READ?')
                data=[False, y_value]
                
                self.emit( QtCore.SIGNAL ( "readsignal(PyQt_PyObject)" ), data )
                sleep(self.delay)
                
            self.exit()