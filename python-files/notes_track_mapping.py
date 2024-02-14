from mido import MidiFile
import pretty_midi

def main():
    # Replace 'your_file.mid' with the path to your MIDI file
    midi_file_path = '../algorithmic-analysis-classical-music/src/composers/romantic/chopin/chp_op18.mid'
    midi = MidiFile(midi_file_path)

    # A dictionary to store notes, their onset times, and the track they belong to
    note_onsets = {}

    # Iterate through all tracks in the MIDI file
    for i, track in enumerate(midi.tracks):
        cumulative_time = 0  # Initialize cumulative time for this track
        for msg in track:
            if msg.type == 'note_on' and msg.velocity > 0:  # Check for note_on message with velocity > 0 to filter out note_off messages
                cumulative_time += msg.time  # Update cumulative time with the delta time of the current message
                note_info = (msg.note, i)  # Tuple of note and track index
                if cumulative_time not in note_onsets:
                    note_onsets[cumulative_time] = [note_info]
                else:
                    note_onsets[cumulative_time].append(note_info)

    # Sorting the onsets by time
    sorted_onsets = sorted(note_onsets.items(), key=lambda item: item[0])

    # Printing out the notes for each onset, sorted by time, along with track information
    for onset_time, notes_info in sorted_onsets:
        print(f"Time {onset_time}:")
        for note, track in notes_info:
            # Converting note number to note name for readability
            note_name = pretty_midi.note_number_to_name(note)
            print(f"  Track {track}: {note_name}")

if __name__ == "__main__":
    main()