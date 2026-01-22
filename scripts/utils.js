/**
 * LIFTS Website - Utility Functions
 * Helper functions used across the site
 */

// Date formatting
const formatDate = (date, options = {}) => {
    const defaults = { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
    };
    return new Date(date).toLocaleDateString('en-US', { ...defaults, ...options });
};

// Time remaining calculation
const getTimeRemaining = (targetDate) => {
    const total = Date.parse(targetDate) - Date.now();
    return {
        total,
        days: Math.floor(total / (1000 * 60 * 60 * 24)),
        hours: Math.floor((total / (1000 * 60 * 60)) % 24),
        minutes: Math.floor((total / 1000 / 60) % 60),
        seconds: Math.floor((total / 1000) % 60)
    };
};

// Debounce function
const debounce = (func, wait = 250) => {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
};

// Throttle function
const throttle = (func, limit = 250) => {
    let inThrottle;
    return function executedFunction(...args) {
        if (!inThrottle) {
            func(...args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
};

// Smooth scroll to element
const scrollTo = (element, offset = 0) => {
    const target = typeof element === 'string' 
        ? document.querySelector(element) 
        : element;
    
    if (target) {
        const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top, behavior: 'smooth' });
    }
};

// Local storage helpers
const storage = {
    get(key, defaultValue = null) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch {
            return defaultValue;
        }
    },
    set(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
        } catch (e) {
            console.warn('localStorage not available');
        }
    },
    remove(key) {
        localStorage.removeItem(key);
    }
};

// URL parameter helpers
const params = {
    get(name) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(name);
    },
    set(name, value) {
        const url = new URL(window.location);
        url.searchParams.set(name, value);
        window.history.replaceState({}, '', url);
    },
    remove(name) {
        const url = new URL(window.location);
        url.searchParams.delete(name);
        window.history.replaceState({}, '', url);
    }
};

// Form validation helpers
const validate = {
    email(value) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    },
    required(value) {
        return value !== null && value !== undefined && value.trim() !== '';
    },
    minLength(value, min) {
        return value.length >= min;
    },
    maxLength(value, max) {
        return value.length <= max;
    }
};

// Fetch wrapper with error handling
const api = {
    async get(url, options = {}) {
        try {
            const response = await fetch(url, { ...options, method: 'GET' });
            if (!response.ok) throw new Error(response.statusText);
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    },
    async post(url, data, options = {}) {
        try {
            const response = await fetch(url, {
                ...options,
                method: 'POST',
                headers: { 'Content-Type': 'application/json', ...options.headers },
                body: JSON.stringify(data)
            });
            if (!response.ok) throw new Error(response.statusText);
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }
};

// Export for module usage
if (typeof module !== 'undefined') {
    module.exports = { 
        formatDate, 
        getTimeRemaining, 
        debounce, 
        throttle, 
        scrollTo, 
        storage, 
        params, 
        validate, 
        api 
    };
}
