// script.js (FINAL VERSION for PythonAnywhere)

// Event listeners for buttons 
document.addEventListener('DOMContentLoaded', () => {
    
    // 3. Auto-load cached data on page load
    loadData();
    
    // Back to Top Button Setup
    setupBackToTop();
});

// REMOVED: scrapeData function is not needed in the production frontend.

async function loadData() {
    // NOTE: 'loading' element is now present in index.html!
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    
    loading.style.display = 'block';
    results.innerHTML = '';
    
    try {
        // IMPORTANT: Use the relative URL /api/data
        const response = await fetch('/api/data'); 
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        displayData(data);
        announceToScreenReader('Data loaded successfully');
    } catch (error) {
        results.innerHTML = '<p style="color: red;" role="alert">Error loading data. Please check server status.</p>';
        announceToScreenReader('Error occurred while loading cached data');
    } finally {
        loading.style.display = 'none';
    }
}

// NOTE: displayData, announceToScreenReader, escapeHtml, and setupBackToTop 
// functions remain the same as your previous versions.