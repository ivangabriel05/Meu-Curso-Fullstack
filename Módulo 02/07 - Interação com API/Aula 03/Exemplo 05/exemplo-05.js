async function bomdia(){
    var pedrinho= await fetch("pizza.txt")
    var vaitomanoc = await pedrinho.text()
    alert(vaitomanoc)
}
