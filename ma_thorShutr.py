# import pyvisa
#
# rm = pyvisa.ResourceManager()
# print(rm.list_resources())
# inst = rm.open_resource('ASRL3::INSTR')
# print(inst.query("id?\r"))
import time

import pyvisa as visa
import numpy as np


rm = visa.ResourceManager()
instruments = np.array(rm.list_resources())
print(instruments)

my_instrument = rm.open_resource('ASRL3::INSTR')
my_instrument.read_termination = '\r'
my_instrument.write_termination = '\r'
my_instrument.query('id?')
try:
    # my_instrument.write('id?')
    identity = my_instrument.read()
    print("Resource is" + str(my_instrument))
    print("instrument is: " + identity + '\n')
except visa.VisaIOError:
    print('No connection to: ' + str(my_instrument))

my_instrument.query('ens?')
shut_state = my_instrument.read()  # warning says read is not available but it does not work without it
print(shut_state)

my_instrument.query('ens')
# time.sleep(1)
my_instrument.query('ens?')
shut_state = my_instrument.read()  # warning says read is not available but it does not work without it
print(shut_state)

print("es el final")