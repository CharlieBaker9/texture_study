from mido import MidiFile
import pretty_midi
import matplotlib.pyplot as plt

def main():
  # Replace 'your_file.mid' with the path to your MIDI file
  midi_file_path = 'chopin/chp_op18.mid'

  # Using pretty midi package for note analysis
  midi_data = pretty_midi.PrettyMIDI(midi_file_path)

  # Get pitch histogram
  histogram = midi_data.get_pitch_class_histogram()

  # Plot the histogram
  plt.bar(range(12), histogram, color='skyblue')
  plt.xlabel('Pitch Class')
  plt.ylabel('Frequency')
  plt.title('Pitch Class Histogram')
  plt.xticks(range(12), ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])
  plt.show()

if __name__ == "__main__":
    main()
