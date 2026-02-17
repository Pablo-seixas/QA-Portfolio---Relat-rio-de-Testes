  QA Portfolio - Evidências de Testes

Este diretório contém as evidências geradas pelos testes automatizados e manuais das APIs públicas utilizadas no projeto.

  Ferramentas utilizadas
 Pytest (automatização de testes em Python)
  Postman (testes manuais e coleções de API)
  CURL (chamadas diretas a APIs)
  Python (processamento de XML e geração de relatórios Markdown)

  Estrutura de Evidências

 `pytest/` → Relatórios dos testes Pytest em Markdown e XML
 `postman/` → Relatórios dos testes Postman / Newman
 `curl/` → Logs e respostas das chamadas cURL
 `analysis/` → Arquivos de análise e processamento de resultados
 `final-report/` → Relatórios finais consolidados

Testes realizados

| Ferramenta | API/Teste | Status | Tempo (s) |
|------------|-----------|--------|-----------|
| Pytest     | JSONPlaceholder | PASS | 1.036 |
| Pytest     | Africa Countries | PASS | 2.049 |
| Pytest     | World Bank | PASS | 1.235 |


Conclusão
Todos os testes passaram com sucesso. Os relatórios gerados podem ser usados como referência para QA, auditoria ou apresentação do portfólio profissional.

