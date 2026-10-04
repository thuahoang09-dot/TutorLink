// TutorLink Main JS
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips if Bootstrap is present
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Initialize Theme Switcher
    initThemeToggle();
});

// Theme Switcher Logic
function initThemeToggle() {
    if (window.syncThemeUI) {
        window.syncThemeUI();
    }

    const legacyBtn = document.getElementById('theme-toggle-btn');
    if (legacyBtn) {
        legacyBtn.addEventListener('click', function(e) {
            e.preventDefault();
            if (window.toggleThemeMode) {
                window.toggleThemeMode();
            }
        });
    }
}

function confirmAction(message) {
    return confirm(message || "Bạn có chắc chắn muốn thực hiện thao tác này?");
}
