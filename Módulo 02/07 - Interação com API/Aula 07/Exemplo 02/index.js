// Função assincrona para fazer uso do Await
// fetch() faz uma
async function buscar(){
    let procura = await fetch("lista-produtos.json")
    let achados = await procura.json()

    let grupoDiv = document.getElementById("lista-dell")
        for( let produto of achados){
            grupoDiv.innerHTML += `
                <div class="card">
                    <h3>${produto.nome}</h3>
                    <p>${produto.descrição}</p>
                    <p>${produto.valorComdescoto}</p>
                    <p>${produto.valorSemdescoto}</p>
                </div>
            `

    }
}
buscar()