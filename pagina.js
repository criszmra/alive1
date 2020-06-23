function sumarlike(){

  let nLikes = document.getElementById('nlikes').innerHTML;
  console.log(nLikes);
  let total = parseInt(nLikes)+1
  document.getElementById('nlikes').innerHTML = total
}

function sumardislike(){

  let nDislikes = document.getElementById('ndislikes').innerHTML;
  console.log(nDislikes);
  let total = parseInt(nDislikes)+1
  document.getElementById("ndislikes").innerHTML = total
}
