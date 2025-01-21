## ENd to ENd MAchine LEarning PRoject

## Try credit-card-default-prediction app on streamlit.
https://credit-card-default-prediction-app.streamlit.app/
=======
# Credit-Card-Default-Prediction
>>>>>>> 8d830a0189afff6f2cd5e747046fd155ecfdc1a2



# Credit Card Default Prediction

This project predicts whether a credit card holder will default on their payment in the next month. The project leverages machine learning for prediction and includes a web interface built using Streamlit for easy interaction.

## Directory Structure

```
CREDIT-CARD-DEFAULT-PREDICTION
|
|-- .ebextensions         # Configuration files for deployment on Elastic Beanstalk
|-- artifacts             # Directory to store trained models, processed data, etc.
|-- Data                  # Raw and processed datasets
|-- logs                  # Log files for monitoring the pipeline and debugging
|-- mlproject.egg-info    # Metadata for the Python project
|-- models                # Pretrained and saved machine learning models
|-- notebooks             # Jupyter notebooks for exploratory data analysis (EDA) and experiments
|-- src                   # Source code for the ML pipeline
|   |-- pipeline          # Contains PredictPipeline and other pipeline components
|
|-- templates             # HTML templates for web interface
|   |-- home.html         # Homepage template
|   |-- index.html        # Landing page template
|
|-- .gitattributes        # Git attributes for managing file settings
|-- .gitignore            # Files and folders to be ignored by Git
|-- app.py                # Flask app for backend API
|-- config.yaml           # Configuration file for the project
|-- README.md             # Project documentation
|-- requirements.txt      # Python dependencies
|-- setup.py              # Setup file for packaging the project
|-- stream.py             # Streamlit web app for user interaction
```

## Features

- **Streamlit Web Interface**: Interactive UI for users to input data and get predictions.
- **Machine Learning Pipeline**: Predicts the likelihood of credit card default using historical data.
- **Exploratory Data Analysis**: Notebooks for understanding the dataset.
- **Deployment Ready**: Configurations for Elastic Beanstalk deployment.

## How to Run the Project

### Prerequisites

- Python 3.8 or later
- Recommended: Create a virtual environment

### Steps

1. **Clone the repository:**

   ```bash
   git clone <https://github.com/Mrsenjiii/Credit-Card-Default-Prediction/edit/main/README.md>
   cd CREDIT-CARD-DEFAULT-PREDICTION
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run stream.py
   ```

   Alternatively, run the Flask API:

   ```bash
   python app.py
   ```

## Usage

1. Open the Streamlit app in your browser.
2. Input the required features such as `LIMIT_BAL`, `AGE`, repayment statuses, and other credit card details.
3. Click the "Predict" button to get the result.

## Data

The dataset contains the following key features:

- `LIMIT_BAL`: Credit limit
- `AGE`: Age of the individual
- `PAY_x`: Repayment statuses for different months
- `BILL_AMTx`: Bill amounts for different months
- `PAY_AMTx`: Payment amounts for different months
- Categorical features such as `SEX`, `EDUCATION`, and `MARRIAGE`

## Machine Learning Pipeline

The pipeline includes:

- **Preprocessing steps**: Standardization, encoding, and handling missing values
- **Model**: Trained on labeled data to predict default probabilities

## Deployment

The project is configured for deployment using AWS Elastic Beanstalk. Additional deployment options can be explored as needed.

## Author

**Rohit**  
Email: 21f3003125@ds.study.iitm.ac.in

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Scikit-learn](https://scikit-learn.org/) for machine learning
- [Streamlit](https://streamlit.io/) for web application
- [Flask](https://flask.palletsprojects.com/) for API development
