from mido import MidiFile
import pretty_midi
import matplotlib.pyplot as plt

def midi_to_notes(file_path):
  notes = []
  
  midi = MidiFile(file_path)
  
  for i, track in enumerate(midi.tracks):
    for msg in track:
      if msg.type == 'note_on':
        notes.append({
          'note': msg.note,
          'velocity': msg.velocity,
          'time': msg.time,
          'channel': i  # Track index as channel for differentiation
        })
  
  return notes

def main():
  # Replace 'your_file.mid' with the path to your MIDI file
  # midi_file_path = '../algorithmic-analysis-classical-music/src/composers/baroque/bach/bach_847.mid'
  midi_file_path = '../algorithmic-analysis-classical-music/src/composers/classical/beethoven/appass_1.mid'
  notes = midi_to_notes(midi_file_path)
  
  channels = []
  notes_1 = []
  count_1 = 0
  notes_2 = []
  count_2 = 0

  for note in notes:
    if note['channel'] == 1:
      count_1 += 1
      if note['note'] not in notes_1:
        notes_1.append(note['note'])

    elif note['channel'] == 2:
      count_2 += 1
      if note['note'] not in notes_2:
        notes_2.append(note['note'])

      # print(note)
  notes_1.sort()
  notes_2.sort()

  print("\n-------------------------------------\n")
  print("Track information embedded within the midi file")
  print("\n-------------------------------------\n")
  midi = MidiFile(midi_file_path)
  for i, track in enumerate(midi.tracks):
    print(f"Track {i}: {track.name}")
    
    # Iterate through messages in the track
    for msg in track:
        if str(msg)[:7] == "note_on":
          continue
        if msg.is_meta and msg.type == 'key_signature':
            print(f"Key Signature: {msg.key} at time {msg.time}")
        elif msg.is_meta and msg.type == 'time_signature':
            print(f"Time Signature: {msg.numerator}/{msg.denominator}")
        # elif msg.is_meta and msg.type == 'set_tempo':
        #     tempo_bpm = int(mido.tempo2bpm(msg.tempo))
        #     print(f"Tempo: {tempo_bpm} BPM set at time {msg.time}" )

  # print("\n-------------------------------------\n")
  # print("Note information on piece itself")
  # print("\n-------------------------------------\n")
  # print("channel 1 had " + str(count_1) + " notes in it")
  # print("these are all of the notes that appeared in channel 1")
  # print(notes_1)
  # print(len(notes_1))
  # print("channel 2 had " + str(count_2) + " notes in it")
  # print("these are all of the notes that appeared in channel 2")
  # print(notes_2)
  # print(len(notes_2))

  # # Using pretty midi package for note analysis
  # midi_data = pretty_midi.PrettyMIDI(midi_file_path)

  # # Get chroma matrix
  # chroma_matrix = midi_data.get_chroma()
  # print(chroma_matrix)

  # # Get pitch transition matrix
  # matrix = midi_data.get_pitch_class_transition_matrix()
  # print(matrix)

if __name__ == "__main__":
    main()
