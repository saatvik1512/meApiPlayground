# Me-API Playground

A backend assessment project that stores candidate profile information and exposes it via a REST API with a minimal frontend.

## Architecture

- **Backend**: Flask (Python) with SQLite database
- **Frontend**: React.js
- **Database**: SQLite
- **API**: RESTful endpoints for CRUD operations and queries

## Setup

### Local Development

#### Backend
1. Navigate to the project directory
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Seed the database: `python seed_data.py`
6. Run the server: `python app.py`

#### Frontend
1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Start the development server: `npm start`

### Production Deployment

The application can be deployed to platforms like:
- **Backend**: Heroku, Render, or PythonAnywhere
- **Frontend**: Netlify, Vercel, or GitHub Pages
- **Database**: For production, consider using PostgreSQL or MySQL instead of SQLite

## API Endpoints

- `GET /health` - Health check
- `GET /profile` - Get candidate profile
- `PUT /profile` - Update candidate profile
- `GET /projects` - Get all projects
- `GET /projects?skill={skill}` - Filter projects by skill
- `GET /skills/top` - Get top skills
- `GET /search?q={query}` - Search across all data

## Database Schema

The SQLite database consists of the following tables:
- `profile` - Stores basic candidate information
- `skill` - Stores skills associated with the candidate
- `project` - Stores project details
- `work_experience` - Stores work experience
- `link` - Stores external links (GitHub, LinkedIn, etc.)

## Sample Requests

### Get Profile
```bash
curl -X GET http://localhost:5000/profile
```
### Get Profile
```bash
curl -X GET http://localhost:5000/profile
```
### Update Profile
```bash
curl -X PUT http://localhost:5000/profile \
  -H "Content-Type: application/json" \
  -d '{"name": "New Name", "email": "new@email.com"}'
```
### Get Projects by Skill
```bash
curl -X GET "http://localhost:5000/projects?skill=python"
```
### Search
```bash
curl -X GET "http://localhost:5000/search?q=python"
```
## Known Limitations
- SQLite is used which may not be suitable for production environments with high traffic
- No authentication mechanism for write operations
- Basic error handling with limited validation
- Frontend is minimal and not optimized for mobile devices

## Resume
This is my resume [Saatvik Pathak Resume](https://drive.google.com/file/d/1eAlRB-wDkrPMHr7_dBYeWFWXJmNVvXTD/view).

## Live Demo
- [Backend](https://meapiplayground.onrender.com/health)
- [FrontEnd](http://localhost:3000/)
