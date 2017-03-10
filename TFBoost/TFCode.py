"""
Author: @gabvaztor
StartDate: 04/03/2017

This file contains the next information:
    - Libraries to import with installation comment and reason.
    - Data Mining Algorithm.
    - Sets (train,validation and test) information.
    - ANN Arquitectures.
    - A lot of utils methods which you'll get useful advantage


The code's structure is:
    - Imports
    - Interface
    - Reading data algorithms
    - Data Mining
    - Training and test
    - Show final conclusions

Notes:
    * This file use TensorFlow code version 1.0.
"""

"""
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# IMPORTS
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
"""
# --------------------------------------------------------------------------
'''LOCAL IMPORTS
* UtilsFunctions is a library that contains a lot of functions which will help us
to code expressively, clearly and efficiently.
* TensorFlowGUI's library contains all GUI's methods. Contains EasyGUI.
Here you can download the library: https://pypi.python.org/pypi/easygui#downloads
It had been used the version: 0.98.1
'''

import UsefulTools.UtilsFunctions as uf
import TFBoost.TFEasyGui as eg
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
''' TensorFlow: https://www.tensorflow.org/
To upgrade tensorflow to last version:
*CPU: pip3 install --upgrade tensorflow
*GPU: pip3 install --upgrade tensorflow-gpu
'''
import tensorflow as tf
print("TensorFlow: " + tf.__version__)
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
''' Numpy is an extension to the Python programming language, adding support for large,
multi-dimensional arrays and matrices, along with a large library of high-level
mathematical functions to operate on these arrays.
It is mandatory to install 'Numpy+MKL' before scipy.
Install 'Numpy+MKL' from here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
http://www.numpy.org/
https://en.wikipedia.org/wiki/NumPy '''
import numpy as np
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
'''
# You need to install the 64bit version of Scipy, at least on Windows.
# It is mandatory to install 'Numpy+MKL' before scipy.
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
# We can find scipi in the url: http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy'''
import scipy.io as sio
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
'''# Matlab URL: http://matplotlib.org/users/installing.html'''
import matplotlib.pyplot as plt
# --------------------------------------------------------------------------

"""
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# ---- USER INTERFACE ----
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
"""

'''Creating user interface'''
properties = eg.EasyGui()
uf.pt("Typos GUI",properties.types)



"""
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# ---- READING DATA ----
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
"""




"""
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# ---- Inicio de Sesión de TensorFlow ----
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
"""
init = tf.global_variables_initializer()
sess = tf.InteractiveSession()
sess.run(init)