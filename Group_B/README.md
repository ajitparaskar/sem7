# Group B Jupyter Notebooks

Install: `pip install numpy pandas scikit-learn matplotlib notebook`

Open any `.ipynb` in Jupyter Notebook, JupyterLab, VS Code or Colab. Run all cells. Set CSV_PATH in the second cell to your dataset path. Without a CSV, synthetic demonstration data is used.

- B1: Uber Fare Prediction: Linear vs Random Forest, outliers, correlation, R2, RMSE — https://www.kaggle.com/yasserh/uber-fares-dataset
- B2: Spam Classification: KNN vs SVM — https://www.kaggle.com/uciml/sms-spam-collection-dataset
- B3: Bank Customer Churn: Neural Network — https://www.kaggle.com/competitions/churn-modelling/data
- B4: Diabetes Prediction: KNN and classification metrics — https://www.kaggle.com/mragpavank/pima-indians-diabetes-database/data
- B5: Customer Segmentation: K-Means and elbow method — https://www.kaggle.com/search?q=sales_data_sample.csv

B3 uses scikit-learn MLPClassifier (neural network). B5 writes B5_elbow.png and B5_customer_clusters.csv to the current working directory.
