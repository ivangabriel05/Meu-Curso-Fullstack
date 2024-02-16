 async function tabela(){
    /*let relogar = await fetch("lista.json")
    let obtido = await relogar.json()
    alert(obtido)*/
    let procura = await (await fetch("folha.json")).json()
    //alert(buscar)
    for(let x in procura){
        let indice = parseInt(Math.random()) * 4
        document.body.innerHTML += `
            <h1 style="color:${[indice]}">  
                ${procura[x]}
            </h1>
        `
    }
}
tabela()