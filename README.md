# ML-XCT Segmentation

A brief description of your project goes here.

---

## Setup Instructions

This guide explains how to set up and run this project using a virtual environment and the provided `requirements.txt` file.

---

## 1. Create Virtual Environment

Run the following in your terminal **from the root of the repo**:

```sh
python -m venv .venv
```

## 2. Activate Virtual Environment 

Run the following in your terminal **from the root of the repo**:

```sh
.venv\Scripts\activate
```

## 3. Install Dependancies

Run the following in the terminal:

```sh
pip install -r requirements.txt
```

## 4. Run Test Files

Run the following in the terminal:

```sh
python main.py
```

## 5. Deactivate the Virtual Environment

Run the following in the terminal:

```sh
deactivate
```

## Exmaple

```sh
# Clone the repo
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Create and activate venv
python -m venv .venv
source .venv/bin/activate

# Install packages
pip install -r requirements.txt

# Run the app
python main.py
```


## 99. Notes

Automatically Add Pakcages to Requirements, from within the virtual environment:

```sh
pip freeze > requirements.txt
```