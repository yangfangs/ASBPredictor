# **ASBPredictor**

`ASBPredictor` is a Python package for predicting **ASB (Asymptomatic Bacteriuria)** risk. It uses a pre-trained `RandomForestClassifier` model and generates predictions based on clinical data in CSV format. This package is suitable for medical data analysis and clinical research.

---

## **Features**

- **Fast Prediction**: Supports batch input data and generates ASB risk predictions.
- **Easy to Use**: Command-line interface for straightforward operation.
- **Flexible Input**: Supports multi-row CSV input files, with results saved to a new file with predicted probabilities.
- **Customizable**: Allows replacement of the default model with custom-trained models.

---

## **Installation**

### Install from PyPI
Run the following command:
```bash
pip install ASBPredictor
```

## **Usage**

Command-Line Interface
Once installed, you can run ASBPredictor directly from the command line.

Basic Command:
```bash
ASBPredictor -i <input_csv_path> -o <output_csv_path>
```

## **Example**

```bash
git clone https://github.com/yangfangs/ASBPredictor.git
cd ASBPredictor/examples/
ASBPredictor -i input_data.csv -o output_data.csv
```

## **Requirements**
```angular2html
Python version >= 3.6
Required libraries:
pandas >= 1.0.0
scikit-learn >= 1.5.0
```
