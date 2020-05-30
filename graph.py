from music21 import *

inputMidi = converter.parse('./data/NorwegianWood.mid')
parseMidi = inputMidi.parts[1].recurse()
pitch = []
quarterLength = []
for element in parseMidi:
    if isinstance(element, note.Note):
        pitch.append(int(element.pitch.ps))
        quarterLength.append(float(round(element.quarterLength,6)))

notes = []
for i in range(len(pitch)):
    notes.append([pitch[i],quarterLength[i]])
print(notes)

import numpy as np

from htm.bindings.sdr import SDR
from htm.bindings.encoders import ScalarEncoder, ScalarEncoderParameters
from htm.algorithms import SpatialPooler as SP
from htm.algorithms import TemporalMemory as TM
from htm.bindings.algorithms import Classifier
from htm.bindings.algorithms import Predictor

import matplotlib
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

pitchParams = ScalarEncoderParameters()
pitchParams.minimum = 48
pitchParams.maximum = 83
pitchParams.activeBits = 3
pitchParams.size = 24
pitchParams.clipInput  = True

encPitch = ScalarEncoder(pitchParams)
lengthParams = ScalarEncoderParameters()
lengthParams.minimum = 0
lengthParams.maximum = 1
lengthParams.activeBits = 3
lengthParams.size = 24
lengthParams.clipInput  = True

encLength = ScalarEncoder(lengthParams)
inputSDR  = SDR( dimensions = (48, ) )
activeSDR = SDR( dimensions = (576,) )
sp = SP(inputDimensions  = inputSDR.dimensions,
        columnDimensions = activeSDR.dimensions,
        localAreaDensity = 0.02,
        globalInhibition = True,
        seed             = 1,
        synPermActiveInc   = 0.01,
        synPermInactiveDec = 0.008)
tm = TM(
    columnDimensions = (576,),
    cellsPerColumn=8,
    initialPermanence=0.5,
    connectedPermanence=0.5,
    minThreshold=8,
    maxNewSynapseCount=20,
    permanenceIncrement=0.1,
    permanenceDecrement=0.0,
    activationThreshold=8,
)
for i in range(len(notes)):
    pitchBits        = encPitch.encode(notes[i][0])
    lengthBits = encLength.encode(notes[i][1])

    plt.cla
    encoding = SDR( dimensions = (48, ) ).concatenate([pitchBits, lengthBits])
    encodingSDR=encoding.dense.reshape(6,8)
    plt.subplot(1,2,2)
    plt.imshow(encodingSDR, cmap = "Greens")
    plt.pause(0.001)

    inputSDR = SDR( dimensions = (48, ) ).concatenate([pitchBits, lengthBits])
    sp.compute(inputSDR, True, activeSDR)

    sampleSDR=activeSDR.dense.reshape(24,24)
    plt.subplot(1,2,2)
    plt.imshow(sampleSDR, cmap = "Blues")
    plt.pause(0.001)

    tm.compute( activeSDR, learn=True)
    tm.activateDendrites(True)
    
    activeColumnsIndices   = [tm.columnForCell(i) for i in tm.getActiveCells().sparse]
    predictedColumnIndices = [tm.columnForCell(i) for i in tm.getPredictiveCells().sparse]

    reshapeActiveCells =tm.getActiveCells().dense.reshape(24,8,24)
    
    plt.cla
    for j in range(24):
        plt.subplot(7,4,j+1)
        plt.imshow(reshapeActiveCells[j], cmap = "Purples")
    plt.pause(0.001)

    reshapePredictCells =tm.getPredictiveCells().dense.reshape(24,8,24)
    
    for j in range(24):
        plt.subplot(7,4,j+1)
        plt.imshow(reshapePredictCells[j], cmap = "Reds")
    plt.pause(0.001)