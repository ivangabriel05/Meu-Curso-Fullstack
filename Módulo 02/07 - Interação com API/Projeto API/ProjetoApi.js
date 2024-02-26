async function chamar(){
        let busca = await fetch("ProjetoApi.json")
        let produtos = await busca.json()
        let grupoDiv = document.getElementById("Lista-card")
        for(let produto of produtos ){
    
            grupoDiv.innerHTML += `
                <div class="card">
                    <img src="${produto.imagem}" width="200px" height="auto">
                    <h3>${produto.marca}</h3>
                    <p>${produto.valor}R$</p>
                    <p>${produto.modelo}</p>
                    <p>${produto.sistemaOperacional}</p>
       
                </div>
            `
        }
    }
chamar()