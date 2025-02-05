document.addEventListener('DOMContentLoaded', function () {
    const filterBox = document.getElementById('filterBox');
    const showFiltersBtn = document.getElementById('showFiltersBtn');

    // Check if we're on mobile
    const isMobile = window.innerWidth < 768;

    if (isMobile) {
        showFiltersBtn.addEventListener('click', () => {
            filterBox.classList.toggle('expanded');
            // Update button text
            showFiltersBtn.textContent = filterBox.classList.contains('expanded')
                ? 'Hide Filters'
                : 'Show Filters';
        });

        // Close filters when clicking outside
        document.addEventListener('click', (e) => {
            if (!filterBox.contains(e.target) &&
                !showFiltersBtn.contains(e.target) &&
                filterBox.classList.contains('expanded')) {
                filterBox.classList.remove('expanded');
                showFiltersBtn.textContent = 'Show Filters';
            }
        });

        // Prevent map interaction when touching the filter box
        filterBox.addEventListener('touchmove', (e) => {
            e.stopPropagation();
        });
    }
});