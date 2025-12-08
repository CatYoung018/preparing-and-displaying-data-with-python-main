// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    // Auto-load cached data on page load
    loadData();
    
    // Back to Top Button Setup
    setupBackToTop();
});

async function loadData() {
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    
    loading.style.display = 'block';
    results.innerHTML = '';
    
    try {
        const response = await fetch('/api/data');
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        displayData(data);
        announceToScreenReader('Data loaded successfully');
    } catch (error) {
        console.error('Error:', error);
        results.innerHTML = '<p style="color: red;" role="alert">Error loading data: ' + error.message + '</p>';
        announceToScreenReader('Error occurred while loading cached data');
    } finally {
        loading.style.display = 'none';
    }
}

function displayData(data) {
    const results = document.getElementById('results');
    const stats = document.getElementById('stats');
    results.innerHTML = '';
    
    let totalAnimals = 0;
    const categories = Object.keys(data);
    
    categories.forEach(category => {
        totalAnimals += data[category].length;
        
        const categoryDiv = document.createElement('div');
        categoryDiv.className = 'category';
        
        const categoryTitle = document.createElement('h2');
        categoryTitle.className = 'category-title';
        categoryTitle.textContent = category;
        categoryDiv.appendChild(categoryTitle);
        
        const animalsGrid = document.createElement('div');
        animalsGrid.className = 'animals-grid';
        animalsGrid.setAttribute('role', 'list');
        
        data[category].forEach(animal => {
            const card = document.createElement('article');
            card.className = 'animal-card';
            card.setAttribute('role', 'listitem');
            
            const name = document.createElement('div');
            name.className = 'animal-name';
            name.textContent = escapeHtml(animal.name);
            
            const classLabel = document.createElement('span');
            classLabel.className = 'animal-class';
            classLabel.textContent = escapeHtml(animal.class || 'Unknown');
            classLabel.setAttribute('aria-label', `Classification: ${animal.class || 'Unknown'}`);
            
            const link = document.createElement('a');
            link.href = animal.url;
            link.className = 'animal-link';
            link.textContent = 'Learn more';
            link.setAttribute('aria-label', `Learn more about ${animal.name}`);
            link.target = '_blank';
            link.rel = 'noopener noreferrer';
            
            card.appendChild(name);
            card.appendChild(classLabel);
            card.appendChild(link);
            animalsGrid.appendChild(card);
        });
        
        categoryDiv.appendChild(animalsGrid);
        results.appendChild(categoryDiv);
    });
    
    document.getElementById('totalAnimals').textContent = totalAnimals;
    document.getElementById('totalCategories').textContent = categories.length;
    stats.style.display = 'flex';
}

function announceToScreenReader(message) {
    const announcement = document.createElement('div');
    announcement.setAttribute('role', 'status');
    announcement.setAttribute('aria-live', 'polite');
    announcement.className = 'sr-only';
    announcement.textContent = message;
    document.body.appendChild(announcement);
    setTimeout(() => document.body.removeChild(announcement), 1000);
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function setupBackToTop() {
    const backToTopButton = document.getElementById('backToTop');
    
    if (!backToTopButton) {
        console.error('Back to top button not found');
        return;
    }
    
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTopButton.classList.add('show');
        } else {
            backToTopButton.classList.remove('show');
        }
    });
    
    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
        announceToScreenReader('Scrolled to top of page');
    });
    
    backToTopButton.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            backToTopButton.click();
        }
    });
}