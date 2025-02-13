import mido
from mido import Message
from mido import MidiFile
import os

directoryPath = 'MidiRecordings/Chopin'

for fileName in os.listdir(directoryPath):
    if fileName.endswith(".mid"):

        fullFilePath = directoryPath + '/' + fileName

        mid = MidiFile(fullFilePath)

        for i, track in enumerate(mid.tracks):
            print('Track {}: {}'.format(i, track.name))
            for msg in track:
                if msg.type == "note_on" or msg.type == "note_off" or msg.type == "polytouch":
                    print("Original note = " + str(msg.note))
                    msg.note = 127-msg.note #Flipped from middle of keyboard
                    #The messages here being modified are still attached to their
                    #parent midi file somehow
                    print("Flipped note = " + str(msg.note))

        composer = os.path.basename(directoryPath)

        mid.save('FlippedMidiRecordings/' + composer + '/flipped_' + fileName)
    else:
        continue
