let url = 'http://127.0.0.1:5000/api/v1/users';

let form = document.querySelector('#search-form');

let data = {
}

let sendRequest = (data) => {
    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            mode: "no-cors"
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(data => {
        
        console.log(data);
            
            
          
    })
}

form.addEventListener('submit', function(e){
    e.preventDefault();
    let first_name = document.querySelector("#input").value
    
    data.first_name = first_name
    
    console.log(data.first_name)

    sendRequest(data)
})