document.addEventListener('DOMContentLoaded', function () {
    // Function to open and populate the modal with historical data
    function openHistoricoModal(planoId) {
        // Fetch the historico data from the server for the given plano ID
        fetch(`/teletrabalho/plano/${planoId}/historico/`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const historico = data.historico;

                    // Create the modal content
                    const modalContent = `
                        <div class="modal fade" id="historicoModal" tabindex="-1" aria-hidden="true">
                            <div class="modal-dialog modal-lg modal-dialog-scrollable">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title">Plano de Trabalho e Atividades - Histórico</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <ul class="list-group">
                                            ${historico.map(entry => `
                                                <li class="list-group-item">
                                                    <strong>${entry.data}</strong> - ${entry.origem} - ${entry.status}
                                                    ${['Modalidade Contínua Aprovada', 'Modalidade Contínua Não Aprovada', 'Não Aprovado', 'Insatisfatória', 'Satisfatória'].includes(entry.status)
                            ? `<br><br>Justificativa: ${entry.justificativa || 'Sem justificativa'}`
                            : ''}

                                                </li>
                                            `).join('')}
                                        </ul>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Fechar</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;

                    // Append modal content to body and display it
                    document.body.insertAdjacentHTML('beforeend', modalContent);
                    const modal = new bootstrap.Modal(document.getElementById('historicoModal'));
                    modal.show();

                    // Remove the modal from DOM on close
                    document.getElementById('historicoModal').addEventListener('hidden.bs.modal', function () {
                        document.getElementById('historicoModal').remove();
                    });
                } else {
                    alert('Erro ao carregar o histórico.');
                }
            })
            .catch(error => console.error('Error fetching historical data:', error));
    }

    // Event listener to trigger the modal on a button click
    document.querySelectorAll('.btn-historico').forEach(button => {
        button.addEventListener('click', function () {
            const planoId = this.dataset.planoId;
            openHistoricoModal(planoId);
        });
    });
});
