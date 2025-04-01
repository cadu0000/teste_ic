<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <input v-model="termo" placeholder="Digite o nome da operadora" />
    <button @click="buscarOperadoras" :disabled="loading">Buscar</button>
    
    <p v-if="min">É necessário digitar ao menos dois caracteres antes da pesquisa</p>

    <p v-if="loading">Carregando...</p>

    <ul v-if="operadoras.length && !loading">
      <li v-for="operadora in operadoras" :key="operadora.cnpj">
        <strong>{{ operadora.nome_fantasia }}</strong> - CNPJ: {{ operadora.cnpj }}
      </li>
    </ul>
    
    <p v-else-if="erro && !loading">Nenhuma operadora encontrada para "{{ termo }}".</p>
    <p v-else>Faça uma busca para ver as operadoras.</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  async buscarOperadoras() {
  if (this.termo.trim().length < 2) {
    this.min = true;
    this.operadoras = [];
    return;
  }

  this.min = false; 
  this.erro = false; 
  this.loading = true;

  try {
    const response = await axios.get(`http://127.0.0.1:5000/operadora?name=${this.termo}`);
    
    console.log('Resposta da API:', response);  

    if (Array.isArray(response.data)) {
      this.operadoras = response.data;
    } else {
      this.operadoras = [response.data]; 
    }

    if (this.operadoras.length === 0) {
      this.erro = true;
    }
  } catch (error) {
    this.erro = true;
    console.error("Erro ao buscar operadoras:", error);
  } finally {
    this.loading = false; 
  }
}

};
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  text-align: center;
}
input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
}
button {
  padding: 8px 12px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  padding: 5px;
  border-bottom: 1px solid #ddd;
}
p {
  color: #888;
}
</style>