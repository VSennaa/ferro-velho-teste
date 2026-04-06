<h1>Ferro-Velho Tech - Sistema de Gestão</h1>

<p align="center">
<strong>[ PROJETO EXPERIMENTAL ]</strong>

<em>Este software foi desenvolvido para fins de estudo e experimentação técnica em integração de IA e Desenvolvimento Web.</em>
</p>

<p>Sistema web de gestão desenvolvido integralmente através do <strong>OpenCode (Gemini API)</strong>, focado na automação de processos de pesagem e controle de materiais em ambientes de reciclagem.</p>

<h2>Contexto do Experimento</h2>
<ul>
<li><strong>Origem:</strong> Gerado via prompts assistidos por IA para testar as capacidades do modelo <em>Gemini 3.1 Flash Lite</em> em arquitetura Django.</li>
<li><strong>Propósito:</strong> Estudar a viabilidade de aplicações autocontidas e deploy em nuvem (Render/Supabase) para micro-negócios.</li>
<li><strong>Status:</strong> Em fase de experimentação técnica e refinamento de interface.</li>
</ul>

<h2>Arquitetura e Funcionalidades</h2>
<ul>
<li><strong>PDV Mobile:</strong> Interface responsiva projetada para tablets e smartphones via Bootstrap 5.</li>
<li><strong>Gestão Dinâmica:</strong> CRUD de materiais com atualização de preços em tempo real.</li>
<li><strong>Inteligência de Dados:</strong> Dashboard consolidado com soma de estoque e capital gasto via <code>Django Aggregation</code>.</li>
<li><strong>PWA Ready:</strong> Estrutura preparada para instalação como Web App (Progressive Web App).</li>
</ul>

<h2>Tecnologias</h2>
<ul>
<li><strong>IA Engine:</strong> Google Gemini (via OpenCode)</li>
<li><strong>Framework:</strong> Django 5.x / Python 3.14</li>
<li><strong>Estilo:</strong> Bootstrap 5 (Mobile-First)</li>
<li><strong>Banco:</strong> PostgreSQL (Supabase)</li>
</ul>

<h2>Execução Local</h2>
<ol>
<li><code>git clone https://github.com/VSennaa/ferro-velho-teste.git</code></li>
<li><code>python -m venv venv</code></li>
<li><code>.\venv\Scripts\activate</code></li>
<li><code>pip install -r requirements.txt</code></li>
<li><code>python manage.py migrate</code></li>
<li><code>python manage.py runserver</code></li>
</ol>

<hr>
<p align="center">
<strong>Autor:</strong> Vinicios Martins (Senna)

Estudante de Engenharia de Controle e Automação - IFMG Campus Ibirité
</p>
