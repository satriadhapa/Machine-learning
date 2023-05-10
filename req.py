import requests

# Define input data in JSON format
input_data = {
    "Nama": "Mahasiswa Baru",
    "Minat_kemampuan": "Suka bermain komputer dan menemukan cara kerja komputer;Memiliki ketertarikan dalam dunia menulis, khususnya menulis sebuah cerita fiksi;Cenderung lebih mudah bekerja dan berpikir mengenai hal-hal yang berhubungan dengan angka"
}

# Send POST request to Flask API
response = requests.post('http://localhost:5000/predict_major', json=input_data)

# Print the predicted major recommendation
print(response.text)