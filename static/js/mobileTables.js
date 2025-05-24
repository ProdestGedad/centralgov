document.addEventListener('DOMContentLoaded', function () {
    // Select all tables with the class 'table-bordered'
    const tables = document.querySelectorAll('.table-bordered');

    tables.forEach(function (table) {
        const headers = table.querySelectorAll('thead th'); // Get table headers
        const rows = table.querySelectorAll('tbody tr'); // Get all rows in the body

        // Loop through each row and each cell
        rows.forEach(function (row) {
            const cells = row.querySelectorAll('td'); // Get cells in the row

            // Loop through each cell in the row
            cells.forEach(function (cell, index) {
                const header = headers[index]; // Get corresponding header

                if (header) {
                    // Add the data-label attribute to the cell
                    cell.setAttribute('data-label', header.textContent.trim());
                }
            });
        });
    });
});
