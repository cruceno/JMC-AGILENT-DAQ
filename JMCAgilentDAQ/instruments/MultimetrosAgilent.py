# -*- coding: utf-8 -*-
'''
Created on 17/10/2013

@author: Cruceno Javier
    
'''
import visa
# Necesita NI-VISA instalado en el sistema. Ver documentacion PyVISA https://pyvisa.readthedocs.io
rm = visa.ResourceManager()

class AG344XXA():
    '''
    classdocs
    '''
    def __init__(self, address, model=None, id_number=None ):
        '''
        Constructor
        '''
        self.address = address
        self.dev =rm.open_resource(self.address, query_delay= 0.1)
        self.idn = self.dev.query('*IDN?')
        self.model = model if model else self.idn.split(',')[1]
        self.id_number =id_number if id_number else self.idn.split(',')[2]
        self.type='pyvisa'
        if self.model == '34410A':
            self.message=True
        else : 
            self.message=False
            
    def temperature_calibration(self, temp_data):
    #           Pasar de milivoltios a gracdos centigrado el valor leido por el multimetro
        # Polinomio para rango intermedio  -272 a 150 C

        if temp_data < 2: 
            
            Y = 25.39459 * temp_data 
            Y-= 0.44494 * temp_data ** 2 
            Y+= 0.05652 * temp_data ** 3 
            Y-= 0.00412 * temp_data ** 4 
            Y+= 0.0011 * temp_data ** 5 
            Y-= 1.39776E-4 * temp_data ** 6 
            Y+= 4.40583E-6 * temp_data ** 7 
            Y+= 7.709E-8 * temp_data ** 8
            
        #Polinomio para rango positivo 0 a 500 C     
        if temp_data >=2 :
            
            Y = 25.26032 * temp_data
            Y-= 0.57128 * temp_data ** 2
            Y+= 0.13393 * temp_data ** 3
            Y-= 0.01411 * temp_data ** 4
            Y+= 7.7329E-4 * temp_data ** 5
            Y-= 2.32438E-5 * temp_data ** 6
            Y+= 3.64924E-7 * temp_data ** 7
            Y-= 2.34283E-9 * temp_data ** 8
            
        return Y
    
def list_agilent_multimeters():
    lista= rm.list_resources()
    devices=[]
    for inst in lista:
        try: 
            device=rm.open_resource(inst)
            idn = device.query('*IDN?')
            device.close()
            multimeter=(inst, idn.split(',')[1], idn.split(',')[2] )
            devices.append(multimeter)  
        except: 
            continue
    return devices