# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:34:57 2020

@author: snow_
"""

import numpy as np
import matplotlib.pyplot as plt


def cnt_yaxis(*ylist):
    """
    cnt ydata size and  sorting the data and ylabel and ranges 

    Parameters
    ----------
    *ylist : tuple
        data groups decribed
        
    Returns
    -------
    Data : dict
        Data array.
    ylabel : dict
        yaxis title array.
    ylim : dict
        yaxis limit 
        
    """
    #Set Counter
    cnt = 0
    
    Data = {}
    ylable = {}
    ylim = {}
    for i,yn in enumerate(ylist[0]): #need [0] to avoid error
        
        if i == 0:
            #first data must be Data
            Data[cnt] = yn
            continue
        elif isinstance(yn, str):
            #str data is legend
            ylable[cnt] = yn      
        elif len(yn) == 2:
            #word length equal 2 is yaxis limitation
            ylim[cnt] =yn
        else:
            cnt += 1 #cnt up before the data update 
            Data[cnt] = yn
            
    return Data,ylable,ylim
    
    
    
def make_figure_window(Windows_number):
    """
    make multi-matplotlib figure window

    Parameters
    ----------
    Windows_number : int
        Window number.

    Returns
    -------
    axes : figure axes
        it starts number 1 .ex axes[1] indicate Top of window. not axes[0]
        if return axes = 0, maybe windows_number is mistake.

    """
    plt.figure()
    
    #Error Check
    if Windows_number <= 0:
        print('Windows_number must be a greater than 0@make_figure_window')
        return 0
    
    #axes handle start from 1
    axes ={}
    for i in range(Windows_number):
        #share xlabel
        if i != 0:
            axes[i+1] = plt.subplot(Windows_number,1,i+1,sharex=axes[1])
        else:
            axes[i+1] = plt.subplot(Windows_number,1,i+1)

        #delete xtick
        if i != Windows_number -1:
            plt.setp(axes[i+1].get_xticklabels(), visible=False)
    
    return axes


def set_plot_data(Time,Data,legend,ylim,axes):
    """
    Set Plot Data for figure Windows
    ----------
    Time : Array of float 64
        Time series time data.
    Data : dict
        Data Group made by cnt_yaxis
    legend : dict
        legend group data made by cnt_yaxis.
    ylim : dict
        yaxis limitation group made by cnt_yaxis.
    axes : dict
        axes group made by make_figure_window.

    Returns
    -------
    None.Windos is renewable

    """
    #plot Data
    for i in Data.keys():
        axes[i+1].plot(Time,Data[i])

    #set legend
    for i in legend.keys():
        axes[i+1].set_ylabel(legend[i])

    #set legend
    for i in ylim.keys():
        axes[i+1].set_ylim(ylim[i])
        
    return
        
    
def time_plot(Time,*args):
    """
    Usage:   time_plot(Times,Data,[0,2.8],'hoge1',Data*2,Data*3,[0,1], \
              Data*4,'hoge4')
    it will be return a matplot window data.
    Parameters
    ----------
    Time : array
        Time Series Data
    *args : TYPE
        Datay1,legendy1,xlimy1.....

    Returns
    -------
    None.

    """
    Data,legend,ylim = cnt_yaxis(args)
    axes = make_figure_window(len(Data.keys()))
    set_plot_data(Time,Data,legend,ylim,axes)
        
    return
    

if __name__ == "__main__":

    #closefigure
    #plt.close('all')
    # How to Use this function
    Times = np.arange(0,1,0.001)
    Data = np.sin(2*np.pi*Times)
    
    #plot example
    time_plot(Times,Data,[0,2.8],'hoge1',Data*2,Data*3,[0,1], \
              Data*4,'hoge4')
    
    time_plot(Times,Data,[0,2.8],'hoge1',Data*2)
   
    