## 10. Micro Challenge: Pickle(The Warning)


## Goal: Save a python Object(Class) to file.


import pickle


class academy:

    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

a = academy("Intelligence Academy and Mejbah vai", "is Best")


with open("academy.pkl", "wb") as f:
    pickle.dump(a,f)

with open("academy.pkl", "rb") as f:
    load_pkl = pickle.load(f)
    print(load_pkl.name, load_pkl.quality)



