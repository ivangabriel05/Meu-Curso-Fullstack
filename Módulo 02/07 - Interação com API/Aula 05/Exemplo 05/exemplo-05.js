async function imprimir(){
    let busca = await fetch("tarefas.json")
    let tarefas = await busca.json()

    let buscar2 = await fetch("cores.json")
    let cores = await buscar2.json()

    for(let x in tarefas){
        let indice = parseInt(match.random() * 4)

        document.body.innerHTML += `
            <p style="color:${cores[indice]}">
                ${tarefas[x]}
            </p>
        `
    }
}
imprimir()
//() serve para passa parametros e condiçoes 