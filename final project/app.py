from flask import *
import logging
import pandas as pd
from pipeline_for_deployement import pipeline as pfd

app = Flask(__name__, template_folder='statics', static_folder='css_files')


logging.basicConfig(filename='Music_Recommendation_System.log', level=logging.INFO,
                    format='%(levelname)s %(asctime)s %(message)s')

df = pd.read_csv('.//model//data//data.csv')

sample_05 = df.sample(5)['name']


@app.route("/", methods=['POST', 'GET'])
def home_page():
    global sample_05
    song_list = sample_05.values
    song_index = sample_05.index
    song0 = song_list[0]
    song1 = song_list[1]
    song2 = song_list[2]
    song3 = song_list[3]
    song4 = song_list[4]

    try:
        # sample_05 = df.sample(5)['name']
        if request.method == 'POST':
            a = request.form['song_1']
            sample_05 = df.sample(5)['name']
            return redirect(url_for('suggest', usr=song_index[int(a)]))
    except Exception as e:
        logging.error(e)

    return render_template('home.html', song_0=song0, song_1=song1, song_2=song2, song_3=song3, song_4=song4)


@app.route("/suggection_song<int:usr>")
def suggest(usr):
    song_name_list = pfd()
    index = song_name_list.recommend_song_name(int(usr))[0]
    song_name = []
    for ind in index:
        song_name.append(df.iloc[ind]['name'])
    # if request.method == "GET":
    return render_template("recommadation.html", song_l0=song_name[0], song_l1=song_name[1], song_l2=song_name[2], song_l3=song_name[3], song_l4=song_name[4])


app.run(debug=True)
