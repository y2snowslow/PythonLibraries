# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:34:57 2020

@author: snow_
"""

import numpy as np
import matplotlib.pyplot as plt


def __cnt_yaxis(*ylist):
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
        elif len(yn) == 2 and len(np.shape(yn)) == 1:
            #word length equal 2 and yn is 1D list  equal yaxis limitation
            ylim[cnt] =yn
        else:
            #if is not yn str and not len != 2, it is data.
            cnt += 1 #cnt up before the data update 
            Data[cnt] = yn
            
    return Data,ylable,ylim
    
    
    
def __make_figure_window(Windows_number):
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
    plt.figure(figsize=(12.8, 10))
    
    #Default Fontsize Setting
    plt.rcParams['font.size'] = 18
    
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


def __set_plot_data(Time,Data,legend,ylim,axes):
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
        temp_data = Data[i]
        if len(temp_data) == 1 \
            or not isinstance(temp_data,list):
            axes[i+1].plot(Time,Data[i])
        else:
            for j,x in enumerate(temp_data):
                axes[i+1].plot(Time,x)
                
    #set legend
    for i in legend.keys():
        axes[i+1].set_ylabel(legend[i],fontname="MS Gothic")

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
    Data,legend,ylim = __cnt_yaxis(args)
    axes = __make_figure_window(len(Data.keys()))
    __set_plot_data(Time,Data,legend,ylim,axes)
        
    return
    

if __name__ == "__main__":

    #closefigure
    plt.close('all')
    # How to Use this function
    Times = np.arange(0,1,0.001)
    Data = np.sin(2*np.pi*Times)
    
    #plot example
    time_plot(Times,[Data,Data*5,Data*10],[-10,10],'日本語',[Data*2,Data*0.5],Data*3,[0,1], \
              Data,'hoge4')
    
    #time_plot(Times,Data,[-5,5],'hoge1',Data*2)
   
    