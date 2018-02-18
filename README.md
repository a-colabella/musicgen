# musicgen

This is a music machine learning project by Andrew Colabella.

This uses Midicsv/Csvmidi and
text generation with LSTM recurrent neural networks.

MidiCSV was created by John Walke
https://www.fourmilab.ch/webtools/midicsv/

The LSTM Recurrent Neural Networks is based off of
https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/

How to use:

In the top level directory, there exists a shell file called
"runall.sh". This is the master script that runs everything.

All midi files to be used as input should be placed in
the inputfiles/midis directory

The runall.sh script will call midicsv on all midi input files,
converting them to csv. These csvs will be placed in the directory inputfiles/csvs. These will then be converted to text files
using the editCSV python script. The editCSV python script
reduces the csv files to just the instrument tracks and
replaces descriptors such as Note_on_c and Note_off_c with integers,
thus creating a text file with only integers, brackets ('[', ']'), and commas. This allows for a minimal amount of characters
the recurring neural network needs to learn while still
maintaining to complex data that represents these musical tracks.

