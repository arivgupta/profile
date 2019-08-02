var a = new Array(),
  n = ''
a[1] = 'I'
a[2] = ' '
a[3] = 'A'
a[4] = 'M'
a[5] = ' '
a[6] = 'A'
a[7] = 'N'
a[8] = ' '
a[9] = 'I'
a[10] = 'D'
a[11] = 'I'
a[12] = 'O'
a[13] = 'T'
a[14] = '!'

function one() {
  t = document.f.txt.value;
  j = t.length;

  if (j > 0) {
    for (var i = 1; i <= j; i++) {
      n = n + a[i];
      if (i == 15) {
        document.f.txt.value = "";
        n = "";
      }
    }
  }
  document.f.txt.value = n;
  n = "";
  setTimeout("one()", 1);
}

function on() {
  one()
}
