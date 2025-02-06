document.addEventListener('DOMContentLoaded', function () {
    const filterBox = document.getElementById('filterBox');
    const showFiltersBtn = document.getElementById('showFiltersBtn');

    // Check if we're on mobile
    // const isMobile = window.innerWidth < 768;

    // Function to remove mobile functionality
    function cleanupMobileView() {
        showFiltersBtn.removeEventListener('click', toggleFilters);
        document.removeEventListener('click', handleOutsideClick);
    }

    // if (isMobile) {
    function setupMobileView() {
        showFiltersBtn.addEventListener('click', toggleFilters);

        // Close filters when clicking outside
        document.addEventListener('click', handleOutsideClick);
      

        // Prevent map interaction when touching the filter box
        filterBox.addEventListener('touchmove', (e) => {
            e.stopPropagation();
        });
    }

    function toggleFilters() {
        filterBox.classList.toggle('expanded');
        
        // Update button text
        showFiltersBtn.textContent = filterBox.classList.contains('expanded')
            ? 'Hide Filters'
            : 'Show Filters';
    }

    function handleOutsideClick(e) {
        if (!filterBox.contains(e.target) &&
            !showFiltersBtn.contains(e.target) &&
            filterBox.classList.contains('expanded')) 
            {
                filterBox.classList.remove('expanded');
                showFiltersBtn.textContent = 'Show Filters';
            }
    }

    // Function to handle resize
    function handleResize() {
        const isMobile = window.innerWidth < 768;

        // Remove any existing classes/listeners
        cleanupMobileView();
        filterBox.classList.remove('expanded');
        showFiltersBtn.textContent = 'Show Filters';

        // Setup mobile view if needed
        if (isMobile) {
            setupMobileView();
        }
    }

    // Initial setup
    handleResize();

    // Listen for window resize
    window.addEventListener('resize', handleResize);


});