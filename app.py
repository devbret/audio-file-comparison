import json
import os
import numpy as np

input_file = "/your/file/path/audio_analysis_enhanced.json"
output_file = "audio_analysis_averages.json"

def calculate_average_for_metric(metric_data, key="value"):
    values = [entry[key] for entry in metric_data]
    if values:
        return np.mean(values)
    return None

def calculate_averages_for_song(song_data):
    averaged_data = {}

    if "onsets" in song_data:
        averaged_data["average_onsets"] = calculate_average_for_metric(song_data["onsets"])

    if "timbre" in song_data:
        averaged_data["average_timbre"] = {}
        for mfcc_key in song_data["timbre"]:
            mfcc_key_label = list(mfcc_key.keys())[0] 
            averaged_data["average_timbre"][mfcc_key_label] = calculate_average_for_metric(mfcc_key[mfcc_key_label])

    if "loudness" in song_data:
        averaged_data["average_loudness"] = calculate_average_for_metric(song_data["loudness"])

    if "chroma" in song_data:
        averaged_data["average_chroma"] = {}
        for chroma_key in song_data["chroma"]:
            chroma_key_label = list(chroma_key.keys())[0]
            averaged_data["average_chroma"][chroma_key_label] = calculate_average_for_metric(chroma_key[chroma_key_label])

    if "tempo" in song_data:
        averaged_data["average_tempo"] = calculate_average_for_metric(song_data["tempo"])

    if "spectral_centroid" in song_data:
        averaged_data["average_spectral_centroid"] = calculate_average_for_metric(song_data["spectral_centroid"])

    if "spectral_bandwidth" in song_data:
        averaged_data["average_spectral_bandwidth"] = calculate_average_for_metric(song_data["spectral_bandwidth"])

    if "zero_crossing_rate" in song_data:
        averaged_data["average_zero_crossing_rate"] = calculate_average_for_metric(song_data["zero_crossing_rate"])

    if "spectral_contrast" in song_data:
        averaged_data["average_spectral_contrast"] = {}
        for contrast_key in song_data["spectral_contrast"]:
            contrast_key_label = list(contrast_key.keys())[0]
            averaged_data["average_spectral_contrast"][contrast_key_label] = calculate_average_for_metric(contrast_key[contrast_key_label])

    if "spectral_rolloff" in song_data:
        averaged_data["average_spectral_rolloff"] = calculate_average_for_metric(song_data["spectral_rolloff"])

    if "mel_spectrogram" in song_data:
        averaged_data["average_mel_spectrogram"] = {}
        for mel_key in song_data["mel_spectrogram"]:
            mel_key_label = list(mel_key.keys())[0] 
            averaged_data["average_mel_spectrogram"][mel_key_label] = calculate_average_for_metric(mel_key[mel_key_label])

    if "tonnetz" in song_data:
        averaged_data["average_tonnetz"] = {}
        for tonnetz_key in song_data["tonnetz"]:
            tonnetz_key_label = list(tonnetz_key.keys())[0] 
            averaged_data["average_tonnetz"][tonnetz_key_label] = calculate_average_for_metric(tonnetz_key[tonnetz_key_label])

    if "harmonics" in song_data:
        averaged_data["average_harmonics"] = calculate_average_for_metric(song_data["harmonics"])

    if "percussives" in song_data:
        averaged_data["average_percussives"] = calculate_average_for_metric(song_data["percussives"])

    return averaged_data

def process_audio_analysis(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Input file {input_file} does not exist.")
        return
    
    with open(input_file, 'r') as f:
        audio_analysis_data = json.load(f)

    averaged_results = {}
    for song, data in audio_analysis_data.items():
        averaged_results[song] = calculate_averages_for_song(data)

    with open(output_file, 'w') as f:
        json.dump(averaged_results, f, indent=4)
    
    print(f"Averaged audio analysis completed. Results are saved in {output_file}")

if __name__ == "__main__":
    process_audio_analysis(input_file, output_file)
