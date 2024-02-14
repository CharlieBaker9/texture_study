from mido import MidiFile
import pretty_midi

def main():
  # Replace 'your_file.mid' with the path to your MIDI file
  midi_file_path = '../algorithmic-analysis-classical-music/src/composers/classical/beethoven/appass_1.mid'
  midi = MidiFile(midi_file_path)

  # A dictionary to store notes and their onset times
  note_onsets = {}

  # Iterate through all tracks in the MIDI file
  for track in midi.tracks:
    cumulative_time = 0  # Initialize cumulative time for this track
    for msg in track:
      if msg.type == 'note_on' and msg.velocity > 0:  # Check for note_on message with velocity > 0 to filter out note_off messages
        cumulative_time += msg.time  # Update cumulative time with the delta time of the current message
        if cumulative_time not in note_onsets:
          note_onsets[cumulative_time] = [msg.note]
        else:
          note_onsets[cumulative_time].append(msg.note)

  # Sorting the onsets by time
  sorted_onsets = sorted(note_onsets.items(), key=lambda item: item[0])

  # Printing out the notes for each onset, sorted by time
  for onset_time, notes in sorted_onsets:
    # Converting note numbers to note names for readability
    note_names = [pretty_midi.note_number_to_name(note) for note in notes]
    print(f"Time {onset_time}: {note_names}")
    # print(f"Time {onset_time}: {set(note_names)}")

if __name__ == "__main__":
  main()
