#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a module which contains classes for obtaining values used in a bokeh
plot.
@author: amberkiser
"""
#import pandas as pd

class VpdPlot(object):
    """
    This class creates an object that can be used in a bokeh plot for a
    specific disease incidence rate. The plot should describe the incidence
    rate of vaccine-preventable diseases in the US for each year.

    Attributes:
        data = pandas dataframe of values; columns should include Year and
        rate for a specific disease

        x_values = values used in the x axis of the plot; should be a list of
            Years

        y_values = values used in the y axis of the plot; should be a list of
            incidence rates

        color = color of the line in the plot
            can include:
                any of the 147 named CSS colors
                RGB(A) hex value
                3-tuple of (r,g,b)
                4-tuple of (r,g,b,a)

        disease = specific disease of interest
    """
    def __init__(self, df, color, disease):
        self.data = (df, disease)
        self.x_values = (df, disease)
        self.y_values = (df, disease)
        self.disease = disease
        self.color = color

    @property
    def data(self):
        """
        defines data attribute
        """
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = make_new_df(value)

    @property
    def x_values(self):
        """
        defines x_values attribute
        """
        return self.__x_values
    @x_values.setter
    def x_values(self, value):
        new_df = make_new_df(value)
        self.__x_values = list(new_df['year'])

    @property
    def y_values(self):
        """
        defines y_values attribute
        """
        return self.__y_values
    @y_values.setter
    def y_values(self, value):
        new_df = make_new_df(value)
        self.__y_values = list(new_df['incidence_rate'])

    @property
    def disease(self):
        """
        defines disease attribute
        """
        return self.__disease
    @disease.setter
    def disease(self, value):
        self.__disease = value

    @property
    def color(self):
        """
        defines color attribute
        """
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        """
        When printing a VpdPlot object, the first 5 lines of data along with
        color specified for the line will appear.
        """
        return str(self.data.head()) + '\n Line color: ' + self.color


# Helper methods for classes
def make_new_df(value):
    """
    This method creates a new dataframe given a tuple.

    input:
        value = tuple of (df, vaccine)

    returns pandas dataframe
    """
    temp = value[0]
    vpd = value[1]
    new_df = temp[temp['disease'] == vpd]
    new_df = new_df.sort_values(by='year')
    return new_df
