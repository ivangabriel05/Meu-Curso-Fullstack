async function mina(){
    let busca = await fetch("atvd.json")
    let produtos = await busca.json()
    let grupoDiv = document.getElementById("Lista-card")
    for(let produto of produtos ){

        grupoDiv.innerHTML += `
            <div class="card">
                <h3>${produto.nome}</h3>
                <p>${produto.marca}</p>
                <p>${produto.valor}</p>
            </div>
        `
    }
}
mina()