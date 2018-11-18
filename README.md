# PyScan3D
Uses data gathered from the Structure Sensor by Occipital to classify things into their respective shapes. 
Python is required to be able to run this program.

## Features:
**Mail Parser** - Log in to your email to select and download scans <br>
**Object Classifier** - Load a .obj or .ply file to classify its shape

## Installation:
Clone the repository using HTTPS:
```
git clone https://github.com/emilieez/pyscan.git
```

Clone the repository using SSH:

```
git clone git@github.com:emilieez/pyscan.git
```


A virtual environment is provided if the dependencies are not installed.

## Run the PyScan virtual environment
### Windows:

Run the following line in Command Prompt:
```
PyScan\Scripts\activate.bat
```

### Linux or MacOS: 

Run the following line in the terminal:
```
source /PyScan/bin/activate
```

The terminal should now have look something like this:
```
(PyScan) D:\pyscan>
```

To deactivate the virtual environment, simply type:
```
deactivate
```

### Running the PyScan3D Application
In the root folder of the repository type:
```
python pyscan.py
```