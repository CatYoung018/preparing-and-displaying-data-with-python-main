# 🐾 Endangered Species Tracker

A full-stack web application that scrapes endangered species data and displays it in an accessible, responsive interface. Built as a portfolio project demonstrating Python backend development, web scraping, API design, and accessible frontend implementation.

**[🌐 View Live Demo](https://cyoun002.pythonanywhere.com)**

---

## 🎬 Demo

![Endangered Species Tracker Demo](Endangered.gif)

*Auto-loads 198 endangered species with instant display, responsive design, and full accessibility support.*

---

## ✨ Features

- **Web Scraping**: Automatically scrapes endangered species data from source website and Wikipedia
- **Classification System**: Fetches biological classifications (Mammalia, Reptilia, etc.) from Wikipedia
- **REST API**: Flask backend with `/api/data` and `/api/scrape` endpoints
- **Instant Loading**: Pre-cached data for immediate display (no 3-4 minute wait)
- **Responsive Design**: Mobile-first CSS Grid layout with breakpoints for all devices
- **Full Accessibility**: 
  - WCAG 2.1 AA compliant
  - Screen reader support with ARIA labels
  - Keyboard navigation (Tab, Enter, Space)
  - Focus indicators and live regions
  - Reduced motion support
  - High contrast mode compatible
- **Back-to-Top Button**: Smooth scroll navigation with accessibility features
- **Professional UI**: Purple gradient design with hover effects and animations

---

## 🛠️ Tech Stack

**Backend:**
- Python 3.10
- Flask (web framework)
- Flask-CORS (API access)
- BeautifulSoup4 (web scraping)
- Requests (HTTP library)

**Frontend:**
- HTML5 (semantic markup)
- CSS3 (Grid, Flexbox, media queries)
- Vanilla JavaScript (ES6+)
- Fetch API (async data loading)

**Deployment:**
- PythonAnywhere (backend hosting)
- Git/GitHub (version control)

---
## 📊 Data

- **198 endangered species** across 7 categories
- **Critically Endangered, Endangered, Vulnerable** classification levels
- **Biological classifications** (Mammalia, Reptilia, Aves, etc.)
- **Direct Wikipedia links** for each species

---

## 🚀 Local Development Setup

### Prerequisites
- Python 3.10+
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/CatYoung018/preparing-and-displaying-data-with-python-main.git
cd preparing-and-displaying-data-with-python-main/combining-web-scrapers
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the backend**
```bash
python main.py
```
Backend runs on `http://127.0.0.1:5000`

5. **Serve the frontend** (in a separate terminal)
```bash
python3 -m http.server 8000
```
Frontend available at `http://localhost:8000`

6. **Visit the app**
Open your browser to `http://localhost:8000`

---

## 🌐 Deployment

**Backend:** Deployed on [PythonAnywhere](https://www.pythonanywhere.com)
- Persistent hosting with uWSGI
- Cached JSON data for instant loading
- CORS enabled for API access

**Why PythonAnywhere?**
- Free tier for portfolio projects
- Python-specific hosting (no cold starts)
- Always-on availability
- Perfect for bootcamp demonstrations

---

## 🎯 API Endpoints

### `GET /api/data`
Returns cached endangered species data
```json
{
  "Critically endangered(CR)": [
    {
      "name": "addax",
      "url": "/wiki/Addax",
      "class": "Mammalia"
    }
  ]
}
```

### `GET /api/scrape`
Scrapes fresh data (takes 3-4 minutes)
- Scrapes species list from source
- Fetches classifications from Wikipedia
- Caches results in `endangered_species.json`

---

## ♿ Accessibility Features

This project prioritizes accessibility for all users:

- **Semantic HTML5**: Proper use of `<main>`, `<header>`, `<nav>`, `<article>`, `<section>`
- **ARIA Attributes**: `role`, `aria-label`, `aria-live`, `aria-busy` for dynamic content
- **Keyboard Navigation**: Full site navigation without a mouse
- **Screen Reader Support**: Announcements for dynamic content updates
- **Focus Management**: Clear focus indicators (3px purple outline)
- **Color Contrast**: WCAG AA compliant color ratios
- **Motion Preferences**: Respects `prefers-reduced-motion`
- **Touch Targets**: Minimum 44×44px tap areas (WCAG 2.5.5)

---

## 📁 Project Structure
```
combining-web-scrapers/
├── venv/                          # Virtual environment
├── .gitignore                     # Git ignore rules
├── endangered_species.json        # Cached scraped data
├── index.html                     # Frontend structure
├── styles.css                     # Responsive styling
├── script.js                      # Data fetching & display
├── main.py                        # Flask backend & scraping
├── README.md                      # This file
└── requirements.txt               # Python dependencies
```

---

## 🎓 Learning Outcomes

This project demonstrates:

1. **Backend Development**: Building REST APIs with Flask
2. **Web Scraping**: Extracting structured data from HTML
3. **Async JavaScript**: Fetch API and promise handling
4. **Responsive Design**: Mobile-first CSS with media queries
5. **Accessibility**: WCAG compliance and inclusive design
6. **Version Control**: Git workflow and GitHub collaboration
7. **Deployment**: Production hosting configuration
8. **Problem Solving**: Debugging CORS, timing issues, caching

---

## 🔮 Future Enhancements

- [ ] Search/filter functionality
- [ ] Sort by classification or endangerment level
- [ ] Export data to CSV
- [ ] Species detail modal with images
- [ ] Auto-refresh data weekly via cron job
- [ ] PostgreSQL database integration
- [ ] User favorites/bookmarking system

---

## 🙏 Acknowledgments

- [Skillcrush](https://skillcrush.com/) - For the bootcamp curriculum
- Endangered species data source: [Skillcrush GitHub](https://skillcrush.github.io/web-scraping-endangered-species/)
- Animal classification data: [Wikipedia](https://wikipedia.org)

## 📧 Contact

**Cat Young**
- Portfolio: [catyoung018.github.io/Cat-Young-Dev](https://catyoung018.github.io/Cat-Young-Dev/)
- LinkedIn: [linkedin.com/in/catrilliayoung](https://linkedin.com/in/catrilliayoung)
- GitHub: [github.com/CatYoung018](https://github.com/CatYoung018)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Created as a portfolio project for Skillcrush - December 2025**

---


