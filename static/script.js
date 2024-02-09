// static/script.js
document.addEventListener('DOMContentLoaded', function () {
    const imageContainer = document.querySelector('.image-container');

    // Function to handle image click (show pop-up)
    function handleImageClick(imageSrc) {
        // Add your logic to display a pop-up or navigate to a new page
        alert('Image clicked!'); // Example: Show an alert
    }

    // Fetch all uploaded images and create click event listeners
    const images = document.querySelectorAll('.image-container img');
    images.forEach(image => {
        image.addEventListener('click', () => {
            const imageSrc = image.src;
            handleImageClick(imageSrc);
        });
    });
});
