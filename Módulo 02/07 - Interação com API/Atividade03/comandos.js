async function chamada(){
    let procura = await fetch ("atvd.json")
    let busca = await procura.json()
    let grupoDiv = document.getElementById("lista-dell")
    for( let x of busca ){
        
        grupoDiv.innerHTML += `
        <div class="dell">
                <h2>Lista de motos</h2>
                <img src="${x.imagem}" width="300px" height="auto">
                <h3>${x.marca}</h3>
                <h3>${x.nome}</h3>
                <h3>${x.valor}</h3>
                <h3>${x.cilindrada}</h3>
        </div>
        `
    }
}
chamada()

        
            
            