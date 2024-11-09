# Machine Learning Model Repository

This repository is dedicated to the study, training, and storage of machine learning models. It provides Jupyter notebooks for model exploration and training, as well as a structure for storing datasets and trained models ready for deployment. These models can be utilized by the [Machine Learning API project](https://github.com/thiagofmiranda/machine-learning-api) for serving predictions and model-based services.

## Repository Structure

```
machine-learning-models/
├── data/
│   ├── language-detection.csv
│   └── ... # Data used for training and evaluation
├── models/
│   └── saved_models/
│       ├── language-detection-0.1.0.pkl
│       └── ... # More trained models ready for use
├── notebooks/
│   ├── language-detection.ipynb
│   └── ... # More Jupyter notebooks for ML studies
└── README.md
```

### Folder Details

- **`data/`**: This folder contains datasets used for training and evaluating the machine learning models. Ensure that data privacy and handling protocols are followed when using this folder.

- **`notebooks/`**: This folder holds Jupyter notebooks that explore, analyze, and train different machine learning models. The notebooks demonstrate preprocessing, model creation, training, and evaluation steps.

- **`models/saved_models/`**: This folder stores the trained machine learning models in various formats (e.g., `.pkl`, `.h5`) that are ready to be used by other services such as the [Machine Learning API project](https://github.com/thiagofmiranda/machine-learning-api) for serving predictions.

## Getting Started

1. **Environment Setup**:
   - Ensure you have Python installed (recommended version >= 3.7).
   - Create a virtual environment and install dependencies:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     pip install -r requirements.txt
     ```
   - Note: Ensure any dependencies required for specific Jupyter notebooks are also installed.

2. **Running the Jupyter Notebooks**:
   - Launch Jupyter Notebook in your browser to explore or modify existing models.
     ```bash
     jupyter notebook
     ```
   - Open any of the notebooks in the `notebooks/` directory to begin your exploration.

3. **Data Usage**:
   - Place data files in the `data/` directory.
   - Ensure data formatting and preprocessing steps align with the requirements of the models you are working on.

4. **Trained Models for Deployment**:
   - Trained models stored in `models/saved_models/` can be used for deployment. Integrate these models into your API or other services for predictions.

## Integration with Machine Learning API

- This repository complements the [Machine Learning API project](https://github.com/thiagofmiranda/machine-learning-api) by providing trained models that are ready to be served through a web API.
- The API project can utilize models from the `models/saved_models/` folder for serving real-time predictions, offering a seamless pipeline from model training to deployment.

## Contributing

Contributions, such as improvements to models, data preprocessing, or adding new studies, are welcome! Please open an issue or submit a pull request to propose changes or enhancements.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute as per the license terms.