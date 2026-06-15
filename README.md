# Aicite Approval Portal

A web application that allows users to submit approval forms and manage authentication.

## Features
- Sign‑in with token stored in `sessionStorage` for automatic login across page reloads.
- Reactive navigation bar that updates Sign‑In / Logout state instantly.
- Approval form component with rich styling and validation.
- Backend API (FastAPI/Django) integration at `http://127.0.0.1:8000`.

## Prerequisites
- **Node.js** (v18+)
- **npm**
- **Python** 3.10+ with backend dependencies installed.

## Frontend Setup
```bash
# Clone the repository (if not already)
git clone <repo-url>
cd Aicite-Approval-Portal/Frontend

# Install dependencies
npm install

# Run development server
npm run dev
```
The app will be available at `http://localhost:5173`.

## Backend Setup
```bash
cd ../Backened
# Install Python dependencies (preferably in a virtualenv)
python -m venv env
env\Scripts\activate   # Windows
pip install -r requirements.txt

# Run the server
python manage.py runserver
```
The API runs on `http://127.0.0.1:8000`.

## Usage
1. Open the frontend URL in a browser.
2. Sign in using the form – upon successful login you will be redirected to the **Approval** page automatically.
3. Fill out the approval form and submit; the data is posted to the backend.
4. Use the navigation bar to logout; the UI updates instantly.

## Contributing
Feel free to open issues or submit pull requests. Follow the standard Git workflow:
```bash
git checkout -b feature/your-feature
# make changes
git commit -m "Add feature"
git push origin feature/your-feature
```

## License
MIT License – see `LICENSE` file for details.
