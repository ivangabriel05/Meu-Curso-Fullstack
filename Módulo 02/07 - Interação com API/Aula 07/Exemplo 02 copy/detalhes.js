async function buscarDetalhes(){
     // Consumo da API
     let busca = await fetch("lista-produtos.json")
     let produtos = await busca.json()
     console.log(produtos)
     

     // Criou um objeto URLSearchParams e passou
     //a coleta dos paramentros da URL nele.
     let parametros = new URLSearchParams(window.location.search)

     // Obteve do parametro "produto-id", o seu valor
     let parametroID =parametros.get("produto-id")

     //Criou uma variavel vazia para a atribuição
     let indiceProd
     //usou o for para percorrer toda a lista de produtos do JSON 
     for(let x in produtos){
          //verifica se o ID de cada produto é igual ao ID 
          //coletado na URL da página no navegador
          if(produtos[x].id == parametroID ){
               //Atribui á variavel vazia, o valor de x, que contém 
               // o indice do produtor que corresponde ao ID da URL  
               indiceProd = x
          }
     }
     
     // Adiciona na TAG BODY do HTML, um código HTML concatenado
     // com valores do objeto produto encontrado
     document.getElementById("detalhes").innerHTML += `
     <img src="${produtos[indiceProd].imagem[0]}" id="frame" width="250" heigth="250"/>     
     <h3>${produtos[indiceProd].nome}</h3>
     <h3>${produtos[indiceProd].descrição}</h3>
     <div class="miniaturas" id="miniaturas">
     </div>
     <p>${produtos[indiceProd].descrição}</p>
     <div class="valores">
          <h3>Valor Com Desconto R$ ${produtos[indiceProd].valorComdesconto}</h3>
          <h3>Valor Sem Desconto R$ ${produtos[indiceProd].valorSemdesconto}</h3>
     </div>  
     `
     let divMiniaturas = document.getElementById("miniaturas")
     for(let y of produtos[indiceProd].imagem){
          divMiniaturas.innerHTML += ` 
          <img src="${y}" class="mini" width="80" heigth="80" style="border: 1px solid #000"/>
          `
     }

     let minizinhas = document.getElementsByClassName("mini")
     for(let a of minizinhas){
          a.addEventListener("mouseover", deslize)
     }

}

function deslize(){
     document.getElementById("frame").src = this.src
}

buscarDetalhes()