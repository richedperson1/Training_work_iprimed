"""
Author : Vornoi Practitioners
   Group Captain  : Mrinal Bhardwaj
   Group Member 1 : Ankita R Desai
   Group Member 2 : Ashutosh Kumar Bharti
   Group Member 3 : Muskan A
   Group Member 4 : Rutvik S Jaiswal"
   
"""

import pickle
import numpy as np
import music_recommedation_oops as mro
import pandas as pd


class pipeline:
    """
    This class is created to utilize the Nearest Neighbor model.
    Functions builtin within this class helps with the recommendation of songs based on the user's choice from the random list of songs provided to the user.
    This class also includes features for data purification which gets our data ready for further processes.
    """
    def __init__(self) -> None:
        data = pd.read_csv('./data/data.csv')
        self.dataframe_result = data

    def pure_data(self):
        """This function helps in clearing the categorical data and providing you with the numerical types so that you can continue your operations on the data set."""
        try:
            copy_data_frame = self.dataframe_result.copy()
            object = mro.preprocessing(copy_data_frame)
            object.remove_string_object()
            object.all_feacture_std()
            self.pure_dataframe = object.show_dataframe()
            return self.pure_dataframe
        except Exception as e:
            return e

    def recommend_song_name(self, index):
        """This function recommend song based on the input provided and model trained."""
        try:
            with open('model_pkl', 'rb') as f:
                lr = pickle.load(f)

            pure_dataframe = self.pure_data()
            distances, indices = lr.kneighbors(
                pure_dataframe.iloc[index, :].values.reshape(1, -1), n_neighbors=8)

            for i in range(0, len(distances.flatten())):
                if i == 0:
                    print(
                        "Recommendation for song -> {0} -:\n".format(self.dataframe_result.iloc[index]['name']))
                else:
                    print('{0}: {1} -> with distance of {2}:'.format(i,
                                                                     self.dataframe_result.iloc[indices[0][i]]['name'], distances.flatten()[i]))
            return "⬆⬆ Best song for you ⬆⬆"
        except Exception as e:
            return e

    def random_song_recommendation(self):
        """If you want random recommendation this function is going to help you do that."""
        try:
            index = np.random.choice(self.dataframe_result.shape[0])
            self.recommend_song_name(index)
            return "⬆⬆ Best song for you ⬆⬆"
        except Exception as e:
            return e

    def recommend_song_list(self):
        """For a recommendation of songs list. This is the perfect fit function for you"""
        try:
            song_series = self.dataframe_result.sample(7)['name']
            song_list = song_series.values
            song_index = song_series.index
            print()
            print("id  Song name")
            for idx,data in enumerate(song_list):
                print(f"{idx} : {data}")

            id_song = int(input("Please enter id of song : "))
            if id_song > len(song_index)-1:
                return "Select proper id please"

            index = song_index[id_song]
            print()
            self.recommend_song_name(index)
        except Exception as e:
            return e
