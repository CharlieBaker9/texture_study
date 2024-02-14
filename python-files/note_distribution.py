import pretty_midi
import matplotlib.pyplot as plt

def process_midi_and_plot(file_path):
    midi_data = pretty_midi.PrettyMIDI(file_path)
    beats = midi_data.get_beats()

    # Initialize lists to hold global beat positions and pitches
    global_beats = []
    pitches = []

    # Process each note
    for instrument in midi_data.instruments:
        for note in instrument.notes:
            # Calculate global beat for the start of the note
            start_beat_index = min(range(len(beats)), key=lambda i: abs(beats[i] - note.start)) + 1
            global_beats.append(start_beat_index)
            pitches.append(note.pitch)

    # Plotting
    plt.figure(figsize=(14, 8))
    plt.scatter(global_beats, pitches, alpha=0.5)  # Adjust alpha for point opacity
    plt.title("Note Distribution Over Time")
    plt.xlabel("Global Beat Number")
    plt.ylabel("Pitch")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    process_midi_and_plot("../algorithmic-analysis-classical-music/src/composers/romantic/chopin/chp_op18.mid")
