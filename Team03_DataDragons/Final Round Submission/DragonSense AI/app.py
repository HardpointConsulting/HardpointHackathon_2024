from flask import Flask, render_template, request, jsonify
import os
import pathlib
from flask import request
from pydub import AudioSegment
from sql_llm import sql_to_llm
from werkzeug.datastructures import ImmutableMultiDict
from moviepy.editor import VideoFileClip
from voice_to_text import voice_to_text
from database_config import username, password, host, database

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if(request.method=="GET"):
        return render_template('home.html')
    else:
        # print(request.files)
        print(request.form)
        text_input = request.form['message']
        # username = "root"
        # password = "root"
        # host = "localhost"
        # database =  "atliq_tshirts"
        flag = 0
        if text_input!="":
            text_input
        elif 'audio' in request.files:
            audio_file = request.files['audio']
            print('audio file', audio_file)
            audio_file.save("audio.webm")
            audio = AudioSegment.from_file("audio.webm", fomat="webm")
            audio.export("audio.wav", format="wav")
            text_input = voice_to_text("audio.wav")
            print(text_input)
            flag = 1
         
      
        sql_res = sql_to_llm(username, password, host, database, text_input)
        # print("ti", text_input)
        # return render_template('home.html', data=text_input)
        if flag==1:
            processed_text = sql_res["result"]
            return jsonify(result = processed_text, query=sql_res["query"] )
        else:
            processed_text = sql_res["result"]
            return jsonify(result = processed_text)
            # print("pre", processed_text) 
        
    # return jsonify({'result': processed_text})


if __name__=="__main__":
    app.run(debug=True)