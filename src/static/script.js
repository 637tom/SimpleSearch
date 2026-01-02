const searchInput = document.getElementById('searchInput');

searchInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        performSearch();
    }
});

async function performSearch() {
    const query = searchInput.value;
    if (!query) return;

    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '<li style="text-align:center">Searching...</li>';

    try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();

        resultsContainer.innerHTML = '';

        if (data.length === 0) {
            resultsContainer.innerHTML = '<li class="no-results">No results found</li>';
            return;
        }

        data.forEach(result => {
            const li = document.createElement('li');
            li.className = 'result-item';
            li.innerHTML = `
                <div class="result-title"><a href="${result.url}" target="_blank">${result.title}</a></div>
                <div class="result-url">${result.url}</div>
            `;
            resultsContainer.appendChild(li);
        });
    } catch (error) {
        console.error('Error:', error);
        resultsContainer.innerHTML = '<li style="color:red; text-align:center">Error performing search</li>';
    }
}
