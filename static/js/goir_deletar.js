// goir_deletar.js

function createDeleteModal() {
    const modalHtml = `
    <div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="deleteModalLabel">Deletar</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Tem certeza que deseja deletar <strong>"<span id="itemName"></span>"</strong> e todos os seus filhos?<br>Esta ação é irreverssível!!!<br>Considere que talvez o correto seja INATIVAR este item.<br>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button id="confirmDeleteBtn" class="btn btn-outline-danger">Deletar</button>
                </div>
            </div>
        </div>
    </div>`;

    // Create a div to hold the modal
    const modalContainer = document.createElement('div');
    modalContainer.innerHTML = modalHtml;
    document.body.appendChild(modalContainer);
}

function openDeleteModal(button) {
    // Get data attributes
    const modelName = button.getAttribute('data-model');
    const itemName = button.getAttribute('data-name');
    const itemId = button.getAttribute('data-id');
    
    // Set the item name in the modal
    document.getElementById('itemName').textContent = itemName;

    // Set a click event on the confirm button to delete the item
    const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
    confirmDeleteBtn.onclick = function() {
        window.location.href = `/goir/${modelName}/deletar/${itemId}/`;  // Redirect to deletion URL
    };

    // Show the modal
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
}

// Create the modal on page load
document.addEventListener('DOMContentLoaded', createDeleteModal);
