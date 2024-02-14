import os
import pretty_midi
import matplotlib.pyplot as plt

def process_midi_and_plot(file_path):
    midi_data = pretty_midi.PrettyMIDI(file_path)
    beats = midi_data.get_beats()

    global_beats = []
    pitches = []

    for instrument in midi_data.instruments:
        for note in instrument.notes:
            start_beat_index = min(range(len(beats)), key=lambda i: abs(beats[i] - note.start)) + 1
            global_beats.append(start_beat_index)
            pitches.append(note.pitch)

    plt.figure(figsize=(14, 8))
    plt.scatter(global_beats, pitches, alpha=0.5)
    plt.title("Note Distribution Over Time")
    plt.xlabel("Global Beat Number")
    plt.ylabel("Pitch")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Save the plot as a PNG file
    output_filename = os.path.join(os.path.dirname(file_path), f"{os.path.basename(file_path)}_note_distribution.png")
    plt.savefig(output_filename)
    plt.close()  # Close the plot to free memory

    def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".mid") or file.endswith(".midi"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                process_midi_and_plot(file_path)

if __name__ == "__main__":
    base_directories = ["../algorithmic-analysis-classical-music/src/composers/romantic",
                        "../algorithmic-analysis-classical-music/src/composers/classical",
                        "../algorithmic-analysis-classical-music/src/composers/baroque"]
    for base_directory in base_directories:
        process_directory(base_directory)
