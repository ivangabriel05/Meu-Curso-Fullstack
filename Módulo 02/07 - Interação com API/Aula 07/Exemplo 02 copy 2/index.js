// Função assincrona para fazer uso do Await
// fetch() faz uma
async function mocura(){
    let procura = await fetch("lista-produtos.json")
    let achados = await procura.json()

    let grupoDiv = document.getElementById("dell-card")
        for( let produto of achados){
            grupoDiv.innerHTML += `
                <div class="card" data-id="${produto.id}">
                    <img src="${produto.imagem}" alt="" width="200" heigth="200px">
                    <h2>${produto.nome}</h2>
                    <h3>${produto.descrição}</h3>
                    <div class="valores">
                        <h4>R$ ${produto.valorComdesconto.toFixed(2)}</h4>
                        <h4>R$ ${produto.valorSemdesconto.toFixed(2)}</h4>
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
mocura()
// window
// coleta qual que valor do atributo "data-id" do elemento HTML que acionou o evento de escurta
function toggleDropdown() {
    var dropdownContent = document.getElementById("dropdown").querySelector(".dropdown-content");
    dropdownContent.style.display === "none" ? dropdownContent.style.display = "block" : dropdownContent.style.display = "none";
  }
  
  // Fechar o menu quando clicar fora dele
  // Fechar o menu quando clicar fora dele
window.onclick = function(event) {
    if (!event.target.matches('.dropdown-button')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.style.display === "block") {
          openDropdown.style.display = "none";
        }
      }
    }
  }