# Audio File Comparison

![Graphs comparing thirteen metrics from separate audio files.](https://hosting.photobucket.com/bbcfb0d4-be20-44a0-94dc-65bff8947cf2/a2c80672-6b31-4afb-87b4-2d70e7cf25b5.png)

Process detailed audio analysis data with Python to calculate average track metrics, then visualize the results with D3.js bar charts for clear comparisons.

## Application Overview

Using Python and NumPy, this project processes an enhanced audio analysis `JSON` file and reduces metric data into representative averages for each track. The script calculates mean values for core audio features such as onsets, loudness, tempo, percussive content and others.

For multidimensional metrics, including timbre, chroma and tonnetz data, the script preserves individual feature bands while calculating an average for each one. The result is a cleaner `audio_analysis_averages.json` file which keeps the structure needed for comparison.

The processed JSON output is then loaded by the frontend to generate bar charts. Together, the Python processing script and D3 visualizations create a workflow to turn dense audio analysis data into clear visual comparisons.

## Basic Setup Instructions

Below are the required software programs and instructions for installing and using this application on a Linux machine.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository: `git clone git@github.com:devbret/audio-file-comparison.git`

4. Navigate to the repo's directory: `cd audio-file-comparison`

5. Create a virtual environment: `python3 -m venv venv`

6. Activate a virtual environment: `source venv/bin/activate`

7. Install the needed dependencies: `pip install -r requirements.txt`

8. Place your `audio_analysis_enhanced.json` file at the root of this repo

9. Run the script: `python3 app.py`

10. Launch an HTTP server: `python3 -m http.server`

11. Access the frontend in a browser: `http://localhost:8000`

12. When finished, shutdown the HTTP server: `CTRL + c`

13. Exit the virtual environment: `deactivate`

## Other Considerations

The sections below cover details about this repo which fall outside of setup and usage. The first outlines the skills this project is meant to demonstrate, while the second section explains the terms under which the code is licensed and how to get in touch.

### Abilities Demonstrated

This project repo is intended to demonstrate an ability to do the following:

- Process detailed audio analysis data with Python and visualize track comparisons using D3.js bar charts

- Convert complex audio metrics into simplified averages so users can easily compare multiple tracks

- Analyze audio feature data, calculate representative averages and turn the results into clear comparisons

- Create a workflow for transforming audio analysis JSON into readable visual insights

### License Information

This project is released under the [MIT License](LICENSE). You are free to use, modify, publish, distribute and sell copies of this software so long as the original copyright notice and permission notice are included with any substantial portion of the code. The software is provided "as is", without warranty of any kind, and the author is not liable for any claim or damages arising from its use.

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
