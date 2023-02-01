import json

class Model:
 author = 'Leo Tolstoy'
 title = 'War and Peace'
 text = 'War and Peace is a vast epic centred on Napoleon war with Russia'

 def save(self):
  model_dict = Model.__dict__
  new_dict = str(model_dict)
  with open('dict.json', 'w') as f:
   json.dump(new_dict, f)
  print(new_dict)


model1 = Model()
model1.save()