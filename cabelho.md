# PROVA – Introdução à Programação (BIA)
**Nome completo:** FELIPE RODRIGUES DE SOUSA
**Matrícula:** 202504000
**E-mail institucional:** sousafelipe@discente.ufg.br

## QUESTÃO5
### a)
Nós estamos utilizando vários frameworks:

Flask - para transformar o produto em uma aplicação web.
PyMuPDF - para realizar a leitura de arquivos PDF.
PyGithub - para acessar os dados do GitHub de forma mais eficiente.
Além disso, estamos integrando nosso projeto com a API do Gemini para auxiliar nas análises dos perfis do GitHub.

### b)
Nosso projeto é um analisador de currículos chamado SkillScan. O funcionamento é o seguinte: o setor de RH de uma empresa carrega o currículo de um candidato que inclua um link para o GitHub, ou cola o link diretamente. Nosso programa então acessa o GitHub do candidato e analisa seus repositórios, considerando boas práticas de programação, complexidade do código, linguagens utilizadas, número de commits, entre outros fatores. Com base nessa análise, atribui uma nota de 0 a 10 para cada repositório e calcula uma média geral de acordo com o número de repositórios no perfil. O resultado é um feedback para o RH, incluindo uma nota que pode ser usada para ranquear candidatos a uma vaga, além de um breve resumo dos pontos positivos e negativos identificados. Adicionalmente, pretendemos usar essa mesma funcionalidade para monitorar a evolução dos funcionários de uma empresa, implementando um sistema de gamificação para incentivar o aprimoramento de suas habilidades.

### c)
Ainda enfrentamos alguns desafios na integração da API do Gemini para que ela realize a análise dos repositórios da maneira que idealizamos

