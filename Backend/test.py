import create_new as cn 
import junction_model as jm
import pandas as pd
import json
import os

df = pd.read_csv('test.csv')
models = cn.create_new_models(df, 'Michael')
print(models)

#df_new = cn.clean_data("traffic_main.csv")
#cutoff_date = '2016-11-01 00:00:00'
#df_filtered = df_new[df_new['DateTime'] < cutoff_date]
#df_filtered = df_filtered[df_filtered["Junction"] == 1].drop("Junction",axis=1)
#df_filtered['Vehicles'] = 0
#df_filtered.to_csv("empty_pred.csv")
#path = os.path.join(os.getcwd(), 'created_models')
#path = os.path.join(path, "1-v2-Michael")
#model = jm.junctionPredict(path, '1-v2', 'Michael')
#stats = model.generate_stats()
#with open('output.json', 'w') as json_file:
    #json.dump(stats, json_file, indent=4)
#def test(userid):
    #models = []
    ##for f in os.listdir("created_models"):
    #    f_string = str(f)
    #    if str(userid) in f_string:
     #       models.append(f_string)
   # return models

#rint(f"{test('Michael')}")