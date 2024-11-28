document.getElementById('image-upload-button').addEventListener('click', function() {
    document.getElementById('image-upload').click();
});

document.getElementById('image-upload').addEventListener('change', function(event) {
    const imageContainer = document.getElementById('image-container');
    const predictionContainer = document.getElementById('prediction-container');
    
    // Clear previous contents
    imageContainer.innerHTML = '';
    predictionContainer.innerHTML = '';
    
    const file = event.target.files[0];
    if (file) {
        // Display input image on the left
        const inputImage = document.createElement('img');
        inputImage.src = URL.createObjectURL(file);
        inputImage.style.maxWidth = '100%';
        imageContainer.appendChild(inputImage);

        // When you get the prediction result, display it on the right
        // This is where you'd handle the prediction and display the result
        fetch('/predict', {
            method: 'POST',
            body: new FormData(event.target.form)
        })
        .then(response => response.json())
        .then(data => {
            const resultImage = document.createElement('img');
            resultImage.src = data.predicted_image_path; // or however you receive the result image
            resultImage.style.maxWidth = '100%';
            predictionContainer.appendChild(resultImage);
        });
    }
});
