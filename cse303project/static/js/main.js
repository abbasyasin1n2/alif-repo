document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');
    const toggleBtn = document.querySelector('#sidebar-toggle');

    // Check localStorage for sidebar state
    if (localStorage.getItem('sidebarCollapsed') === 'true') {
        sidebar.classList.add('collapsed');
        mainContent.classList.add('expanded');
    }

    toggleBtn.addEventListener('click', function () {
        sidebar.classList.toggle('collapsed');
        mainContent.classList.toggle('expanded');
        // Save state to localStorage
        localStorage.setItem('sidebarCollapsed', sidebar.classList.contains('collapsed'));
    });

    var elems = document.querySelectorAll('.submenu-trigger');
    elems.forEach(function(elem) {
        elem.addEventListener('click', function(event) {
            if (!sidebar.classList.contains('collapsed')) {
                event.preventDefault();
                this.classList.toggle('active');
            }
        });
    });
});
