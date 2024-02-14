import pretty_midi
import matplotlib.pyplot as plt

def process_midi(file_path):
    midi_data = pretty_midi.PrettyMIDI(file_path)
    # Assuming a constant tempo and time signature for simplicity
    if midi_data.time_signature_changes:
        time_signature = midi_data.time_signature_changes[0]
    else:
        # Default time signature 4/4 if not specified
        time_signature = pretty_midi.TimeSignature(4, 4, 0)

    beats_per_measure = time_signature.numerator  # Beats per measure
    beats = midi_data.get_beats()  # Get the times of each beat

    # Group notes by measure and adjust beat numbering to start at 1
    measures = {}
    for instrument in midi_data.instruments:
        for note in instrument.notes:
            start_beat_index = min(range(len(beats)), key=lambda i: abs(beats[i] - note.start)) + 1  # Adjust for 1-based indexing
            end_beat_index = min(range(len(beats)), key=lambda i: abs(beats[i] - note.end)) + 1
            measure_number = (start_beat_index - 1) // beats_per_measure
            if measure_number not in measures:
                measures[measure_number] = []
            measures[measure_number].append((start_beat_index, end_beat_index, note.pitch))

    # Plotting notes with adjustments
    for measure_number, notes_info in measures.items():
        plt.figure(figsize=(10, 6))
        min_pitch = min(notes_info, key=lambda x: x[2])[2]
        max_pitch = max(notes_info, key=lambda x: x[2])[2]
        for start_beat, end_beat, pitch in notes_info:
            plt.plot([(start_beat - 1) % beats_per_measure + 1, (end_beat - 1) % beats_per_measure + 1], [pitch, pitch], marker='o')
        plt.title(f"Measure {measure_number + 1}")
        plt.xlabel("Beat")
        plt.xticks(range(1, beats_per_measure + 2))  # Adjust for 1-based indexing
        plt.ylabel("Pitch")
        plt.ylim(min_pitch - 1, max_pitch + 1)  # Dynamic y-axis range
        plt.show()

if __name__ == "__main__":
  process_midi("../algorithmic-analysis-classical-music/src/composers/romantic/chopin/chp_op18.mid")
