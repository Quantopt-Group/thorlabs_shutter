# thorlabs_shutter
python script to control the Thorlabs SC10 shutter controller

once it works it can be turned into a widget to be able to be incorporated in the python gui


# end of the day it worked very straightforwardly by using pyVisa:
https://pyvisa.readthedocs.io/en/latest/introduction/communication.html
https://lampz.tugraz.at/~hadley/num/ch9/python/9.2.php

I only implemented the initial query and turn on/off function though


# initialy I had used code from the following links which I then deleted

https://github.com/hebecked/PyDAQ/blob/master/bin/rotational_stage/old/instruments/thorlabs/sc10.py

and 

https://instrumentkit.readthedocs.io/en/latest/_modules/instruments/thorlabs/sc10.html

# packages required:

quantities:
pip install quantities

flufl.enum:
pip install flufl.enum


