# Machine-Intelligence-Watanebe

Machine Intelligence Watanabe is reminded of a phrase in the music that follows.

![1.png](https://github.com/PonDad/Machine-Intelligence-Watanebe/blob/master/data/1.png)

**Input Midi pharase**

![2.png](https://github.com/PonDad/Machine-Intelligence-Watanebe/blob/master/data/2.png)

**Output Midi pharase**

![3.png](https://github.com/PonDad/Machine-Intelligence-Watanebe/blob/master/data/3.png)

## How it works

Machine Intelligence Watanabe uses is Hierarchical Temporal Memory.

![4.png](https://github.com/PonDad/Machine-Intelligence-Watanebe/blob/master/data/4.png)

Hawkins, J. et al. 2016-2020. Biological and Machine Intelligence.

   Release 0.4. Accessed at [numenta](https://numenta.com/resources/biological-and-machine-intelligence/).

## Requierment

- [htm.core](https://github.com/htm-community/htm.core) 
- [numpy](https://numpy.org/) 
- [matplotlib](https://matplotlib.org/users/installing.html)
- [music21](http://web.mit.edu/music21/)
    - [musescore](https://musescore.org/ja)
    - [pygame](https://www.pygame.org/news)

## Usage

### data pre-processing

The Midi file, which is the basis of the learning data, was downloaded from the following site.

[FreeMidi.org](https://freemidi.org/download3-1118-norwegian-wood-beatles)

Extract the data with "Music21".

### Encode

Converts "Mudi number" and "Quarter length" to SDR format.

![6.gif](https://github.com/PonDad/Machine-Intelligence-Watanebe/blob/master/data/6.gif)

### Spatial Pooling

Input SDR is learned by spatial pooling.

![7.gif](https://github.com/PonDad/Machine-Intelligence-Watanebe/blob/master/data/7.gif)

### Temporal Memory

Active SDR is learned by Temporal Memory.

![8.gif](https://github.com/PonDad/Machine-Intelligence-Watanebe/blob/master/data/8.gif)

### Predictor

Active cells learned by Predictor.

![9.gif](https://github.com/PonDad/Machine-Intelligence-Watanebe/blob/master/data/9.gif)