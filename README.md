# Sentiment and Emotion Analysis Tool

This project is a sentiment and emotion analysis tool that classifies text data (e.g., customer reviews, social media posts) into sentiment categories (positive, negative, neutral) and emotion categories (happiness, anger, sadness).

## Technologies Used:
- Python
- Hugging Face Transformers
- FastAPI
- PyTorch
- Scikit-learn

## How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-emotion-analysis.git
   ```

2. Navigate to the project folder:
   ```bash
   cd sentiment-emotion-analysis
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate # On macOS/Linux
   ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```

## License:
This project is licensed under the MIT License.
