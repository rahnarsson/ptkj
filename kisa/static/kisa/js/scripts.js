function osallistujaInfo(id) {  
  $('#kisaajainfo-content').load('/kisa/kisaajainfo/' +id, function () {
    var options = {};
    UIkit.modal( '#kisaajainfo', options).show();
  })

}
