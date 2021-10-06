//simple change
$('#id_NOC_Engineer').on('keyup', function(){
    $('#id_Resolved_by_Engineer').val($(this).val());
})
