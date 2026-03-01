from flask import Flask, jsonify, request
import json
import junction_model as jm
import create_new as cn
import os
import io
import csv 
import pandas as pd


app = Flask(__name__)

@app.route("/user/<string:userid>")
def fetch_model(userid):
   models = []
   for f in os.listdir("created_models"):
      f_string = str(f)
      if str(userid) in f_string:
         models.append(f)
   model_json = []
   for m in models:
      path = os.path.join(os.getcwd(), 'created_models')
      path = os.path.join(path, m)
      model = jm.junctionPredict(path, m, userid)
      stats = model.generate_stats()
      model_json.append({m : stats})
   return jsonify(model_json), 200

@app.route('/uploadcsv/<string:userid>', methods=['POST'])
def receive_csv(userid):
   if 'file' not in request.files:
      return jsonify({"error": "No file part"}), 400
   uploaded_file = request.files['file']
   if uploaded_file.filename == '':
      return jsonify({"error": "No selected file"}), 400
   if not uploaded_file.filename.endswith('.csv'):
      return jsonify({"error": "File is not a CSV"}), 400
   if uploaded_file:
      try:
        df = pd.read_csv(uploaded_file, header=None)
        df.columns = ["DateTime","Junction","Vehicles"]
      except Exception as e:
        return jsonify({"error": str(e)}), 500
      models = cn.create_new_models(df, userid)
      model_json = []
      for m in models:
         path = os.path.join(os.getcwd(), 'created_models')
         path = os.path.join(path, m)
         model = jm.junctionPredict(path, m, userid)
         stats = model.generate_stats()
         model_json.append({m : stats})
   return jsonify(model_json), 200

if __name__ == '__main__':
   app.run(port=5000)