// static/js/table-enhancements.js

// Declare the table variable in the global scope
var table;

$(document).ready(function() {

    $.fn.dataTable.moment('DD/MM/YYYY');
    $.fn.dataTable.moment('DD/MM/YYYY kk:mm:ss');

    // Use the `tableDefaultOrder` variable or fallback to the default order if not set
    var defaultOrder = typeof tableDefaultOrder !== 'undefined' ? tableDefaultOrder : [[0, 'asc']];
    
    table = $('#myTable').DataTable({
        "paging": false,        // Enable pagination
        "searching": true,     // Enable search
        "ordering": true,      // Enable sorting
        "info": true,          // Show table info
        "autoWidth": false,     // Adjust column width automatically
        "order": defaultOrder,
        "language": {
                    "url": "https://cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Portuguese.json"
                },      
        "columnDefs": [
                    { "orderable": false, "targets": -1 }
                ]
    });

});