# 📊 Mean-Variance-Standard-Deviation-Calculator
A calculator that computes mean, variance, standard deviation, min, max, and sum for a 3×3 matrix, created as part of the FreeCodeCamp - Data Analysis with Python certification.
## ✨ Features
- Calculates statistics for:
  - Each row
  - Each column
  - The entire matrix
- Built with clean modular code.
- Includes input validation and error handling.
- Compatible with FreeCodeCamp’s automated test suite.
## 📋 Prerequisites
Before running this project, ensure you have:
- Python 3.8+
- NumPy
- A basic understanding of Python lists and matrices
## 🚀 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/your-username/Mean-Variance-Standard-Deviation-Calculator.git
cd Mean-Variance-Standard-Deviation-Calculator
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the project:
```bash
python main.py
```
## 🎬 Screenshots / Demo
(Coming Soon...)
## 🗂️ Project Structure
```
📁 Mean-Variance-Standard-Deviation-Calculator
├── main.py             # Entry script (if exists)
├── mean_var_std.py     # Core calculations
├── test_module.py      # FCC test script
├── requirements.txt
└── README.md

```
## 🛠️ Usage
Example usage inside Python:
```python
from mean_var_std import calculate

result = calculate([0,1,2,3,4,5,6,7,8])
print(result)

```
Expected output:
```python
{
  'mean': [1., 4., 7.],
  'variance': [...],
  'standard deviation': [...],
  'max': [...],
  'min': [...],
  'sum': [...]
}

```
## 💾 Data Storage
No data is stored.
All calculations are performed in-memory on the provided list.
## ✅ Tests
Run the FreeCodeCamp test suite:
```bash
python test_module.py
```
## 🤝 Contributing
Contributions are welcome!
1. Fork the repository
2. Create a new feature branch
3. Submit a pull request
Please ensure your code is clean structure and well-commented.
## 📝 License
This project is licensed under the MIT license - see the LICENSE file for details. 
## 📞 Support
If you have questions or issues:
Open an Issue on GitHub
Or contact me on LinkedIn
