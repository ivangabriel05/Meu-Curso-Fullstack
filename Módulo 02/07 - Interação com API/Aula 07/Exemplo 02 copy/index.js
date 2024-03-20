// Função assincrona para fazer uso do Await
// fetch() faz uma
async function buscar(){
    let procura = await fetch("lista-produtos.json")
    let achados = await procura.json()

    let grupoDiv = document.getElementById("lista-card")
        for( let produto of achados){
            grupoDiv.innerHTML += `
                <div class="card" data-id${produto.id}"">
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
}
buscar()