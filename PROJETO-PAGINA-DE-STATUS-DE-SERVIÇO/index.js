// Simula a verificação de um serviço, retornando aleatoriamente online ou offline
const checkService = async (serviceName) => { // Esta função simula uma chamada a um backend, você faria uma requisição fetch aqui para um endpoint que checa a saúde do seu serviço. A função retorna uma Promise que resolve com o status do serviço
    return new Promise(resolver =>{  

         // simula o tempo de resposta de uma API (1 a 3 segundos)
         const delay = Math.floor(Math.random() *2000) + 1000;
         setTimeout(() => {

            // 80% de canche de estar online, 20% de cahcne dee star offline
            const isOnline = Math.random() > 0.2;
            resolver({  name: serviceName, status: isOnline ? 'online' : 'offline'});
        }, delay);
        });
    };

// Lista de serviços que queremos monitorar 
const services = ['API de Usuarios', 'Serviço de Pagamentos', 'Banco de Dados', 'API de Notificações']; // Um array com os nomes dos serviços que queremos monitorar

// Função para renderizar o status dos serviços na página
const renderServicesStatus = async () => {  // Seleciona os elementos da página onde o conteúdo será inserido
//  Usa Promise.all() para rodar todas as verificações de serviço simultaneamente 
// ele que checar um por um. Após receber todos os resultados, ele limpa o container e cria o HTML para cada serviço, adicionando a classe online ou offline no indicador.
// Por fim, atualiza o horário da última checagem.

    const statusContainer = document.querySelector('.status-container');
    const loadingMessage = document.getElementById('loading');
    const lastUpdated = document.getElementById('last-updated');

    // Remove a mensagem de carregamento se existir 
    if (loadingMessage) {
        loadingMessage.remove();
    }
     
    // Exibe a mensagem de carregamento enquanto fazemos as verificações 
    statusContainer.innerHTML = '<div id="loading">Carregando status...</div>';

    // Dispara todas as verificações de serviço em paralelo
    const statusChecks = services.map(serviceName => checkService(serviceName));
    const results = await Promise.all(statusChecks);

    // Cria e insere o HTML para cada serviço
    results.forEach(result => {
        const statusItem = document.createElement('div');
        statusItem.className = 'service-item';
        statusItem.innerHTML = `
            <span>${result.name}</span>
            <div>
                <span class="status-indicator ${result.status}"></span>
                <span class="status-text">${result.status === 'online' ? 'Online' : 'Offline'}</span>
            </div>
        `;
        statusContainer.appendChild(statusItem);
    });

    // Atualiza a hora da última verificação
    const now = new Date();
    lastUpdated.textContent = now.toLocaleString('pt-BR');
};

// Atualiza o status a cada 10 segundos
renderServicesStatus();
setInterval(renderServicesStatus, 10000); //Essa função faz com que a função renderServicesStatus seja chamada a cada 10.000 milissegundos (10 segundos), mantendo a página sempre atualizada

