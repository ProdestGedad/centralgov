// Dynamically create the modal HTML and append it to the body
function createConfirmModal() {
  const modalHtml = `
  <div class="modal fade" id="confirmModal" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalLabel">Confirmar Ação</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          Tem certeza de que deseja realizar esta ação?
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cancelar</button>
          <button type="button" id="confirmButton" class="btn btn-outline-primary">Confirmar</button>
        </div>
      </div>
    </div>
  </div>
  `;
  document.body.insertAdjacentHTML('beforeend', modalHtml);
}

// Function to open the modal, display action name, and store the action in the form
function openConfirmModal(action, formId, actionLabel) {
  document.getElementById('actionInput').value = action;
  
  // Update modal title to show the action label
  document.getElementById('modalLabel').innerText = `${actionLabel}`;

  // Show modal
  const confirmModal = new bootstrap.Modal(document.getElementById('confirmModal'));
  confirmModal.show();

  // Add event listener to the confirm button to submit the form
  document.getElementById('confirmButton').addEventListener('click', function () {
      document.getElementById(formId).submit();
  }, { once: true });
}

// Initialize the modal when the page loads
document.addEventListener('DOMContentLoaded', function () {
  createConfirmModal();
});
