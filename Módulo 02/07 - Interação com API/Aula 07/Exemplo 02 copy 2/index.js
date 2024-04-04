async function buscarProdutos() {
  try {
      const response = await fetch("lista-produtos.json")
      const produtos = await response.json()

      const grupoDiv = document.getElementById("dell-card")
      for (const produto of produtos) {
          grupoDiv.innerHTML += `
              <div class="card" data-id="${produto.id}">
                  <img src="${produto.imagem}" alt="" width="200" height="200">
                  <h2>${produto.nome}</h2>
                  <h3>${produto.descrição}</h3>
                  <div class="valores" id="valores">
                  <h4>R$ ${produto.valorComdesconto.toFixed(2)}</h4>
                      <h5>R$ ${produto.valorSemdesconto.toFixed(2)}</h5>
                  </div>
              </div>`
      }

      const divsCards = document.querySelectorAll(".card")
      divsCards.forEach(card => {
          card.addEventListener("click", () => {
              const elementoId = card.getAttribute("data-id")
              window.location.href = `detalhes.html?produto-id=${elementoId}`
          })
      })
  } catch (error) {
      console.error("Erro ao buscar produtos:", error);
  }
}

function toggleDropdown() {
    var dropdownContent = document.getElementById("dropdown").querySelector(".dropdown-content")
    dropdownContent.style.display = dropdownContent.style.display === "none" ? "block" : "none"
}

// Adicionar evento de clique aos links dentro do menu suspenso
document.addEventListener("DOMContentLoaded", function() {
    var dropdownLinks = document.querySelectorAll(".dropdown-content a")
    dropdownLinks.forEach(function(link) {
        link.addEventListener("click", function() {
            toggleDropdown(); // Fecha o menu suspenso ao clicar em uma opção
            // Adicione aqui o código para o que você deseja que aconteça ao clicar em uma opção do menu suspenso
            console.log("Você clicou em: " + link.innerText)
        })
    })
})

buscarProdutos()