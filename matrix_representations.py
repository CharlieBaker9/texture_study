import pretty_midi
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def main():
  # Replace 'your_file.mid' with the path to your MIDI file
  midi_file_path = 'chopin/chp_op18.mid'

  # Using pretty midi package for note analysis
  midi_data = pretty_midi.PrettyMIDI(midi_file_path)

  # Plot chroma matrix
  chroma_matrix = midi_data.get_chroma()
  plt.figure(figsize=(12, 6))
  plt.subplot(2, 1, 1)
  sns.heatmap(chroma_matrix.T, cmap='viridis', xticklabels=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])
  plt.title('Chroma Matrix')

  # Plot pitch transition matrix
  transition_matrix = midi_data.get_pitch_class_transition_matrix()
  plt.subplot(2, 1, 2)
  sns.heatmap(transition_matrix, cmap='viridis', xticklabels=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
              yticklabels=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])
  plt.title('Pitch Transition Matrix')

  plt.tight_layout()
  plt.show()

if __name__ == "__main__":
    main()
