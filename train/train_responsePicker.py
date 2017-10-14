from keras.models import Sequential
from keras.layers import Dense, Activation
from constants import *

model = Sequential()

"""

Model: Multi-Layer Perceptron, Categorical
Takes: Raw user input
Returns: Response ID

Types of responses:

0 - Greeting (in response to something like "hi, how are you")
1 - Answer to personal question ("what is your name?", "what is your favorite color?")
2 - Recollection ("What did you do today?", "What was that like?")
3 - Creative (Asking a question, telling a story)

"""

model.add(Dense(units=100, input_dim=INPUT_LIMIT, activation="relu"))
model.add(Dense(units=100, activation="relu"))
model.add(Dense(units=4, activation="softmax"))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
