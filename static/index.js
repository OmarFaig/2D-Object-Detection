const uploadButton = document.getElementById('image-upload-button');
const imageInput = document.getElementById('image-upload');
const imageContainer = document.getElementById('image-container');

uploadButton.addEventListener('click', () => {
    imageInput.click(); // Triggers the file input click event
        });
      // Handling image uploads and displaying them
imageInput.addEventListener('change', (event) => {
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

        reader.readAsDataURL(file); // Read the file as a data URL to display it
    });
});
/*const uploadPictureButton = document.querySelector(".photo-upload");

  uploadPictureButton.addEventListener('change', function () {
    displayPicture(this);
  });

 function displayPicture(input) {
    if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      document.getElementById('the-picture').setAttribute('src', e.target.result);
    };

    reader.readAsDataURL(input.files[0]);
  }
 }*/