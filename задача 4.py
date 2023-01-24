import json

class Model:

    def save(self, author, title, text, dict = {}):
     self.author = author
     self.title = title
     self. text = text
     self.dict = dict

     dict[author] = 'author'
     dict[title] = 'title'
     dict[text] = 'text'
     with open('dict.json', 'w') as f:
         json.dump(dict, f)
     print(dict)




model1 = Model()
model1.save('Varvar', 'art of war', 'random text')