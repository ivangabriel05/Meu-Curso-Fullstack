async function mucuraPreta(){
    // Consumo da API
    let achado = await fetch("lista-produtos.json")
    let itens = await achado.json()
    console.log(itens)
    

    // Criou um objeto URLSearchParams e passou
    //a coleta dos paramentros da URL nele.
    let parametros = new URLSearchParams(window.location.search)

    // Obteve do parametro "produto-id", o seu valor
    let parametroID =parametros.get("produto-id")

    //Criou uma variavel vazia para a atribuição
    let indiceProd
    //usou o for para percorrer toda a lista de produtos do JSON 
    for(let x in itens){
        //verifica se o ID de cada produto é igual ao ID 
        //coletado na URL da página no navegador
        if(itens[x].id == parametroID ){
            //Atribui á variavel vazia, o valor de x, que contém 
            // o indice do produtor que corresponde ao ID da URL  
            indiceProd = x
        }
    }
    
    // Adiciona na TAG BODY do HTML, um código HTML concatenado
    // com valores do objeto produto encontrado
    document.body.innerHTML = `
        <div class="card-detalhes">
        <img src="${itens[indiceProd].imagem}" width="250" heigth="250"/>     
        <h3>${itens[indiceProd].nome}</h3>
        <h3>${itens[indiceProd].descrição}</h3>
        <h4>Valor Com Desconto R$ ${itens[indiceProd].valorComdesconto}</h4>
        <h4>Valor Sem Desconto R$ ${itens[indiceProd].valorSemdesconto}</h4>
        </div>
    `
    
}
mucuraPreta()
