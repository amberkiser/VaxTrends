#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a module which contains classes for obtaining values used in a bokeh
plot.
@author: amberkiser
"""
import pandas as pd

class AllPlot(object):
    """
    This class creates an object that can be used in a bokeh plot, including
    all vaccines. The plot should describe the vaccine coverage in the US for
    each year.

    Attributes:
        data = pandas dataframe of values; columns should include Year and
        Coverage

        x_values = values used in the x axis of the plot; should be a list of
            Years

        y_values = values used in the y axis of the plot; should be a list of
            rates of coverage

        color = color of the line in the plot
            can include:
                any of the 147 named CSS colors
                RGB(A) hex value
                3-tuple of (r,g,b)
                4-tuple of (r,g,b,a)
    """
    def __init__(self, df, color):
        self.data = (df, 'All')
        self.color = color
        self.x_values = (df, 'All')
        self.y_values = (df, 'All')

    @property
    def data(self):
        """
        defines data attribute
        """
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value[0]

    @property
    def color(self):
        """
        defines color attribute
        """
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def x_values(self):
        """
        defines x_values attribute
        """
        return self.__x_values
    @x_values.setter
    def x_values(self, value):
        data_frame = value[0]
        self.__x_values = list(data_frame['year'])

    @property
    def y_values(self):
        """
        defines y_values attribute
        """
        return self.__y_values
    @y_values.setter
    def y_values(self, value):
        data_frame = value[0]
        self.__y_values = list(data_frame['coverage'])

    def __str__(self):
        """
        When printing an AllPlot object, the first 5 lines of data along with
        color specified for the line will appear.
        """
        return str(self.data.head()) + '\n Line color: ' + self.color

class VaxPlot(AllPlot):
    """
    This class creates an object that can be used in a bokeh plot for a
    specific vaccine. The plot should describe the vaccine coverage in the US
    for each year.

    Attributes:
        data = pandas dataframe of values; columns should include Year and
        Coverage for the specific vaccine

        x_values = values used in the x axis of the plot; should be a list of
            Years

        y_values = values used in the y axis of the plot; should be a list of
            rates of coverage

        color = color of the line in the plot
            can include:
                any of the 147 named CSS colors
                RGB(A) hex value
                3-tuple of (r,g,b)
                4-tuple of (r,g,b,a)

        vaccine = the specific vaccine of interest

        shadex_values = list of values used in the xaxis when plotting the
        confidence intervals

        shadey_values = list of confidence interval values

        shade_color = color of the confidence interval band

        shade_alpha = transparency of the confidence interval band
    """
    def __init__(self, df, color, vaccine, shade_color, shade_alpha):
        super(VaxPlot, self).__init__(df, color)
        self.data = (df, vaccine)
        self.x_values = (df, vaccine)
        self.y_values = (df, vaccine)
        self.vaccine = vaccine
        self.shadex_values = (df, vaccine)
        self.shadey_values = (df, vaccine)
        self.shade_color = shade_color
        self.shade_alpha = shade_alpha

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
        self.__y_values = list(new_df['coverage'])

    @property
    def vaccine(self):
        """
        defines vaccine attribute
        """
        return self.__vaccine
    @vaccine.setter
    def vaccine(self, value):
        self.__vaccine = value

    @property
    def shadex_values(self):
        """
        defines shadex attribute
        """
        return self.__shadex_values
    @shadex_values.setter
    def shadex_values(self, value):
        shade = make_shade_df(value)
        self.__shadex_values = list(shade['year'])

    @property
    def shadey_values(self):
        """
        defines shadey attribute
        """
        return self.__shadey_values
    @shadey_values.setter
    def shadey_values(self, value):
        shade = make_shade_df(value)
        self.__shadey_values = list(shade['CI'])

    @property
    def shade_color(self):
        """
        defines shade color attribute
        """
        return self.__shade_color
    @shade_color.setter
    def shade_color(self, value):
        self.__shade_color = value

    @property
    def shade_alpha(self):
        """
        defines shade alpha attribute
        """
        return self.__shade_alpha
    @shade_alpha.setter
    def shade_alpha(self, value):
        self.__shade_alpha = value


# Helper methods for classes
def make_new_df(value):
    """
    This method creates a new dataframe given a tuple.

    input:
        value = tuple of (df, vaccine)

    returns pandas dataframe
    """
    temp = value[0]
    vax = value[1]
    return temp[temp['vaccine'] == vax]

def make_shade_df(value):
    """
    This method creates the dataframe required to show the CI on the graph
    with the background shaded.
    The dataframe will consist of the upper and lower confidence intervals for
    each year.

    input:
        value = tuple of (df, vaccine)

    returns pandas dataframe
    """
    new_df = make_new_df(value)
    lower = new_df[['year', 'ci_lower']].rename(index=str, columns=
                                                {'ci_lower':'CI'})
    upper = new_df[['year', 'ci_upper']].rename(index=str, columns=
                                                {'ci_upper':'CI'}).sort_values(
                                                    'year', ascending=False)
    return pd.concat([lower, upper])
