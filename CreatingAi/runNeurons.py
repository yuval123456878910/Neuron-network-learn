def runNeurons(layersList: list):
    import nerronsConnection, neuronsCaulculation
    for layer in layersList[1:len(layersList)]:
        placeNum = layersList.index(layer)
        nerronsConnection.neuronsConnection(layer,layersList[placeNum-1])

    for layer in layersList[1:len(layersList)]:
        placeNum = layersList.index(layer)
        neuronsCaulculation.neuronCaulculation(layer,layersList[placeNum-1])
    
    return layersList

