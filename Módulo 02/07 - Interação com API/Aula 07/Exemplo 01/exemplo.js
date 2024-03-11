async function aki(){
    let bemvindo = await fetch("exemplo.json")
    let ola = await bemvindo.json()
    let grupoDiv = document.getElementById("lista-iphone")
    
    for(let eaw of ola){

        grupoDiv.innerHTML += `
            <div class="iphone">
            <img src="${eaw.imagem}" alt"" width"auto" heigth"320px" title="sapatos e sandalias">
                <h3>${eaw.marca}</h3>
                <p>${eaw.preco}</p>
                <p>${eaw.cor}</p>
                
            </div>    
            
        `
    }
}
aki()