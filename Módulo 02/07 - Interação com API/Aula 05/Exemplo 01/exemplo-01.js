
// O RESUTADO DA BUSCAR ESTA SENDO ATRIBUIDA A LISTA
async function buscar(){
  let procura = await  fetch("api/tarefas.json")
  let lista = await procura.json()

  for (let x in lista)

    //alert(lista[x])
    alert(lista[0])
    alert(lista[1])
    alert(lista[2])
    


}
buscar()