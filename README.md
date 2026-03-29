# Community Resource Finder

A desktop application built with Python and PyQt5 that helps users search for community resources such as food banks, shelters, free clinics, mental health services, and job help by city or ZIP code.

## Demo

![App Screenshot](app.png)

---

## Features

- Search by city or ZIP code  
- Category-based resource search  
- Real-time results using Google Places API  
- Clean PyQt5 desktop interface  
- Scrollable results display  

---

## Technologies Used

- Python  
- PyQt5  
- Google Places API  
- requests  

---

## Project Structure

community-resource-finder/  
├── app.py  
├── README.md  
├── requirements.txt  
├── .gitignore  
└── services/  
  ├── __init__.py  
  └── places_api.py  

---

## How to Run

1. Clone the repository  
git clone https://github.com/rishabsati/community-resource-finder.git  

2. Navigate into the project folder  
cd community-resource-finder  

3. Install dependencies  
pip install -r requirements.txt  

4. Set your Google API key  

Windows (PowerShell):  
setx GOOGLE_API_KEY "your_api_key_here"  

Restart your terminal or VS Code after setting it.  

5. Run the application  
python app.py  

---

## Future Improvements

- Add map-based visualization of results  
- Improve UI styling and responsiveness  
- Add filters (distance, ratings, etc.)  
- Expand supported resource categories  

---

## Author

Rishab Sati  
ASU Computer Science Undergraduate