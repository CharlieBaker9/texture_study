import os
import re
import json
from mido import MidiFile

def extract_title(tracks):
  title = None
  copyright_re = re.compile(r'Copyright|http://|\d{4}')
  
  for track in tracks:
    if copyright_re.search(track):
      break  # Stop at the first sign of copyright or related info
    title = track  # Keep updating 'title' until we hit copyright info
  
  # Optional: Further process 'title' to extract the exact part you want
  if title:
    title = title.split(": ", 1)[-1]  # Split on first occurrence of ": " and take the second part
      
  return title

def extract_title_from_midi(midi_file_path):
  midi = MidiFile(midi_file_path)

  tracks = []
  for i, track in enumerate(midi.tracks):
    # Assuming track names are stored in track.name for mido; adjust as necessary
    track_name = f"Track {i}: " + track.name if hasattr(track, 'name') else "Unnamed Track"
    tracks.append(track_name)
    
  title = extract_title(tracks)

  return title

def update_json_with_title(composer_dir, midi_file, title):
  json_file_path = os.path.join('..', 'algorithmic-analysis-classical-music', 'src', 'composers', 'json', f"{composer_dir}.json")
  if os.path.exists(json_file_path):
    with open(json_file_path, 'r+') as json_file:
      data = json.load(json_file)
      if "pieces" not in data:
        data["pieces"] = {}
      data["pieces"][midi_file] = {"title": title}
      
      json_file.seek(0)  # Rewind to the beginning of the file
      json.dump(data, json_file, indent=2)
      json_file.truncate()  # Remove remaining part of old data

def process_composer_folders(base_path='../algorithmic-analysis-classical-music/src/composers'):
  for root, dirs, files in os.walk(base_path):
    for file in files:
      if file.endswith('.mid'):
        midi_file_path = os.path.join(root, file)
        title = extract_title_from_midi(midi_file_path)
        composer_dir = os.path.basename(os.path.normpath(root))  # Get the composer's directory name
        update_json_with_title(composer_dir, file, title)
        print(f"Updated {composer_dir}.json with title '{title}' for {file}")

if __name__ == "__main__":
  process_composer_folders()