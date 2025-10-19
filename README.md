# AI Product Recommendation & Analytics Web App

This project is a full-stack application that uses Machine Learning, NLP, and Computer Vision to provide furniture recommendations. It features a FastAPI backend, a React frontend, and leverages Pinecone for vector search and Google's Gemini API for generative text.

## 🚀 Live Demo

*(Link to deployed application if available)*

## 📸 Screenshots

| Recommendation Page | Analytics Page |
| :---: | :---: |
| *(Insert Screenshot of Recommend Page)* | *(Insert Screenshot of Analytics Page)* |

## ✨ Features

- **AI-Powered Recommendations**: Get furniture recommendations based on natural language queries.
- **Hybrid Search**: Combines semantic search with a cross-encoder reranker for improved relevance.
- **Generative Descriptions**: Product descriptions are enhanced by Google's Gemini API.
- **Data Analytics**: An analytics dashboard provides insights into the product dataset.
- **Feedback Loop**: Users can provide feedback on recommendations.

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python
- **Frontend**: React, JavaScript
- **Vector Database**: Pinecone
- **GenAI**: Google Gemini
- **ML/NLP**: Sentence-Transformers, LangChain, Scikit-learn
- **CV**: CLIP
- **Deployment**: (e.g., Vercel, Heroku, AWS)

## 🏛️ Architecture

```
/------------------\      /------------------\      /------------------\
|   React Frontend |----->|  FastAPI Backend |----->|      Pinecone      |
\------------------/      \------------------/      \------------------/
        |                        |                        ^
        |                        |                        |
        v                        v                        |
/------------------\      /------------------\            |
| Analytics (Charts) |      |   Google Gemini  |------------/
\------------------/      \------------------/
```

## ⚙️ Setup and Installation

### Prerequisites

- Python 3.10+
- Node.js 14+
- Pinecone Account (API Key)
- Google Cloud Account (Gemini API Key)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/product-recommender.git
cd product-recommender
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in the `backend` directory and add your API keys:

```env
PINECONE_API_KEY=YOUR_PINECONE_API_KEY
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

### 3. Frontend Setup

```bash
cd ../frontend
npm install
```

## ▶️ Running the Application

### 1. Run the Backend Server

Navigate to the `backend` directory and run:

```bash
uvicorn main:app --reload
```

The backend will be available at `http://127.0.0.1:8000`.

### 2. Run the Frontend Development Server

Navigate to the `frontend` directory and run:

```bash
npm start
```

The frontend will be available at `http://localhost:3000`.

### 3. Data Processing and Model Training

Open and run the Jupyter Notebooks in the `notebooks` directory to process the data, train the models, and populate the Pinecone index.

1.  `notebooks/model_training.ipynb`: Cleans the data, generates embeddings, and populates the Pinecone index.
2.  `notebooks/analytics.ipynb`: Performs data analysis and generates insights.

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/recommend` | Fetches product recommendations. |
| `GET` | `/analytics` | Retrieves analytics data. |
| `GET` | `/health` | Health check for the backend. |
| `POST` | `/feedback` | Submits user feedback. |

## Design Choices

- **Reranking**: A cross-encoder is used to rerank the initial results from the vector search, which significantly improves the relevance of the recommendations.
- **CLIP for CV**: CLIP's zero-shot classification capabilities are used for image classification to avoid the need for a custom-trained model.
- **LangChain**: LangChain is used to streamline the interaction with the Gemini API, making the code cleaner and more modular.

## Limitations & Next Steps

- **Scalability**: The current analytics implementation reads from a CSV file on every request. For a production environment, this should be replaced with a more scalable solution like a data warehouse or a pre-computed analytics store.
- **Multi-Turn Conversation**: The recommendation engine is stateless. Future improvements could include session management to allow for multi-turn conversational queries.
- **Real-time Inventory**: The dataset is static. A real-world application would require integration with an inventory management system.
