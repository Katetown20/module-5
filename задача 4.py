import json

class Model:
 author = 'Leo Tolstoy'
 title = 'War and Peace'
 text = 'War and Peace is a vast epic centred on Napoleon war with Russia'

 def save(self):
  model_dict = filter(lambda x: not x.startswith('_'), dir(Model))
  model_to_json = dict.fromkeys(model_dict)
  with open('dict.json', 'w') as f:
         json.dump(model_to_json, f)
  print(model_to_json)


model1 = Model()
model1.save()