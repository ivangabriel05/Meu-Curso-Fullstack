 async function lista(){
    /*let relogar = await fetch("lista.json")
    let obtido = await relogar.json()
    alert(obtido)*/
    let buscar = await (await fetch("lista.json")).json()
    //alert(buscar)
    for(let x in buscar){
        document.body.innerHTML += `
            <h1>  
                ${buscar[x]}
            </h1>
        `
    }
}
lista()