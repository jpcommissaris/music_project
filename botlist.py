import pickle


# read in model with pickle
pickle_in = open("studentmodel.pickle", "rb")
df = pickle.load(pickle_in)



