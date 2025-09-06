from app import app, db
from models import Profile, Skill, Project, WorkExperience, Link

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create profile with YOUR information
        profile = Profile(
            name="Saatvik Pathak",
            email="pathaksaatvik15@gmail.com",
            education="B.Tech in Computer Science and Engineering, Shri Ram Institute of Technology (CGPA: 7.84, 2021-2025)"
        )
        db.session.add(profile)
        db.session.commit()
        
        # Add YOUR skills
        skills = [
            "Python", "Java", "JavaScript", "SQL", "HTML/CSS",
            "Spring Boot", "Flask", "Streamlit", "Node.js", "Express.js", "React.js",
            "Hugging Face Transformers", "LangChain",
            "MySQL", "PostgreSQL", "MongoDB", "SQLite",
            "Git", "GitHub", "Postman", "Docker", "REST APIs",
            "OAuth 2.0", "JWT", "Gmail API", "Gemini API"
        ]
        for skill_name in skills:
            skill = Skill(name=skill_name, profile_id=profile.id)
            db.session.add(skill)
        
        # Add YOUR projects
        projects = [
            {
                "title": "Bus Management System",
                "description": "Full-stack system with Spring Boot backend and React frontend; role-based access (Admin, SuperAdmin, User), JWT auth, REST APIs for buses, stops, and admins, containerized with Docker.",
                "skills": "Java,Spring Boot,React,MongoDB,Docker",
                "links": "https://github.com/saatvik1512/busManagementApplication"
            },
            {
                "title": "Mail Master – AI Email Assistant",
                "description": "AI-powered tool using Gemini API + Gmail API for drafting, scheduling, and sending mails; Flask-based web app with real-time suggestions reducing manual effort by 70%.",
                "skills": "Python,Flask,Gemini API,Gmail API,OAuth2",
                "links": "https://github.com/saatvik1512/mailmaster"
            },
            {
                "title": "News Summarizer",
                "description": "Flask app fetching real-time news via NewsAPI, summarizing and analyzing sentiment using Hugging Face Transformers (DistilBERT). Includes auth, article saving, and interactive UI with dark mode.",
                "skills": "Python,Flask,Hugging Face,DistilBERT,SQLite",
                "links": "https://github.com/saatvik1512/News-Summarizer"
            }
        ]
        
        for proj in projects:
            project = Project(
                title=proj["title"],
                description=proj["description"],
                skills_str=proj["skills"],
                links=proj["links"],
                profile_id=profile.id
            )
            db.session.add(project)
        
        # Add YOUR work experience
        work_experiences = [
            {
                "company": "Infosys SpringBoard",
                "position": "AI Intern (Remote)",
                "duration": "Oct 2024 – Dec 2024",
                "description": "Developed a meeting analysis tool converting audio/video meetings into insights using Whisper (transcription), GPT-3.5 Turbo (action plan), Hugging Face (sentiment analysis), integrated with Gradio UI."
            }
        ]
        
        for work in work_experiences:
            work_exp = WorkExperience(
                company=work["company"],
                position=work["position"],
                duration=work["duration"],
                description=work["description"],
                profile_id=profile.id
            )
            db.session.add(work_exp)
        
        # Add YOUR links
        links = [
            {"platform": "GitHub", "url": "https://github.com/saatvik1512"},
            {"platform": "LinkedIn", "url": "https://linkedin.com/in/saatvik-pathak-46707523b"},
            {"platform": "Portfolio", "url": "mailto:pathaksaatvik15@gmail.com"}  # can update with actual portfolio later
        ]
        
        for link in links:
            link_obj = Link(
                platform=link["platform"],
                url=link["url"],
                profile_id=profile.id
            )
            db.session.add(link_obj)
        
        db.session.commit()
        print("Database seeded successfully with Saatvik Pathak's data!")

if __name__ == '__main__':
    seed_data()