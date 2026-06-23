// Array de dados contendo casos de estudo e a nova categoria 'automacao'
// Substitua o array 'const projetos' do seu script.js por este:
const projetos = [
    {
        titulo: "Robô Monitorador de Preços e E-commerce",
        categoria: "automacao",
        tagTexto: "Automação / Python",
        descricao: "Desenvolvimento de um robô em Python que automatiza a coleta diária de preços de produtos em sites concorrentes, realiza o tratamento dos dados e exporta um relatório estruturado em Excel para tomada de decisão.",
        tecnologias: ["Python", "BeautifulSoup", "Pandas"],
        linkGithub: "https://github.com/DouglasNunesDN/monitor-precos-python"
    }
];

function renderizarProjetos(filtro = "todos") {
    const grid = document.getElementById("grid-projetos");
    grid.innerHTML = ""; 
    
    const projetosFiltrados = projetos.filter(p => filtro === "todos" || p.categoria === filtro);

    if (projetosFiltrados.length === 0) {
        grid.innerHTML = `<p class="font-mono" style="color: var(--text-muted); text-align: center; grid-column: span 2; padding: 3rem 0;">// nenhum caso de estudo publicado nesta categoria</p>`;
        return;
    }

    projetosFiltrados.forEach(projeto => {
        const badges = projeto.tecnologias
            .map(tech => `<span class="badge font-mono">${tech}</span>`)
            .join('');

        const cardHTML = `
            <div class="card animate-fade-in">
                <div>
                    <span class="font-mono card-tag">${projeto.tagTexto}</span>
                    <h4>${projeto.titulo}</h4>
                    <p>${projeto.descricao}</p>
                </div>
                <div>
                    <div class="badges">${badges}</div>
                    <a href="${projeto.linkGithub}" target="_blank" class="card-link font-mono">
                        // checar_codigo_fonte ↗
                    </a>
                </div>
            </div>
        `;
        grid.innerHTML += cardHTML;
    });
}

function gerenciarEstiloBotoes(categoriaAtiva) {
    const categorias = ['todos', 'fullstack', 'datascience', 'automacao'];
    
    categorias.forEach(id => {
        const btn = document.getElementById(`btn-${id}`);
        if (btn) {
            if (id === categoriaAtiva) {
                btn.className = "btn-filtro ativo";
            } else {
                btn.className = "btn-filtro inativo";
            }
        }
    });
}

function filtrarProjetos(categoria) {
    gerenciarEstiloBotoes(categoria);
    renderizarProjetos(categoria);
}

window.onload = () => {
    renderizarProjetos();
};