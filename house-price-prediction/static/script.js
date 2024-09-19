document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form data
    const formData = {
        Area: document.getElementById('area').value,
        Bedrooms: document.getElementById('bedrooms').value,
        Bathrooms: document.getElementById('bathrooms').value,
        Floors: document.getElementById('floors').value,
        Age: document.getElementById('age').value,
        Garage: document.getElementById('garage').value,
        'Lot Size': document.getElementById('lot-size').value,
        Garden: document.getElementById('garden').value
    };

    // Send data to the Flask API
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Update the result on the page
        document.getElementById('price').textContent = `$${data['Predicted Price'].toFixed(2)}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('price').textContent = 'Error occurred!';
    });
});
