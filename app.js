function submitImage() {
    const imageInput = document.getElementById('imageInput');
    if (imageInput.files.length > 0) {
        const imageFile = imageInput.files[0];
        const reader = new FileReader();
        
        reader.onloadend = function() {
            fetch('/analyze-image', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ imageBase64: reader.result.split(',')[1] }) // remove the base64 prefix
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        };

        reader.readAsDataURL(imageFile);
    }
}
