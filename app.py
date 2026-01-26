from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    projects = [
        {
            "title": "Deep Learning-based SAITS for Ionospheric TEC Modeling",
            "description": (
                "Developed a deep learning-based SAITS model for ionospheric Total Electron Content (TEC) "
                "modelling using GNSS data. Focused on improving prediction accuracy through data curation "
                "and comparative analysis."
            ),
            "tech": ["Python", "Machine Learning", "Deep Learning", "GNSS", "SAITS"],
            "github": ""
        },
        {
            "title": "Lung Cancer Nodule Classification using Deep Learning",
            "description": (
                "Designed a deep learning system using MobileNet and Inception architectures to classify "
                "CT scan lung nodules as benign or malignant, improving diagnostic accuracy and reducing "
                "analysis time."
            ),
            "tech": ["Python", "Deep Learning", "MobileNet", "Inception", "Image Processing"],
            "github": ""
        }
    ]

    return render_template(
        "index.html",
        name="Marri Saranya",
        title="Computer Science Engineer",
        email="marrisaranya12@gmail.com",
        github="https://github.com/Saranya2328",
        linkedin="https://www.linkedin.com/in/m-saranya23",
        about=(
            "Computer Science Engineer with hands-on experience in AI/ML, medical image processing, GNSS data analysis, and Python–Flask backend development. Worked as a Lab Engineer Trainee (GNSS) at IIT Tirupati Navavishkar I-Hub Foundation. Passionate about AI tools and building intelligent solutions for real-world applications."
            
        ),
        skills={
            "Programming": ["Python", "Java", "SQL"],
            "AI / ML": ["Machine Learning", "Deep Learning", "Scikit-learn"],
            "Backend": ["Flask", "FastAPI"],
            "Web": ["HTML", "CSS", "JavaScript", "ReactJS", "Tailwind"],
            "Tools": ["Git", "GitHub", "VS Code", "Google Colab"]
        },
        experience={
            "role": "Lab Engineer (GNSS)",
            "org": "IIT Tirupati Navavishkar I-Hub Foundation",
            "duration": "Mar 2025 – Sep 2025",
            "points": [
                "Processed and structured large-scale GNSS GPS time-series data by filtering constellations and converting high-frequency timestamps to hourly resolution.",
                "Implemented a SAITS deep learning model to capture temporal patterns and perform event-based analysis on GNSS data.",
                "Visualized phase-wise and event-driven variations using scientific plotting techniques for temporal interpretation.",
                "Evaluated model performance using quantitative metrics and developed supporting GPS ↔ Gregorian calendar conversion tools in Python."
            ]
        },
        projects=projects
    )

if __name__ == "__main__":
    app.run()

