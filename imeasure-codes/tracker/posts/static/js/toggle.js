$(document).ready(function () {
    toggleFields();
    $("#id_Escalated").change(function () {
        toggleFields();
    });

});

function toggleFields() {
    if ($("#id_Escalated").val() === "Yes")
        $("#id_Escalated_to").show() && $("#id_Escalated_Reason").show() && $('label[for=id_Escalated_to], input#id_Escalated_to').show() && $('label[for=id_Escalated_Reason], input#id_Escalated_Reason').show();
    else
        $("#id_Escalated_to").hide() && $("#id_Escalated_Reason").hide() && $('label[for=id_Escalated_to], input#id_Escalated_to').hide() && $('label[for=id_Escalated_Reason], input#id_Escalated_Reason').hide();
}
