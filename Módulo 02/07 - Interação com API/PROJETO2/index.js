ocument.addEventListener("DOMContentLoaded", function() {
    // Seletor para todos os botões "Adicionar ao Carrinho"
    const addButtons = document.querySelectorAll('.produto button')

    // Adiciona um evento de clique a cada botão
    addButtons.forEach(button => {
        button.addEventListener('click', function() {
            const produto = this.parentNode; // Obtém o elemento pai do botão (o artigo do produto)
            const nome = produto.querySelector('h2').innerText
            const preco = produto.querySelector('p:nth-of-type(2)').innerText

            // Cria um novo item de carrinho
            const novoItem = document.createElement('li')
            novoItem.innerText = `${nome} - ${preco}`

            // Adiciona o novo item ao carrinho
            const carrinho = document.querySelector('.carrinho ul')
            carrinho.appendChild(novoItem)

            // Redireciona para a página de checkout (ou outra página desejada)
            window.location.href = 'pagina-de-checkout.html';
        })
    })
})
