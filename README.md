

# Student Performance Prediction and Risk Assessment

This project is a Flask web application that predicts a student's GPA based on their academic performance metrics. The application also determines the student's risk status based on predefined thresholds.

## Features

- **GPA Prediction**: Uses a trained Random Forest Regressor model to predict a student's GPA based on:
  - Semester 1 GPA
  - Semester 2 GPA
  - Attendance percentage
  - Number of assignments completed
- **Risk Assessment**: Flags students "At Risk" if:
  - Predicted GPA is below 7.0
  - Attendance is below 75%
  - Assignments completed are fewer than 6
- **Interactive Interface**: Frontend built with Flask's templating engine to allow user interaction.
- **REST API**: Exposes an endpoint for programmatic prediction and risk assessment.

## Dataset

The model is trained on a dataset (`student_performance.csv`) containing information about students' performance. Replace the dataset path in the script with the correct path on your system.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/student-performance-predictor.git
   ```
2. Install the required Python packages:
   ```bash
   pip install flask pandas numpy scikit-learn
   ```
3. Place the `student_performance.csv` dataset in the appropriate path.

## Usage

1. Run the Flask application:
   ```bash
   python main.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000/`.

### API Endpoint

- **`/predict`** (POST): Accepts a JSON payload with the following keys:
  - `sem1_gpa`: Semester 1 GPA (float)
  - `sem2_gpa`: Semester 2 GPA (float)
  - `attendance`: Attendance percentage (integer)
  - `assignments_completed`: Number of assignments completed (integer)

  **Response**:
  ```json
  {
    "Predicted GPA": 7.5,
    "Risk Status": "Not At Risk"
  }
  ```

## Example Request

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "sem1_gpa": 8.5,
  "sem2_gpa": 7.9,
  "attendance": 80,
  "assignments_completed": 10
}' http://127.0.0.1:5000/predict
```

## Project Structure

```
.
├── main.py               # Main application script
├── templates/
│   └── index.html        # Frontend template
├── student_performance.csv # Dataset (replace with your own)
└── README.md             # Project documentation
```

## Future Improvements

- Add more performance metrics to enhance the prediction accuracy.
- Implement user authentication for secure access.
- Visualize GPA predictions and risk analysis with charts.
- Deploy the application to a cloud platform like Heroku or AWS.

