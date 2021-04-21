import numpy as np

vodka = 1.0
rain = 0.0
friend = 1.0


def activation_function(x):
    if x >= 0.5:
        return 1
    else:
        return 0


def predict(vod, ra, fri):
    inputs = np.array([vod, ra, fri])
    weights_input_to_hidden_1 = [0.25, 0.25, 0]
    weights_input_to_hidden_2 = [0.5, -0.4, 0.9]
    weights_input_to_hidden = np.array([weights_input_to_hidden_1, weights_input_to_hidden_2])

    weights_input_to_output = np.array([-1, 1])

    hidden_input = np.dot(weights_input_to_hidden, inputs)
    print("hidden_input: " + str(hidden_input))

    hidden_output = np.array([activation_function(x) for x in hidden_input])
    print("hidden_output: " + str(hidden_output))

    output = np.dot(weights_input_to_output, hidden_output)
    print("output: " + str(output))
    return activation_function(output) == 1


print("result: " + str(predict(vodka, rain, friend)))
