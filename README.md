# Prosperity Prognosticator: Machine Learning for Startup Success Prediction

Prosperity Prognosticator is a machine learning–based application designed to predict the **success or failure of startups** using historical startup data. The system analyzes key business parameters such as funding details, milestones, and organizational attributes to provide **data-driven insights** that support entrepreneurs and investors in making informed decisions.

---

## Team Details

| Field           | Information            |
| --------------- | ---------------------- |
| **Team ID**     | LTVIP2026TMIDS66150    |
| **Team Size**   | 4                      |
| **Team Leader** | Pathakota Harinath     |
| **Member 1**    | Bodimani Yagna Deepika |
| **Member 2**    | Shaik Asreen           |
| **Member 3**    | Derangula Rupa         |

---

## Project Demo

*https\://drive.google.com/file/d/1Ld\_tLOjF\_IIM9jY6dTCe8hy0fsYKXzyw/view?usp=sharing*

---

## Technologies Used

| Category             | Technology          |
| -------------------- | ------------------- |
| Programming Language | Python              |
| Machine Learning     | Scikit-learn        |
| Data Processing      | Pandas, NumPy       |
| Visualization        | Matplotlib, Seaborn |
| Web Framework        | Flask               |
| Interface            | HTML, CSS           |
| Model Storage        | Joblib / Pickle     |
| Platform             | jupyter notebook    |
| Repository           | GitHub              |

---

## Dataset

- **Source:** Kaggle
- **Dataset Name:** Startup Success Prediction
- **Link:** [https://www.kaggle.com/datasets/manishkc06/startup-success-prediction](https://www.kaggle.com/datasets/manishkc06/startup-success-prediction)

The dataset contains historical startup information such as funding rounds, milestones, startup age, and business relationships.

---

## Project Setup

### 1. Clone the Repository

```bash
git clone <your-github-repo-link>
cd startup_pred
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\\Scripts\\activate
```

**Linux / Mac**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install flask pandas numpy scikit-learn matplotlib seaborn joblib
```

### 4. Train the Model

Run the Jupyter Notebook to train the model:

```bash
jupyter notebook startup-prediction-eda-model.ipynb
```

This process performs:

- Exploratory Data Analysis (EDA)
- Data preprocessing
- Model training and evaluation

The trained model is saved as:

```
random_forest_model.pkl
```

### 5. Run the Web Application

```bash
python app.py
```

Open the browser and navigate to:

```
http://127.0.0.1:5000/
```

Enter startup parameters and click **Predict** to view the result.

---

## Project Structure

```text
startup_pred/
│
├── app.py
├── random_forest_model.pkl
├── startup_data.csv
├── startup-prediction-eda-model.ipynb
├── templates/
│   ├── index.html
│   |---result.html
|   |---adaptivity.html
|   |---home.html
└── static/ (optional)
```

---

## Expected Results

- Accurate prediction of startup success or failure
- Fast predictions using a trained ML model
- User-friendly web interface
- Reliable and repeatable results

---

## Future Enhancements

- Integration with cloud platforms (AWS / GCP / Azure)
- Use of advanced ML models such as XGBoost or Neural Networks
- Authentication and role-based access control
- Larger and more diverse datasets
- Advanced dashboards and analytics

---

## Conclusion

Prosperity Prognosticator demonstrates how **machine learning** can be effectively applied to real-world business problems. By integrating data analysis, predictive modeling, and web deployment, the project delivers a practical startup success prediction system that supports data-driven decision-making.

---

## License

This project is developed for **educational and research purposes only**.

