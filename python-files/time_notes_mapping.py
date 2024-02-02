from mido import MidiFile
import pretty_midi

def main():
  # Replace 'your_file.mid' with the path to your MIDI file
  midi_file_path = 'chopin/chp_op18.mid'
  chords = {}
  midi = MidiFile(midi_file_path)
  for i, track in enumerate(midi.tracks):
    for msg in track:
        if str(msg)[:7] == "note_on":
          if msg.time in chords:
            chords[msg.time].append(msg.note)
          else:
            chords[msg.time] = [msg.note]
  
  # Printing out chords
  sorted_note_onsets = sorted(chords.keys())
  for key in sorted_note_onsets:
    values = chords[key]
    unique_values = list(set(values))  # Remove duplicates

    notes = []
    for val in unique_values:
      notes.append(pretty_midi.note_number_to_name(val))
    print(f"{key}: {notes}")

if __name__ == "__main__":
    main()
