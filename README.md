# HateDetectorDicMD
This project aims to identify and classify toxic comments from a list of user inputs. It uses a predefined list of toxic words to detect potentially harmful language.

Download the compressed project as a .zip file and decompress it. Navigate to the file folder in terminal, and run script.py or python script.py.
下载压缩包为.zip文件并解压，在终端中进入文件夹，运行script.py或者python script.py。


## Setup

1. **Create a virtual environment:**

   Run the following command to create a virtual environment for the project:

   ```bash
   python -m venv sifu
   ```

2. **Activate the virtual environment:**

   - On **Windows**:
     ```bash
     sifu\Scripts\activate
     ```
   - On **Linux/Mac**:
     ```bash
     source sifu/bin/activate
     ```

3. **Prepare data files:**

   - `comments.txt`: This file should contain one comment per line.
   - `toxic_words.txt`: A list of toxic words, each on a separate line.

## Running the Script

To run the script and detect toxic comments, use the following command:

```bash
python script.py
```

The script will read comments from the `comments.txt` file and compare them against the words in `toxic_words.txt`. Toxic comments will be flagged and saved in `comment_toxicity_results.csv`.

## Output

- **toxic_comments.txt**: This file will contain all the flagged toxic comments.

## Customization

You can modify the list of toxic words in `toxic_words.txt` by adding or removing words based on your requirements.
