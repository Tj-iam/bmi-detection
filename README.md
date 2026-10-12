
# BMI Detection
A machine learning project to predict BMI (Body Mass Index) category from height and weight data.
## Project Overview
This project uses machine learning to classify BMI categories based on gender, height (cm), and weight (kg).
## Dataset
- **Source**: Custom dataset (bmi.csv)
- **Features**: Gender, Height (cm), Weight (kg)
- **Target**: BMI Index (0-5 categories)
  - 0: Underweight (Severe)
  - 1: Underweight (Weak)
  - 2: Normal
  - 3: Overweight
  - 4: Obesity (Moderate)
  - 5: Obesity (Severe)
## Tech Stack
- Python 3
- scikit-learn
- pandas
- numpy
- matplotlib
## How to Run
1. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`
2. Run the training script:
\`\`\`bash
python train.py
\`\`\`
## Results
| Metric | Value |
|--------|-------|
| Accuracy | XX% |
| Precision | XX% |
| Recall | XX% |
| F1 Score | XX% |
## Project Structure
\`\`\`
BMI PROJECT/
├── bmi.csv          # Dataset
├── train.py         # Training script
├── README.md        # This file
└── requirements.txt # Dependencies
\`\`\`
## Author
Tijani
## License
MIT
