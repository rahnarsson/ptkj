function osallistujaInfo(id) {
  $('#kisaajainfo-content').load('/kisa/kisaajainfo/' +id, function () {
    var options = {};
    UIkit.modal( '#kisaajainfo', options).show();
  })
}
function editKisaaja(id) {
  $.get('/kisa/getkisaaja/' +id, function (data) {
    console.log($.parseJSON(data)[0]);
    data = $.parseJSON(data)[0];
    fields = data.fields;
    $('#edit-kisaaja .uk-modal-title').text('Muokkaa kisaajan tietoja: '+ fields.nimi_etu + ' ' + fields.nimi_suku);
    $('#edit-kisaaja input[name="kisaaja_id"]').val(data.pk);
    $('#edit-kisaaja input[name="nimi_etu"]').val(fields.nimi_etu);
    $('#edit-kisaaja input[name="nimi_suku"]').val(fields.nimi_suku);
    $('#edit-kisaaja input[name="email"]').val(fields.email);
    $('#edit-kisaaja textarea[name="allergiat"]').val(fields.ruoka_allergiat);
    var options = {};
    UIkit.modal( '#edit-kisaaja', options).show();
  }, 'json')
}
