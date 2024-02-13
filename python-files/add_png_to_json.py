import os
import json

def extract_info(midi_filename):
  base_name = os.path.splitext(midi_filename)[0]
  return {
    'chroma_matrix': f'{base_name}_chroma_matrix.png',
    'pitch_histogram': f'{base_name}_pitch_histogram.png',
    'transition_matrix': f'{base_name}_transition_matrix.png'
  }

def update_json(composer_dir, midi_file, info):
  json_path = os.path.join('..', 'algorithmic-analysis-classical-music', 'src', 'composers', 'json', f"{composer_dir}.json")
  if os.path.exists(json_path):
    with open(json_path, 'r+') as file:
      data = json.load(file)
      piece_key = os.path.splitext(midi_file)[0]
      if piece_key in data.get("pieces", {}):
        data["pieces"][piece_key].update(info)
      else:
        print(f"No entry for {piece_key} in {composer_dir}.json")
      
      file.seek(0)
      json.dump(data, file, indent=2)
      file.truncate()

def process_folders(base_path='../algorithmic-analysis-classical-music/src/composers'):
  for root, _, files in os.walk(base_path):
    midi_files = [f for f in files if f.endswith('.mid')]
    composer_dir = os.path.basename(root)
    for midi_file in midi_files:
      info = extract_info(midi_file)
      update_json(composer_dir, midi_file, info)
      print(f"Processed {midi_file} in {composer_dir}")

if __name__ == "__main__":
  process_folders()
