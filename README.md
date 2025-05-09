## Clear Unnecessary Files

### Prerequisites
Make sure you have **Python** installed on your computer. You can check by running the following command in your terminal or command prompt:

```bash
python --version
```

### Usage
1. Place the Python file in your current working directory where you are coding.
2. Run the Python script whenever you want to clear unnecessary files.

To execute the script, use the following command:

```bash
python clear.py
```

Replace `clear.py` with the actual name of your Python file.

### For Swift Users (VS Code Code Runner Extension)

Replace the Swift configuration in your **Code Runner** script with the following:

```json
"swift": "swiftc \"$fileName\" -o \"$fileNameWithoutExt.exe\" && ./$fileNameWithoutExt.exe",
```
