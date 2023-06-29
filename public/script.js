function sendData(event) {
    event.preventDefault()

    var title = document.getElementById("title").value;
    var description = document.getElementById("description").value;

    var data = {
        "title": title,
        "description": description
    }

    document.getElementById("result").innerHTML = "Creation of the video...";

    fetch("http://localhost:8000/api/video", {
        method: 'POST',
        headers: {
            'Content-Type': "application/json"
        },
        body: JSON.stringify(data)   
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("result").innerHTML = result.message;
        document.getElementById("title").value = "";
        document.getElementById("description").value = "";
    })
    .catch(err => console.error(err))
}

document.getElementById("create-video-form").addEventListener('submit', sendData);