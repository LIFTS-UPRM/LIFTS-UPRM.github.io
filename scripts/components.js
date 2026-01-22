/**
 * LIFTS Website - Component Library
 * Reusable JavaScript components
 */

// Toast Notification System
const Toast = {
    container: null,
    
    init() {
        this.container = document.createElement('div');
        this.container.className = 'toast-container';
        document.body.appendChild(this.container);
    },
    
    show(message, type = 'info', duration = 3000) {
        if (!this.container) this.init();
        
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.textContent = message;
        
        this.container.appendChild(toast);
        
        setTimeout(() => {
            toast.style.opacity = '0';
            setTimeout(() => toast.remove(), 300);
        }, duration);
    },
    
    success(message) { this.show(message, 'success'); },
    error(message) { this.show(message, 'error'); },
    warning(message) { this.show(message, 'warning'); }
};

// Modal System
const Modal = {
    open(id) {
        const modal = document.getElementById(id);
        if (modal) {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    },
    
    close(id) {
        const modal = document.getElementById(id);
        if (modal) {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }
    },
    
    init() {
        // Close on backdrop click
        document.querySelectorAll('.modal-backdrop').forEach(backdrop => {
            backdrop.addEventListener('click', () => {
                const modal = backdrop.closest('.modal');
                if (modal) this.close(modal.id);
            });
        });
        
        // Close on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                document.querySelectorAll('.modal.active').forEach(modal => {
                    this.close(modal.id);
                });
            }
        });
    }
};

// Accordion Component
const Accordion = {
    init() {
        document.querySelectorAll('.accordion-header').forEach(header => {
            header.addEventListener('click', () => {
                const item = header.parentElement;
                const isActive = item.classList.contains('active');
                
                // Close all items in same accordion
                const accordion = item.closest('.accordion');
                accordion.querySelectorAll('.accordion-item').forEach(i => {
                    i.classList.remove('active');
                });
                
                // Toggle clicked item
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        });
    }
};

// Tabs Component
const Tabs = {
    init() {
        document.querySelectorAll('.tab-button').forEach(button => {
            button.addEventListener('click', () => {
                const tabId = button.dataset.tab;
                const tabs = button.closest('.tabs');
                
                // Update buttons
                tabs.querySelectorAll('.tab-button').forEach(btn => {
                    btn.classList.remove('active');
                });
                button.classList.add('active');
                
                // Update panels
                tabs.querySelectorAll('.tab-panel').forEach(panel => {
                    panel.classList.remove('active');
                });
                tabs.querySelector(`#${tabId}`).classList.add('active');
            });
        });
    }
};

// Initialize all components
document.addEventListener('DOMContentLoaded', () => {
    Modal.init();
    Accordion.init();
    Tabs.init();
});

// Export for module usage
if (typeof module !== 'undefined') {
    module.exports = { Toast, Modal, Accordion, Tabs };
}
