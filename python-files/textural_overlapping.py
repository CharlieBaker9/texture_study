import os
import pretty_midi
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

def quantize_position(position, subdivisions_per_beat=4):
  # Quantize the position to the nearest subdivision
  quantized_position = round(position * subdivisions_per_beat) / subdivisions_per_beat
  return np.float64(quantized_position)

def calculate_density(positions):
  """
  Calculate the density of note positions using a Gaussian kernel density estimate.
  Adjust the method to ensure sufficient variation in density values.
  """
  positions_array = np.array(positions)
  density = gaussian_kde(positions_array)
  density.covariance_factor = lambda: .25
  density._compute_covariance()
  densities = density(positions_array)
  # Normalize densities to a range before scaling
  min_density, max_density = min(densities), max(densities)
  normalized_densities = (densities - min_density) / (max_density - min_density)
  return normalized_densities * 100 + 10  # Apply scaling and ensure a minimum size

def calculate_position_within_measure(note_start_time, midi_data, ts_changes):
  # Find the time signature active at the note's start time
  current_ts = None
  for ts in reversed(ts_changes):
    if note_start_time >= ts.time:
      current_ts = ts
      break
  if not current_ts:
    # Default to 4/4 if no time signature is found
    current_ts = pretty_midi.TimeSignature(4, 4, 0)

  # Calculate beats per minute at the note's start time
  tempo = midi_data.estimate_tempo()
  
  # Calculate the beat of the note's start time
  seconds_per_beat = 60.0 / tempo
  beat = note_start_time / seconds_per_beat
  
  # Calculate the position within the measure
  beats_per_measure = current_ts.numerator
  measure_start_beat = np.floor(beat / beats_per_measure) * beats_per_measure
  position_within_measure = beat - measure_start_beat
  
  # Normalize the position within the measure
  normalized_position = position_within_measure / beats_per_measure
  return normalized_position

def process_midi_by_time_signature(file_path):
  midi_data = pretty_midi.PrettyMIDI(file_path)
  ts_changes = midi_data.time_signature_changes
  offset = 0.02
  
  # Assuming the first time signature is representative if there are multiple
  if not ts_changes:
    # Default to 4/4 if no time signature changes are present
    ts_changes = [pretty_midi.TimeSignature(4, 4, 0)]
  
  # Prepare plots for each time signature found
  curr = 0
  for ts in ts_changes:
    ts_key = f"{ts.numerator}/{ts.denominator}"
    positions_within_measure = []
    relative_pitches = []
    
    # Update the plotting section to apply quantization
    for instrument in midi_data.instruments:
      for note in instrument.notes:
        normalized_position = calculate_position_within_measure(note.start, midi_data, ts_changes)
        # Apply quantization to the normalized position
        quantized_position = quantize_position(normalized_position, subdivisions_per_beat=64)

        positions_within_measure.append(quantized_position)
        relative_pitches.append(note.pitch - min([n.pitch for n in instrument.notes]))

    sizes = calculate_density(positions_within_measure)  # Scale factor for visibility
          
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(positions_within_measure, relative_pitches, alpha=0.5, s=sizes)
    plt.title(f"Note Positions Within Measures for Time Signature {ts_key}")
    plt.xlabel("Position Within Measure")
    plt.ylabel("Pitch Relative to Lowest Note")
    plt.xlim(0-offset, 1-offset)
    plt.ylim(min(relative_pitches) - 1, max(relative_pitches) + 1) 
    
    currString = str(curr)
    output_filename = os.path.join(os.path.dirname(file_path), f"{os.path.basename(file_path)}_textural_overlap_{currString}.png")
    plt.savefig(output_filename)
    plt.close()  # Close the plot to free memory
    curr += 1
    print("saved graph")

def process_directory(directory_path):
  for root, dirs, files in os.walk(directory_path):
    for file in files:
      if file.endswith(".mid") or file.endswith(".midi"):
        file_path = os.path.join(root, file)
        print(f"Processing: {file_path}")
        process_midi_by_time_signature(file_path)

if __name__ == "__main__":
  base_directories = ["../algorithmic-analysis-classical-music/src/composers/classical"]
  # base_directories = ["../algorithmic-analysis-classical-music/src/composers/romantic",
  #                     "../algorithmic-analysis-classical-music/src/composers/classical",
  #                     "../algorithmic-analysis-classical-music/src/composers/baroque"]
  for base_directory in base_directories:
    process_directory(base_directory)