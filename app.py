from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Profile, Skill, Project, WorkExperience, Link
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

with app.app_context():
    db.create_all()


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200


@app.route('/profile', methods=['GET', 'PUT'])
def profile():
    if request.method == 'GET':
        profile = Profile.query.first()
        if not profile:
            return jsonify({"error": "Profile not found"}), 404
            
        profile_data = {
            "id": profile.id,
            "name": profile.name,
            "email": profile.email,
            "education": profile.education,
            "skills": [skill.name for skill in profile.skills],
            "projects": [{
                "id": p.id,
                "title": p.title,
                "description": p.description,
                "skills": p.skills_str.split(",") if p.skills_str else [],
                "links": p.links.split(",") if p.links else []
            } for p in profile.projects],
            "work_experience": [{
                "id": w.id,
                "company": w.company,
                "position": w.position,
                "duration": w.duration,
                "description": w.description
            } for w in profile.work_experiences],
            "links": {link.platform: link.url for link in profile.links}
        }
        return jsonify(profile_data), 200
        
    elif request.method == 'PUT':
        data = request.json
        profile = Profile.query.first()
        
        if not profile:
            profile = Profile(
                name=data.get('name'),
                email=data.get('email'),
                education=data.get('education')
            )
            db.session.add(profile)
        else:
            if 'name' in data:
                profile.name = data['name']
            if 'email' in data:
                profile.email = data['email']
            if 'education' in data:
                profile.education = data['education']
        
        db.session.commit()
        return jsonify({"message": "Profile updated successfully"}), 200


@app.route('/projects', methods=['GET'])
def get_projects():
    skill_filter = request.args.get('skill')
    projects = Project.query.all()
    
    if skill_filter:
        projects = [p for p in projects if p.skills_str and skill_filter.lower() in p.skills_str.lower()]
    
    result = [{
        "id": p.id,
        "title": p.title,
        "description": p.description,
        "skills": p.skills_str.split(",") if p.skills_str else [],
        "links": p.links.split(",") if p.links else []
    } for p in projects]
    
    return jsonify(result), 200

@app.route('/skills/top', methods=['GET'])
def top_skills():
    
    skills = Skill.query.all()
    skill_counts = {}
    
    for skill in skills:
        if skill.name in skill_counts:
            skill_counts[skill.name] += 1
        else:
            skill_counts[skill.name] = 1

    top_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    return jsonify([{"skill": skill, "count": count} for skill, count in top_skills]), 200

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    
    results = {
        "projects": [],
        "skills": [],
        "work_experience": []
    }
    
    projects = Project.query.filter(
        (Project.title.ilike(f"%{query}%")) | 
        (Project.description.ilike(f"%{query}%")) |
        (Project.skills_str.ilike(f"%{query}%"))
    ).all()
    
    results["projects"] = [{
        "id": p.id,
        "title": p.title,
        "description": p.description
    } for p in projects]
    
    skills = Skill.query.filter(Skill.name.ilike(f"%{query}%")).all()
    results["skills"] = [s.name for s in skills]
    
    #  work experience
    work_exps = WorkExperience.query.filter(
        (WorkExperience.company.ilike(f"%{query}%")) | 
        (WorkExperience.position.ilike(f"%{query}%")) |
        (WorkExperience.description.ilike(f"%{query}%"))
    ).all()
    
    results["work_experience"] = [{
        "id": w.id,
        "company": w.company,
        "position": w.position
    } for w in work_exps]
    
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)