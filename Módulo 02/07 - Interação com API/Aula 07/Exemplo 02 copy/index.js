// Função assincrona para fazer uso do Await
// fetch() faz uma
async function buscar(){
    let procura = await fetch("lista-produtos.json")
    let achados = await procura.json()

    let grupoDiv = document.getElementById("lista-card")
        for( let produto of achados){
            grupoDiv.innerHTML += `
                <div class="card" data-id="${produto.id}">
                <img src="${produto.imagem}" alt"" width"200" heigth"200px"
                    <h2>${produto.nome}</h2>
                    <h3>${produto.descrição}</h3>
                    <div class="valores">
                        <span>${produto.valorComdescoto.toFixed(2)}</span>
                        <span>${produto.valorSemdescoto.toFixed(2)}</span>
                    </div>
            </div>
        `
    }
    let divsCards = document.getElementsByClassName("card")
    // add em cada Div card um evento que escuta quando 
    // o usuario clica nele, e chama uma função.
    for( let card of divsCards){
        card.addEventListener("click", clicou)
    }
}

function clicou(){
    let elementoId = this.getAttribute("data-id")
    window.location.href = "detalhes.html?produto-id=" + elementoId
}
buscar()
