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

   - `incels-5000.xlsx`: This file should contain one comment per line.
   - `toxic_words.txt`: A list of toxic words, each on a separate line.

## Running the Script

To run the script and detect toxic comments, use the following command:

```bash
python script.py
```

## Input Files (Not Included in Repository) 
The following input files are **not included**  in the repository and must be provided locally: 
- **incels-5000.xlsx** : This file contains the list of comments. Each comment should be on a separate row under the 'comment' column.
 
- **toxic_words.txt** : A list of toxic words, each on a separate line, used to detect harmful language.

Please ensure that these files are added to the appropriate directory before running the script.

## Output Files (Not Included in Repository) 
 
- **comment_toxicity_results.csv** : This file contains the results of the toxicity analysis.

These files are generated during the execution of the script and are excluded from the repository.

## Customization

You can modify the list of toxic words in `toxic_words.txt` by adding or removing words based on your requirements.
