import os
import json
import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def extract_info(midi_filename, root_dir):
    base_name = os.path.splitext(midi_filename)[0]
    info = {}
    for suffix in ['chroma_matrix', 'pitch_histogram', 'transition_matrix']:
        image_filename = f"{base_name}_{suffix}.png"
        image_path = os.path.join(root_dir, image_filename)
        if os.path.exists(image_path):
            info[suffix] = encode_image_to_base64(image_path)
        else:
            print(f"Image file not found: {image_path}")
    return info

def update_json(composer_dir, midi_file, info):
    json_path = os.path.join('..', 'algorithmic-analysis-classical-music', 'src', 'composers', 'json', f"{composer_dir}.json")
    if os.path.exists(json_path):
        with open(json_path, 'r+') as file:
            data = json.load(file)
            piece_key = os.path.splitext(midi_file)[0]
            key = piece_key + ".mid"
            if key not in data["pieces"]:
                data["pieces"][key] = {}
            data["pieces"][key].update(info)
            
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

def process_folders(base_path='../algorithmic-analysis-classical-music/src/composers'):
    for root, _, files in os.walk(base_path):
        midi_files = [f for f in files if f.endswith('.mid')]
        composer_dir = os.path.basename(root)
        for midi_file in midi_files:
            info = extract_info(midi_file, root)
            update_json(composer_dir, midi_file, info)
            print(f"Processed {midi_file} in {composer_dir}")

if __name__ == "__main__":
    process_folders()
