
// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption

var img = document.querySelectorAll(".myImg");
// alert(img.length)

var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

for (let i = 0; i < img.length; i++) {
  img[i].onclick = function(){
    // var modal = document.querySelectorAll(".mmyModal");
      modal.style.display = "block";
      modalImg.src = this.src;  
      
}
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
} 
function copy_Share_Button() {
  var sURL = window.location.href; //The actual address of the website
  sTemp = "<input id=\"copy_to_Clipboard\" value=\"" + sURL + "\" />"    //creates new input button
  $("body").append(sTemp);//append as html child elements to the body element
  $("#copy_to_Clipboard").select();
  document.execCommand("copy"); //system runs this command
  $("#copy_to_Clipboard").remove();
}