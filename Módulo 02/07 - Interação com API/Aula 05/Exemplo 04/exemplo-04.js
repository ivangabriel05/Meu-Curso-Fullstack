 async function tabela(){
    /*let relogar = await fetch("lista.json")
    let obtido = await relogar.json()
    alert(obtido)*/
    let procura = await (await fetch("folha.json")).json()
    //alert(buscar)
    for(let x in procura){
        
        document.body.innerHTML += `
            <h1>  
                ${procura[x]}
            </h1>
        `
    }
}
tabela()