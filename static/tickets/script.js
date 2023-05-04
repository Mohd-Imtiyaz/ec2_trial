// Data tables script
$("#list_company").DataTable({
    // tables config
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching: true,
    bInfo: true,
    bSort: true,
})

$("#list_tickets").DataTable({
    // tables config
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching: true,
    bInfo: true,
    bSort: true,
    order :[], //Disable order
})