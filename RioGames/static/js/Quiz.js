function myFunction() {
    var checkBox = document.querySelectorAll("#myCheck");
    var text = document.getElementById("155");
    var butto = document.getElementById("145");
    let cpt = 0;
    for (let i = 0; i < checkBox.length; i++) {
      if(checkBox[i].checked == true){
        cpt++;
      }
    }
    let res = ((cpt/checkBox.length) * 100).toFixed(2)
    text.innerHTML = "Votre score est " + res + "/100"
    if (cpt > 0)
    {
      butto.style.visibility = "hidden";
      text.style.visibility = "visible";
    } else {
      swal("il faut repondez aux quiz !!"); 
      butto.style.visibility ="visible";
    }
  }