# Escolta

**Sistema de Segurança Privada Inteligente** / Intelligent Private Security System

[![License: LGPL v2.1](https://img.shields.io/badge/License-LGPL%20v2.1-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Descrição / Description

Escolta é um sistema inteligente de segurança privada que permite monitoramento em tempo real através de sensores, câmeras e alertas automatizados.

Escolta is an intelligent private security system that enables real-time monitoring through sensors, cameras, and automated alerts.

## Características / Features

- 🎥 **Monitoramento de Câmeras** / Camera Monitoring
- 🚨 **Detecção de Movimento** / Motion Detection
- 📱 **Sistema de Alertas** / Alert System
- 🔔 **Notificações** / Notifications (Email, SMS, Push)
- ⚙️ **Configuração Flexível** / Flexible Configuration
- 🌐 **API REST** / REST API
- 📊 **Registro de Eventos** / Event Logging

## Instalação / Installation

### Requisitos / Requirements

- Python 3.8 or higher
- pip

### Instalação Básica / Basic Installation

```bash
# Clone o repositório / Clone the repository
git clone https://github.com/ultrakillcz-web/Escolta.git
cd Escolta

# Instale as dependências / Install dependencies
pip install -r requirements.txt

# Ou instale o pacote / Or install the package
pip install -e .
```

## Uso / Usage

### Uso Básico / Basic Usage

```python
from escolta.core.security_monitor import SecurityMonitor
from escolta.sensors.camera_sensor import CameraSensor
from escolta.sensors.motion_sensor import MotionSensor
from escolta.alerts.alert_manager import AlertManager

# Inicializar o sistema / Initialize the system
monitor = SecurityMonitor()
alert_manager = AlertManager()

# Adicionar sensores / Add sensors
camera = CameraSensor(
    sensor_id="cam-001",
    name="Front Door Camera",
    location="Entrance"
)

motion = MotionSensor(
    sensor_id="motion-001",
    name="Living Room Motion",
    location="Living Room"
)

monitor.add_sensor(camera)
monitor.add_sensor(motion)

# Ativar sensores / Activate sensors
camera.activate()
motion.activate()

# Iniciar monitoramento / Start monitoring
monitor.start()
```

### Executar a Aplicação Principal / Run Main Application

```bash
python main.py --log-level INFO
```

## Estrutura do Projeto / Project Structure

```
Escolta/
├── escolta/              # Pacote principal / Main package
│   ├── core/            # Funcionalidades principais / Core functionality
│   ├── sensors/         # Módulos de sensores / Sensor modules
│   ├── alerts/          # Sistema de alertas / Alert system
│   ├── config/          # Gerenciamento de configuração / Configuration management
│   ├── database/        # Modelos de banco de dados / Database models
│   ├── api/             # API REST / REST API
│   └── utils/           # Utilitários / Utilities
├── tests/               # Testes / Tests
│   ├── unit/           # Testes unitários / Unit tests
│   └── integration/    # Testes de integração / Integration tests
├── main.py             # Ponto de entrada / Entry point
├── setup.py            # Configuração de instalação / Setup configuration
├── requirements.txt    # Dependências / Dependencies
└── README.md          # Este arquivo / This file
```

## Testes / Testing

```bash
# Executar testes unitários / Run unit tests
python -m unittest discover tests/unit

# Executar teste específico / Run specific test
python -m unittest tests.unit.test_security_monitor
```

## Configuração / Configuration

O sistema pode ser configurado através de um arquivo JSON:

The system can be configured through a JSON file:

```json
{
  "system": {
    "name": "Escolta Security System",
    "log_level": "INFO"
  },
  "sensors": {
    "scan_interval": 5,
    "auto_activate": true
  },
  "alerts": {
    "enabled": true,
    "default_severity": "medium"
  },
  "notifications": {
    "email_enabled": false,
    "sms_enabled": false,
    "push_enabled": true
  }
}
```

## Contribuindo / Contributing

Contribuições são bem-vindas! Por favor, sinta-se à vontade para enviar pull requests.

Contributions are welcome! Please feel free to submit pull requests.

## Licença / License

Este projeto está licenciado sob a GNU Lesser General Public License v2.1 - veja o arquivo [LICENSE](LICENSE) para detalhes.

This project is licensed under the GNU Lesser General Public License v2.1 - see the [LICENSE](LICENSE) file for details.

## Contato / Contact

Para questões e suporte, por favor abra uma issue no GitHub.

For questions and support, please open an issue on GitHub.
