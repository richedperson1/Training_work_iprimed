"""
Author : Vornoi Practitioners
   Group Captain  : Mrinal Bhardwaj
   Group Member 1 : Ankita R Desai
   Group Member 2 : Ashutosh Kumar Bharti
   Group Member 3 : Muskan A
   Group Member 4 : Rutvik Jaiswal"
"""

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
import re
import logging
from sklearn.preprocessing import StandardScaler as std
from sklearn.neighbors import NearestNeighbors

logging.basicConfig(filename='Music_Recommendation_System.log', level=logging.INFO,
                    format='%(levelname)s %(asctime)s %(message)s')

class preprocessing:
    """
    This Class is constructed to help with the preprocessing of the data file.
    Here while initializing the object of the class you have to pass your data frame as an argument.
    And then you can utilize the function builtin within this class which helps you in preprocessing of the data.
    """

    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe

    def all_info(self):
        """
        all_info function utilizes info() and describe() function
        to display details about the data.
        """
        return self.dataframe.info(), display(self.dataframe.describe())

    def remove_unwanted_element(self, string):
        """
        Remove_unwanted_element : helps in converting the artist name which is a list set up as a string 
        to a cleaner list value.
        """
        try:
            patten = re.findall(r"'([^']*)'", string)
            for idx, word in enumerate(patten):
                word = re.sub(' ', '_', word)
                patten[idx] = word
            return patten

        except Exception as e:
            logging.error(str(e))
            logging.error(str(e))
            return e

    def clear_artist(self):
        """
        clear_artist helps drop the artist list whenever we need computation with the numerical data only 
        we can utilize this function
        """
        try:
            if "artists" not in self.dataframe.columns:
                return "Refer Other DataFrame. It does'nt contain artist feature !"

            self.dataframe['artists'] = self.dataframe['artists'].map(
                self.remove_unwanted_element)
            return self.dataframe

        except Exception as e:
            logging.error(str(e))
            logging.error(str(e))
            return e

    def remove_string_object(self):
        """
        Helps in removing object type data from the data frame.
        This function comes in handy when you only want to operate on you numerical data values.
        """
        try:
            self.clear_artist()
            for x in self.dataframe.columns:
                if self.dataframe[x].dtype == 'O':
                    self.dataframe.drop(x, axis=1, inplace=True)
#             return self.dataframe.info()

        except Exception as e:
            logging.error(str(e))
            logging.error(str(e))
            return e

    def show_dataframe(self):
        
        """Can be utlized to show the dataframe and everything it consists."""
        return self.dataframe

    def standarization_data(self, col):
        """This function will help you standardize the values for the argument passed.
        """
        try:
            stadarization_series_data = std()
            x = self.dataframe[col].values.reshape(-1, 1)
            columns_standard = stadarization_series_data.fit_transform(x)
            return columns_standard
        except Exception as e:
            return e

    def all_feacture_std(self, drop_col='year'):
        """ Utilizing the standarization_data() function it standarize all the data columns for us.
        """
        try:
            all_col = self.dataframe.columns
            all_col = all_col.drop(drop_col)
            for data in all_col:
                self.dataframe[data] = self.standarization_data(data)
            return self.dataframe
        except Exception as e:
            return e


class plotting_tool(preprocessing):
    """ 
    Plotting tool class helps in utlizing the plotting functions to visualize out dataframe.
    This class is a base class to our preprocessing class it inherits the features of the pre-processing
    class and also helps you enjoy the plotting features orginally built in within this class.
    """
    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe

    def box_plot(self):
        """ This function helps in box plotting the data frame values which can help you understand outliers in your dataset """
        try:
            fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(15, 15))
            index = 0
            ax = ax.flatten()

            for col, value in self.dataframe.items():
                sns.boxplot(y=col, data=self.dataframe,
                            color='orange', ax=ax[index])
                index += 1
            plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=5.0)

        except Exception as e:
            logging.error(str(e))
            logging.error(str(e))
            return e

    def correlation(self):
        """This function helps in plotting the correlation heat map for the data, correlation between the features can very well be understanded using this map."""
        correlation = self.dataframe.corr()
        plt.figure(figsize=(10, 8))

        correlation.style.background_gradient(cmap='coolwarm')
        sns.heatmap(correlation, cbar=True, square=True, fmt='.2f',
                    annot=True, annot_kws={'size': 8}, cmap='Blues')

    def dataframe_kdeplot(self, col_name):
        """ This function can be utlized for kde plot of any column we require helps us understand the shape of our data values. """
        plt.figure(figsize=(12, 8))
        sns.kdeplot(self.dataframe[col_name])
        plt.show()
