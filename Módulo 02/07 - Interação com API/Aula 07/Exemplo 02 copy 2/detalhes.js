async function mucuraPreta() {
    // Consumo da API
    let resposta = await fetch("lista-produtos.json");
    let itens = await resposta.json();
    

    // Criando um objeto URLSearchParams e obtendo os parâmetros da URL
    let parametros = new URLSearchParams(window.location.search);

    // Obtendo o valor do parâmetro "produto-id"
    let parametroID = parametros.get("produto-id");

    // Criando uma variável vazia para atribuição
    let indiceProd;
    // Percorrendo a lista de produtos do JSON
    for (let x in itens) {
        // Verificando se o ID de cada produto é igual ao ID coletado na URL
        if (itens[x].id == parametroID) {
            // Atribuindo à variável vazia o valor de x, que contém o índice do produto correspondente ao ID da URL
            indiceProd = x;
        }
    }

    // Adicionando HTML dinâmico ao corpo do documento com base no produto encontrado
    document.body.innerHTML = `
        <div class="card-detalhes">
            <img src="${itens[indiceProd].imagem}" id="frame" width="250" height="250"/>
            <div class="minituras" id="miniaturas">
            </div>  
            <h3>${itens[indiceProd].nome}</h3>
            <h4>${itens[indiceProd].descrição}</h4>
            <h3>Valor Com Desconto R$ ${itens[indiceProd].valorComdesconto}</h3>
            <h3>Valor Sem Desconto R$ ${itens[indiceProd].valorSemdesconto}</h3>
        </div>
    `
    
    let divMiniaturas = document.getElementById("miniaturas")
     for(let y of itens[indiceProd].imagem){
          divMiniaturas.innerHTML += ` 
          <img src="${y}" class="mini" width="80" heigth="80" style="border: 1px solid #000"/>
          `
    }
    
    let minizinhas = document.getElementsByClassName("mini");
    for (let a of minizinhas) {
        a.addEventListener("mouseover", deslize); // Supondo que 'deslize' esteja definido em outro lugar
    }
   
}

function deslize(){
    document.getElementById("frame").src = this.src
}

mucuraPreta()