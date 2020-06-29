# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:54:10 2020

@author: atul.a.karkhanis
"""
import matplotlib.pyplot as plt
import numpy as np

#Define the range for the graph
wave_frequency=np.arange(0,8*np.pi,0.2)

#Sine graph
sine_graph = np.sin(wave_frequency)

#cosine graph
cosine_graph = np.cos(wave_frequency)

#Plot sine graph
plt.plot(wave_frequency,sine_graph)
plt.show()

#plot cosine_graph
plt.plot(wave_frequency,cosine_graph)
plt.show()


#Print both sine and cosine together
plt.plot(wave_frequency,sine_graph,wave_frequency,cosine_graph)
plt.show()
