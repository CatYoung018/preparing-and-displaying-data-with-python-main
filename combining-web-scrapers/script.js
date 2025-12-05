// Use relative URLs since frontend and backend are on same domain
const API_BASE_URL = '';  // Empty string means same domain

// Event listeners for buttons 
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('scrapeBtn').addEventListener('click', scrapeData);
    document.getElementById('loadBtn').addEventListener('click', loadData);
    
    // Auto-load cached data on page load
    loadData();
    
    // Back to Top Button Setup
    setupBackToTop();
});

async function scrapeData() {
    const btn = document.getElementById('scrapeBtn');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    
    btn.disabled = true;
    btn.setAttribute('aria-busy', 'true');
    loading.style.display = 'block';
    results.innerHTML = '';
    
    try {
        const response = await fetch(`/api/scrape`);
        const data = await response.json();
        displayData(data);
        
        // Announce completion to screen readers
        announceToScreenReader('Data scraping completed successfully');
    } catch (error) {
        results.innerHTML = '<p style="color: red;" role="alert">Error: ' + error.message + '</p>';
        announceToScreenReader('Error occurred while scraping data');
    } finally {
        btn.disabled = false;
        btn.setAttribute('aria-busy', 'false');
        loading.style.display = 'none';
    }
}

async function loadData() {
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    
    loading.style.display = 'block';
    results.innerHTML = '';
    
    try {
        const response = await fetch('http://127.0.0.1:5000/api/data');
        const data = await response.json();
        displayData(data);
        announceToScreenReader('Data loaded successfully');
    } catch (error) {
        results.innerHTML = '<p style="color: red;" role="alert">No cached data available. Please scrape first.</p>';
    } finally {
        loading.style.display = 'none';
    }
}

function displayData(data) {
    const results = document.getElementById('results');
    const stats = document.getElementById('stats');
    
    let totalAnimals = 0;
    let html = '';
    
    for (const [category, animals] of Object.entries(data)) {
        totalAnimals += animals.length;
        
        html += `
            <article class="category">
                <h2 class="category-title">${escapeHtml(category)}</h2>
                <div class="animals-grid" role="list">
        `;
        
        animals.forEach(animal => {
            html += `
                <div class="animal-card" role="listitem">
                    <div class="animal-name">${escapeHtml(animal.name)}</div>
                    <span class="animal-class" aria-label="Animal class: ${escapeHtml(animal.class)}">${escapeHtml(animal.class)}</span>
                    <a href="${escapeHtml(animal.url)}" 
                       target="_blank" 
                       rel="noopener noreferrer"
                       class="animal-link"
                       aria-label="View ${escapeHtml(animal.name)} on Wikipedia, opens in new tab">
                        View on Wikipedia →
                    </a>
                </div>
            `;
        });
        
        html += `
                </div>
            </article>
        `;
    }
    
    document.getElementById('totalAnimals').textContent = totalAnimals;
    document.getElementById('totalCategories').textContent = Object.keys(data).length;
    stats.style.display = 'flex';
    results.innerHTML = html;
}

// Helper function to announce to screen readers
function announceToScreenReader(message) {
    const announcement = document.createElement('div');
    announcement.setAttribute('role', 'status');
    announcement.setAttribute('aria-live', 'polite');
    announcement.className = 'sr-only';
    announcement.textContent = message;
    document.body.appendChild(announcement);
    
    // Remove after announcement
    setTimeout(() => {
        document.body.removeChild(announcement);
    }, 1000);
}

// Escape HTML to prevent XSS attacks (security bonus!)
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Back to Top Button Functionality
function setupBackToTop() {
    const backToTopButton = document.getElementById('backToTop');
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTopButton.classList.add('show');
        } else {
            backToTopButton.classList.remove('show');
        }
    });
    
    // Scroll to top when clicked
    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
        
        // Announce to screen readers
        announceToScreenReader('Scrolled to top of page');
    });
    
    // Keyboard support (Enter or Space)
    backToTopButton.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            backToTopButton.click();
        }
    });
}