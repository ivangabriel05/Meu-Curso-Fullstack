async function imprimir(){
    let busca = await fetch("tarefas.json")
    let tarefas = await busca.json()

    let buscar2 = await fetch("cores.json")
    let cores = await buscar2.json()

    for(let x in tarefas){
        document.body.innerHTML += `

            <h1 style="color: ${cores[x]}">
                ${tarefas[x]}
            </h1>

        `

    }
}
imprimir()
//() serve para passa parametros e condiçoes 