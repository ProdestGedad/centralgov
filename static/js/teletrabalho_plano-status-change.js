document.addEventListener('DOMContentLoaded', function () {
    const csrfToken = document.getElementById('csrf_token').value;
    const statusChangeUrl = '/teletrabalho/plano-status-change/';

    // Role-Action Mapping for modal content customization
    const roleActionMapping = {
        'aprova_servidor': {
            title: "Validar Plano de Trabalho e Atividades",
            question: "Tem certeza que deseja validar este Plano de Trabalho e Suas Atividades? Não será possível realizar Alterações até que seja aprovado pelo gestor.",
            options: [
                { id: 'validateOption', label: 'Validar', value: 'aprovar', checked: true }
            ]
        },
        'aprova_final': {
            title: "Avaliação Final do Plano de Teletrabalho e Atividades",
            question: "Mediante o acompanhamento da entrega das atividades propostas, qual a sua Avaliação Final deste Plano de Teletrabalho e Atividades? Esta ação é irreversível.",
            options: [
                { id: 'approveOption', label: 'Satisfatória', value: 'aprovar', checked: true },
                { id: 'rejectOption', label: 'Insatisfatória', value: 'recusar' }
            ],
            requireTextarea: true, // Flag to enable textarea
            textareaPlaceholder: "Avaliação Final (obrigatória)",
        },
        'aprova_continuo_gerencia': {
            title: "Aprovar/Não Aprovar Modalidade de Teletrabalho Contínuo",
            question: "Deseja aprovar o requerimento de Teletrabalho na Modalide Contínua? Em caso de recusa, a modalidade será automaticamente alterada para 'Híbrido'. Esta ação é necessária antes da aprovação do Regime de Teletrabalho pela Gerência.",
            options: [
                { id: 'approveOption', label: 'Aprovar', value: 'aprovar', checked: true },
                { id: 'rejectOption', label: 'Não Aprovar', value: 'recusar' }
            ],
            requireTextarea: true, // Flag to enable textarea
            textareaPlaceholder: "Justificativa (obrigatória)",
        },
        'aprova_continuo_diretoria': {
            title: "Aprovar/Não Aprovar Modalidade de Teletrabalho Contínuo",
            question: "Deseja aprovar o requerimento de Teletrabalho na Modalide Contínua? Em caso de recusa, a modalidade será automaticamente alterada para 'Híbrido'. Esta ação é necessária antes da aprovação do Regime de Teletrabalho pela Gerência.",
            options: [
                { id: 'approveOption', label: 'Aprovar', value: 'aprovar', checked: true },
                { id: 'rejectOption', label: 'Não Aprovar', value: 'recusar' }
            ],
            requireTextarea: true, // Flag to enable textarea
            textareaPlaceholder: "Justificativa (obrigatória)",
        },
        'recusa_servidor': {
            title: "Recusar Plano de Trabalho",
            question: "Tem certeza que deseja recusar este plano?",
            options: [
                { id: 'rejectOption', label: 'Recusar', value: 'recusar', checked: true }
            ]
        },
        'default': {
            title: "Aprovar/Não Aprovar Teletrabalho",
            question: "Tem certeza que deseja executar a ação abaixo?",
            options: [
                { id: 'approveOption', label: 'Aprovar Teletrabalho', value: 'aprovar', checked: true },
                { id: 'rejectOption', label: 'Não Aprovar Teletrabalho', value: 'recusar' }
            ]
        }
    };

    // Check if modal already exists before creating it
    if (!document.getElementById('confirmationModal')) {
        const modalHTML = `
            <div class="modal fade" id="confirmationModal" tabindex="-1" aria-labelledby="confirmationModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="confirmationModalLabel"></h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <p id="confirmationQuestion"></p>
                            <div id="actionOptions"></div>
                            <textarea id="justificativa" class="form-control mt-2" placeholder="Insira a Justificativa" style="height: 150px; display: none;"></textarea>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cancelar</button>
                            <button type="button" class="btn btn-outline-primary" id="confirmButton">Confirmar</button>
                        </div>
                    </div>
                </div>
            </div>`;
        document.body.insertAdjacentHTML('beforeend', modalHTML);
    }
    
    const statusChangeButtons = document.querySelectorAll('.status-change-button');
    const confirmButton = document.getElementById('confirmButton');
    const modal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    const confirmationTitle = document.getElementById('confirmationModalLabel');
    const confirmationQuestion = document.getElementById('confirmationQuestion');
    const actionOptionsContainer = document.getElementById('actionOptions');
    const justificativaInput = document.getElementById('justificativa');

    // Function to populate modal based on role-action mapping
    function populateModalContent(actionKey) {
        const content = roleActionMapping[actionKey] || roleActionMapping['default'];
        confirmationTitle.innerText = content.title;
        confirmationQuestion.innerText = content.question;

        // Clear existing options
        actionOptionsContainer.innerHTML = '';
        justificativaInput.style.display = 'none';
        justificativaInput.value = '';

        // Add options
        content.options.forEach(option => {
            const optionHTML = `
            <div class="form-check">
                <input type="radio" id="${option.id}" name="action" value="${option.value}" class="form-check-input" ${option.checked ? 'checked' : ''}>
                <label for="${option.id}" class="form-check-label">${option.label}</label>
            </div><br>`;
            actionOptionsContainer.insertAdjacentHTML('beforeend', optionHTML);
        });

        // Handle specific case for 'aprova_final'
        if (actionKey === 'aprova_final') {
            justificativaInput.style.display = 'block';
            justificativaInput.placeholder = "Avaliação Final (obrigatória)";
        } else if (actionKey === 'aprova_continuo_gerencia') {
            justificativaInput.style.display = 'block';
            justificativaInput.placeholder = "Justifique sua Decisão (obrigatório)";
        } else if (actionKey === 'aprova_continuo_diretoria') {
            justificativaInput.style.display = 'block';
            justificativaInput.placeholder = "Justifique sua Decisão (obrigatório)";
        } else if (content.requireTextarea) {
            justificativaInput.style.display = 'block';
            justificativaInput.placeholder = content.textareaPlaceholder || '';
        }

        // Reattach change listener for showing/hiding justificativa field
        document.querySelectorAll('input[name="action"]').forEach((radio) => {
            radio.addEventListener('change', function () {
                const shouldShowJustificativa = 
                    this.value === 'recusar' || 
                    actionKey === 'aprova_final' || 
                    actionKey === 'aprova_continuo_gerencia' ||
                    actionKey === 'aprova_continuo_diretoria';
                
                justificativaInput.style.display = shouldShowJustificativa ? 'block' : 'none';
                
                if (!shouldShowJustificativa) {
                    justificativaInput.value = ''; // Clear justificativa if it is hidden
                }
            });
        });
    }
   

    statusChangeButtons.forEach((button) => {
        button.addEventListener('click', function () {
            const planoId = this.getAttribute('data-plano-id');
            const userRole = this.getAttribute('data-role');
            console.log(userRole);
            const actionKey = `aprova_${userRole}`;
    
            // Populate modal based on role-action mapping
            populateModalContent(actionKey);
    
            // Set data attributes for confirm button
            confirmButton.dataset.planoId = planoId;
            confirmButton.dataset.userRole = userRole;
            confirmButton.dataset.actionKey = actionKey;
    
            modal.show();
        });
    });

    // Confirm button action
    confirmButton.addEventListener('click', function () {
        const planoId = this.dataset.planoId;
        const userRole = this.dataset.userRole;
        const actionKey = this.dataset.actionKey; // Retrieve the action key
        const selectedAction = document.querySelector('input[name="action"]:checked').value;
        const action = selectedAction === 'aprovar' ? 'aprova' : 'recusa';
        const justificativa = justificativaInput.value.trim();

        // Validate input based on actionKey
        if (actionKey === 'aprova_final' || actionKey === 'aprova_continuo_gerencia' || actionKey === 'aprova_continuo_diretoria' || selectedAction === 'recusar') {
            if (justificativa === '') {
                alert('Por favor, forneça uma justificativa para a ação selecionada.');
                return;
            }
        }


        // Send AJAX request
        $.ajax({
            url: statusChangeUrl,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': csrfToken,
                'plano_id': planoId,
                'action': `${action}_${userRole}`,
                'justificativa': justificativa
            },
            success: function (response) {
                if (response.success) {
                    location.reload();
                } else {
                    alert(`Erro: ${response.message}`);
                }
            },
            error: function (response) {
                alert(`Erro: ${response.message}`);
            },
            complete: function () {
                confirmButton.disabled = false;
                modal.hide();
            }
        });
    });
});
