# Resume Analyzer 📄✨

## 🚀 Overview
**Resume Analyzer** is an innovative FastAPI-based application designed to simplify the resume evaluation process. It extracts text from PDF resumes and uses Google's Gemini AI API to analyze the content. This tool not only helps candidates improve their resumes with actionable feedback but also assists hiring managers by quickly identifying the most suitable applicants.

Whether you're a job seeker wanting to polish your resume or a recruiter aiming to streamline candidate screening, Resume Analyzer offers a powerful, automated solution.

## 🔧 Features
- **Upload PDF Resumes:** Easily upload your resume in PDF format.
- **Text Extraction:** Automatically extracts text from your PDF using robust parsing techniques.
- **AI-Powered Analysis:** Leverages the Gemini AI API to evaluate resumes, assessing skills, education, and experience.
- **Instant Feedback:** Returns a clear verdict on candidate suitability with recommendations.
- **User-Friendly API Documentation:** Explore the API interactively with Swagger and Redoc interfaces.

📂 File Descriptions
- **Content/geminiaicode.py**  
  The Heart of the Analyzer
  *The Core API & AI Integrator*  
  Sets up the main FastAPI application and defines endpoints that interface with Google's Gemini AI API. This file handles resume analysis by sending the extracted text to the AI and returning a verdict.

- **Content/pdfreader.py**  
  *The Resume Extractor*  
  Responsible for reading PDF files and extracting text. It ensures that resume data is accurately parsed before analysis.

- **Content/database.py**  
  *The Data Manager*  
  Manages database connections and operations. It sets up the connection to your database (e.g., using SQLAlchemy), ensuring that user data and resume analysis records are stored securely.

- **Content/models.py**  
  *The Data Models*  
  Contains definitions of the database models. These models represent the structure of your data (such as users, resumes, and analysis results) and are used by the ORM to interact with the database.

- **Content/schemas.py**  
  *The Data Validators*  
  Defines Pydantic schemas used for data validation and serialization. These schemas ensure that the data coming in and out of your API conforms to expected formats, which is crucial for maintaining data integrity.

- **Content/hashing.py**  
  *The Security Utility*  
  Provides functions for securely hashing passwords and other sensitive information. This is vital for user authentication and data protection.

- **Content/oauth2.py**  
  *The Authentication Gateway*  
  Implements OAuth2 protocols for generating and validating tokens. This module ensures that API endpoints are secured and accessible only to authorized users.

- **Content/token.py**  
  *The Token Handler*  
  Manages the creation, validation, and expiration of tokens. It works in tandem with `oauth2.py` to maintain secure authentication flows throughout the application.
- **requirements.txt**
  Dependency List
  This file lists all the Python libraries and packages required to run the project. It makes setting up the environment quick and straightforward.

## 🛠️ Installation

### **1️⃣ Clone the Repository**
Open your terminal and run:
git clone https://github.com/Siddharthpandey20/Resume_Analyser.git
cd Resume_Analyser
2️⃣ Create a Virtual Environment (Recommended)
Creating a virtual environment ensures dependencies are managed separately:
python -m venv environment
Activate the environment:

On Mac/Linux:
source environment/bin/activate
On Windows:
environment\Scripts\activate
3️⃣ Install Dependencies
Install all required packages:

pip install -r requirements.txt

🚀 Running the API

This project runs two separate API servers—one for the main functionality and another for PDF processing. Open two terminal windows:

Terminal 1: Start the Main API Server

uvicorn geminiaicode:app --reload

Terminal 2: Start the PDF Reader API Server

uvicorn pdfreader:app --host 127.0.0.1 --port 8001 --reload

Now, open your browser and visit:

Swagger UI: http://127.0.0.1:8000/docs
Redoc UI: http://127.0.0.1:8000/redoc

🏗️ How It Works
Upload a Resume: The application accepts a PDF resume via the /upload-resume/ endpoint.
Extract & Process: The text is extracted from the PDF and sent to the Gemini AI API.
AI Analysis: The API evaluates the content, checking for key details like skills, education, and experience.
Feedback: A verdict is returned indicating the candidate's suitability for a role, with insights for improvement.

📜 API Endpoints

Method	Endpoint	Description
POST	/upload-resume/	Upload a PDF resume for analysis
GET	/docs/	Access interactive API documentation (Swagger)

🌟 Future Scopes & Enhancements
Advanced AI Analysis:
Expand the resume evaluation by integrating more sophisticated NLP techniques to provide personalized feedback and deeper insights into a candidate's profile.

Multi-Format Support:
Extend support to additional file formats such as DOCX, or even scanned images using OCR technology, to widen the tool's usability.

Interactive Web Interface:
Develop a dynamic, user-friendly web portal that offers real-time resume analysis, interactive dashboards, and visual feedback to both job seekers and hiring managers.

Job Platform Integration:
Integrate the application with popular job boards and Applicant Tracking Systems (ATS) to streamline recruitment processes and offer automated candidate shortlisting.

Customizable Evaluation Metrics:
Allow users to define or adjust analysis criteria based on industry standards, job roles, or personal preferences, making the tool more adaptable.

Mobile Application:
Create a mobile app version of Resume Analyzer to provide on-the-go resume evaluation and instant feedback.

Data-Driven Insights:
Incorporate analytics and reporting features to help users understand trends in resume quality and identify common areas for improvement.

Enhanced Security & Privacy:
Improve data protection measures to ensure that sensitive personal information is securely handled, building trust with users and stakeholders.

🛠️ Built With

FastAPI: A modern, fast web framework for building APIs with Python.
Gemini AI API: Provides advanced, AI-driven analysis of resume content.
PyMuPDF: For efficient PDF text extraction.

💡 Why Resume Analyzer?
For Candidates:

Gain insights on how your resume stands out.
Receive tailored feedback to improve presentation and content.
Understand which skills and experiences are in demand.
For Hiring Managers:

Quickly filter through resumes with an objective, AI-driven analysis.
Save time during the recruitment process by identifying the best-fit candidates.
Enhance your recruitment strategy with data-driven insights.

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch:

git checkout -b feature-branch

Make your changes and commit them:

git commit -m "Added feature XYZ"

Push your branch to GitHub:

git push origin feature-branch

Open a Pull Request for review.

👤 Contact

Siddharth Pandey

📧 siddharthpandeyofficial@gmail.com

📍 IIIT Naya Raipur

📜 License
This project is open-source and available under the MIT License.

If you find this project useful, please consider giving it a star on GitHub. Thank you for your interest and happy coding!
