weight = 0.1


def neural_network(idata, weight):
    prediction = idata * weight
    return prediction


number_of_toes = [8.5, 9.5, 10, 9]
pred = neural_network(number_of_toes[0], weight)
print(pred)
