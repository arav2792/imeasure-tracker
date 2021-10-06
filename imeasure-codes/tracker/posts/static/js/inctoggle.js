$(document).ready(function () {
    toggleFieldss();
    $("#id_Incident_Type").change(function () {
        toggleFieldss();
    });

});

function toggleFieldss() {
    if ($("#id_Incident_Type").val() === "Alert")
        $("#id_Alert").show() && $("#id_Task").hide() && $("#id_General_Health_Check").hide() && $("#id_If_Others_Please_Specify").hide() && $('label[for=id_Alert], input#id_Alert').show() && $('label[for=id_Task], input#id_Task').hide()  && $('label[for=id_General_Health_Check], input#id_General_Health_Check').hide()
        && $('label[for=id_If_Others_Please_Specify], input#id_If_Others_Please_Specify').hide() ;


    else if ($("#id_Incident_Type").val() === "Task")
        $("#id_Alert").hide() && $("#id_Task").show() && $("#id_General_Health_Check").hide() && $("#id_If_Others_Please_Specify").hide() && $("#id_Remediation").hide() && $('label[for=id_Alert], input#id_Alert').hide() && $('label[for=id_Task], input#id_Task').show()  && $('label[for=id_General_Health_Check], input#id_General_Health_Check').hide()
        && $('label[for=id_If_Others_Please_Specify], input#id_If_Others_Please_Specify').hide() && $('label[for=id_Remediation], input#id_Remediation').hide() ;


    else if ($("#id_Incident_Type").val() === "GHC")
        $("#id_Alert").hide() && $("#id_Task").hide() && $("#id_General_Health_Check").show() && $("#id_If_Others_Please_Specify").hide() && $("#id_Remediation").hide() && $('label[for=id_Alert], input#id_Alert').hide() && $('label[for=id_Task], input#id_Task').hide()  && $('label[for=id_General_Health_Check], input#id_General_Health_Check').show()
        && $('label[for=id_If_Others_Please_Specify], input#id_If_Others_Please_Specify').hide() && $('label[for=id_Remediation], input#id_Remediation').hide() ;


    else if ($("#id_Incident_Type").val() === "Other")
        $("#id_Alert").hide() && $("#id_Task").hide() && $("#id_General_Health_Check").hide() && $("#id_If_Others_Please_Specify").show() && $("#id_Remediation").hide() && $('label[for=id_Alert], input#id_Alert').hide() && $('label[for=id_Task], input#id_Task').hide()  && $('label[for=id_General_Health_Check], input#id_General_Health_Check').hide()
        && $('label[for=id_If_Others_Please_Specify], input#id_If_Others_Please_Specify').show() && $('label[for=id_Remediation], input#id_Remediation').hide() ;
    }
