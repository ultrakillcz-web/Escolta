# Guia de Contribuição / Contributing Guide

Obrigado por considerar contribuir para o Escolta! / Thank you for considering contributing to Escolta!

## Como Contribuir / How to Contribute

### Reportar Bugs / Reporting Bugs

Se você encontrar um bug, por favor crie uma issue incluindo:
If you find a bug, please create an issue including:

- Descrição clara do problema / Clear description of the problem
- Passos para reproduzir / Steps to reproduce
- Comportamento esperado / Expected behavior
- Comportamento atual / Actual behavior
- Versão do Python e sistema operacional / Python version and operating system

### Sugerir Funcionalidades / Suggesting Features

Para sugerir novas funcionalidades:
To suggest new features:

1. Verifique se já não existe uma issue similar / Check if there isn't a similar issue already
2. Crie uma nova issue descrevendo a funcionalidade / Create a new issue describing the feature
3. Explique por que seria útil / Explain why it would be useful

### Processo de Pull Request

1. Fork o repositório / Fork the repository
2. Crie uma branch para sua funcionalidade (`git checkout -b feature/nova-funcionalidade`)
3. Faça suas alterações / Make your changes
4. Adicione testes para suas alterações / Add tests for your changes
5. Execute os testes (`python -m unittest discover tests`)
6. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
7. Push para a branch (`git push origin feature/nova-funcionalidade`)
8. Abra um Pull Request

### Padrões de Código / Code Standards

- Siga o PEP 8 para código Python
- Adicione docstrings para todas as classes e métodos públicos
- Mantenha a cobertura de testes acima de 80%
- Use nomes descritivos para variáveis e funções

### Executar Testes / Running Tests

```bash
# Todos os testes / All tests
python -m unittest discover tests

# Apenas testes unitários / Unit tests only
python -m unittest discover tests/unit

# Apenas testes de integração / Integration tests only
python -m unittest discover tests/integration
```

### Estrutura de Commits / Commit Structure

Use mensagens de commit claras e descritivas:
Use clear and descriptive commit messages:

- `feat: adiciona nova funcionalidade`
- `fix: corrige bug em sensor de movimento`
- `docs: atualiza documentação`
- `test: adiciona testes para AlertManager`
- `refactor: melhora estrutura do código`

## Código de Conduta / Code of Conduct

- Seja respeitoso / Be respectful
- Aceite críticas construtivas / Accept constructive criticism
- Foque no que é melhor para a comunidade / Focus on what's best for the community

## Dúvidas? / Questions?

Se tiver dúvidas, abra uma issue ou entre em contato através do GitHub.
If you have questions, open an issue or contact us through GitHub.
