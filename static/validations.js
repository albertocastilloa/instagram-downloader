function validate_input(){
    var txt_input;
    txt_input = document.getElementById("url").value;
    if (txt_input == ""){
        alert("Please insert a valid URL")
        return false
    };
}