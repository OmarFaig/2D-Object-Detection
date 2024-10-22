const uploadButton = document.getElementById('image-upload-button');
const imageInput = document.getElementById('image-upload');
const imageContainer = document.getElementById('image-container');
const predcitionContainer = document.getElementById('prediction-container');

uploadButton.addEventListener('click', () => {
    imageInput.click(); // Triggers the file input click event
});

// Handling image uploads and sending to FastAPI
imageInput.addEventListener('change', async (event) => {
    const files = event.target.files;
    imageContainer.innerHTML = ''; // Clear the container before adding new images
    Array.from(files).forEach(file => {
        const reader = new FileReader();
        // When the file is read, display the image
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.alt = file.name;
            img.style.maxWidth = '100%'; // Optional: adjust image size to fit in container
            img.style.margin = '10px';
            imageContainer.appendChild(img);
        };
        reader.readAsDataURL(file); }); //
    // Loop over selected files
    Array.from(files).forEach(async (file) => {
        const formData = new FormData();
        formData.append('file', file);

        // Make the POST request to FastAPI
        try {
            const response = await fetch('http://localhost:8000/predict', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                // Get the result image from the server
                const blob = await response.blob();
                const imgUrl = URL.createObjectURL(blob);

                // Display the returned image
                const img = document.createElement('img');
                img.src = imgUrl;
                img.alt = file.name;
                img.style.maxWidth = '100%';
                img.style.margin = '10px';
                predcitionContainer.appendChild(img);
            } else {
                console.error('Error uploading image:', response.statusText);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
