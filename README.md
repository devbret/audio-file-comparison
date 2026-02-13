# Audio File Comparison

![Graphs comparing thirteen metrics from separate audio files.](https://hosting.photobucket.com/bbcfb0d4-be20-44a0-94dc-65bff8947cf2/a2c80672-6b31-4afb-87b4-2d70e7cf25b5.png)

Processes detailed audio data with Python to compute average metrics and then visualizes those comparisons using D3.js bar and grouped bar charts.

## Overview

Using Python and NumPy, the app first extracts key metrics. The script then aggregates the data into single representative averages for each metric, producing a simplified JSON output for track-to-track comparison.

Next, the frontend dynamically loads the processed JSON file and generates both standard bar charts and grouped bar charts. This allows users to visually compare multiple audio tracks in a structured format.

The Python backend and D3-based frontend create a complete pipeline for transforming audio data into clear visual insights.

## Set Up

### Programs Needed

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs.
2. Open a shell window (for Windows open PowerShell, for MacOS open Terminal and for Linux open your distro's terminal emulator).
3. Clone this repository using `git` by running the following command; `git clone git@github.com:devbret/audio-file-comparison.git`.
4. Navigate to the repo's directory by running; `cd audio-file-comparison`.
5. Install the needed dependencies for running the script with the following command; `pip install -r requirements.txt`.
6. Update line five in app.py, with the path to the correct JSON file.
7. Run the script with the command `python3 app.py`.
8. To view the audio comparisons with the index.html file, you will need to run a local web server. To do this run `python3 -m http.server`.
