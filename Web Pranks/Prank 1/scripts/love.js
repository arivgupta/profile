pos = 1;
function f1() {
  alert("I love you too! And even if you don't, sudo YOU MUST LOVE ME\nPlease enter password:")
}

function f2(){
  if (pos==1 || (pos!=2) && (pos!=3)){
    btnNo.style.top=400;
    btnNo.style.left=400;
    pos=2;
  }
  else if (pos==2) {
    btnNo.style.top=500;
    btnNo.style.left=50;
    pos=3;
  }
  else if (pos==3) {
    btnNo.style.top=50;
    btnNo.style.left=100;
    pos=1;
  }
}
