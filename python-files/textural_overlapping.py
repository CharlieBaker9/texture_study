import pretty_midi
import matplotlib.pyplot as plt
import numpy as np

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
    
    # Assuming the first time signature is representative if there are multiple
    if not ts_changes:
        # Default to 4/4 if no time signature changes are present
        ts_changes = [pretty_midi.TimeSignature(4, 4, 0)]
    
    # Prepare plots for each time signature found
    for ts in ts_changes:
        ts_key = f"{ts.numerator}/{ts.denominator}"
        positions_within_measure = []
        relative_pitches = []
        
        for instrument in midi_data.instruments:
            for note in instrument.notes:
                normalized_position = calculate_position_within_measure(note.start, midi_data, ts_changes)
                positions_within_measure.append(normalized_position)
                relative_pitches.append(note.pitch - min([n.pitch for n in instrument.notes]))  # Relative to the lowest note
                
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.scatter(positions_within_measure, relative_pitches, alpha=0.5, s=10)
        plt.title(f"Note Positions Within Measures for Time Signature {ts_key}")
        plt.xlabel("Position Within Measure")
        plt.ylabel("Pitch Relative to Lowest Note")
        plt.xlim(0, 1)
        plt.show()

if __name__ == "__main__":
    process_midi_by_time_signature("../algorithmic-analysis-classical-music/src/composers/romantic/chopin/chp_op18.mid")
