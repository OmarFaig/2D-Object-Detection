        // JavaScript to trigger the file input when the button is clicked
        const imageUpload = document.getElementById('image-upload');
        const imageUploadButton = document.getElementById('image-upload-button');

        imageUploadButton.addEventListener('click', () => {
            imageUpload.click(); // Triggers the file input click event
        });