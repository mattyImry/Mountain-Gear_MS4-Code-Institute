/* Code from Boutique ado */

let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#92a396');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#92a396');
    } else {
        $(this).css('color', '#495057');
    }
});