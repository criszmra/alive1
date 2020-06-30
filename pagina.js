function sumarlike(id){

  let nLikes = document.getElementById(id).innerHTML;
  console.log(nLikes);
  let total = parseInt(nLikes)+1
  document.getElementById(id).innerHTML = total
}

function sumardislike(id){

  let nDislikes = document.getElementById(id).innerHTML;
  console.log(nDislikes);
  let total = parseInt(nDislikes)+1
  document.getElementById(id).innerHTML = total
}
