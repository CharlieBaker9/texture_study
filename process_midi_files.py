import mido
from mido import MidiFile

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
  midi_file_path = 'chopin/chp_op18.mid'
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

  print("channel 1 had " + str(count_1) + " notes in it")
  print("these are all of the notes that appeared in channel 1")
  print(notes_1)
  print(len(notes_1))
  print("channel 2 had " + str(count_2) + " notes in it")
  print("these are all of the notes that appeared in channel 2")
  print(notes_2)
  print(len(notes_2))

if __name__ == "__main__":
    main()
