# Projeto do Aluno: Pontuação de Clientes Interessados em Seguro Automóvel + Machine Learning + Google Sheets (Apps Script)

![banner_insurance](https://github.com/ctosta/Insurance-Company-Ranking/assets/84297748/5f9ef029-1685-4d9f-96c8-05b79904ed34)


# 1. Problema de Negócios

A Insurance All dedica-se a oferecer seguros de saúde de qualidade aos seus clientes. Como parte de seus esforços para ampliar sua gama de serviços, a empresa também almeja disponibilizar seguros automotivos. No entanto, a empresa enfrenta limitações financeiras que dificultam a aquisição de novos clientes, levando-a a implementar a estratégia de venda cruzada, na qual oferece o segundo seguro aos clientes já segurados. Além disso, devido à sua capacidade limitada, por causa do tamanho moderado da equipe de vendas, torna-se desafiador contatar todos os clientes.

Nesse contexto, a empresa realizou uma pesquisa junto aos seus clientes para avaliar a possibilidade de aquisição de um novo seguro. Com o feedback de mais de 380 mil clientes, os dados solicitadas do formulário foram devidamente organizadas no Google Sheets, e podem ser facilmente acessados por lá.

Agora, o desafio consiste em identificar os potenciais clientes que receberão a oferta do seguro automotivo e efetuar o plano de vendas no decorrer de dois meses, mantendo-se dentro da restrição orçamentária estabelecida.


## 1.1. Reforçando conceitos mencionados anteriormente

- Seguro: trata-se de um contrato financeiro realizado por uma empresa especializada no setor, com a finalidade de proteger uma pessoa física ou jurídica contra perdas financeiras em situações específicas, como enfermidades, acidentes, danos à propriedade, entre outros.

- Seguradora: entidade responsável que garante a indenização ou atendimento a um segurando, pessoa física ou jurídica, quando ocorre um evento coberto pela apólice de seguro.

- Aquisição de Novos Clientes (CAC - Custo de Aquisição de Clientes): gastos que empresa têm para adquirir novos clientes. Compreende despesas referentes a marketing, vendas e outros recursos essenciais para atrair e converter um potencial cliente em um cliente legítimo.

- Venda Cruzada (Cross-Sell): técnica de vendas, onde uma empresa oferece produtos ou serviços complementares ao que o cliente está adquirindo. O objetivo é aumentar o valor final de cada transação e, ao mesmo tempo, fortalecer o relacionamento com o cliente.

## 1.2. Sobre os dados

Os dados do projeto foram obtidos através do [Kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction): Health Insurance Cross Sell Prediction.

O conjunto de dados inclui as seguintes informações:

Variável | Definição
-------- | -----------
id | ID exclusivo do cliente
gender	| Gênero do cliente
age	| Idade do cliente
driving_license | 0 : O cliente não tem Carteira de Habilitação, 1 : O cliente possui Carteira de Habilitação
region_code	| Código exclusivo para a região do cliente
previously_insured	| 1 : Cliente já possui seguro automóvel, 0 : Cliente não possui seguro automóvel
vehicle_age	| Idade do Veículo
vehicle_damage | 1 : O veículo do cliente sofreu danos anteriormente, 0 : O veículo do cliente não sofreu danos anteriormente
annual_premium | O valor que o cliente paga como prêmio no ano, quanto ao seguro saúde
policy_sales_channel | Código anonimizado para o canal de divulgação ao cliente (por correio, por telefone, pessoalmente, etc.)
days_associated| Número de dias desde que o cliente se tornou associado à empresa por meio da aquisição do seguro de saúde
response | 1 : O cliente está interessado, 0 : O cliente não está interessado

# 2. Premissas de Negócios

- A empresa entrará em contato com seus clientes por meio de ligações telefônicas;
- A empresa possui recursos limitados e ligações telefônicas limitadas;
- A equipe de vendas já utiliza o Google Sheets como uma ferramenta corporativa e a pontuação da propensão para adquirir seguro automotivo deve ser integrada a essa plataforma;

- Os cenários de faturamento serão calculados, levando em conta as premissas abaixo: 
    - Todos os clientes interessados irão adquirir adquirir o seguro automóvel; 
    - O custo médio de abordar um contato na lista para fins de prospecção, incluindo o tempo do funcionário e os gastos com comunicação, é de 1250 rúpias indianas;
    - O ticket médio para um seguro saúde anual da Insurance All é: ₹30564.39. O ticket médio do seguro automóvel anual corresponde a 40% do ticket médio do seguro saúde, ou seja, 12225.76 rúpias indianas.

# 3. Estratégia de Solução

## 3.1. Produto Final
- Utilizar a plataforma Render para hospedar o modelo de Machine Learning, o qual será acessado por meio de uma API para responder às requisições;
- Integrar a solução de forma que se conecte ao Google Sheets; 
- Por meio de um botão na barra de ferramentas, atribuir uma pontuação para os clientes existentes (ou qualquer novo cliente adicionado à planilha) com base em sua probabilidade de adquirir o seguro automóvel;

- Fornecer um relatório que inclui análises e respostas para as seguintes questões:
    - Quais são os principais insights acerca dos atributos mais significativos de clientes interessados em seguro automóvel?
    - Qual a porcentagem de clientes interessados em seguro automóvel que a equipe de vendas conseguirá atingir com 20 mil ligações?
    - Se a capacidade da equipe de vendas for ampliada para 40 mil ligações, qual a porcentagem dos clientes interessados em adquirir um seguro automotivo a equipe será capaz de contatar?
    - Quantas ligações a equipe de vendas precisará realizar para alcançar 80% dos clientes interessados em adquirir um seguro automóvel?

## 3.2. Processo

A abordagem escolhida para resolver o desafio se fundamenta na metodologia  CRISP-DM:

### 3.2.1 Compreensão do Negócio (Business Understanding):

- O principal propósito do projeto é tornar mais eficiente e econômico o processo de oferta de seguros automotivos pela Insurance All, reduzindo tanto o tempo quanto os custos envolvidos, além de impulsionar o aumento da receita.
### 3.2.2 Compreensão dos Dados (Data Understanding):

- Coletar dados no Kaggle;
- Dividir os dados em conjuntos de treinamento, validação e teste;
- Avaliar a qualidade dos dados, compreender o significado de cada atributo, renomeá-los, identificar eventuais problemas e proceder com a limpeza dos dados, se necessário;
- Elaborar um mapa de hipóteses;
- Efetuar engenharia de atributos (feature engineering), criando os atributos necessárias para validar as hipóteses;
- Explorar os dados para uma compreensão mais profunda dos atributos que influenciam a variável resposta;
- Gerar insights de negócio;
### 3.2.3 Preparação dos Dados (Data Preparation):

- Preparar os dados para a etapa posterior, realizando técnicas como a normalização, reescalonamento e transformação dos dados;
- Selecionar atributos relevantes para os modelos de machine learning, através da sugestão de algoritmos que listam os melhores atributos. Foi utilizado o Extra Trees, Boruta e LightGBM; 

### 3.2.4 Modelagem (Modeling):

- Definir os algoritmos a serem aplicados. Os escolhidos foram: KNN, LogisticRegression, XGBoost, Extra Trees e LightGBM;
- Treinar os modelos usando os dados de treinamento e validação, além do método de validação cruzada;
- Avaliar o desempenho dos modelos, através da plotagem da curva de ganho limitativo e lift;
- Avaliar o desempenho dos modelos através das métricas precision at K, recall at K e roc auc score, organizando os valores numa tabela;
- Ajustar os parâmetros por meio do GridSearchCV e Optuna e determinar qual deles resultou em um desempenho superior para o modelo;
### 3.2.5 Avaliação (Evaluation):

- Responder as questão de négocios;
- Comparar os resultados entre a lista aleatória e a lista ordenada por probabilidade de compra;
- Traduzir o desempenho do modelo em termos financeiros para a Insurance All; 
### 3.2.6 Implantação (Deployment):

- Criar as classes para publicação em produção e testá-las localmente;
- Implementar o modelo no Render;
- Utilizar o App Script para integrar o algoritmo de pontuação à planilha do Google Sheets e criar um botão para acessar a solução;

# 4. Modelos de Machine Learning e Performance

Ao longo do desenvolvimento de projetos, empregamos métricas para avaliar a eficácia do modelo e alcançar a solução desejada. Para este propósito específico, foram selecionadas duas ferramentas visuais: a Curva de Ganho Acumulativo (Cumulative Gains Curve) e a Curva de Elevação (Lift Curve), juntamente com as métricas de precision at k, recall at k e roc auc score.

Através da **Cumulative Gains Curve**, é possível observar que o modelo contribui para a redução de custos (evitando alcançar todos os clientes da empresa) e, ao mesmo tempo, busca não incomodar os clientes que não têm interesse em adquirir o seguro. A curva é alcançada a partir das seguintes etapas:

- A probabilidade da resposta "sim" (igual a 1), é prevista pelo modelo. Essas observações são organizadas em ordem descrescente, com o objetivo de priorizar as pessoas mais propensas a adquirir o seguro no topo da lista;

- O conjunto de dados é dividido em decis, ou seja, em 10 grupos. O número de observações positivas (resposta = 1) é calculado em cada decil e o número cumulativo de positivos até o decil atual;

- O ganho é calculado como a razão entre o número cumulativo de observações positivas até o decil atual e o número total de observações positivas no conjunto de dados. O gráfico da Curva de Ganho Acumulado é plotado com o ganho no eixo vertical e o decil no eixo horizontal.

Com a **Lift Curve**, que é basicamente derivada do gráfico de ganhos, é fornecida uma maneira  fácil de visualizar quantas vezes a lista ordenada do modelo supera a lista aleatória. 

- Sendo o eixo horizontal (x), a porcentagem da amostra e no eixo vertical (y), a razão entre os ganhos do modelo e os ganhos de um modelo aleatório;

- Logo, Lift Curve é o gráfico entre a elevação no eixo y e o decil correspondente no eixo x. Ao observar o eixo y, torna-se evidente que o modelo performa melhor;

A **precision at k**, é útil quando é crucial garantir que as classificações de maior destaque sejam altamente precisas. Envolve o cálculo da proporção de respostas corretas ("sim") até a posição k (top k) da lista.

O objetivo do **recall at k**, reside em garantir que o modelo seja capaz de identificar a maioria das observações positivas, mesmo que isso resulte em algumas observações falsamento positivas. Calcula-se a proporção de respostas corretas até a posição k (top k) da lista em relação ao número total de respostas corretas no conjunto de dados.

A métrica **ROC-AUC score**, calcula a área sob a curva ROC-AUC, a partir das pontuações de previsão. É uma ferramenta útil pois facilita a comparação entre modelos e contribui na escolha do limiar de classificação com base na necessidade específica do problema. Quanto maior o valor, melhor é o poder discriminatório do modelo. 

Consta a seguir os resultados das análises obtidas, após a validação de cada modelo testado:

 Precision_Top_K | Recall_Top_K | ROC | Model Name
 ----------------|--------------|-----|-----------
 0.28 | 0.930 | 0.854 | XGBClassifier
 0.28 | 0.932 | 0.856 | LGBMClassifier
 0.27 | 0.900 | 0.812 | LogisticRegression
 0.26 | 0.876 | 0.804 | KNeighborsClassifier
 0.25 | 0.838 | 0.768 | ExtraTreesClassifier

O algoritmo de árvore de decisão, LGBM, foi selecionado para avançar com o projeto. Após a otimização dos hiperparâmetros, o desempenho do modelo será avaliado considerando uma perspectiva de negócios.
# 5. Resultados de Negócio

 As perguntas solicitadas anteriormente pelo gestor serão agora abordadas e respondidas, além das suposições iniciais formuladas na etapa de feature engineering, que após testadas, ajudaram a extrair insights importantes do conjunto de dados.

## 5.1. Quais são os principais insights acerca dos atributos mais significativos de clientes interessados em seguro automóvel?

Com base nos algoritmos de seleção de atributos, os considerados mais importantes são: ***age, region_code, previously_insured, vehicle_age, vehicle_damage, annual_premium e policy_sales_channel.***

Ao analisar as hipóteses abaixo, percebe-se que todas elas seguem uma linha de raciocínio contrária ao que foi inicialmente considerado. Portanto, os principais insights são direcionados a clientes que não manifestam interesse pelo seguro.  

- ***H3: O canal mais utilizado é o canal com mais clientes interessados em comprar o seguro automóvel***

    **Falsa** - O canal 152 é o mais usado, porém é por meio dele que os clientes mais rejeitam a oferta. Enquanto os canais 26 e 124, são os mais efetivos na prospecção.

    **Insight de negócio:** É fundamental considerar que uma escolha específica de meio de comunicação com o cliente pode resultar em impacto negativo quando se trata de questionar sobre a aquisição de outro seguro. Portanto, é responsabilidade da empresa avaliar se as chamadas telefônicas representarão a única abordagem para oferecer o seguro, uma vez que essa abordagem pode não ser a preferida por todos.

- ***H5: Os clientes mais interessados em comprar um seguro automóvel são os que têm mais dias associados***

    **Falsa** - Para melhor análise, os dias foram transformados em trimestres, e com isso podemos notar que clientes com mais dias associados recusaram a oferta. 

    **Insight de negócio:** Implementar estratégias distintas para clientes que estão se aproximando da renovação de seus contratos de seguro saúde em comparação com os demais. Adicionalmente, obter informações sobre a satisfação do cliente com a seguradora. 

- ***H7: Os clientes mais interessados em contratar um seguro automóvel são o que possuem um modelo novo***

    **Falsa** - Clientes cujos veículos têm um ano ou mais de uso demonstram maior interesse em adquirir o seguro.

    **Insight de negócio:** Analisar se o valor anual definido para veículos mais recentes está excessivamente alto, pois o cliente pode decidir que o risco de ficar sem seguro é menor do que o custo do prêmio.


![hipoteses-readme](https://github.com/ctosta/Insurance-Company-Ranking/assets/84297748/95f946bb-8da7-457b-a69d-a77449664808)


## 5.2. Qual a porcentagem de clientes interessados em seguro automóvel que a equipe de vendas conseguirá atingir com 20 mil ligações?

Por lista ordenada (modelo), dos 381.109 clientes da Insurance All, cerca de 18% deles estão interessados pelo seguro automóvel. Logo, pode-se esperar que das 20.000 ligações, haverá 8.417 novos contratos, e uma receita estimada de ₹92.38M por ano.

Já por lista aleatória, dos 381.109 clientes da Insurance All,  aproximadamente 5% deles demonstram interesse pelo seguro automotivo. Consequentemente, é razoável esperar que, a partir de 20.000 ligações, sejam estabelecidos 2.451 contratos, resultando em uma receita estimada de ₹26.9M por ano.

O uso do modelo produzirá resultados 3.43 vezes melhores que a lista aleatória, representando um ganho adicional estimado de ₹65.48M para a empresa.

![20mil](https://github.com/ctosta/Insurance-Company-Ranking/assets/84297748/2c3361d0-fcae-45a0-88b7-d16d20903956)


## 5.3. Se a capacidade da equipe de vendas for ampliada para 40 mil ligações, qual a porcentagem dos clientes interessados em adquirir um seguro automotivo a equipe será capaz de contatar?

Por lista ordenada (modelo), dos 381.109 clientes da Insurance All, cerca de 34% deles estão interessados pelo seguro automóvel. Portanto, pode-se esperar que das 40.000 ligações, serão firmados 15.648 novos contratos, resultando em uma receita estimada de ₹171.75M por ano.

Por lista aleatória, dos 381.109 clientes da Insurance All, cerca de 10% demonstraram interesse pelo seguro automóvel. Logo, pode-se esperar que das 40.000 ligações, haverá 4.903 contratos, e uma receita estimada de ₹53.81M por ano.

 O uso do modelo produzirá resultados 3.19 vezes melhores que a lista aleatória, representando um ganho adicional estimado de ₹117.93M para a empresa.

![40mil](https://github.com/ctosta/Insurance-Company-Ranking/assets/84297748/bd36a0aa-ec4e-4d87-ab16-73f601ffb272)

## 5.4. Quantas ligações a equipe de vendas precisará realizar para alcançar 80% dos clientes interessados em adquirir um seguro automóvel?

A equipe de vendas precisará realizar 117.200 ligações, resultando na celebração de 37.382 novos contratos e uma receita estimada de ₹410.3M por ano.

O uso do modelo produzirá resultados 2.6 vezes melhores que a lista aleatória, representando um ganho adicional estimado de ₹252.64M para a empresa.

![80porcento](https://github.com/ctosta/Insurance-Company-Ranking/assets/84297748/084f38b7-da40-4c2a-921a-eb7750765954)

# 6. Modelo em Produção e Acesso ao Algoritmo de Pontuação

A plataforma Render foi utilizada para implementar o modelo de ML, que atenderá às solicitações via API. Isso possibilita que toda a equipe de vendas acesse a solução por meio de um botão na barra de ferramentas do Google Sheets que foi criado pelo Apps Script. Quando esse botão é acionado, uma pontuação é gerada para cada registro de cliente existente na planilha ou para novos registros. Essa pontuação representa a probabilidade de os clientes adquirirem o seguro automóvel.

https://github.com/ctosta/Insurance-Company-Ranking/assets/84297748/f04d1051-3ac0-4d10-8145-9e6275bfb251

# 7. Aprendizados

- Ainda que a pontuação seja pequena, o modelo contribui para aprimorar o processo de prospecção de clientes;
- Para um conjunto de dados desbalanceado, deve-se compreender quais parâmetros têm o maior impacto na pontuação. Para alcançar isso, é necessário explorar diferentes combinações de parâmetros até encontrar a configuração ideal para o cenário específico;
- É necessário testar técnicas diferentes de atributos na fase de preparação dos dados, uma vez que isso não apenas influencia o desempenho dos modelos, mas também o resultado final. Isso é particularmente relevante neste projeto, especialmente na elaboração do mecanismo que atribui pontuações aos registros.  No entanto, é importante observar que técnicas de transformação que introduzem novas colunas podem entrar em conflito com a estrutura da planilha já existente no Google Sheets, o que pode tornar o processo de correção bastante oneroso.

# 8. Próximos Passos

- Para enriquecer o aprendizado dos modelos, buscar novos atributos. Esses atributos, ausentes no formulário de prospecção, têm o potencial de influenciar tanto o valor da apólice de seguro quanto a probabilidade de futuras contratações de seguros. Portanto, é de suma importância incorporá-los ao aprendizado do modelo e tê-los na análise exploratória, para consequentemente gerar novos insights para o negócio;

- Otimizar a interface do Google Sheets com outras funcionalidades, visando a aprimorar a experiência do usuário.