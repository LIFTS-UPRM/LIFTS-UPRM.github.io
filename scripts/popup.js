document.addEventListener('DOMContentLoaded', function() {
    const videoPopup = document.getElementById('video-popup');
    const watchVideoBtn = document.getElementById('watch-video-btn');
    const closeBtn = document.querySelector('.close-btn');

    watchVideoBtn.addEventListener('click', function(e) {
        e.preventDefault();
        videoPopup.style.display = 'flex';
    });

    closeBtn.addEventListener('click', function() {
        videoPopup.style.display = 'none';
        const iframe = videoPopup.querySelector('iframe');
        const iframeSrc = iframe.src;
        iframe.src = iframeSrc;
    });

    window.addEventListener('click', function(e) {
        if (e.target == videoPopup) {
            videoPopup.style.display = 'none';
            const iframe = videoPopup.querySelector('iframe');
            const iframeSrc = iframe.src;
            iframe.src = iframeSrc;
        }
    });
});
