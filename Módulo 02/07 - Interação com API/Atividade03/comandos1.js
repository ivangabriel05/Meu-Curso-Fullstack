async function chamado(){
    let procura = await fetch ("atvd1.json")
    let busca = await procura.json()
    let grupoDiv1 = document.getElementById("lista-dell")
    for(let x of busca)
    grupoDiv1.innerHTML +=`
    <div class="dell">
        <h2>Lista de motos</h2>
        <img src="${x.imagem}" width="300px" height="auto">
        <h4>${x.marca}</h4>
        <h4 >${x.nome}</h4>
        <h4>${x.valor}</h4>
        <h4>${x.cilindrada}</h4>
    </div>
`
}
chamado()